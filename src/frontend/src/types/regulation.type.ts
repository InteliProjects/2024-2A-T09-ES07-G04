export interface Regulation {
    id: number,
    documentnumber: number,
    documenttype_name: string,
    documenturl: string,
    organization_name: string,
    plaintext: string,
    publicationdate: string,
    regulator_name: string,
    regulator_scrapingurl: string,
    status: true,
    tags: Array<string>;
    topic: string,
    xmltext: string
    relations: {
        id: number,
        documentnumber: number,
        documenttype_name: string,
    }[],
    incomplete_backlink: {
        documenturl: string,
        documentname: string,
    }[]
}
export interface RegulationFindAll {
    regulations: Regulation[],
    quantity: number,
}