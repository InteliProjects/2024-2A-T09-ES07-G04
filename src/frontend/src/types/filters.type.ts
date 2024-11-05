export interface Tag {
    id: number,
    name: string,
} 

export interface Regulator {
    id: number,
    name: string,
}

export interface Filters {
    tags: Tag[],
    regulators: Regulator[],
} 