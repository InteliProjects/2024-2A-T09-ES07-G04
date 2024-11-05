// jest.config.js
const nextJest = require('next/jest');

const createJestConfig = nextJest({
  dir: './', // Diretório raiz do projeto Next.js
});

const customJestConfig = {
  testEnvironment: 'jest-environment-jsdom',
  moduleNameMapper: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy', // Ignora arquivos de estilo
    '^@/(.*)$': '<rootDir>/src/$1', // Mapeia o alias '@' para a pasta 'src'
  },
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'], // Configurações adicionais para Jest
};

// Exporta a configuração do Jest
module.exports = createJestConfig(customJestConfig);
