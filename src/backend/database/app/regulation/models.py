from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from ..database import db

# Represents a backlink between two regulations, establishing relationships between them
class RegulationBacklink(db.Model):
    __tablename__ = "regulationbacklink"
    id = db.Column(db.Integer, primary_key=True)  # Adicionando uma coluna de ID
    sourceregulationid = db.Column(db.Integer, db.ForeignKey('regulation.id'))
    targetregulationid = db.Column(db.Integer, db.ForeignKey('regulation.id'), nullable=True)
    documenturl = db.Column(db.String, nullable=True)
    documentname = db.Column(db.String, nullable=True)


# Main regulation model that captures the metadata for legal documents/regulations
class Regulation(db.Model):
    __tablename__ = "regulation"
    
    # Regulation details
    id = db.Column(db.Integer, primary_key=True, index=True)
    regulatorid = db.Column(db.Integer, db.ForeignKey('regulator.id'), nullable=False)
    documenttypeid = db.Column(db.Integer, db.ForeignKey('documenttype.id'), nullable=False)
    documentnumber = db.Column(db.Integer)
    publicationdate = db.Column(db.Date)
    topic = db.Column(db.String)
    organizationid = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    status = db.Column(db.Boolean)
    documenturl = db.Column(db.String)
    xmltext = db.Column(db.String)
    plaintext = db.Column(db.String)
    
    # Relationships to other models
    tags = relationship('Tag', secondary='regulationtags', backref='regulations')
    document_type = relationship('DocumentType', backref='regulations')
    
    # Regulation can have multiple relations through backlinks (both as source and target)
    source_relations = relationship(
        'Regulation',
        secondary='regulationbacklink',
        primaryjoin=id == RegulationBacklink.sourceregulationid,
        secondaryjoin=id == RegulationBacklink.targetregulationid,
        backref='source_of'
    )
    
    target_relations = relationship(
        'Regulation',
        secondary='regulationbacklink',
        primaryjoin=id == RegulationBacklink.targetregulationid,
        secondaryjoin=id == RegulationBacklink.sourceregulationid,
        backref='target_of'
    )

    # Method to serialize the regulation data into a dictionary
    def to_dict(self):
        combined_relations = set(self.source_relations + self.target_relations)  # Combine both source and target relations
        
        Session = sessionmaker(bind=db.engine)
        session = Session()

        # Find incomplete backlinks where the targetregulationid is None in the RegulationBacklink table
        incomplete_backlinks = session.query(RegulationBacklink).filter(
            RegulationBacklink.sourceregulationid == self.id,
            # RegulationBacklink.targetregulationid.is_(None)
        ).all()

        print(f"Incomplete backlinks for sourceregulationid {self.id}: {len(incomplete_backlinks)}")

        return {
            'id': self.id,
            'regulatorid': self.regulatorid,
            'documenttypeid': self.documenttypeid,
            'documentnumber': self.documentnumber,
            'publicationdate': self.publicationdate.isoformat(),
            'topic': self.topic,
            'organizationid': self.organizationid,
            'status': self.status,
            'documenturl': self.documenturl,
            'xmltext': self.xmltext,
            'plaintext': self.plaintext,
            'tags': [tag.name for tag in self.tags],
            'documenttype_name': self.document_type.name if self.document_type else None,
            'relations': [
                {
                    'documenttype_name': relation.document_type.name if relation.document_type else None,  # Nome do tipo do documento relacionado
                    'id': relation.id,
                    'documentnumber': relation.documentnumber,
                } for relation in combined_relations
            ],
            'incomplete_backlink': [
                {
                    'sourceregulationid': backlink.sourceregulationid,
                    'documenturl': backlink.documenturl,
                    'documentname': backlink.documentname,
                } for backlink in incomplete_backlinks
            ]
        }


# Represents a tag that can be associated with a regulation
class Tag(db.Model):
    __tablename__ = "tag"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)

    # Serialize tag data into a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


# Many-to-many relationship between regulations and tags
class RegulationTags(db.Model):
    __tablename__ = "regulationtags"
    
    regulationid = Column(Integer, ForeignKey('regulation.id'), primary_key=True)
    tagid = Column(Integer, ForeignKey('tag.id'), primary_key=True)

    # Serialize relationship data into a dictionary
    def to_dict(self):
        return {
            'regulationid': self.regulationid,
            'tagid': self.tagid,
        }


# Represents the type of a document associated with a regulation
class DocumentType(db.Model):
    __tablename__ = "documenttype"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)

    # Serialize document type data into a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }