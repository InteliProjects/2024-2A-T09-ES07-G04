export function formatNumberWithDots(number: number) {
  // Verifica se o valor é realmente um número
  if (typeof number !== 'number' || isNaN(number)) {
    console.error('Valor inválido para formatar:', number);
    return '0';  // Retorne um valor padrão ou '0'
  }
  return number.toLocaleString('pt-BR');
}

export const formatDate = (dateString: string) => {
  // Converte a string de data para um objeto Date
  const date = new Date(dateString);

  // Opções de formatação para a data
  const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' };

  // Retorna a data formatada no estilo brasileiro
  return date.toLocaleDateString('pt-BR', options);
};
