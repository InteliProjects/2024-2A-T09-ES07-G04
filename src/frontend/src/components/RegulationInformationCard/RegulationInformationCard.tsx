import { Regulation } from '@/types/regulation.type';
import { LuExternalLink } from "react-icons/lu";
import styles from './RegulationInformationCard.module.css';
import Tag from '../Tag/Tag';
import Anchor from '../Anchor/Anchor';
import Button from '../Button/Button';
import { formatNumberWithDots } from '@/utils/helpers';

export default function RegulationInformationCard({ regulation }: { regulation: Regulation }) {
    console.log(regulation.incomplete_backlink)
    return (
        <div className={styles.card}>
            <div>
                <h1>Assunto</h1>
                <p>{regulation.topic}</p>
            </div>
            {regulation.tags.length ? <div>
                <h1>Tags</h1>
                <div className={styles['tags-div']}>
                    {regulation.tags?.map(tag => (
                        <Tag key={tag} maxWidth="20rem" width="fit-content">{tag}</Tag>
                    ))}
                </div>
            </div> : null}
            <div>
                {(regulation.relations && regulation.relations.length > 0 || regulation.incomplete_backlink.length > 0) ?
                    <>
                        <h1>Regulamentações relacionadas</h1>
                        <div className={styles['anchors-div']}>
                            {regulation.relations.map((relation) => (
                                <Anchor href={`/regulations/${relation.id}`} key={relation.id}>
                                    {`${relation.documenttype_name} nº ${formatNumberWithDots(relation.documentnumber)}`}
                                </Anchor>
                            ))}
                            {regulation.incomplete_backlink.map((relation, index) => (
                                <Anchor href={relation.documenturl} key={index}>
                                    {relation.documentname}
                                </Anchor>
                            ))}
                        </div>
                    </> : null
                }
            </div>
            <Button onClick={() => { window.open(regulation.documenturl, '_blank') }} icon={<LuExternalLink />}>Visualizar norma pelo site</Button>
        </div >
    );
};
