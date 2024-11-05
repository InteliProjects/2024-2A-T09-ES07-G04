import { render, screen } from '@testing-library/react';
import RegulationInformationCard from '@/components/RegulationInformationCard/RegulationInformationCard';
import '@testing-library/jest-dom';
import { useRouter } from 'next/router';
import { title } from 'process';

jest.mock('next/router', () => ({
  useRouter: jest.fn(),
}));


// Mock corrigido com todos os campos esperados
const mockRegulation = {
  id: 1,
  title: 'Norma de Segurança',
  description: 'Esta é uma norma de segurança.',
  publicationdate: '2023-09-25',
  topic: 'Este é um tópico',
  tags: [{ id: 1, name: 'Segurança', color: '#ff0000' }], // Incluindo 'color'
  relations: [{ id: 2, title: 'Regulação relacionada' }],
  documenturl: 'https://example.com/document',
  documentnumber: '12345',
  documenttype_name: 'Tipo de Documento',
  organization_name: 'Nome da Organização',
  plaintext: 'Texto simples',
  // Add other missing properties here
};

describe('RegulationInformationCard', () => {

  const mockPush = jest.fn(); // Criar o mock da função push
  (useRouter as jest.Mock).mockReturnValue({
    push: mockPush,
  });

  beforeEach(() => {
    mockPush.mockClear(); // Limpar o mock antes de cada teste
  });

  
  it('renders the regulation topic and tags', () => {
    render(<RegulationInformationCard regulation={mockRegulation} />);
    expect(screen.getByText('Assunto')).toBeInTheDocument();
    expect(screen.getByText(mockRegulation.topic)).toBeInTheDocument();
    expect(screen.getByText('Tags')).toBeInTheDocument();

    // Verifica se as tags estão sendo exibidas corretamente
    mockRegulation.tags?.map(tag => (
      expect(screen.getByText(tag.name)).toBeInTheDocument()
    ));
  });

  it('renders related regulations when available', () => {
    render(<RegulationInformationCard regulation={mockRegulation} />);
    expect(screen.getByText(mockRegulation.relations[0].title)).toBeInTheDocument();
  });

  it('shows message when no related regulations are found', () => {
    render(<RegulationInformationCard regulation={{ ...mockRegulation, relations: [] }} />);
    expect(screen.getByText('Nenhuma regulamentação relacionada encontrada.')).toBeInTheDocument();
  });

  it('opens document URL in a new tab when button is clicked', () => {
    const { getByText } = render(<RegulationInformationCard regulation={mockRegulation} />);
    const openSpy = jest.spyOn(window, 'open').mockImplementation(() => null);
    getByText('Visualizar norma pelo site').click();
    expect(openSpy).toHaveBeenCalledWith(mockRegulation.documenturl, '_blank');
  });
});
