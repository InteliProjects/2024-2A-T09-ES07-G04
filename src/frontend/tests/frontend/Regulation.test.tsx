import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import Regulation from '@/components/Regulation/Regulation';
import { useRouter } from 'next/router';
import { Regulation as RegulationType } from '@/types/regulation.type';

// Mock do useRouter
jest.mock('next/router', () => ({
    useRouter: jest.fn(),
}));

const mockPush = jest.fn();
(useRouter as jest.Mock).mockReturnValue({
    push: mockPush,
});

const regulation: RegulationType = {
    id: 1,
    title: 'Título do Documento', 
    documentnumber: 1,
    documenturl: 'https://example.com/document',
    organization_name: 'Nome da Organização',
    plaintext: 'Texto Plano',
    regulator_name: 'Nome do Regulador',
    regulator_scrapingurl: 'https://example.com/regulator',
    status: true,
    topic: 'Assunto',
    documenttype_name: 'Tipo de Documento',
    publicationdate: '2023-10-01',
    xmltext: 'Texto do XML',
    tag_name: ['Tag1', 'Tag2'],
};

describe('Regulation Component', () => {
    test('deve renderizar corretamente', () => {
        render(<Regulation regulation={regulation} />);

        // Verificar se o título é renderizado
        expect(screen.getByText('Tipo de Documento')).toBeInTheDocument();

        // Verificar se a data é renderizada
        expect(screen.getByText('1 de outubro de 2023')).toBeInTheDocument();

        // Verificar se o texto é renderizado
        expect(screen.getByText('Texto do XML')).toBeInTheDocument();

        // Verificar se as tags são renderizadas
        expect(screen.getByText('Tag1')).toBeInTheDocument();
        expect(screen.getByText('Tag2')).toBeInTheDocument();
    });

});