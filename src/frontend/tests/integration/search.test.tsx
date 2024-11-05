import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import SearchBar from "@/components/Searchbar/Searchbar";
import { useRouter } from 'next/router';
import { RegulationFindAll } from '@/types/regulation.type';

const mockSetInputText = jest.fn();
const mockSetGetAutomatic = jest.fn();

// Mock do useRouter
jest.mock('next/router', () => ({
    useRouter: jest.fn(),
}));

jest.mock('../../src/store/input.store', () => ({
    inputStore: jest.fn(() => ({
        inputText: 'Quero comunicados',
        getAutomatic: true,
        setGetAutomatic: mockSetGetAutomatic,
    })),
}));

// Mock da função fetch
const fetch = jest.fn() as jest.Mock;
global.fetch = fetch;

describe('Search for regulations', () => {
    const mockRouter = {
        push: jest.fn(),
    };

    beforeEach(() => {
        (useRouter as jest.Mock).mockReturnValue(mockRouter); // Mock do useRouter
        fetch.mockClear(); // Limpar mocks do fetch antes de cada teste
    });

    afterEach(() => {
        jest.restoreAllMocks(); // Restaurar mocks após cada teste
    });

    test('renders search bar', () => {
        const { getByTestId } = render(<SearchBar />);

        const input: HTMLInputElement = getByTestId('input') as HTMLInputElement;
        const searchButton: HTMLElement = getByTestId('search-button');

        expect(input).toBeInTheDocument();
        expect(searchButton).toBeInTheDocument();
    });

    test('search by text and navigate on Enter', async () => {
        const { getByTestId } = render(<SearchBar onClick={() => {
            mockSetInputText('Quero comunicados');
            mockSetGetAutomatic(true);
            mockRouter.push('/regulations');
        }} />);

        const input: HTMLInputElement = getByTestId('input') as HTMLInputElement;

        // Simular digitação no campo de busca
        fireEvent.change(input, { target: { value: 'Quero comunicados' } });
        expect(input.value).toBe('Quero comunicados');

        // Simular pressionar a tecla "Enter"
        fireEvent.keyDown(input, { key: 'Enter', code: 'Enter', charCode: 13 });

        // Verificar se as funções do Zustand foram chamadas
        expect(mockSetInputText).toHaveBeenCalledWith('Quero comunicados');
        expect(mockSetGetAutomatic).toHaveBeenCalledWith(true);

        // Verificar se o router.push foi chamado
        expect(mockRouter.push).toHaveBeenCalledWith('/regulations');

        const mockResponseData: RegulationFindAll = {
            regulations: [
                {
                    id: 1,
                    title: 'Regulação Exemplo',
                    documentnumber: 123456,
                    documenttype_name: 'Tipo de Documento',
                    documenturl: 'http://example.com/document',
                    organization_name: 'Nome da Organização',
                    plaintext: 'Texto em formato plano',
                    publicationdate: '2024-01-01',
                    regulator_name: 'Nome do Regulador',
                    regulator_scrapingurl: 'http://example.com/scraping',
                    status: true,
                    tag_name: ['tag1', 'tag2'],
                    topic: 'Tópico de Exemplo',
                    xmltext: '<xml>exemplo</xml>',
                },
            ],
            quantity: 1,
        };

        // Mock da resposta da API
        fetch.mockResolvedValueOnce({
            ok: true,
            json: jest.fn().mockResolvedValueOnce(mockResponseData),
        });

        // Realiza a chamada de fetch
        const response = await fetch('http://127.0.0.1:5000/pln/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input: 'Quero comunicados' }),
        });

        const data = await response.json();

        expect(response.ok).toBe(true); // Verifica se a resposta é OK
        expect(data).toMatchObject<RegulationFindAll>({
            regulations: expect.arrayContaining([
                expect.objectContaining({
                    id: expect.any(Number),
                    title: expect.any(String),
                    documentnumber: expect.any(Number),
                    documenttype_name: expect.any(String),
                    documenturl: expect.any(String),
                    organization_name: expect.any(String),
                    plaintext: expect.any(String),
                    publicationdate: expect.any(String),
                    regulator_name: expect.any(String),
                    regulator_scrapingurl: expect.any(String),
                    status: expect.any(Boolean),
                    tag_name: expect.arrayContaining([expect.any(String)]),
                    topic: expect.any(String),
                    xmltext: expect.any(String),
                }),
            ]),
            quantity: expect.any(Number),
        });
    });
});
