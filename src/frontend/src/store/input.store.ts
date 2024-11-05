import { create } from 'zustand';

interface InputState {
    inputText: string;
    setInputText: (value: string) => void;
    getAutomatic: boolean;
    setGetAutomatic: (value: boolean) => void;
}

export const inputStore = create<InputState>((set) => ({
    inputText: '',
    setInputText: (value) => set({ inputText: value }),
    getAutomatic: false,
    setGetAutomatic: (value) => set({ getAutomatic: value }),
}));
