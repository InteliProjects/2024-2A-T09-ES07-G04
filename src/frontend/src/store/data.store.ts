import { RegulationFindAll } from '@/types/regulation.type';
import { create } from 'zustand';

interface DataState {
    data: RegulationFindAll;
    setData: (value: RegulationFindAll) => void;
}

export const dataStore = create<DataState>((set) => ({
    data: { regulations: [], quantity: 0 },
    setData: (value) => set({ data: value }),
}));
