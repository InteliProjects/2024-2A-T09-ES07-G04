<table>
<tr>
<Table>
  <tr>
    <td width=50%><a href="https://bofabrasil.com.br/PHXBrazil/BrazilCMS/#/home"><img src="../assets/bofa-logo.jpg" alt="Bank of America" border="0"></td>
    <td>
      <a href= "https://www.inteli.edu.br/"><img src="../assets/inteli-logo.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
    </td>
  </tr>
</table>

# Vox

## Desenvolvido por Vox Group

## 👨‍🎓 Integrantes

- [Bruna Brasil](https://www.linkedin.com/in/bruna-brasil-alexandre/)
- [Clara Mohammad](https://www.linkedin.com/in/claramohammad/)
- [Joselito Junior](https://www.linkedin.com/in/joselitojunior/)
- [Luigi Macedo](https://www.linkedin.com/in/luigiotavio/)
- [Renan Feitosa](https://www.linkedin.com/in/renanfeit/)

## Sumário

- [1. Entendimento de Negócios](#1-entendimento-de-negócios)

  - [1.1 Entendimento do Parceiro](#11-entendimento-do-parceiro)

    - [1.1.1 Partes Interessadas](#111-partes-interessadas)
    - [1.1.2 Contexto da indústria](#112-contexto-da-indústria)
    - [1.1.3 Modelo de negócios](#113-modelo-de-negócios)
    - [1.1.4 Canvas de Proposta de Valor](#114-canvas-de-proposta-de-valor)
    - [1.1.5 Tendências do Mercado](#115-tendências-do-mercado)

  - [1.2 Descrição do Problema](#12-descrição-do-problema)
  - [1.3 Proposta de Solução](#13-proposta-de-solução)
    - [1.3.1 Descrição da Solução](#131-descrição-da-solução)
    - [1.3.2 Matriz de Riscos](#132-matriz-de-riscos)
    - [1.3.3 Estimativa de Investimentos](#133-estimativa-de-investimentos)
    - [1.3.4 Prova de Conceito (PoC)](#134-prova-de-conceito-poc)

- [2. Entendimento do Design](#2-entendimento-do-design)

  - [2.1. Estudo sobre o usuário do sistema](#21-estudo-sobre-o-usuário-do-sistema)
    - [2.1.1 Perfil do Usuário](#211-perfil-do-usuário)
    - [2.1.2 Persona](#212-persona)
    - [2.1.3 Jornada do Usuário](#213-jornada-do-usuário)
  - [2.2 Proposta de UX para o Sistema](#22-proposta-de-ux-para-o-sistema)
  - [2.3 Pilha de tecnologias para implementação do Sistema](#23-pilha-de-tecnologias-para-implementação-do-sistema)
  - [2.4 Mockups do Sistema](#24-mockups-do-sistema)

- [3. Entendimento da Arquitetura do Sistema](#3-entendimento-da-arquitetura-do-sistema)

  - [3.1 Proposta de Arquitetura do Sistema](#31-proposta-de-arquitetura-do-sistema)
  - [3.2 Requisitos Funcionais e Não Funcionais do Sistema](#32-requisitos-funcionais-e-não-funcionais-do-sistema)
    - [3.2.1 Requisitos Funcionais](#321-requisitos-funcionais)
    - [3.2.2 Requisitos Não Funcionais](#322-requisitos-não-funcionais)
  - [3.3 Padrões de Trabalho](#33-padrões-de-trabalho)

- [4. Sistema de NLP](#4-sistema-de-nlp)

  - [4.1 API para implementar a etapa de Speech to Text](#41-api-para-implementar-a-etapa-de-speech-to-text)
  - [4.2 Algoritmo de NLP utilizado e sua implementação](#42-algoritmo-de-nlp-utilizado-e-sua-implementação)
  - [4.3 Processo de deploy do algoritmo em nuvem](#43-processo-de-deploy-do-algoritmo-em-nuvem)
  - [4.4 API para receber os áudios enviados pelo usuário](#44-api-para-receber-os-áudios-enviados-pelo-usuário)

- [5. Construção do Banco de Dados](#5-construção-do-banco-de-dados)

  - [5.1 Modelagem do Banco de Dados](#51-modelagem-do-banco-de-dados)
  - [5.2 Implementação do Banco de Dados](#52-implementação-do-banco-de-dados)

- [6. Construção do Backend da Solução](#6-construção-do-backend-da-solução)

  - [6.1 Endpoints do backend](#61-endpoints-do-backend)
  - [6.2 Integração do Speech-to-text](#62-integração-do-speech-to-text)
  - [6.3 Webhook](#63-webhook)
  - [6.4 Serviço de mensageria (RabbitMQ)](#64-serviço-de-mensageria-rabbitmq)

- [7. Construção do Frontend da Solução](#7-construção-do-frontend-da-solução)

- [8. Integração Front e Back](#8-integração-front-e-back)
  - [8.1 Intruções para integração](#81-intruções-para-integração)

- [9. Guia de configuração](#9-guia-de-configuração)

- [10. Testes de Software](#10-testes-de-software)

  - [10.1 Plano de testes](#101-plano-de-testes)
  - [10.2 Casos de uso - Testes unitário de frontend](#102-casos-de-uso)
  - [10.3 Casos de uso - Testes integração de frontend e backend](#102-casos-de-uso)
  - [10.4 Relatório de testes](#104-relatório-de-testes)

- [11. Deploy da solução](#11-deploy-da-solução)
  - [11.1 Monitoramento](#111-monitoramento)
  - [11.2 Testes de Produção](112-testes-de-produção)
  - [11.3 Como Utilizar o Docker Compose](113-como-utilizar-o-docker-compose)

- [12. Benefícios entregues pelo projeto](#12-benefícios-entregues-pelo-projeto)

- [13. Aperfeiçoamentos Futuros](#13-aperfeiçoamentos-futuros)
  - [13.1] Possíveis aperfeiçoamentos futuros](#121-possíveis-aperfeiçoamentos-futuros)

- [Referências](#referências)
- [Apêndice](#apêndice)

# 1. Entendimento de Negócios

&emsp;&emsp; O sucesso de qualquer projeto depende de uma compreensão profunda do ambiente de negócios em que ele está inserido. No contexto do sistema "Vox", o entendimento de negócios envolve uma análise detalhada das necessidades, desafios e oportunidades do setor bancário. Essa compreensão permite alinhar o desenvolvimento da solução às exigências regulatórias e às expectativas dos usuários, garantindo que o sistema ofereça funcionalidades que agreguem valor real às operações diárias dos profissionais que lidam com regulamentações.

## 1.1 Entendimento do Parceiro

&emsp;&emsp; A parceria com o Bank of America é essencial para o desenvolvimento do sistema "Vox". Compreender as necessidades, expectativas e os padrões do Bank of America nos permite alinhar nosso projeto aos altos padrões de qualidade e segurança exigidos pelo setor financeiro. Esse entendimento mútuo garante que o "Vox" seja uma solução eficaz, atendendo de forma precisa às demandas do mercado bancário, a seção a seguir aborda os detalhes desta parceria.

### 1.1.1 Partes Interessadas

&emsp;&emsp;As partes interessadas no projeto de desenvolvimento da solução tecnológica para otimização do acompanhamento das mudanças regulatórias na indústria financeira no Brasil são essenciais para o sucesso do projeto. Cada grupo traz uma perspectiva única e contribuições valiosas que ajudam a moldar a solução final. Abaixo estão descritas as principais partes interessadas e suas funções:

&emsp;&emsp;1. **Bank of America (BofA)**: O Bank of America é uma das principais instituições financeiras globais com uma presença significativa no Brasil. O BofA atua no mercado de banco de atacado, banco de investimento e serviços de mercados de capitais no Brasil, com aproximadamente 1.000 funcionários e um faturamento anual em torno de US$ 1 bilhão. O banco busca otimizar o processo de acompanhamento das mudanças regulatórias para garantir conformidade e eficiência operacional. O BofA é o principal cliente e patrocinador do projeto. A empresa define os requisitos e expectativas para a solução, fornece feedback contínuo e valida a eficácia da solução desenvolvida. A colaboração próxima com a equipe de desenvolvimento é crucial para garantir que a solução atenda às necessidades específicas de compliance e gestão de mudanças regulatórias.

&emsp;&emsp;2. **Professor Orientador - Hermano Peixoto**: Professor orientador responsável por fornecer orientação acadêmica e técnica ao projeto. Atua como mentor e guia acadêmico, oferecendo suporte na definição do escopo do projeto, revisão da documentação e validação das metodologias adotadas. Sua expertise assegura que o projeto esteja alinhado com as melhores práticas acadêmicas e técnicas.

&emsp;&emsp;3. **Líderes de Projeto - Otávio Braga e Leonardo Meira**: Líderes responsáveis pela coordenação geral do projeto e pela supervisão das atividades diárias. Coordenam o desenvolvimento e a implementação da solução, garantem que o projeto esteja no caminho certo para atender aos objetivos definidos, e comunicam-se com todas as partes interessadas para assegurar que os requisitos sejam cumpridos e que o projeto avance conforme o planejado.

&emsp;&emsp;4. **Ponto Focal Backup e Líder de Negócio - Gabriel Paganini**: Ponto focal adicional que garante a continuidade das operações em caso de ausência dos líderes de projeto. Auxilia na coordenação do projeto e assume responsabilidades em situações onde os líderes principais não estão disponíveis, garantindo que o progresso do projeto não seja comprometido.

&emsp;&emsp;5. **Líder Executivo [Onboarding Executivo] - Leonardo Meira**: Líder responsável pela integração da solução com as operações e a estratégia executiva do BofA. Facilita o alinhamento estratégico entre a solução desenvolvida e os objetivos executivos do BofA, assegura que a solução se integre de forma eficaz aos processos e operações existentes e apoia a adoção da solução pelos executivos da empresa.

&emsp;&emsp;6. **Compliance Officers**: Usuários finais da solução, responsáveis por garantir que o BofA esteja em conformidade com as regulamentações. Utilizam a solução diariamente para monitorar e gerenciar as mudanças regulatórias, fornecem feedback sobre a eficácia da solução e ajudam a identificar melhorias necessárias.

&emsp;&emsp;7. **Inteli**: O Inteli se destaca por sua excelência técnica, assegurando que as tecnologias adotadas no desenvolvimento do projeto atendam as necessidades específicas. A instituição oferece suporte crucial aos alunos e ao grupo de trabalho, promovendo a aplicação das melhores práticas de engenharia de software e garantindo a entrega de soluções tecnológicas robustas e de alta qualidade.

&emsp;&emsp;8. **Equipe de Desenvolvimento**: A equipe de desenvolvimento é formada por alunos do Inteli altamente motivados e dedicados, que aplicam seus conhecimentos acadêmicos e habilidades práticas para criar e implementar a solução tecnológica. Esses alunos são responsáveis por todo o ciclo de vida do projeto, desde a definição dos requisitos e planejamento até o desenvolvimento, testes e refinamento da solução. Com orientação e suporte dos instrutores e especialistas, a equipe busca aplicar as melhores práticas de engenharia de software, garantindo que a solução atenda às expectativas dos stakeholders.

&emsp;&emsp;A colaboração e a comunicação eficaz entre o Bank of America, os líderes de projeto, os especialistas técnicos e os usuários finais são cruciais para o sucesso do projeto. Cada parte interessada contribui com uma perspectiva e expertise única que ajuda a garantir que a solução atenda às necessidades do BofA, otimize o processo de acompanhamento das mudanças regulatórias e alcance os objetivos de conformidade e eficiência operacional.

### 1.1.2 Contexto da Indústria

&emsp;&emsp;A indústria financeira no Brasil é diversificada e desempenha um papel crucial no desenvolvimento econômico do país. Esta indústria abrange uma ampla gama de serviços, incluindo bancos comerciais, bancos de investimento, corretoras, seguradoras e administradoras de fundos de pensão. O setor é dominado por grandes bancos, tanto nacionais quanto internacionais, que controlam uma parte significativa dos ativos financeiros. Dentre as instituições internacionais, o Bank of America (BofA) se destaca como um dos principais atores, especialmente nos segmentos de banco de atacado, banco de investimento e serviços de mercados de capitais. No Brasil, o BofA possui aproximadamente 1.000 colaboradores e gera um faturamento anual em torno de US$ 1 bilhão, reforçando sua presença significativa no mercado financeiro nacional e sua posição de liderança global.

&emsp;&emsp;Nos últimos anos, a indústria financeira brasileira tem passado por uma transformação significativa, impulsionada por avanços tecnológicos, mudanças regulatórias e aumento da competitividade. A digitalização dos serviços bancários, por exemplo, tem revolucionado a interação dos clientes com as instituições financeiras. O surgimento das _Fintechs_, empresas que introduzem inovações nos mercados financeiros por meio do uso intenso de tecnologia, tem desafiado os bancos tradicionais ao oferecer soluções mais rápidas, convenientes e muitas vezes a custos mais baixos. Essas startups têm desempenhado um papel importante na inclusão financeira, atingindo áreas historicamente desatendidas pelos grandes bancos.

### Regulação e Compliance

&emsp;&emsp;A regulação é um dos pilares fundamentais da indústria financeira no Brasil. A estrutura regulatória é complexa, envolvendo diversas entidades governamentais, como o Banco Central do Brasil (BACEN), a Comissão de Valores Mobiliários (CVM) e o Conselho Monetário Nacional (CMN). Esses órgãos são responsáveis por garantir a estabilidade financeira, proteger os investidores e manter a integridade do sistema financeiro. Para as instituições financeiras, o cumprimento das normas regulatórias é essencial, sendo que o não cumprimento pode resultar em severas multas, sanções e até mesmo na perda da licença para operar.

&emsp;&emsp;No contexto global, especialmente para uma instituição como o BofA, que atua em múltiplos países, o desafio regulatório é ainda maior. As normas e regulamentos variam significativamente entre as jurisdições, exigindo uma capacidade robusta de adaptação e compliance para evitar riscos legais e operacionais.

### Competitividade e Inovação

&emsp;&emsp;A concorrência no setor financeiro brasileiro é intensa, com bancos tradicionais, _Fintechs_ e bancos digitais disputando a preferência dos consumidores. Instituições como o Itaú, Bradesco, Santander, e o JPMorgan Chase são alguns dos principais concorrentes do Bank of America no Brasil, especialmente no segmento de banco de atacado e de investimento. Nesse mercado dinâmico e competitivo, o BofA enfrenta desafios para se destacar, no entanto, sua forte presença global e expertise em serviços de banco de investimento e mercado de capitais, aliados à capacidade de oferecer soluções financeiras integradas e personalizadas para grandes empresas e investidores institucionais, conferem uma vantagem competitiva significativa.

&emsp;&emsp;A inovação tornou-se uma estratégia essencial para manter a competitividade. As instituições financeiras no Brasil têm investido pesadamente em tecnologia para melhorar a eficiência operacional, oferecer melhores serviços aos clientes e cumprir as exigências regulatórias de maneira mais eficaz. Ferramentas como inteligência artificial, análise de dados e blockchain estão sendo cada vez mais incorporadas para automatizar processos, reduzir custos e aprimorar a tomada de decisões.

&emsp;&emsp;Portanto, podemos concluir que a indústria financeira no Brasil é complexa e desafiadora, mas também cheia de oportunidades. Para instituições como o Bank of America, navegar nesse ambiente exige não apenas uma sólida base de conhecimento regulatório, mas também uma constante capacidade de inovação e adaptação. A destreza do BofA em banco de atacado e investimento, aliada ao seu compromisso com a conformidade regulatória e a inovação tecnológica, posiciona a instituição de maneira favorável para continuar crescendo e atendendo às necessidades de seus clientes no Brasil.

### 1.1.3 Modelo de Negócios

&emsp;&emsp;O Bank of America Corporation é uma das maiores instituições financeiras do mundo, oferecendo uma ampla gama de produtos e serviços financeiros a consumidores individuais, pequenas e médias empresas, e grandes corporações. Fundado em 1904 e com sede em Charlotte, Carolina do Norte, o banco opera em mais de 35 países.

O modelo de negócio do Bank of America é diversificado e pode ser dividido em quatro segmentos principais:

Serviços Bancários ao Consumidor:
Produtos e Serviços tradicionais, como: Contas correntes e de poupança, cartões de crédito e débito, empréstimos pessoais e hipotecas; Canais de Distribuição: Agências bancárias, caixas eletrônicos, online banking, mobile banking.

Gestão de Riqueza:
Oferecendo serviços de consultoria financeira e de investimento para indivíduos de alta renda e Serviços de gestão de patrimônio para clientes ultra-ricos, incluindo planejamento financeiro, gestão de investimentos, serviços fiduciários e planejamento imobiliário.

Banca Global:
Serviços financeiros para grandes corporações, incluindo crédito, gerenciamento de caixa, serviços de tesouraria e soluções de capital e Consultoria para fusões e aquisições, serviços de subscrição de dívida e capital, e outros serviços de mercado de capitais.

Mercados Globais:
Negociação de ações, títulos de renda fixa, câmbio e commodities e Serviços para fundos de hedge, incluindo financiamento, execução e custódia de ativos.

Estrutura de Receita:
O Bank of America gera receita principalmente através de Juros (Provenientes de empréstimos, hipotecas e outros produtos de crédito), Receitas de Tranding (Obtidos através de negociação em mercados financeiros), Taxas e comissões (Serviços bancários, gestão de investimentos, underwriting, consultoria e trading). Esta receita é resultado da venda de dinheiro, tendo em vista que este é o principal produto de qualquer banco.

As principais estratégias de crescimento do Bank of America incluem Inovação em Tecnologias, Expansão Internacional e Práticas de impacto social, sendo estas detalhadas abaixo:

Inovação Tecnológica: Investimento em tecnologia para melhorar a experiência do cliente e aumentar a eficiência operacional. Exemplos incluem o desenvolvimento de plataformas de mobile banking e soluções de inteligência artificial como o assistente virtual Erica.

Expansão Internacional: Crescimento em mercados internacionais, especialmente na Ásia e Europa, para diversificar a base de receita.

Sustentabilidade e Responsabilidade Social: Foco em práticas sustentáveis e responsabilidade social corporativa, incluindo investimentos em energia renovável e apoio a comunidades locais.

O modelo de negócio do Bank of America é robusto e diversificado, permitindo-lhe atender a uma ampla gama de necessidades financeiras globais. Através de sua estratégia de inovação, expansão internacional e foco em sustentabilidade, o Bank of America busca manter sua posição como líder no setor financeiro, enquanto navega pelos desafios do ambiente econômico e regulatório.

### 1.1.4 Canvas de Proposta de Valor

&emsp;&emsp;O Canvas de Proposta de Valor é uma ferramenta estratégica que ajuda empresas a definir e comunicar de forma clara e estruturada a proposta de valor de um produto ou serviço. Ele permite que esssas organizações identifiquem e alinhem os benefícios que oferecem aos clientes com suas reais necessidades e dores. Através de um visual simples, o Canvas facilita a compreensão das relações entre o que a empresa oferece e o que o cliente busca, ajudando a criar produtos e serviços que realmente agregam valor. Dessa forma, o Canvas é utilizado no contexto de projeto para fins acadêmicos, dispondo das mesmas técnicas utilizadas no mercado em um contexto de parceria entre a faculdade e a empresa Bank Of America.

&emsp;&emsp;A priori, estrutura do Canvas é dividida em duas partes principais: Segmento de Clientes e Proposta de Valor. No lado do Segmento de Clientes, são analisadas as tarefas que os clientes precisam realizar, suas dores (frustrações, desafios) e os ganhos (benefícios, expectativas) que desejam alcançar. Já no lado da Proposta de Valor, a empresa detalha como seus produtos e serviços ajudam os clientes a resolver suas dores e alcançar os ganhos desejados, através de elementos como Pain Relievers (aliviadores de dores), Gain Creators (geradores de benefícios) e a própria oferta de produtos e serviços. A imagem abaixo ilustra essa estrutura:

<div align="center">
  <sub>Figura 1 - Canvas Proposta de Valor</sub>
  <img src="./assets/canvasvalue.png" width="100%" alt='Imagem Canvas de Valor'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

<b>Customer Segments (Segmento de Clientes)</b>

<b>Customer Jobs (Tarefas do Cliente):</b>

Agilidade e precisão na pesquisa de regulamentos para o banco: Os clientes buscam ferramentas que facilitem e tornem mais ágil a busca por regulamentos bancários.

<b>Concentração da informação em uma única plataforma:</b> Há uma necessidade de consolidar todas as informações relevantes em um só lugar para facilitar o acesso e a consulta.

<b>A consulta e leitura das normas atualizadas com feedback na própria plataforma:</b> Os clientes precisam de uma forma prática de acessar normas atualizadas e receber feedback diretamente na plataforma que utilizam.

<b>Gains (Ganhos):</b>

<b>Agilidade e precisão na pesquisa de regulamentos para o banco:</b> Aumentar a eficiência e a velocidade na busca por regulamentos é um ganho significativo para os usuários.

<b>Concentração da informação em uma única plataforma:</b> Ter todas as informações centralizadas economiza tempo e reduz a complexidade na gestão de regulamentos.

<b>Pains (Dores):</b>

<b>Tempo gasto para encontrar atualizações em normas bancárias e, caso tenha sido alterado alguma outra, o feedback da mudança:</b> Um problema importante é o tempo e esforço necessário para encontrar as atualizações nas normas e as dificuldades em obter feedback sobre essas mudanças.

<b>Value Proposition (Proposta de Valor)</b>

<b>Gain Creators (Geradores de Benefícios):</b>

<b>Eficiência aumentada nas buscas de normas:</b> O software promete melhorar significativamente a eficiência das buscas.

<b>Atualização contínua:</b> Manter os usuários atualizados continuamente com as últimas normas.

<b>Redução de erros na pesquisa de regulamentos:</b> Diminuição da probabilidade de erros durante as buscas, oferecendo informações mais precisas.

<b>Products & Services (Produtos e Serviços):</b>

<b>Software de busca automatizado por PLN (Processamento de Linguagem Natural):</b> Um software que automatiza a busca por regulamentos utilizando técnicas de PLN para tornar o processo mais eficiente.

<b>Plataforma de busca de regulamentos para o banco:</b> Uma plataforma que centraliza a busca de regulamentos, facilitando o acesso e a gestão das normas.

<b>Pain Relievers (Aliviadores de Dores):</b>

<b>Economia de tempo na busca de atualizações nos regulamentos:</b> O software promete reduzir significativamente o tempo necessário para encontrar atualizações em normas bancárias.

<b>Busca facilitada e notificada sobre qualquer atualização dos regulamentos bancários:</b> Oferece uma funcionalidade que notifica os usuários sobre qualquer atualização relevante nas normas, reduzindo a necessidade de busca manual.

&emsp;&emsp;Dessa forma, o Canvas de Proposta de Valor tem como objetivo esclarecer os valores, soluções, estratégias, stakeholders e as principais finalidades do desenvolvimento do projeto em questão.

### 1.1.5 Tendências do Mercado

A área financeira, especialmente em instituições como o Bank of America, está passando por transformações profundas impulsionadas por avanços tecnológicos, mudanças econômicas e novas expectativas dos funcionários e clientes. O objetivo desta documentação é explorar essas tendências de forma abrangente, oferecendo uma visão holística sobre o futuro do setor.

### Inteligência Artificial e Automação

A inteligência artificial (IA) está revolucionando a maneira como o Bank of America opera. Ferramentas de IA são cada vez mais utilizadas para melhorar a eficiência operacional, prever tendências de mercado e personalizar a experiência do cliente. Um exemplo notável é o assistente virtual Erica, que utiliza IA para oferecer insights financeiros personalizados, responder perguntas e executar tarefas bancárias básicas. A automação, combinada com IA, está permitindo que processos anteriormente manuais, como a análise de crédito e a detecção de fraudes, sejam realizados de maneira mais rápida e precisa. Essa tendência não apenas aumenta a eficiência, mas também libera os funcionários para se concentrarem em atividades mais estratégicas e de maior valor agregado.

### Inovação Tecnológica e Segurança Cibernética

A evolução tecnológica vai além da IA. O Bank of America está investindo em blockchain, uma tecnologia que promete transformar a forma como as transações são realizadas, proporcionando maior transparência e segurança. Com o aumento das ameaças cibernéticas, a segurança cibernética se tornou uma prioridade máxima. O banco está desenvolvendo soluções de segurança de última geração, incluindo a autenticação multifator e a criptografia avançada, para proteger os dados dos clientes e garantir a integridade das transações. Além disso, a utilização de big data e análise avançada está permitindo ao banco identificar padrões de comportamento anormais, prevenindo fraudes antes que elas ocorram.

### Tendências Econômicas e Impacto Global

No cenário econômico, o Bank of America está atento às tendências globais, como a digitalização crescente das economias, a mudança para uma sociedade sem dinheiro físico e as pressões inflacionárias. A pandemia de COVID-19 acelerou a adoção de pagamentos digitais, e o banco está investindo em soluções que suportem essa transição, como plataformas de pagamento móvel e carteiras digitais. Além disso, a instituição está se posicionando para lidar com as mudanças nas políticas monetárias globais, que impactam diretamente as taxas de juros e a oferta de crédito. A crescente ênfase em sustentabilidade também está moldando as estratégias do banco, com iniciativas voltadas para o financiamento de projetos verdes e a redução da pegada de carbono da instituição.

### Tendências de Recursos Humanos e Cultura Organizacional

As tendências em recursos humanos no Bank of America refletem a evolução do ambiente de trabalho global. Com o aumento do trabalho remoto, o banco está reestruturando suas políticas de trabalho para oferecer maior flexibilidade aos funcionários. A cultura de inovação e aprendizado contínuo está sendo incentivada através de programas de capacitação em novas tecnologias e habilidades digitais. Além disso, a diversidade e a inclusão são áreas de foco crescente, com iniciativas destinadas a promover um ambiente de trabalho mais inclusivo e equitativo. O bem-estar dos funcionários também ganhou destaque, com o banco implementando programas de suporte à saúde mental e física, reconhecendo a importância de uma força de trabalho saudável e engajada.

### Tendências no Atendimento ao Cliente e Experiência do Usuário

O atendimento ao cliente no Bank of America está sendo redefinido pela digitalização e pela personalização. O uso de IA para oferecer suporte 24/7 através de assistentes virtuais é apenas o começo. A personalização das interações com os clientes, baseada em análise de dados, está se tornando a norma. Isso inclui desde ofertas financeiras sob medida até recomendações proativas de investimento. A experiência do usuário, tanto em plataformas digitais quanto em agências físicas, está sendo repensada para garantir que os clientes tenham uma jornada sem fricções, intuitiva e segura.

### Sustentabilidade e Responsabilidade Social Corporativa

A sustentabilidade é uma tendência crescente no Bank of America, refletindo a importância de práticas empresariais responsáveis. O banco está comprometido com a redução de suas emissões de carbono e está investindo em projetos de energia renovável. A responsabilidade social corporativa vai além do meio ambiente, englobando também iniciativas para apoiar comunidades locais, promover a educação financeira e incentivar o empreendedorismo. Essas ações não são apenas uma resposta às demandas dos stakeholders, mas também uma estratégia para garantir o crescimento sustentável a longo prazo.

Em suma, as tendências que estão moldando o Bank of America são indicativas de uma transformação mais ampla no setor financeiro. A convergência de tecnologia, economia, cultura organizacional e responsabilidade social está criando um ambiente dinâmico e desafiador. O sucesso futuro do banco dependerá de sua capacidade de inovar, adaptar-se e liderar em um mundo em constante mudança. Este documento buscou apresentar uma visão abrangente dessas tendências, oferecendo uma base sólida para entender os desafios e oportunidades que se apresentam.

## 1.2 Descrição do Problema

&emsp;&emsp; A gestão de mudanças regulatórias é um processo fundamental para instituições financeiras, como o Bank of America, que precisam monitorar constantemente as alterações nas leis, regras e regulamentos (LRRs) emitidos por diversos órgãos reguladores. O cenário regulatório atual é extremamente dinâmico, caracterizado por um alto volume e complexidade de normas que afetam diretamente as operações financeiras e os procedimentos internos das empresas. Essa crescente demanda por conformidade regulatória exige que as instituições se mantenham atualizadas e ajustem seus processos de acordo com novas exigências.

&emsp;&emsp; No contexto brasileiro, a diversidade de órgãos reguladores, como o Banco Central do Brasil, a Comissão de Valores Mobiliários (CVM), a ANBIMA, entre outros, adiciona camadas de complexidade ao processo. Cada um desses órgãos publica suas normas em diferentes formatos e locais, o que dificulta o acompanhamento centralizado e ágil das LRRs. Além disso, muitas vezes é necessário acesso restrito por login ou o uso de ferramentas de autenticação, como captchas, o que torna o processo ainda mais oneroso e sujeito a falhas humanas.

&emsp;&emsp; Essa situação resulta em desafios operacionais para as equipes de compliance que precisam gerenciar um alto volume de normas e garantir que todas as mudanças relevantes sejam identificadas, analisadas e aplicadas de maneira eficiente. A falta de uma solução tecnológica adequada que automatize o monitoramento dessas mudanças pode gerar retrabalho, aumentar os riscos de não conformidade e, consequentemente, resultar em penalidades ou perda de eficiência no cumprimento das obrigações regulatórias.

## 1.3 Proposta de Solução

&emsp;&emsp;Esta seção descreve uma proposta para automatizar o processo de busca, categorização e análise de documentos regulatórios. Desenvolvida em parceria entre estudantes do Inteli e o Bank of America, nossa plataforma, Vox, utiliza técnicas avançadas de Processamento de Linguagem Natural (PLN) para centralizar e otimizar o acesso a documentos normativos. No cenário atual, a crescente quantidade de documentos regulatórios e normativos gera um desafio significativo para empresas e profissionais que precisam acessar, interpretar e gerenciar essas informações de maneira eficiente. O processo manual de busca, categorização e análise é demorado e propenso a erros, resultando em atrasos, aumento de custos e potencial não conformidade com as regulações.

### 1.3.1 Descrição da Solução

&emsp;&emsp;O Vox é uma aplicação web que integra técnicas de PLN para proporcionar um sistema centralizado e automatizado de gerenciamento de documentos regulatórios. A plataforma aborda os principais desafios enfrentados no gerenciamento de normas, oferecendo uma interface intuitiva e funcionalidades avançadas para facilitar o trabalho dos usuários. Através do uso de PLN, a plataforma é capaz de buscar documentos regulatórios de diversas fontes de forma automática, eliminando a necessidade de pesquisas manuais. Utilizando algoritmos de machine learning, a solução categoriza os documentos de maneira precisa, garantindo que as informações relevantes sejam facilmente acessíveis.

&emsp;&emsp;Nossa solução extrai texto de documentos em formato PDF e outros formatos, transcreve áudio para texto e aplica tagueamento automático para facilitar a organização. Com a capacidade de analisar e interpretar o conteúdo dos documentos, a plataforma fornece resumos em bullet points e identifica o status das normas, como se estão revogadas ou se revogam outras normas. Ao centralizar os documentos regulatórios em uma única plataforma, oferecemos uma solução onde os usuários podem visualizar, adicionar, editar e baixar documentos de forma simples e eficiente. A busca avançada por rótulos e o processamento de áudio como entrada de pesquisa garantem que as informações sejam acessíveis de múltiplas maneiras, atendendo às diversas necessidades dos usuários.

&emsp;&emsp;Para manter os usuários sempre informados, a plataforma envia notificações automáticas sobre atualizações de documentos relevantes, novos documentos adicionados e quaisquer mudanças significativas. Essa funcionalidade garante que as empresas permaneçam em conformidade com as regulações vigentes sem a necessidade de monitoramento manual constante. A solução também facilita o compartilhamento de documentos por e-mail e permite aos usuários marcar regulamentações como favoritas, promovendo a colaboração entre equipes e a rápida disseminação de informações cruciais.

&emsp;&emsp;Dessa forma, o Vox representa um avanço significativo na gestão de documentos regulatórios, combinando a eficiência do processamento automatizado com a precisão do PLN. Essa abordagem permite uma classificação e organização mais rápida e precisa de grandes volumes de informações, além de identificar de forma automática mudanças e requisitos regulatórios, reduzindo significativamente o tempo e os recursos necessários para a conformidade.

### 1.3.2 Matriz de Riscos

&emsp;&emsp;A Matriz de Risco é uma ferramenta essencial para a avaliação e priorização de riscos em projetos e processos. Ela ajuda a identificar e classificar riscos com base em sua probabilidade de ocorrência e no impacto potencial que podem causar. A matriz organiza esses riscos em uma grade, permitindo visualizar quais são mais críticos e, portanto, requerem maior atenção e gestão.

&emsp;&emsp;Além de avaliar riscos, a matriz também identifica oportunidades—situações ou condições que, se exploradas, podem trazer benefícios significativos ou vantagens para o projeto. Essas oportunidades são analisadas para potencializar o crescimento e a melhoria.

&emsp;&emsp;Abaixo, a imagem da Matriz de Risco, que ilustra como os riscos e oportunidades são classificados e visualizados, em perspectiva do projeto.

<div align="center">
	<sub>Imagem x - Matriz de risco</sub>
	<img src="./assets/risk-matrix.png"/>
</div>

#### Planos de Ação para Ameaças

1. **Dificuldade em integrar scraping de sites com diferentes estruturas.**

- **Ação:** Desenvolver um sistema modular para scraping, permitindo a personalização para diferentes estruturas de sites ou adotar medidas alternativas que evita o uso do scraping.

2. **Má manipulação e criação de tags.**

- **Ação:** Validar tags que similares ou introduzir tags pré-criadas.

3. **Sobrecarga do sistema devido ao alto volume de dados processados diariamente.**

- **Ação:** Escalar a infraestrutura tecnológica para suportar grandes volumes de dados, utilizando técnicas como particionamento de dados e processamento paralelo. Monitorar continuamente o desempenho para ajustes proativos.

4. **Dependências e serviços externos se tornarem obsoletos, indisponíveis ou ineficazes.**

- **Ação:** Manter um inventário atualizado de todas as dependências externas e utilizar tecnologias para o gerenciamento de dependências, como o Dependabot, que monitora automaticamente as dependências do projeto presentes no package.json.

5. **Falhas de comunicação entre a equipe do projeto.**

- **Ação:** Promover reuniões regulares e o uso de ferramentas de comunicação eficazes. Estabelecer canais claros para feedback e resolução de problemas, garantindo que toda a equipe esteja alinhada com os objetivos do projeto.

6. **Informar regulamentações erradas.**

- **Ação:** Implementar um processo rigoroso de verificação de dados regulatórios antes da publicação. Considerar a integração com fontes confiáveis e atualizadas de informações regulatórias e realizar auditorias regulares para garantir a precisão.

7. **Vulnerabilidade no sistema de scraping.**

- **Ação:** Fortalecer a segurança do sistema de scraping, como a validação das páginas, para evitar que o scraper seja redirecionado para websites maliciosos.

8. **Falhas na classificação correta das normas devido a limitações do PLN.**

- **Ação:** Melhorar os modelos de processamento de linguagem natural (PLN) utilizando técnicas mais avançadas de machine learning e reforçando o treinamento com conjuntos de dados ampliados e diversificados.

9. **Falha no desempenho do chatbot devido a limitações do PLN.**

- **Ação:** Revisar e otimizar os algoritmos do chatbot para melhorar sua compreensão e interação. Realizar testes contínuos e ajustamentos baseados em feedback dos usuários para aumentar a eficácia do chatbot.

10. **Falta de organização para realizar as entregas dentro da data estipulada.**

- **Ação:** Adotar metodologias ágeis, como Scrum, para melhorar a organização e o planejamento das entregas. Definir metas claras e realizar sprints curtos para manter a equipe focada e dentro do cronograma.

#### Detalhamento das Oportunidades

1. **Monetização dos dados coletados através de API.**

- **Oportunidade:** Desenvolver e oferecer APIs que permitam a outras empresas acessar e utilizar os dados coletados, gerando uma nova fonte de receita. Garantir que a API seja bem documentada e fácil de integrar.

2. **Solução inovadora e facilmente utilizada por outras organizações.**

- **Oportunidade:** Criar uma solução flexível que possa ser facilmente adaptada e utilizada por diferentes organizações. Promover a solução como um serviço ou produto SaaS (Software as a Service).

3. **Capacidade de personalização da plataforma para novas regulamentações e scrapings.**

- **Oportunidade:** Investir em uma plataforma altamente personalizável que permita ajustes rápidos e eficientes para se adaptar a novas regulamentações e requisitos de scraping. Essa flexibilidade pode se tornar um diferencial competitivo no mercado.

4. **Expansão da solução para outros mercados ou setores com regulamentações complexas.**

- **Oportunidade:** Explorar a adaptação da solução para outros setores que também necessitam de gestão de dados, especialmente aqueles com regulamentações complexas. Isso pode abrir novas verticais de mercado e aumentar a base de clientes.

5. **Uma equipe muito boa e engajada com o projeto.**

- **Oportunidade:** Aproveitar a expertise e o engajamento da equipe para inovar e melhorar continuamente o produto. Manter a equipe motivada e fornecer oportunidades de desenvolvimento profissional para reter talentos.

6. **Grande quantidade de ferramentas prontas para serem utilizadas no projeto.**

- **Oportunidade:** Integrar as ferramentas existentes no projeto para acelerar o desenvolvimento e reduzir custos. Explorar maneiras de otimizar essas ferramentas para atender às necessidades específicas do projeto.

### 1.3.3 Estimativa de Investimentos

&emsp;&emsp;Para o desenvolvimento do Vox, solução proposta para o acompanhamento das mudanças regulatórias na indústria financeira no Brasil, é essencial realizar uma estimativa de investimento. Esse processo é fundamental, pois proporciona uma visão clara dos recursos financeiros necessários para a execução bem-sucedida do projeto, além de atuar como uma ferramenta estratégica para a gestão eficiente desses recursos. Uma estimativa de investimento detalhada permite identificar antecipadamente os custos envolvidos, facilitando a alocação adequada de recursos, a mitigação de riscos financeiros e assegurando que o projeto seja viável e sustentável ao longo de seu ciclo de vida.

&emsp;&emsp;A importância de uma estimativa de investimento bem elaborada se manifesta em diversas áreas críticas do gerenciamento de projetos. Primeiramente, ela permite um planejamento orçamentário preciso, garantindo que os stakeholders tenham uma compreensão clara do montante financeiro necessário, além disso, uma estimativa detalhada apoia a tomada de decisões estratégicas, como a priorização de funcionalidades e a escolha de tecnologias, com base em uma análise de custo-benefício. Estimar os investimentos necessários é essencial para avaliar a viabilidade econômica do projeto, permitindo determinar se os benefícios esperados justificam os custos e se o projeto é financeiramente sustentável.

&emsp;&emsp;Para elaborar uma estimativa de investimento para o projeto Vox, serão considerados, ao longo de um período de 12 meses, os custos relacionados aos desenvolvedores e à infraestrutura necessária. Com essas considerações, será possível construir uma estimativa precisa que orientará o gerenciamento financeiro do projeto em todas as suas fases.

### Desenvolvedores

&emsp;&emsp;Para calcular os custos com desenvolvedores para o projeto Vox, consideraremos uma equipe composta por cinco desenvolvedores juniores e um _Product Owner_ (PO), a fim de representar o contexto do desenvolvimento no Inteli. A escolha de desenvolvedores juniores traz a vantagem de oferecer novas perspectivas e promover um ambiente de aprendizado contínuo, especialmente no que diz respeito às práticas de desenvolvimento ágil. Embora tenham menos experiência, esses profissionais, sob a supervisão e orientação adequadas, podem contribuir de maneira significativa para o avanço do projeto, especialmente em tarefas que exigem alta produtividade e atenção a detalhes específicos.

&emsp;&emsp;O Product Owner, por sua vez, desempenha um papel crítico no sucesso do projeto, sendo o responsável por definir as prioridades e alinhar o desenvolvimento com os objetivos de negócio. Ele atua como o elo entre a equipe de desenvolvimento e os stakeholders, garantindo que o produto final atenda às expectativas e requisitos regulatórios. A presença de um PO experiente é essencial para assegurar que a equipe de desenvolvedores trabalhe de maneira eficiente e que o projeto avance conforme o planejado, minimizando riscos de desvios no escopo e nos prazos. Assim, ao considerar os custos dessa equipe, estamos garantindo um desenvolvimento com um foco claro na entrega de valor e na sustentabilidade financeira do projeto.

&emsp;&emsp;O custo com a equipe de desenvolvimento depende de diversos fatores, como o número de profissionais envolvidos, suas localizações geográficas, suas habilidades e a duração do projeto. Considerando que o desenvolvimento inicial da plataforma será realizado por uma equipe composta por cinco desenvolvedores juniores e um Product Owner, ao longo de 10 semanas no Brasil, é possível fazer a seguinte estimativa para este período:

| Cargo                | Salário Mensal | Período (meses) | Quantidade de Pessoas | Valor Total  |
| -------------------- | -------------- | --------------- | --------------------- | ------------ |
| Desenvolvedor Júnior | R$ 4,1 mil     | 2,5             | 5                     | R$ 51,25 mil |
| Product Owner        | R$ 11 mil      | 2,5             | 1                     | R$ 27,5 mil  |

&emsp;&emsp;Essa tabela representa os custos estimados para o desenvolvimento inicial de 10 semanas, totalizando **R$ 78.750,00**. Após esse período, considerando uma fase de manutenção contínua ao longo de 9,5 meses, a equipe será composta por um desenvolvedor sênior e dois desenvolvedores juniores. A estimativa de custos para essa fase é apresentada na tabela a seguir:

| Cargo                | Salário Mensal | Período (meses) | Quantidade de Pessoas | Valor Total  |
| -------------------- | -------------- | --------------- | --------------------- | ------------ |
| Desenvolvedor Júnior | R$ 4,1 mil     | 9,5             | 2                     | R$ 77,9 mil  |
| Desenvolvedor Sênior | R$ 11 mil      | 9,5             | 1                     | R$ 104,5 mil |

&emsp;&emsp;Somando o valor exposto na tabela, o custo total para a fase de manutenção contínua será de **R$ 182.400,00**. Portanto, ao somar os custos do desenvolvimento inicial de 2,5 meses e da manutenção de 9,5 meses, obtemos um valor total estimado de **R$ 261.150,00** para a equipe de desenvolvedores ao longo de 12 meses.

> Acesse a seção ["Referências"](#referências) deste documento [clicando aqui](#referências) para visualizar a fonte dos dados salariais.

### Infraestrutura

&emsp;&emsp;Para o desenvolvimento e operação do Vox, a infraestrutura tecnológica desempenha um papel fundamental, garantindo que a plataforma funcione de maneira eficiente, escalável e segura. A solução em _cloud computing_ oferece flexibilidade, escalabilidade sob demanda, e a possibilidade de minimizar investimentos iniciais em hardware. Portanto, a infraestrutura do nosso projeto será baseada na nuvem da Amazon Web Services (AWS), que é amplamente reconhecida por sua robustez, flexibilidade e segurança.

&emsp;&emsp;Os **servidores virtuais** hospedados na AWS (Amazon EC2) permitem que a equipe de desenvolvimento configure e gerencie facilmente os ambientes necessários para o desenvolvimento, teste e produção da plataforma. A AWS também oferece **serviços de banco de dados** gerenciados, como o Amazon RDS, que garantem alta disponibilidade e backups automáticos, reduzindo a complexidade operacional e os riscos de perda de dados.

&emsp;&emsp;O desenvolvimento visa uma infraestrutura que pode ser escalada conforme necessário, permitindo que a plataforma cresça junto com as demandas do negócio, sem comprometer a performance ou segurança. Essa abordagem também possibilita um controle mais eficiente dos custos, uma vez que os recursos são pagos conforme o uso, evitando gastos desnecessários. Abaixo, apresentamos uma estimativa detalhada dos custos relacionados aos principais componentes da infraestrutura que serão utilizados ao longo de 12 meses.

| Serviço                   | Custo Mensal Estimado | Período (meses) | Quantidade | Valor Total |
| ------------------------- | --------------------- | --------------- | ---------- | ----------- |
| Servidores Virtuais       | U$ 5,475              | 12              | 4          | U$ 262,80   |
| Banco de Dados Gerenciado | U$ 132,50             | 12              | 1          | U$ 1.590,00 |

&emsp;&emsp;Os Servidores Virtuais (Amazon EC2) são responsáveis por hospedar os ambientes de desenvolvimento, teste e produção da plataforma, e o Banco de Dados Gerenciado (Amazon RDS), é essencial para armazenar e gerenciar os dados da plataforma. Assim, o valor total estimado da infraestrutura para o projeto Vox ao longo de 12 meses é de U$ 1.852,80, em reais, em torno de **R$ 10.134,816**. Esta infraestrutura é dimensionada para garantir a eficiência, segurança e escalabilidade necessárias para o sucesso da plataforma.

> Clicando no seguinte link, é possível visualizar a simulação de preço da [instância EC2 e o banco de dados RDS.](./assets/cost-estimate.png)

### Valor total

&emsp;&emsp;A estimativa de investimentos para o desenvolvimento e operação do projeto Vox foi cuidadosamente elaborada, levando em consideração tanto os recursos humanos quanto a infraestrutura tecnológica necessária para garantir o sucesso do projeto. Portanto, ao combinar os custos de nuvem e desenvolvedores, o valor total estimado do investimento para o projeto Vox ao longo de 12 meses é de **R$ 271.284,82**. Este investimento garantirá que o projeto seja executado com sucesso, proporcionando uma solução robusta e escalável para o acompanhamento das mudanças regulatórias na indústria financeira.

> **Nota:** O custo da infraestrutura foi determinado com base na cotação do dólar estabelecida em R$5,47 em 16 de agosto de 2024. Estes valores estão sujeitos a flutuações cambiais.

### 1.3.4 Prova de Conceito (PoC)

&emsp;&emsp;A Prova de Conceito (PoC) visa validar a viabilidade técnica e funcional da solução Vox em um ambiente controlado. Durante esta fase, um protótipo básico será desenvolvido para demonstrar as funcionalidades principais, assegurando que o projeto atenda aos requisitos regulatórios e técnicos antes de se comprometer com a implementação completa.

&emsp;&emsp;A PoC difere da implementação completa principalmente em termos de infraestrutura. A equipe de desenvolvimento manterá sua estrutura original com cinco desenvolvedores juniores e um Product Owner (PO), garantindo assim a continuidade e consistência. No entanto, a infraestrutura será reduzida para suportar apenas o necessário para testar as funcionalidades essenciais, otimizando custos e recursos.

### Infraestrutura Simplificada para a PoC

&emsp;&emsp;Para a implementação da Prova de Conceito (PoC) do Vox, utilizaremos a estimativa de investimento original como referência, mas com ajustes na infraestrutura para reduzir os custos e atender apenas aos requisitos mínimos de validação.

&emsp;&emsp;No plano de investimento completo, a infraestrutura proposta inclui quatro servidores virtuais (Amazon EC2) e um banco de dados gerenciado (Amazon RDS) ao longo de 12 meses, totalizando U$ 262,80 para servidores e U$ 1.590,00 para o banco de dados. No entanto, para a PoC, simplificaremos a infraestrutura para uma configuração mínima, utilizando apenas um servidor virtual e sem banco de dados gerenciado. Essa configuração mais enxuta permite que a equipe valide as principais funcionalidades da plataforma sem incorrer nos custos completos da infraestrutura projetada para a implementação final.

Esta abordagem otimiza os recursos financeiros para a fase de PoC, permitindo uma redução substancial de custos enquanto ainda assegura a viabilidade técnica do projeto. Isso significa que o único servidor virtual será suficiente para suportar o ambiente de desenvolvimento da PoC, enquanto o banco de dados será substituído por uma solução alternativa, adequada para esta etapa preliminar.

&emsp;&emsp;Portanto, o custo seria em torno de:

| Serviço                   | Custo Mensal Estimado | Período (meses) | Quantidade | Valor Total |
| ------------------------- | --------------------- | --------------- | ---------- | ----------- |
| Servidores Virtuais       | U$ 5,475              | 2,5             | 1          | U$ 13,69    |

&emsp;&emsp;Com base nas adaptações feitas, estimamos que a infraestrutura necessária para validar as funcionalidades principais da solução ao longo de 2,5 meses (tempo de desenvolvimento inicial) envolverá um único servidor virtual, com um custo mensal de U$ 5,475. Ao considerar esse período, o custo total da infraestrutura será de aproximadamente U$ 13,69, em reais, **R$ 74,88**.

&emsp;&emsp;Essa configuração reduzida permite validar a viabilidade técnica do projeto de forma eficiente e econômica, aproveitando uma infraestrutura mínima suficiente para os testes iniciais, mas sem comprometer a performance necessária para as principais funcionalidades. Esta abordagem controlada otimiza o orçamento disponível e garante que a fase de PoC seja realizada com um custo acessível, atendendo aos requisitos preliminares do projeto antes de expandir para a implementação completa.

# 2. Entendimento do Design

&emsp;&emsp; O design desempenha um papel crucial na criação de uma experiência de usuário eficaz e intuitiva. No desenvolvimento do sistema "Vox", o entendimento do design vai além da estética, abrangendo a funcionalidade, a usabilidade e a acessibilidade da interface. Nosso objetivo é criar uma interface que não só seja visualmente atraente, mas que também facilite a interação do usuário com as funcionalidades do sistema de forma fluida e eficiente. Este entendimento nos guia na tomada de decisões que impactam diretamente a experiência final, garantindo que cada elemento do design contribua para a eficiência e a satisfação do usuário.

## 2.1 Estudo sobre o Usuário do Sistema

&emsp;&emsp; Compreender quem são os usuários do sistema "Vox" é fundamental para desenvolver uma solução que realmente atenda às suas necessidades. O estudo sobre o usuário do sistema envolve a análise de perfis, comportamentos, desafios e expectativas dos profissionais que lidam com regulamentações bancárias. A partir desse estudo, podemos adaptar as funcionalidades e o design do "Vox" para garantir que ele seja uma ferramenta útil e eficaz no dia a dia dos seus usuários, proporcionando uma experiência personalizada e otimizada para suas tarefas específicas, as seções a seguir são destacam esse entendimento do usuário.

### 2.1.1 Perfil do Usuário

&emsp;&emsp; Os perfis de usuários são essenciais para entender quem usará a solução desenvolvida, fornecendo uma visão macro e geral sobre os possíveis usuários finais. A análise desses perfis é crucial, pois permite identificar necessidades específicas, características de uso e comportamentos, além de alinhar os recursos da plataforma às expectativas e desafios dos usuários.

&emsp;&emsp; A importância dessa compreensão está em garantir que a solução atenda de forma eficiente às demandas dos diferentes grupos de usuários. Ao analisar os perfis, é possível identificar quais funcionalidades serão mais utilizadas, qual será a frequência de acesso e como cada grupo interage com a plataforma. Dessa forma, é possível personalizar a experiência de uso, garantindo tanto a usabilidade, focando no que é mais relevante pro perfil em questão, quanto a eficácia, atendendo às necessidades específicas de cada usuário.

&emsp;&emsp; Portanto, a seguir estão listadas as características, necessidades, interações com a plataforma, faixa etária e interesses do principal perfil de usuário da solução Vox, o Time de Compliance do Bank of America:

| Time de Compliance             | **Descrição**                                                                                                                                                                                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Características**            | Analistas de compliance responsáveis por garantir que a empresa atenda às normas regulatórias. Esses profissionais precisam acessar a plataforma regularmente para verificar mudanças regulatórias, revisar normas e ajustar processos internos para conformidade.           |
| **Necessidades**               | Uma plataforma eficiente e intuitiva para acompanhar mudanças regulatórias, com recursos para automação de tarefas repetitivas (scraping de normas, classificação e notificações), além de relatórios detalhados e consultas rápidas por texto ou tags.                      |
| **Interação com a plataforma** | Utilizam a plataforma para monitorar diariamente as normas e mudanças regulatórias, revisar e taguear novos documentos, e se manter atualizados sobre as regulamentações que impactam a instituição. Buscam otimizar o tempo e evitar penalidades devido a não conformidade. |
| **Faixa etária**               | De 25 a 45 anos, considerando que muitos analistas de compliance possuem uma formação sólida em finanças ou direito e já acumulam experiência no setor.                                                                                                                      |
| **Interesses**                 | Focados em assegurar conformidade com as normas, buscam eficiência operacional. Estão interessados em novas ferramentas que possam automatizar o monitoramento regulatório e facilitar o cumprimento das obrigações legais da empresa.                                       |

&emsp;&emsp; Ao entender o perfil do time de compliance e suas interações com a solução proposta, é possível refinar funcionalidades e garantir uma usabilidade otimizada. No próximo passo, será fundamental analisar o perfil da persona-chave, que representará um usuário típico da plataforma. Essa persona vai exemplificar com mais detalhes como essas necessidades se materializam no dia a dia de um analista de compliance.

### 2.1.2 Persona

&emsp;&emsp; Segundo Dam<sup>[7](#referências)</sup>, personas são representações fictícias de usuários reais que são criadas com o objetivo de ajudar designers, desenvolvedores e equipes de UX a compreender melhor os diferentes tipos de usuários que podem interagir com um produto ou serviço. Elas são construídas a partir de dados demográficos, comportamentais, necessidades e metas dos usuários reais.

&emsp;&emsp; As personas ajudam a entender melhor as necessidades, expectativas e desafios dos usuários, permitindo que criem experiências mais relevantes e eficazes. Logo, no contexto do Bank of America e do projeto Vox, a criação de personas é essencial para garantir que a solução atenda às dores e necessidades dos usuários finais, desde o desenvolvimento de funcionalidades até a criação de interfaces mais amigáveis e centradas.

<div align="center">
  <sub>Figura X: Persona do Projeto</sub>
  <img src="./assets/persona.png" alt=“Persona" width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox. Fotografia por thispersondoesnotexist.com</sup>
</div>

#### Informações da Persona:

| **Tópico**               | **Descrição**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nome                     | Leonardo Braga                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Idade                    | 37                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Profissão                | Analista de Compliance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Perfil Socioeconômico    | Classe média-alta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Background               | - Nasceu e mora em São Paulo/SP <br> - Casado e pai de dois filhos <br> - Graduado em Direito com especialização em Compliance <br> - Iniciou carreira em instituições financeiras locais <br> - Após se formar, entrou no Bank of America <br> - Alguns anos depois, tornou-se chefe da área de Compliance                                                                                                                                                                                                                                          |
| Personalidade            | - Precavido <br> - Estratégico <br> - Focado em Resultados <br> - Impaciente                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Interesses e Hábitos     | - Costume de revisão periódica de políticas internas <br> - Curioso em relação a tecnologia aplicada à compliance <br> - Apresenta uma rotina de trabalho bem estruturada, com horários bem definidos                                                                                                                                                                                                                                                                                                                                                |
| Dores e Necessidades     | - Automação do processo manual de busca e revisão de normas (Importância alta) <br> - Receber alertas automáticos sobre alterações regulatórias (Importância baixa) <br> - Um meio de pesquisa simplificado das normas dentro da plataforma (Importância média)                                                                                                                                                                                                                                                                                      |
| Citações diretas         | - "Quero garantir que o BofA esteja sempre em conformidade, mas não quero perder tempo com buscas manuais." <br> - "Perder uma atualização importante pode custar caro para a empresa, isso aumenta a pressão no nosso time." <br> - "Seria bom poder automatizar esse processo, aumentaria nossa eficiência e proatividade."                                                                                                                                                                                                                        |
| Interações com a Solução | Leonardo acessa a plataforma diariamente, principalmente no computador de mesa do escritório. <br><br> Ele abre a aplicação e visualiza as atualizações recentes, colocadas na plataforma de forma automatizada. A interface já destacou os documentos novos e a qual regulamentador ele pertence. <br><br> Leonardo filtra as normas por tags que ele definiu com base em áreas estratégicas do negócio. Após isso, também realiza uma busca em linguagem natural para revisar detalhes sobre uma norma específica solicitada por um dos diretores. |
| Letramento Digital       | Leonardo utiliza tecnologias diariamente, especificamente notebooks e celulares. Além disso, já está acostumado com os processos do banco e como o sistema funcionaria. <br><br> Entretanto, apesar da familiaridade com as ferramentas, pode ter dificuldades com tecnologias complexas demais ou interfaces complicadas.                                                                                                                                                                                                                           |

&emsp;&emsp; Portanto, a persona de Leonardo Braga representa um usuário típico da plataforma Vox, um analista de compliance experiente e focado em resultados. Suas dores e necessidades refletem os desafios enfrentados por profissionais de compliance no dia a dia, como a necessidade de automatizar processos manuais, receber alertas sobre alterações regulatórias e simplificar a pesquisa de normas. Ao compreender as características, comportamentos e expectativas do Leonardo, a equipe Vox pode projetar uma solução que atenda às suas necessidades e proporcione uma experiência de usuário satisfatória para todos que compartilham um perfil semelhante.

### 2.1.3 Jornada do Usuário

&emsp;&emsp;A jornada do usuário é um conceito essencial no desenvolvimento de soluções tecnológicas centradas nas necessidades dos usuários. Ela representa, de maneira visual e descritiva, todas as etapas que um usuário percorre ao interagir com um sistema, desde o primeiro contato até a conclusão de uma tarefa específica. Ao mapear as ações, pensamentos e emoções do usuário em cada ponto de interação, a jornada oferece uma visão sobre como ele navega pela interface, quais são suas expectativas e onde podem surgir dificuldades ou oportunidades de melhoria.

&emsp;&emsp;Compreender essa jornada é crucial para aprimorar a experiência de uso, pois permite identificar pontos de frustração e otimizar o fluxo de interação para torná-lo mais intuitivo e agradável. Além disso, esse entendimento ajuda a alinhar o sistema às expectativas dos utentes, priorizando funcionalidades que realmente agreguem valor e contribuam para a eficiência e produtividade no uso da plataforma. Ao antecipar possíveis problemas e adaptar o sistema às necessidades reais, a jornada do usuário contribui para o sucesso da solução, garantindo que ela seja satisfatória e eficaz para os usuários finais. Abaixo mostramos algumas jornadas na plataforma Vox.

### Jornada I - Busca por normas

<div align="center">
  <sub>Figura x: Jornada do usuário I</sub>
  <img src="./assets/user-journey.jpg" width="100%" alt='Jornada do usuário I'>
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

&emsp;&emsp;A imagem acima representa a interação do Leonardo Braga, analista de compliance do BofA, com a plataforma ao buscar atualizações específicas em normas regulatórias, desde o momento em que acessa a plataforma até o compartilhamento dos resultados com sua equipe. O fluxo descrito destaca a experiência fluida e centrada em eficiência e simplicidade, ressaltando a importância de funcionalidades avançadas como o reconhecimento de voz e o Processamento de Linguagem Natural (PLN). Ao permitir que Leonardo dite termos de busca diretamente na barra de pesquisa, o Vox proporciona uma experiência mais intuitiva e direta, além disso, o PLN assegura que os termos de busca sejam compreendidos e processados com alta precisão, garantindo resultados relevantes e acionáveis.

### Jornada II - Notificações

<div align="center">
  <sub>Figura x: Jornada do usuário II</sub>
  <img src="./assets/user-journey2.jpg" width="100%" alt='Jornada do usuário II'>
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

&emsp;&emsp;Essa jornada de monitoramento e recebimento de alertas automatizados complementa a busca manual, garantindo que Leonardo esteja sempre atualizado sem a necessidade de estar constantemente monitorando as normas. Ao receber notificações automáticas, revisar as atualizações e compartilhá-las com sua equipe, Leonardo consegue gerenciar as exigências regulatórias de forma proativa e eficiente, minimizando riscos de não conformidade.

&emsp;&emsp;As jornadas mapeadas acima para a plataforma Vox, centradas nas necessidades do analista de compliance Leonardo Braga, demonstram como uma compreensão profunda das interações do usuário pode transformar a experiência de uso. Desde a busca por atualizações regulatórias específicas até o monitoramento contínuo de mudanças normativas, cada jornada foi projetada para maximizar a eficiência e minimizar frustrações, garantindo que a plataforma atenda de forma precisa e intuitiva às demandas dos usuários.

&emsp;&emsp;Esses exemplos reforçam o papel central que a jornada do usuário desempenha no desenvolvimento de soluções tecnológicas eficazes. Ao alinhar o sistema às necessidades reais dos usuários, a plataforma Vox proporciona uma experiência intuitiva, produtiva e vantajosa.

## 2.2 Proposta de UX para o Sistema

&emsp;&emsp;A proposta de UX para o sistema "Vox" visa proporcionar uma interação dinâmica, personalizável e intuitiva. Inspirada em designs modernos, como os do G1 e do Chat GPT, a interface sugere, desde o primeiro acesso, que o usuário interaja com a IA para fazer perguntas sobre regulamentações. Além disso, filtros específicos são oferecidos para facilitar a busca e a captura de informações nas normas exibidas, garantindo uma experiência de navegação fluida e eficiente.

&emsp;&emsp;Outra funcionalidade destacada é a edição de Tags. Na página dedicada a essa função, o usuário tem a liberdade de habilitar ou desabilitar Tags conforme sua relevância. Essas configurações impactam diretamente as Tags que o modelo de PLN atribui após o processo de Scraping nos documentos de normas, permitindo uma personalização ainda maior na organização e pesquisa dos conteúdos.

&emsp;&emsp;Essas funcionalidades foram estabelecidas com o objetivo de oferecer ao usuário uma ferramenta ágil, capaz de buscar atualizações e realizar consultas às normas bancárias com máxima rapidez e eficiência. Diferente de um Chat Bot tradicional, que se concentra em interações prolongadas e conversacionais entre o usuário e a Inteligência Artificial, o sistema "Vox" prioriza a rapidez e a objetividade na obtenção de informações. A experiência do usuário é, portanto, centrada na eficiência e precisão, garantindo que ele possa acessar as informações necessárias de forma direta e sem complicações. O foco não está em prolongar a interação, mas em fornecer respostas rápidas e relevantes que atendam às necessidades específicas do usuário no contexto bancário.

&emsp;&emsp;As imagens a seguir compõem o Wireframe da solução, detalhando as principais telas e interações planejadas para o sistema "Vox":

### Wireframe

- **Home:**

  <div align="center">
  <sub>Imagem X - Home Wireframe</sub>
  <img src="../assets/homewireframe.png"/>

  </div>

  &emsp;&emsp;Na tela inicial, o sistema apresenta um campo de pesquisa que aceita comandos de voz ou texto em linguagem natural. No menu lateral esquerdo, o usuário pode acessar um "portal" específico para visualizar documentos relacionados a um órgão regulador particular, facilitando a navegação e a organização dos documentos relevantes.

- **Campo de Pesquisa:**

  <div align="center">
  <sub>Imagem X - Resultado de pesquisa Wireframe</sub>
  <img src="../assets/resultadopesquisawireframe.png"/>

  </div>

  &emsp;&emsp;Esta tela exibe os resultados da pesquisa, apresentando resumos dos documentos encontrados e oferecendo a opção de "ver mais" por meio de uma seta para baixo. No canto inferior esquerdo, há a possibilidade de "adicionar" documentos manualmente. Essa função é especialmente útil para garantir a atualização do banco de dados, mesmo em caso de mudanças repentinas nos sites dos órgãos reguladores.

- **Filtro:**

  <div align="center">
  <sub>Imagem X - Filtro Wireframe</sub>
  <img src="../assets/filtrowireframe.png"/>

  </div>

  &emsp;&emsp;A interface de filtros está localizada na parte superior da tela, com Tags que servem como filtros para refinar os resultados de pesquisa. Essa funcionalidade permite que o usuário adapte as pesquisas conforme suas necessidades específicas.

- **Tags:**

  <div align="center">
  <sub>Imagem X - Seleção de Tags Wireframe</sub>
  <img src="../assets/visualizacaotagswireframe.png"/>

  </div>

&emsp;&emsp;Na tela de seleção de Tags, acessível pelo menu lateral esquerdo, o usuário pode visualizar as Tags recomendadas pelo modelo de PLN, bem como selecionar aquelas que fazem mais sentido ou adicionar novas Tags conforme necessário. Isso proporciona uma maior personalização e controle sobre as buscas e categorização dos documentos.

&emsp;&emsp;Em conclusão, o sistema "Vox" foi concebido para revolucionar a forma como os usuários interagem com regulamentações bancárias, oferecendo uma solução rápida, eficiente e altamente personalizável. Ao combinar uma interface intuitiva com funcionalidades avançadas, como a edição de Tags e filtros inteligentes, o "Vox" não apenas facilita a busca por informações, mas também garante que os usuários tenham acesso às normas mais relevantes de maneira simples e direta.

&emsp;&emsp;A proposta de UX prioriza a objetividade e a eficiência, atendendo às necessidades dos profissionais que lidam diariamente com a complexidade das regulamentações. Assim, o "Vox" se posiciona como uma ferramenta indispensável no contexto bancário, oferecendo uma experiência que alia praticidade e precisão, ajudando os usuários a manterem-se atualizados e informados com agilidade.

## 2.3 Pilha de Tecnologias para Implementação do Sistema

A arquitetura do sistema foi projetada com base em uma abordagem modular, utilizando serviços em nuvem, microserviços e tecnologias que garantem escalabilidade e resiliência. A seguir, são descritas as principais tecnologias utilizadas na implementação do sistema.

#### Serviços EC2 da AWS

Os componentes do sistema são distribuídos em várias instâncias EC2 da AWS. Cada serviço roda em sua própria instância, proporcionando maior flexibilidade, controle sobre a configuração dos servidores e escalabilidade horizontal conforme necessário. Essa estrutura garante que cada serviço opere de forma independente, facilitando a manutenção e o monitoramento.

Os principais serviços hospedados em EC2 incluem:

- **Scraping Service**: Responsável pela coleta automática de dados regulatórios de diferentes fontes, essencial para garantir a atualização constante das informações no sistema.
- **STT Service (Speech-to-Text)**: Implementa funcionalidades de conversão de áudio para texto, permitindo a transcrição de arquivos de áudio para posterior processamento.
- **PLN Service**: Processa os dados textuais (no caso do aúdio, após conversão) utilizando técnicas de Processamento de Linguagem Natural (PLN), essenciais para a interpretação e classificação de conteúdos extraídos.
- **Regulation Service**: Analisa e classifica automaticamente as mudanças nas regulamentações, enviando notificações e atualizações conforme necessário.

A utilização de instâncias EC2 permite uma escalabilidade ajustada à demanda de cada serviço, otimizando o desempenho do sistema como um todo.

#### Banco de Dados RDS (PostgreSQL)

O sistema utiliza o **Amazon RDS** com PostgreSQL como seu banco de dados principal. O RDS é uma solução gerenciada que oferece backups automáticos, recuperação em caso de falha e escalabilidade horizontal. O banco de dados armazena todas as informações estruturadas, incluindo dados regulatórios, transcrições e históricos de processamento. 

As vantagens do RDS incluem:
- **Disponibilidade e Recuperação**: Backup automatizado e recuperação rápida em caso de falhas.
- **Escalabilidade**: Capacidade de ajustar automaticamente os recursos conforme o aumento da demanda.
- **Segurança**: Suporte para criptografia de dados em trânsito e em repouso, além de gerenciamento de acesso baseado em políticas.

#### Mensageria - RabbitMQ

A comunicação entre os diferentes serviços é realizada de forma assíncrona utilizando o **RabbitMQ** como fila de mensagens. RabbitMQ é uma ferramenta de mensageria que permite que os serviços enviem e recebam mensagens de forma eficiente, garantindo que os componentes do sistema possam operar de maneira desacoplada e escalável.

A principal função do RabbitMQ no sistema é garantir a comunicação fluida entre os serviços, especialmente em cenários de alta carga. Ele distribui as mensagens entre os componentes do sistema, evitando sobrecarregar qualquer serviço específico.

Benefícios do uso do RabbitMQ:
- **Desacoplamento**: Permite que os serviços operem independentemente, mesmo em situações de falha temporária.
- **Resiliência**: A fila de mensagens garante que as requisições não se percam, mesmo em momentos de pico de tráfego.
- **Escalabilidade**: Facilidade de adicionar novos consumidores de mensagens conforme o aumento da demanda.

#### Arquitetura de Microserviços

O sistema foi desenvolvido utilizando uma arquitetura de microserviços, onde cada componente executa uma função específica de forma independente. Isso permite que cada serviço seja desenvolvido, testado e implantado separadamente, aumentando a flexibilidade e facilitando a evolução contínua do sistema.

Os microserviços são ideais para grandes sistemas distribuídos, pois oferecem as seguintes vantagens:
- **Modularidade**: Facilita a implementação de novas funcionalidades ou atualizações sem impacto em outros serviços.
- **Escalabilidade Independente**: Cada serviço pode ser escalado individualmente de acordo com a sua demanda.
- **Resiliência**: A falha de um serviço não compromete o funcionamento dos outros, aumentando a disponibilidade do sistema.

#### Segurança

A segurança foi uma prioridade na implementação da arquitetura. Todos os serviços utilizam criptografia para proteger os dados em trânsito e em repouso. Além disso, o acesso aos serviços e dados é controlado por meio de políticas de acesso baseadas em funções (RBAC), garantindo que apenas usuários autorizados possam interagir com o sistema.

O uso de VPCs (Virtual Private Clouds) da AWS também garante que os serviços sejam isolados em uma rede privada, protegendo-os de acessos não autorizados.

#### Containerização com Docker e Orquestração com Kubernetes

Neste projeto temos a containerização dos serviços com **Docker**, permitindo que cada microserviço seja isolado em um contêiner padronizado. Isso traria os seguintes benefícios:
- **Portabilidade**: A possibilidade de rodar o sistema em qualquer ambiente, sem preocupações com diferenças de configuração.
- **Facilidade de Deployment**: Os contêineres podem ser facilmente implantados em diferentes ambientes, facilitando o CI/CD.
- **Melhor Controle de Dependências**: Cada serviço teria suas dependências encapsuladas, eliminando conflitos entre versões de bibliotecas.

Aliado a isso, a adoção de um orquestrador de contêineres como o **Kubernetes** traz vantagens em termos de:
- **Autoescalabilidade**: Kubernetes pode escalar automaticamente os serviços com base no tráfego, sem necessidade de intervenção manual.
- **Recuperação Automática de Falhas**: Em caso de falha de algum serviço, o Kubernetes pode reiniciar automaticamente os contêineres comprometidos.
- **Gerenciamento Simplificado de Deployments**: Kubernetes facilita o processo de rollbacks, atualizações contínuas e monitoramento de clusters.

Dessa forma, a combinação de todas essas tecnologias no nosso projeto é a mais adequada considerando termos de aprendizagem (possíveis de aprender no prazo do projeto), disponibilidade (gratuitos) e acadêmicos, isto é, alinhados ao conteúdo Processamento de linguagem Natural".

## 2.4 Mockups do Sistema

&emsp;&emsp; Mockup é uma representação visual de um projeto de design, que permite aos desenvolvedores e stakeholders visualizar a aparência e a interação de uma aplicação antes de sua implementação, sendo um aprimoramento do wireframe por adicionar elementos visuais, cores e outros elementos de design. Os mockups são essenciais para validar o design, a usabilidade e a experiência do usuário, garantindo que a solução proposta atenda às expectativas e necessidades dos usuários finais. A seguir, estão as principais páginas do sistema Vox.

### Tela Inicial

&emsp;&emsp; A tela inicial do Vox apresenta um design limpo e sumarizando as principais funcionalidades e métodos de pesquisa que um usuário utilizaria, com um campo de pesquisa centralizado que aceita comandos de voz e texto em linguagem natural. O menu lateral esquerdo oferece acesso rápido a diferentes seções da plataforma, como explorar, tags e visualizar por regulador específico (contando com notificações para atualizações de normas), proporcionando uma navegação simplificada e eficiente.

<div align="center">
  <sub>Figura X: Vox - Tela Inicial</sub>
  <img src="./assets/Mockup/home.png" alt="Tela Inicial da solução Vox" width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

&emsp;&emsp; A expansão do menu lateral exibe as opções disponíveis para o usuário, sendo as mesmas citadas anteriormente, trazendo labels para facilitar a identificação e a navegação. A interface foi projetada para que, após o usuário se familiarizar com o sistema, ele possa acessar rapidamente as funcionalidades desejadas sem necessitar da expansão do menu, tornando a experiência mais fluida.

<div align="center">
  <sub>Figura X: Vox - Tela Inicial com Menu Expandido</sub>
  <img src="./assets/Mockup/home-expanded-menu.png" alt="Tela Inicial da solução Vox com menu lateral expandido" width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

### Tela de Resultados / Explorar

&emsp;&emsp; A tela de resultados de pesquisa exibe os documentos encontrados após a busca, com resumos e opções para visualizar mais detalhes. É possível adicionar ou remover os filtros de pesquisa, personalizando a busca de acordo com as necessidades. Os resultados são organizados de forma clara e concisa, através de cards, facilitando a identificação e seleção dos documentos relevantes. A barra de pesquisa permanece visível na parte superior da tela, permitindo que o usuário refine a pesquisa ou inicie uma nova busca a qualquer momento.

<div align="center">
  <sub>Figura X: Vox - Tela de Resultado de Buscas</sub>
  <img src="./assets/Mockup/search.png" alt="Tela de resultados de pesquisas da solução Vox" width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

### Tela de Regulamentações

&emsp;&emsp; A tela de regulamentações exibe os detalhes das regulamentações disponíveis no sistema, após a seleção de um documento específico dentro da aba Explorar. Os detalhes incluem informações sobre a norma, data de publicação, tags associadas e um resumo do conteúdo. O usuário pode visualizar o documento completo, ver normas relacionadas com aquele documento no formato de links e ser redirecionado para a página da onde a norma foi retirada.

<div align="center">
  <sub>Figura X: Vox - Tela de Regulamentações</sub>
  <img src="./assets/Mockup/reg-details.png" alt="Tela de regulamentações da solução Vox" width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

&emsp;&emsp; Os mockups apresentados acima representam a interface do sistema Vox, projetada para estudar e planejar uma melhor experiência de usuário. A navegação simplificada através dos mecanismos na barra lateral, a organização dos resultados e a interação fluida com os documentos regulatórios são elementos essenciais para garantir que os analistas de compliance do BofA possam acessar as informações necessárias de forma rápida e produtiva.

# 3. Entendimento da Arquitetura do Sistema

&emsp;&emsp; A arquitetura do sistema apresentada é composta por vários componentes distribuídos, utilizando serviços da AWS (Amazon Web Services). A seguir está uma explicação detalhada de cada componente:

Front-End (Desktop):

&emsp;&emsp;O usuário final interage com o sistema através de uma interface desktop, que é responsável por enviar e receber dados via o BFF (Backend for Frontend).
&emsp;&emsp;O front-end será desenvolvido utilizando Next.js, uma estrutura de React para a construção de interfaces modernas e responsivas.
BFF (Backend for Frontend):

Esta camada age como intermediária entre o front-end e os serviços de backend.
Centraliza as chamadas das APIs e facilita a comunicação entre o front-end e os diferentes microserviços e banco de dados.
Implementada em uma instância EC2 na AWS, garantindo escalabilidade e segurança.

Serviços EC2:

A arquitetura é composta por vários microserviços, cada um hospedado em uma instância EC2 na AWS:
PLN (Processamento de Linguagem Natural): Microserviço dedicado ao processamento e análise de dados textuais, utilizando técnicas de NLP.
Scraping: Responsável por extrair dados da web de forma automatizada, preparando-os para serem armazenados e processados.
Regulamentação: Focado em verificar e garantir que os dados e processos estejam em conformidade com as normas e regulamentos aplicáveis e fazer o 'check' de atualizações, quando comparado ao dia anterior.
Banco de Dados (RDS):

O sistema utiliza o serviço RDS (Relational Database Service) da AWS para gerenciar seu banco de dados relacional.
Este banco de dados armazena todas as informações coletadas e processadas pelos microserviços, como os resultados de scraping, análise de linguagem, e informações regulamentares.

## 3.1 Proposta de Arquitetura do Sistema

A proposta da arquitetura do sistema visa fornecer uma solução escalável, modular e segura, utilizando serviços da AWS para atender às necessidades de processamento de linguagem natural, scraping de dados e conformidade regulamentar. A arquitetura foi desenhada para garantir que cada serviço seja independente, facilitando o desenvolvimento, manutenção e escalabilidade do sistema.

<div align="center">
	<sub>Imagem X - Diagrama de arquitetura</sub>
	<img src="./assets/arquitetura.png"/>
</div>

Escolha das Tecnologias:

Back-End: Desenvolvido em Python, devido à sua simplicidade, versatilidade e grande quantidade de bibliotecas para processamento de linguagem natural e scraping.
Front-End: Implementado em Next.js, escolhido pela sua capacidade de renderização server-side, SEO otimizado, e suporte a funcionalidades modernas de React.
Nuvem: AWS é utilizada pela sua confiabilidade, variedade de serviços e facilidade de integração. O uso de instâncias EC2 permite escalabilidade automática, enquanto o RDS garante a integridade e disponibilidade dos dados.
Camada BFF:

&emsp;&emsp;A introdução do BFF ajuda a separar o front-end do back-end, permitindo que a lógica de negócios e chamadas API sejam centralizadas.
&emsp;&emsp;Além disso, facilita a adaptação do sistema a diferentes plataformas (web, mobile) e melhora a performance geral ao reduzir a carga no front-end.

### Arquitetura de Microserviços:

&emsp;&emsp;O uso da arquitetura de microserviços promove modularidade, permitindo que cada serviço evolua de forma independente, além de simplificar o processo de teste e implantação.  
&emsp;&emsp;Dessa forma, a implementação de cada serviço em instâncias EC2 oferece flexibilidade na escolha de recursos, e a escalabilidade automática garante que o sistema possa lidar com variações na carga de trabalho.

### Banco de Dados:

&emsp;&emsp;O uso do RDS na AWS garante um banco de dados relacional robusto e de alta disponibilidade, com backups automáticos e failover em caso de falha, garantindo a continuidade do serviço.
&emsp;&emsp;Nesse cenário, a separação dos dados em diferentes serviços facilita a manutenção e segurança, ao permitir que cada serviço tenha acesso apenas aos dados necessários.

&emsp;&emsp;Dessa forma, a arquitetura proposta é altamente flexível, permitindo fácil adaptação e expansão conforme as necessidades do negócio evoluem. A utilização dos serviços da AWS proporciona uma infraestrutura robusta, escalável e segura, que suporta o desenvolvimento ágil e a entrega contínua de funcionalidades.

## 3.2 Requisitos Funcionais e Não Funcionais do Sistema

&emsp;&emsp; Requisitos, no contexto de um projeto de software, são as funcionalidades e características que o sistema deve possuir para atender às necessidades dos usuários e do negócio. Eles são divididos em dois tipos: requisitos funcionais e requisitos não funcionais. Os requisitos funcionais são as funcionalidades que o sistema deve possuir, enquanto os requisitos não funcionais são as características que o sistema deve ter, como desempenho, segurança e usabilidade.

&emsp;&emsp; Nesta seção, serão apresentados os requisitos funcionais e não funcionais do sistema, bem como os casos de teste associados a cada requisito.

### 3.2.1 Requisitos Funcionais

### Requisitos de Sistema

#### RF-01: Identificação e Acesso às Fontes

O sistema deve acessar os sites dos órgãos regulamentadores para identificar novas LRRs.

**Casos de Teste**

| ID    | Descrição                                                                               |
| ----- | --------------------------------------------------------------------------------------- |
| CT-01 | Verifica se o sistema acessa os sites dos órgãos regulamentadores conforme agendamento. |
| CT-02 | Verifica se o sistema é capaz de contornar captchas simples.                            |
| CT-03 | Verifica se o sistema identifica atualizações ou novas LRRs.                            |

<br>

#### RF-02: Coleta e Download de Documentos

O sistema deve coletar e fazer o download dos documentos identificados para um repositório.

**Casos de Teste**

| ID    | Descrição                                                                                   |
| ----- | ------------------------------------------------------------------------------------------- |
| CT-04 | Verifica se o sistema consegue coletar documentos em diferentes formatos (PDF, _raw text_). |
| CT-05 | Verifica se o download dos documentos é feito corretamente e sem falhas.                    |
| CT-06 | Verifica se a integridade dos documentos após o download não estão comprometidas.           |

<br>

#### RF-03: Processamento e Extração de Dados

O sistema deve processar e extrair dados relevantes dos documentos.

**Casos de Teste**

| ID    | Descrição                                                                |
| ----- | ------------------------------------------------------------------------ |
| CT-07 | Verifica se o sistema extrai corretamente os dados chave dos documentos. |
| CT-08 | Verifica a precisão do OCR ao extrair texto de PDFs.                     |

<br>

#### RF-04: Inserir e Atualizar Normas na Aplicação

O sistema deve inserir as normas processadas na aplicação web.

**Casos de Teste**

| ID    | Descrição                                                                     |
| ----- | ----------------------------------------------------------------------------- |
| CT-09 | Verifica se as normas são inseridas corretamente no banco de dados.           |
| CT-10 | Verifica se as atualizações em normas existentes são refletidas corretamente. |

<br>

#### RF-05: Mostrar Resumo da Norma com IA

O sistema deve ser capaz de gerar um resumo automatizado das normas dentro da aplicação.

**Casos de Teste**

| ID    | Descrição                                                                            |
| ----- | ------------------------------------------------------------------------------------ |
| CT-11 | Verifica se o resumo gerado pela IA está de acordo com o conteúdo da norma original. |
| CT-12 | Verifica a precisão das informações chave no resumo gerado.                          |

<br>

#### RF-06: Atualizar Status de Revogação de Normas

O sistema deve atualizar se uma norma está revogada ou não e, caso revogue alguma norma, indicar qual.

**Casos de Teste**

| ID    | Descrição                                                                                |
| ----- | ---------------------------------------------------------------------------------------- |
| CT-13 | Verifica se o sistema indica corretamente quando uma norma está revogada.                |
| CT-14 | Verifica se o sistema mostra corretamente qual norma foi revogada pela norma em questão. |
| CT-15 | Verifica se o sistema mostra quais normas estão vigentes dentro das normas revogadas.    |

<br>

#### RF-07: Classificação e Tags

O sistema deve classificar e taguear cada norma com base no processamento de linguagem.

**Casos de Teste**

| ID    | Descrição                                                                      |
| ----- | ------------------------------------------------------------------------------ |
| CT-16 | Verifica se o sistema classifica corretamente as normas.                       |
| CT-17 | Verifica se as tags atribuídas são armazenadas corretamente no banco de dados. |

<br>

#### RF-08: Envio de Notificações

O sistema deve enviar notificações automáticas quando normas são adicionadas ou atualizadas.

**Casos de Teste**

| ID    | Descrição                                                                         |
| ----- | --------------------------------------------------------------------------------- |
| CT-18 | Verifica se as notificações são enviadas corretamente para as normas atualizadas. |
| CT-19 | Verifica se o conteúdo das notificações está correto e relevante.                 |

<br>

#### RF-09: Destacar Novos Documentos

O sistema deve destacar automaticamente os novos documentos adicionados.

**Casos de Teste**

| ID    | Descrição                                                                           |
| ----- | ----------------------------------------------------------------------------------- |
| CT-20 | Verifica se os novos documentos são destacados corretamente.                        |
| CT-21 | Verifica se o destaque permanece até que o documento seja visualizado pelo usuário. |

<br>

### Requisitos de Usuário

Abaixo, são listados os requisitos funcionais relacionados diretamente ao que o usuário deseja fazer na plataforma. Esses requisitos estão ligados a um caso de uso adequado ao contexto.

#### RF-10: Adicionar Documentos Manualmente

O usuário deve ser capaz de adicionar documentos à base de dados manualmente.

**Casos de Teste**

| ID    | Descrição                                                                       |
| ----- | ------------------------------------------------------------------------------- |
| CT-22 | Verifica se o usuário pode adicionar documentos manualmente na aplicação.       |
| CT-23 | Verifica se os documentos adicionados manualmente são processados corretamente. |

---

#### UC-10: Adicionar Documentos Manualmente

**Ator Primário:** Usuário/Analista de Documentos Normativos

**Descrição:** O usuário deve ser capaz de adicionar documentos à base de dados manualmente.

**Fluxo Principal:**

1. O usuário acessa a seção de documentos na aplicação.
2. O usuário seleciona a opção de adicionar novo documento.
3. O sistema exibe um formulário para upload de documentos.
4. O usuário preenche as informações necessárias e faz o upload do documento.
5. O sistema salva o documento na base de dados e confirma a adição.

**Fluxos Alternativos:** Se o usuário não preencher todas as informações obrigatórias, o sistema exibe uma mensagem de erro e solicita a correção.

**Pré-condições:** O usuário deve ter um documento baixado para poder adicioná-lo.

**Pós-condições:** O documento é adicionado à base de dados e pode ser acessado e visualizado.

---

#### RF-11: Buscar Normas por Texto ou Tags

O usuário deve ser capaz de buscar normas utilizando linguagem natural ou tags.

**Casos de Teste**

| ID    | Descrição                                                                 |
| ----- | ------------------------------------------------------------------------- |
| CT-24 | Verifica se a busca por linguagem natural retorna os resultados corretos. |
| CT-25 | Verifica se a busca por tags retorna os resultados corretos.              |

---

#### UC-11: Buscar Normas por Texto ou Tags

**Ator Primário:** Usuário/Analista de Documentos Normativos

**Descrição:** O usuário deve ser capaz de buscar normas utilizando linguagem natural ou tags.

**Fluxo Principal:**

1. O usuário acessa a seção de busca na aplicação.
2. O usuário digita um termo de busca ou seleciona tags associadas a normas.
3. O sistema processa a busca e exibe os resultados relevantes.

**Fluxos Alternativos:** Se não houver resultados para a busca, o sistema informa o usuário e sugere termos alternativos.

**Pré-condições:** O usuário deve realizar a busca em Português do Brasil.

**Pós-condições:** Os resultados da busca são exibidos ao usuário.

---

#### RF-12: Pesquisa de Normas por Áudio

O usuário deve ser capaz de realizar pesquisas de normas por comandos de áudio.

**Casos de Teste**

| ID    | Descrição                                                                     |
| ----- | ----------------------------------------------------------------------------- |
| CT-26 | Verifica se a pesquisa por áudio é transcrita corretamente em texto.          |
| CT-27 | Verifica se os resultados da pesquisa por áudio correspondem ao comando dado. |

---

#### UC-12: Pesquisa de Normas por Áudio

**Ator Primário:** Usuário/Analista de Documentos Normativos

**Descrição:** O usuário deve ser capaz de realizar pesquisas de normas por comandos de áudio.

**Fluxo Principal:**

1. O usuário acessa a seção de busca por áudio na aplicação.
2. O usuário grava um comando de voz.
3. O sistema transcreve o áudio em texto.
4. O sistema processa a busca com base na transcrição e exibe os resultados relevantes.

**Fluxos Alternativos:** Se a transcrição não for precisa, o usuário pode editar o texto manualmente antes de realizar a busca.

**Pré-condições:** O usuário deve falar em Português do Brasil.

**Pós-condições:** Os resultados da busca são exibidos ao usuário.

---

#### RF-13: Visualizar Documentos

O usuário deve ser capaz de visualizar documentos na plataforma.

**Casos de Teste**

| ID    | Descrição                                                       |
| ----- | --------------------------------------------------------------- |
| CT-28 | Verifica se os documentos podem ser visualizados corretamente.  |
| CT-29 | Verifica se os documentos são exibidos em seu formato original. |

---

#### UC-13: Visualizar Documentos

**Ator Primário:** Usuário/Analista de Documentos Normativos

**Descrição:** O usuário deve ser capaz de visualizar documentos na plataforma.

**Fluxo Principal:**

1. O usuário acessa a lista de documentos.
2. O usuário seleciona um documento para visualizar.
3. O sistema exibe o documento no formato original.

**Fluxos Alternativos:** Se o documento não puder ser visualizado, o sistema exibe uma mensagem de erro.

**Pré-condições:** O documento deve estar disponível no sistema.

**Pós-condições:** O documento é exibido corretamente ao usuário.

---

#### RF-14: Adicionar, Remover e Editar Tags de Normas

O usuário deve ser capaz de adicionar, remover e editar tags associadas a normas.

**Casos de Teste**

| ID    | Descrição                                                         |
| ----- | ----------------------------------------------------------------- |
| CT-30 | Verifica se o usuário pode adicionar novas tags a uma norma.      |
| CT-31 | Verifica se o usuário pode remover tags existentes de uma norma.  |
| CT-32 | Verifica se o usuário pode editar tags já associadas a uma norma. |

---

#### UC-14: Adicionar, Remover e Editar Tags de Normas

**Ator Primário:** Usuário/Analista de Documentos Normativos

**Descrição:** O usuário deve ser capaz de adicionar, remover e editar tags associadas a normas.

**Fluxo Principal:**

1. O usuário acessa a seção de gerenciamento de normas.
2. O usuário seleciona uma norma para editar.
3. O usuário adiciona, remove ou edita tags associadas à norma.
4. O sistema salva as alterações e confirma a operação.

**Fluxos Alternativos:** Se as alterações não puderem ser salvas, o sistema exibe uma mensagem de erro.

**Pré-condições:** O usuário deve estar autenticado na aplicação.

**Pós-condições:** As tags são atualizadas conforme as ações do usuário.

---

#### RF-15: Fazer Download de Documentos

O usuário deve ser capaz de fazer download dos documentos armazenados na plataforma.

**Casos de Teste**

| ID    | Descrição                                                       |
| ----- | --------------------------------------------------------------- |
| CT-33 | Verifica se o download dos documentos é realizado corretamente. |
| CT-34 | Verifica a integridade dos documentos após o download.          |

---

#### UC-15: Fazer Download de Documentos

**Ator Primário:** Usuário/Analista de Documentos Normativos

**Descrição:** O usuário deve ser capaz de fazer download dos documentos armazenados na plataforma.

**Fluxo Principal:**

1. O usuário acessa a lista de documentos.
2. O usuário seleciona um documento para download.
3. O sistema prepara o documento para download e inicia o processo.

**Fluxos Alternativos:** Se o download falhar, o sistema exibe uma mensagem de erro e sugere tentar novamente.

**Pré-condições:** O documento deve estar disponível na aplicação.

**Pós-condições:** O documento é baixado com sucesso pelo usuário.

---

#### RF-16: Compartilhar Normas por E-mail

O usuário deve ser capaz de compartilhar normas via email diretamente da plataforma.

Casos de Teste

| ID    | Descrição                                                         |
| ----- | ----------------------------------------------------------------- |
| CT-35 | Verifica se a aplicação web redireciona para o Gmail.             |
| CT-36 | Verifica se o conteúdo do email inclui o documento compartilhado. |

---

#### UC-16: Compartilhar Normas por E-mail

**Ator Primário:** Usuário

**Descrição:** O usuário deve ser capaz de compartilhar normas via email diretamente da plataforma.

**Fluxo Principal:**

1. O usuário acessa a lista de normas.
2. O usuário seleciona uma norma para compartilhar.
3. O usuário escolhe a opção de compartilhar por email.
4. O sistema redireciona para o Outlook com o documento anexado.
5. O usuário completa o envio do email no Outlook.

**Fluxos Alternativos:** Se o redirecionamento falhar, o sistema exibe uma mensagem de erro.

**Pré-condições:** O usuário deve possuir um email Outlook.

**Pós-condições:** O documento é compartilhado via email com sucesso.

Os requisitos funcionais apresentados, juntamente com seus respectivos casos de teste e casos de uso, fornecem uma base sólida para o desenvolvimento e validação da plataforma de gerenciamento de normas. Cada requisito foi cuidadosamente detalhado para garantir que todas as funcionalidades essenciais para o usuário sejam atendidas de maneira eficaz e eficiente.

### 3.2.2 Requisitos Não Funcionais

&emsp;&emsp;Requisitos não funcionais são atributos essenciais que descrevem como um sistema deve operar, focando nas qualidades e comportamentos que garantem aspectos como o desempenho, segurança, usabilidade e a confiabilidade do software. Ao contrário dos requisitos funcionais, que especificam o que o sistema deve fazer, os requisitos não funcionais determinam as condições sob as quais essas funções devem ser executadas. Eles asseguram que o sistema seja eficiente, fácil de usar, seguro, acessível, e compatível com diferentes tecnologias e ambientes.

&emsp;&emsp;A ISO/IEC 25010, conhecida como SQuaRE (_System and Software Quality Requirements and Evaluation_), é uma norma internacional que desempenha um papel fundamental na definição e categorização da qualidade de produtos de software e sistemas. Criada pela Organização Internacional para Padronização (ISO) e pela Comissão Eletrotécnica Internacional (IEC), essa norma é essencial para guiar os desenvolvedores na avaliação e garantia da qualidade de software ao longo de todo o ciclo de vida do produto. No contexto do projeto atual, essa norma serve como uma base sólida para assegurar que todos os aspectos de qualidade, como desempenho, segurança, usabilidade e compatibilidade, sejam rigorosamente avaliados e cumpridos. Abaixo, são apresentados os requisitos não funcionais propostos pelo grupo Vox.

### RNF-01: Desempenho e Eficiência

&emsp;&emsp;A plataforma deve ser projetada para oferecer um desempenho otimizado, garantindo tempos de resposta rápidos e a capacidade de suportar um grande volume de requisições simultâneas sem degradação significativa de desempenho. Isso inclui a otimização de consultas ao banco de dados e o uso de balanceamento de carga.

&emsp;&emsp;**Iso Relacionada:** Eficiência de Desempenho (_Performance Efficiency_), essencial para assegurar que o sistema atenda às demandas dos usuários com tempos de resposta rápidos e alta capacidade de processamento.

#### Critérios de Aceitação

1. O sistema deve ter um tempo de resposta de até 2 segundos para 90% das requisições em condições normais de operação (1000 requisições).
2. O sistema deve ser capaz de suportar um volume de até 10.000 requisições simultâneas sem perda significativa de desempenho.

#### Descrição dos Testes

<div align="center">
  <sub>Tabela x: Teste de Desempenho e Eficiência</sub>

| Nome                       | Pré-condição                       | Procedimentos                                                                             | Resultado esperado                                                              | Pós-condição                                                     |
| -------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Teste de tempo de resposta | Sistema implementado e operacional | Simular 1.000 requisições concorrentes ao sistema e medir o tempo de resposta de cada uma | Pelo menos 90% das requisições devem ser atendidas em até 2 segundos            | Confirmação da eficiência do sistema em situações normais de uso |
| Teste de carga             | Sistema implementado e operacional | Simular 10.000 requisições simultâneas para avaliar a capacidade do sistema               | O tempo de resposta não deve exceder exceder 5 segundos para nenhuma requisição | Garantir que o sistema mantenha a performance sob alta carga     |

<sup>Fonte: Elaborado pelo grupo Vox </sup>

</div>

### RNF-02: Escalabilidade

&emsp;&emsp;A plataforma deve ser capaz de escalar eficientemente para atender ao aumento da carga de usuários e volume de dados, mantendo um desempenho consistente. Isso inclui a capacidade de expandir horizontalmente (adição de novos servidores), conforme necessário, sem interrupção significativa dos serviços.

&emsp;&emsp;**Iso Relacionada:** Flexibilidade (_Flexibility_), que é crucial para garantir que o sistema possa crescer em resposta a um aumento na demanda sem comprometer a funcionalidade ou o desempenho.

#### Critérios de Aceitação

1. O sistema deve ser capaz de escalar horizontalmente para adicionar novos servidores ou instâncias sem a necessidade de interrupção do serviço.
2. Em um cenário de pico, o sistema deve ser capaz de suportar um aumento de 200% na carga usual de usuários e requisições dentro de 15 minutos.
3. O tempo de resposta do sistema não deve aumentar mais que 20% quando a carga de usuários aumentar em até 50% da capacidade atual.

#### Descrição dos Testes

<div align="center">
  <sub>Tabela x: Teste de Escalabilidade</sub>

| Nome                               | Pré-condição                                               | Procedimentos                                                                                                   | Resultado Esperado                                                                                        | Pós-condição                                                                           |
| ---------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Teste de escalabilidade horizontal | Sistema configurado em um ambiente de produção ou simulado | Adicionar novas instâncias de servidor sob carga normal de usuários e monitorar a redistribuição de tráfego     | O sistema deve redistribuir automaticamente o tráfego para as novas instâncias sem interrupção do serviço | Aumento da capacidade de processamento do sistema                                      |
| Teste de carga em cenário de pico  | Sistema em operação normal                                 | Simular um aumento de 200% na carga de usuários em 15 minutos e monitorar o tempo de resposta e uso de recursos | O sistema deve suportar o aumento de carga com um aumento de no máximo 20% no tempo de resposta           | Garantia de que o sistema pode lidar com picos de tráfego sem degradação significativa |

<sup>Fonte: Elaborado pelo grupo Vox </sup>

</div>

### RNF-03: Interface do Usuário Intuitiva

&emsp;&emsp;A plataforma deve oferecer uma interface de usuário que seja fácil de usar, intuitiva e acessível, garantindo que os usuários possam realizar suas tarefas de forma eficiente e sem dificuldades. A interface deve seguir princípios de design de usabilidade e acessibilidade, proporcionando uma experiência agradável para todos os usuários, independentemente de sua experiência técnica.

&emsp;&emsp;**Iso Relacionada:** Capacidade de Interação (_Interaction Capability_), fundamental para garantir que o sistema seja intuitivo, fácil de aprender e operar, proporcionando uma experiência eficiente e satisfatória para os usuários finais. Isso inclui a capacidade do sistema de facilitar a interação dos usuários com as funcionalidades disponíveis, prevenindo erros e oferecendo suporte adequado.

#### Critérios de Aceitação

1. O sistema deve atingir uma pontuação mínima de 75 no SUS (_System Usability Scale_) em testes com usuários representativos.
2. A navegação pelo sistema deve ser intuitiva, com todas as funcionalidades principais acessíveis em até três cliques a partir da tela inicial.
3. Os feedbacks dos usuários durante os testes de usabilidade devem ser monitorados, e pelo menos 90% dos feedbacks devem indicar facilidade de uso ou navegação intuitiva.

#### Descrição dos Testes

<div align="center">
  <sub>Tabela x: Teste de Interface do Usuário Intuitiva</sub>

| Nome                             | Pré-condição                             | Procedimentos                                                                                                                  | Resultado Esperado                                                                                    | Pós-condição                                                       |
| -------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Teste de usabilidade (SUS)       | Sistema com mockup navegável             | Conduzir testes de usabilidade utilizando o questionário SUS com um grupo de usuários que representa o público-alvo            | A pontuação média no SUS deve ser de pelo menos 75, indicando uma boa usabilidade                     | Confirmação de que a interface é intuitiva e fácil de usar         |
| Teste de navegação intuitiva     | Sistema implementado e operacional       | Usuários devem realizar tarefas específicas, como acessar documentos, cronometrando o tempo e o número de cliques necessários  | Todas as funcionalidades principais devem ser acessíveis em até três cliques a partir da tela inicial | Melhoria da eficiência na navegação do sistema                     |
| Análise de feedback dos usuários | Sistema em fase de testes de usabilidade | Coletar feedback qualitativo dos usuários durante os testes de usabilidade, focando em facilidade de uso e navegação intuitiva | Pelo menos 90% dos feedbacks devem ser positivos em relação à usabilidade e navegação                 | Confirmação de que a interface atende às expectativas dos usuários |

<sup>Fonte: Elaborado pelo grupo Vox </sup>

</div>

### RNF-04: Acessibilidade

&emsp;&emsp;A plataforma deve garantir que as combinações de cores utilizadas na interface sejam acessíveis para usuários com daltonismo. O sistema deve seguir as Diretrizes de Acessibilidade para Conteúdo da Web (WCAG) 2.1, com foco no contraste de cores, atendendo aos requisitos mínimos do nível AA para assegurar que o conteúdo seja legível e perceptível para todos os usuários, incluindo aqueles com deficiências visuais.

&emsp;&emsp;**Iso Relacionada:** Capacidade de Interação (_Interaction Capability_), essencial para garantir que o sistema ofereça uma interface de usuário que seja perceptível para usuários com dificuldades visuais, promovendo uma experiência inclusiva e acessível.

#### Critérios de Aceitação

1. O sistema deve garantir que todas as combinações de cores na interface cumpram os requisitos mínimos de contraste do nível AA das WCAG 2.1, assegurando que o texto e os elementos gráficos sejam claramente distinguíveis.
2. As cores escolhidas para a interface devem ser testadas para assegurar que pessoas com diferentes tipos de daltonismo possam distinguir entre elas.

#### Descrição dos Testes

<div align="center">
  <sub>Tabela x: Teste de Acessibilidade Focada em Contraste de Cores</sub>

| Nome                        | Pré-condição                       | Procedimentos                                                                                                                                                            | Resultado Esperado                                                                                           | Pós-condição                                                      |
| --------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Teste de contraste de cores | Sistema implementado e operacional | Utilizar ferramentas de análise de contraste (como o Colour Contrast Analyser) para verificar se todas as combinações de cores cumprem os requisitos mínimos do nível AA | Todas as combinações de cores devem ter contraste suficiente para atender aos requisitos do nível            | Garantir legibilidade para usuários com daltonismo e baixa visão  |
| Teste de daltonismo         | Sistema implementado e operacional | Aplicar filtros de simulação de daltonismo (utilizando ferramentas como o Sim Daltonism) para verificar a distinção entre cores selecionadas                             | Usuários com diferentes tipos de daltonismo devem conseguir distinguir os elementos importantes da interface | Assegurar que a interface seja perceptível para todos os usuários |

<sup>Fonte: Elaborado pelo grupo Vox </sup>

</div>

### RNF-05: Compatibilidade em Navegadores

&emsp;&emsp;A plataforma deve ser compatível com os principais navegadores da web, garantindo que todos os usuários possam acessar e utilizar o sistema independentemente do navegador escolhido. O sistema deve funcionar corretamente nas versões mais recentes dos navegadores Google Chrome, Mozilla Firefox, Microsoft Edge e Safari, assegurando uma experiência consistente e livre de erros em todos os ambientes suportados.

&emsp;&emsp;**Iso Relacionada:** Compatibilidade (_Compatibility_), fundamental para garantir que o sistema possa operar eficazmente em diferentes ambientes de navegação e integrar-se bem com outros sistemas ou serviços.

#### Critérios de Aceitação

1. O sistema deve ser compatível e funcionar sem erros nas versões mais recentes dos navegadores Google Chrome, Mozilla Firefox, Microsoft Edge e Safari.
2. A interface e as funcionalidades devem ser consistentemente renderizadas e operacionais em todos os navegadores suportados, sem necessidade de ajustes manuais.
3. Todos os elementos de interface, incluindo botões, formulários e componentes dinâmicos, devem ser testados para garantir comportamento idêntico em todos os navegadores.

#### Descrição dos Testes

<div align="center">
  <sub>Tabela x: Teste de Compatibilidade em Navegadores</sub>

| Nome                                   | Pré-condição                       | Procedimentos                                                                                                                                                            | Resultado Esperado                                                                                | Pós-condição                                                                   |
| -------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Teste de compatibilidade cross-browser | Sistema implementado e operacional | Utilizar ferramentas de teste automatizado para executar o sistema em diferentes navegadores e verificar o comportamento da interface e funcionalidades                  | O sistema deve se comportar de maneira idêntica e correta em todos os navegadores testados        | Garantir que a experiência do usuário seja consistente em todos os navegadores |
| Teste manual de interface              | Sistema implementado e operacional | Realizar verificação manual da interface em diferentes navegadores, observando a renderização de elementos gráficos, a responsividade e a funcionalidade dos componentes | Todos os elementos devem ser exibidos e funcionar corretamente em todos os navegadores suportados | Confirmação de que o sistema é visualmente e funcionalmente consistente        |

<sup>Fonte: Elaborado pelo grupo Vox </sup>

</div>

&emsp;&emsp;Esses requisitos são cruciais para a qualidade do sistema, pois garantem que ele não apenas funcione corretamente, mas também atenda às expectativas dos usuários em termos de desempenho e experiência de uso. Além disso, eles ajudam a assegurar que o sistema esteja em conformidade com normas e regulamentações, facilitando a manutenção e a evolução futura do software. Portanto, os requisitos não funcionais são fundamentais para o sucesso a longo prazo de qualquer sistema, garantindo que ele seja confiável e alinhado com as necessidades e expectativas dos utentes.

## 3.3. Padrões de trabalho

&emsp;&emsp; A seguir, serão detalhados os padrões de trabalho para o desenvolvimento do Vox, fundamentados nas normas da ABNT (Associação Brasileira de Normas Técnicas). Tais padrões visam proporcionar uma base estruturada e consistente para a criação e manutenção da plataforma, assegurando qualidade, eficiência e clareza em todas as etapas do desenvolvimento. Os principais objetivos deste documento são:

- Padronização: estabelecer normas claras e consistentes para todos os membros da equipe, garantindo que todos sigam as mesmas práticas e procedimentos.
- Qualidade: assegurar que o software desenvolvido seja de alta qualidade, através da aplicação de melhores práticas de codificação, testes e revisão.
- Eficiência: facilitar o desenvolvimento e a manutenção do software, promovendo a reutilização de componentes e a organização lógica do código.
- Colaboração: melhorar a colaboração entre os membros da equipe, através de práticas de comunicação e gestão de projetos bem definidas.
- Qualidade: assegurar que o software desenvolvido seja de alta qualidade, através da aplicação de melhores práticas de codificação, testes e revisão.
- Eficiência: facilitar o desenvolvimento e a manutenção do software, promovendo a reutilização de componentes e a organização lógica do código.
- Colaboração: melhorar a colaboração entre os membros da equipe, através de práticas de comunicação e gestão de projetos bem definidas.

&emsp;&emsp;Este documento abrange todos os aspectos do desenvolvimento da solução Vox, incluindo padrões de desenvolvimento, como convenções de commits, organização de branches, nomenclatura de arquivos e pastas, e práticas de codificação. Ele aborda também padrões de planejamento e acompanhamento de atividades, como a utilização do GitHub Projects, metodologias ágeis e procedimentos de revisão de código. Além disso, são apresentadas considerações sobre a escrita desse documento, que abordam a importância da revisão e atualização contínua do mesmo, bem como o comprometimento da equipe com os padrões estabelecidos.

&emsp;&emsp;Este texto deve ser utilizado como referência durante todo o ciclo de vida do projeto, garantindo que os padrões e práticas aqui descritos sejam seguidos e mantidos, promovendo assim a excelência no desenvolvimento.

### 3.3.1. Padrões de Desenvolvimento

#### 1. _Commits_

- Idioma: todos os commits devem ser escritos em inglês para garantir a compreensão universal.
- Padrão: utilizar o formato _Conventional Commits_ para manter a consistência e clareza. O formato segue a estrutura: `tipo(scope): descrição`. Exemplos de tipos incluem `feat` (nova funcionalidade), `fix` (correção de bugs), `docs` (documentação), `style` (formatação, falta de ponto e vírgula, etc.), `refactor` (refatoração de código), `test` (adicionar ou corrigir testes), e `chore` (atualizações de ferramentas, configuração, etc.).

#### 2. _Pull Requests (PRs)_

- Descrição: cada PR deve conter uma descrição clara e detalhada das mudanças realizadas, o motivo das alterações e, se aplicável, referências a _issues_.
- Tamanho: manter os PRs pequenos e focados em uma única tarefa ou feature para facilitar a revisão.
- Checklist: incluir um checklist para garantir que todas as etapas foram cumpridas, como testes unitários e revisões de código.

#### 3. Desenvolvimento em _Branches_

- Branch Principal: `main` deve ser a branch estável e pronta para produção.
- Branch de Desenvolvimento: `develop` pode ser utilizada para integrar mudanças antes de serem mescladas na `main`.
- Branches de Funcionalidades: utilizar o padrão `tipo/nome-da-feature`, como `feat/nova-funcionalidade` ou `fix/corrigir-bug`.
- Branches de Hotfixes: para correções urgentes em produção, utilizar o padrão `hotfix/descrição-do-hotfix`.

#### 4. Nomenclatura de Arquivos

- Arquivos: devem seguir o padrão CamelCase. Exemplo: `ProcessamentoTexto.java`.
- Pastas: devem seguir o padrão camelCase com inicial minúscula. Exemplo: `processamentoDeTexto`.

#### 5. Padrão de Organização de Código

- Modularização: organizar o código em módulos ou componentes que encapsulam funcionalidades específicas.
- Diretórios: estruturar os diretórios de forma lógica, separando por funcionalidades ou camadas (ex.: `services`, `controllers`, `models`).
- Importações: ordenar as importações alfabeticamente e separá-las por grupos (bibliotecas padrão, bibliotecas de terceiros, módulos internos).

#### 6. Nome de Variáveis

- Descritivo: utilizar nomes de variáveis descritivos que reflitam seu propósito e uso.
- Padrão: seguir o padrão camelCase. Exemplo: `contadorDePalavras`.

#### 7. Componentização

- Reutilização: componentizar o código para promover a reutilização e facilitar a manutenção.
- _Separation of Concerns_: cada componente deve ter uma responsabilidade clara e definida.
- Interface: definir interfaces claras para a comunicação entre componentes.

#### 8. _Test-Driven Development_ (TDD)

- Escrita de Testes: escrever testes unitários antes do código funcional.
- Cobertura de Testes: garantir alta cobertura de testes para capturar possíveis bugs e falhas.
- Ferramentas: utilizar frameworks de testes adequados à linguagem e ao ambiente de desenvolvimento.

#### 9. Documentação de Código

- Comentários: utilizar comentários para explicar trechos complexos de código, mas evitar comentários excessivos.
- Documentação: documentar classes, métodos e funções utilizando ferramentas de documentação como Javadoc ou Doxygen.
- README: manter um arquivo README atualizado com informações relevantes sobre o projeto, como instruções de instalação, uso e contribuições.

#### 10. Padrões de Formatação

- Indentação: utilizar uma indentação consistente (ex.: 4 espaços ou 1 tabulação) em todo o código.
- Linhas: limitar o comprimento das linhas de código (ex.: 80 ou 120 caracteres) para melhorar a legibilidade.
- Linting: utilizar ferramentas de linting para garantir a conformidade com os padrões de formatação e estilo do código.

#### 11. Segurança

- Validação de Entradas: validar todas as entradas de dados para prevenir injeções e outros tipos de ataques.
- Autenticação e Autorização: implementar mecanismos seguros de autenticação e autorização.
- Gerenciamento de Erros: tratar erros e exceções de maneira segura, sem expor detalhes sensíveis.

#### 12. Performance

- Otimização: otimizar código para melhorar a performance, evitando loops desnecessários e consultas ineficientes.
- Monitoramento: implementar monitoramento e logging para identificar e resolver problemas de performance.

&emsp;&emsp; Estes padrões de desenvolvimento foram estabelecidos para assegurar que o software de processamento de linguagem natural seja desenvolvido de maneira eficiente, segura e sustentável, facilitando a manutenção e evolução do projeto.

### 3.3.2. Padrões de Planejamento e Acompanhamento de Atividades

&emsp;&emsp; Uma gestão eficaz das atividades é fundamental para o sucesso de qualquer projeto de desenvolvimento de software. Esta seção descreve os padrões e práticas recomendadas para o planejamento, acompanhamento e gerenciamento das tarefas do Vox.

#### 1. Utilização do GitHub Projects

&emsp;&emsp; O GitHub Projects é uma ferramenta poderosa para o gerenciamento de projetos, permitindo a visualização e organização das tarefas de forma clara e estruturada. A seguir, são detalhados os padrões para sua utilização:

- Quadro de Projetos: cada projeto deve ter um quadro no GitHub Projects que reflete o fluxo de trabalho da equipe.
- Colunas Padrão:

  - ToDo: tarefas identificadas que ainda não foram priorizadas ou agendadas.
  - Ready: tarefas prontas para serem iniciadas, geralmente após o planejamento.
  - In Progress: tarefas que estão atualmente em desenvolvimento.
  - In Review: tarefas concluídas que estão passando por revisão de código ou testes.
  - Done (Develop): tarefas desenvolvidas e aprovadas, aguardando integração final.
  - Main: tarefas totalmente concluídas e integradas na branch principal.

- Cartões: cada cartão representa uma tarefa ou issue. Deve conter uma descrição clara, critérios de aceitação, estimativa de esforço e, se possível, atribuição a um responsável.

- Etiquetas (Labels): utilizar etiquetas para categorizar e priorizar tarefas, como `bug`, `feature`, `enhancement`, `urgent`, etc.

- Automação: configurar automações para mover cartões entre colunas com base em ações específicas, como a abertura de um PR ou a finalização de uma revisão.

#### 2. Metodologia Scrum

&emsp;&emsp; A adoção da metodologia Scrum permite uma abordagem ágil e iterativa no desenvolvimento de software. A seguir, são descritos os elementos essenciais do Scrum a serem implementados:

- Sprints: períodos de trabalho com duração fixa (geralmente 2 a 4 semanas) onde um conjunto de tarefas é planejado e executado.

- Papéis:

  - Product Owner: responsável por definir e priorizar os requisitos do produto.
  - Scrum Master: facilita o processo Scrum, remove impedimentos e garante que a equipe siga as práticas ágeis.
  - Equipe de Desenvolvimento: membros responsáveis pela execução das tarefas técnicas.

- Eventos Scrum:

  - Sprint Planning: reunião no início de cada sprint para definir quais tarefas serão realizadas. Envolve a priorização de tarefas, estimativas de esforço e definição de metas.

  - Daily Scrum (Daily Stand-up): reuniões diárias e breves (15 minutos) onde cada membro da equipe compartilha o progresso, planos para o dia e impedimentos encontrados.

  - Sprint Review: realizada no final de cada sprint para demonstrar o trabalho concluído aos stakeholders e coletar feedback.

  - Sprint Retrospective: após a Sprint Review, a equipe reflete sobre o processo e identifica melhorias para o próximo sprint.

- Artefatos Scrum:

  - Product Backlog: lista priorizada de requisitos e funcionalidades desejadas para o produto.

  - Sprint Backlog: conjunto de tarefas selecionadas do Product Backlog para serem realizadas durante o sprint atual.

  - Increment: soma de todos os itens do Product Backlog concluídos durante o sprint e sprints anteriores.

#### 3. Procedimento de Revisão

&emsp;&emsp; A revisão de código é crucial para manter a qualidade e a consistência do software. Os seguintes procedimentos devem ser adotados:

- Pull Requests (PRs): toda mudança no código deve ser submetida através de um PR, que deve conter descrições detalhadas das alterações.

- Revisores: cada PR deve ser revisado por pelo menos um membro da equipe que não seja o autor do código. Para mudanças críticas, recomenda-se múltiplos revisores.

- Critérios de Revisão:

  - Funcionalidade: verificar se o código atende aos requisitos especificados.

  - Qualidade do Código: avaliar a legibilidade, manutenção e aderência aos padrões de codificação.

  - Testes: confirmar a presença e eficácia dos testes associados às mudanças.

  - Impacto: considerar o impacto das mudanças em outras partes do sistema.

- Feedback: os revisores devem fornecer feedback construtivo e específico, apontando áreas de melhoria e reconhecendo pontos positivos.

- Aprovação: um PR só deve ser mesclado após receber as aprovações necessárias e resolver todos os comentários e solicitações de mudanças.

#### 4. Divisão de Tarefas por Artefato

&emsp;&emsp; A organização das tarefas por artefato facilita a gestão e o acompanhamento do progresso. As seguintes diretrizes devem ser seguidas:

- Identificação de Artefatos: definir claramente quais são os artefatos do projeto, como módulos, componentes, documentos, etc.

- Criação de Tarefas: para cada artefato, criar tarefas específicas que abrangem desenvolvimento, testes, documentação e revisão.

- Granularidade: as tarefas devem ser suficientemente granulares para serem concluídas dentro de um sprint, evitando atividades muito grandes ou vagas.

- Atribuição: designar responsáveis por cada tarefa com base em habilidades e disponibilidade.

- Dependências: identificar e gerenciar dependências entre tarefas para evitar bloqueios e atrasos.

- Rastreabilidade: manter um registro claro de como cada tarefa contribui para o desenvolvimento e evolução de cada artefato.

#### 5. Ferramentas de Comunicação e Colaboração

&emsp;&emsp; Para assegurar uma comunicação eficaz e uma colaboração harmoniosa entre os membros da equipe, as seguintes práticas e ferramentas devem ser adotadas:

- Plataformas de Comunicação: utilizar ferramentas como Slack, Microsoft Teams ou similares para comunicação instantânea.

- Documentação Compartilhada: manter documentos, planos e atas de reuniões em plataformas colaborativas como Google Docs ou Confluence.

- Calendários Compartilhados: agendar eventos, reuniões e deadlines em calendários acessíveis a todos os membros da equipe.

- Feedback Regular: promover uma cultura de feedback contínuo, encorajando os membros a compartilhar insights, preocupações e sugestões.

#### 6. Monitoramento e Relatórios

&emsp;&emsp;Acompanhar o progresso e a eficiência das atividades é essencial para identificar áreas de melhoria. As seguintes práticas devem ser implementadas:

- Métricas de Desempenho: definir e monitorar métricas como velocidade da equipe, taxa de conclusão de tarefas, número de bugs reportados e corrigidos, etc.

- Relatórios Periódicos: gerar relatórios semanais ou mensais que resumam o progresso, desafios enfrentados e planos futuros.

- Reuniões de Revisão: além das reuniões Scrum, realizar reuniões periódicas com stakeholders para apresentar o status do projeto e alinhar expectativas.

&emsp;&emsp;A adoção desses padrões de planejamento e acompanhamento de atividades assegura que o projeto seja conduzido de maneira organizada, transparente e eficiente, promovendo a qualidade e o sucesso do desenvolvimento do software de processamento de linguagem natural.

### 3.3.3 Padrões de Documentação

&emsp;&emsp; A documentação é um elemento essencial no desenvolvimento de software, pois fornece informações críticas sobre a estrutura, funcionalidades e utilização do sistema. Seguir padrões de documentação assegura que todos os stakeholders, incluindo desenvolvedores, usuários finais e equipe de manutenção, possam compreender e utilizar o software de forma eficaz. Este tópico descreve os padrões de documentação a serem seguidos no projeto Vox.

#### 1. Documentação do Código

**Comentários:**

- Comentários de Linha: devem ser utilizados para explicar trechos específicos de código, especialmente aqueles que não são imediatamente claros. Devem ser breves e descritivos.

  ```java
  // Calcula a frequência das palavras no texto
  ```

- Comentários de Bloco: utilizados para fornecer uma visão geral de seções maiores de código. Devem ser colocados no início de funções, métodos ou classes para descrever seu propósito e funcionamento.

  ```python
  """
  Função que processa o texto de entrada e retorna a contagem de palavras.
  Parâmetros:
  texto (str): O texto a ser processado.
  Retorna:
  dict: Um dicionário com a contagem de cada palavra.
  """
  ```

**Documentação de Classes e Métodos:**

- Classes: devem ter uma documentação que descreva sua finalidade, atributos e métodos principais.

  ```python
  class ProcessadorDeTexto:
      """
      Classe para processamento de texto.

      Atributos:
      texto (str): O texto a ser processado.

      Métodos:
      contar_palavras(): Conta as palavras no texto.
      """
  ```

- Métodos: cada método deve ter uma documentação que descreva seu propósito, parâmetros e valor de retorno.

  ```python
  def contar_palavras(self, texto):
      """
      Conta as palavras no texto.

      Parâmetros:
      texto (str): O texto a ser processado.

      Retorna:
      dict: Um dicionário com a contagem de cada palavra.
      """
  ```

#### 2. Documentação do Projeto

#### README

- Descrição do Projeto: breve descrição do objetivo e funcionalidades do projeto.
- Instalação: instruções claras e detalhadas sobre como instalar e configurar o ambiente de desenvolvimento.
- Uso: exemplos de como utilizar o software, incluindo comandos básicos e funcionalidades principais.
- Contribuição: guia para desenvolvedores interessados em contribuir com o projeto, incluindo diretrizes para submissão de PRs e issues.
- Licença: informação sobre a licença do projeto.

#### Index.md

&emsp;&emsp; A documentação do projeto será organizada em um arquivo `Index.md`, estruturado por sprints para refletir o progresso e a evolução do projeto. Abaixo está a estrutura padrão do `Index.md`:

#### Sprint 1:

- Entendimento de Negócios: descreve o levantamento e a análise das necessidades do negócio, requisitos e objetivos do projeto.
- Entendimento do Design: detalha o processo de design inicial, incluindo esboços, wireframes e decisões de design.
- Entendimento da Arquitetura do Sistema: documenta a arquitetura proposta, incluindo diagramas e descrições das principais componentes e interações.

#### Sprint 2:

- Sistema de NLP: descreve a implementação e integração do sistema de processamento de linguagem natural, incluindo algoritmos e modelos utilizados.
- Documentação geral: resumos das atividades, decisões e resultados da Sprint 2.

#### Sprint 3:

- Construção do Backend da Solução: documenta o desenvolvimento do backend, incluindo APIs, serviços e banco de dados.
- Documentação geral: resumos das atividades, decisões e resultados da Sprint 3.

#### Sprint 4:

- Construção do Frontend da Solução: descreve o desenvolvimento do frontend, incluindo interfaces de usuário, frameworks e bibliotecas utilizadas.
- Documentação geral: resumos das atividades, decisões e resultados da Sprint 4.

#### Sprint 5:

- Elaboração da Documentação Final do Projeto: compila toda a documentação final do projeto, incluindo manuais de usuário, guias de instalação e documentos técnicos.
- Apresentação Final: documenta a preparação e execução da apresentação final do projeto, incluindo slides, demos e feedbacks.

#### 3. Documentação de Processos

#### Procedimentos Operacionais

- Procedimentos de Deploy: instruções passo a passo para realizar o deploy do software em diferentes ambientes (desenvolvimento, teste, produção).
- Procedimentos de Backup e Recuperação: instruções para backup e recuperação de dados e configurações do sistema.

#### Padrões de Revisão

- Checklists de Revisão: listas de verificação utilizadas durante a revisão de código para garantir a conformidade com os padrões de qualidade e segurança.
- Relatórios de Revisão: documentação dos resultados das revisões, incluindo feedbacks, melhorias sugeridas e correções realizadas.

#### 4. Ferramentas de Documentação

&emsp;&emsp; Para a documentação do projeto, utilizamos exclusivamente Markdown, por sua simplicidade e compatibilidade com diversas ferramentas e plataformas de desenvolvimento.

- Markdown: utilizar Markdown para documentação em repositórios GitHub, como READMEs, index e outras documentações estruturadas.

#### 5. Manutenção e Atualização da Documentação

- Versões: manter a documentação atualizada com cada nova versão do software, refletindo as mudanças e novas funcionalidades.
- Revisões Periódicas: realizar revisões periódicas da documentação para garantir que esteja sempre correta e relevante.
- Contribuição: Encaminhar contribuições de todos os membros da equipe para a melhoria contínua da documentação, promovendo uma cultura de documentação aberta e colaborativa.

&emsp;&emsp; Estes padrões de documentação são fundamentais para assegurar que o software de processamento de linguagem natural seja compreensível, utilizável e mantível, tanto para os desenvolvedores atuais quanto para os futuros.

# 4. Sistema de NLP

&emsp;&emsp; A seção 4 do documento abordará a implementação do Sistema de Processamento de Linguagem Natural (NLP) desenvolvido para este projeto. Este sistema é fundamental para a análise e compreensão automatizada de dados textuais, e sua arquitetura foi projetada para lidar eficientemente com a transcrição de áudio, o processamento subsequente do texto transcrito e o gerenciamento da implementação em ambiente de nuvem.

&emsp;&emsp; Inicialmente, será discutida a API utilizada para a etapa de conversão de fala para texto, que é um dos pilares do sistema, seguido pela descrição detalhada do algoritmo de NLP empregado, sua lógica de funcionamento, e como ele foi implementado. Em seguida, o documento abordará o processo de deploy do algoritmo em uma infraestrutura de nuvem, garantindo escalabilidade e disponibilidade. Por fim, será apresentada a API desenvolvida para receber os áudios enviados pelos usuários, permitindo uma integração perfeita entre o usuário final e o sistema automatizado de NLP.

## 4.1 API para implementar a etapa de Speech to Text

&emsp;&emsp; Neste projeto, foi utilizada a API IBM Watson Speech to Text para realizar a transcrição de áudio em texto. Essa API é acessada via uma requisição HTTP do tipo POST para a URL `https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/54e5b6e9-0db7-4294-a7d7-ea13487093e8/v1/models/pt-BR_BroadbandModel/recognize`. O áudio a ser transcrito deve estar no formato `.webm`, e é enviado como parte do corpo da requisição.

<div align="center">
	<sub>Imagem X - Tela do Postman mostrando a configuração da requisição POST, incluindo a URL da API e a chave de API usada para autenticação</sub>
	<img src="../assets/postman1.png"/>
</div>

&emsp;&emsp; Para autenticação, utilizamos um esquema de autenticação básica, onde o nome de usuário é "apikey", e a senha é a chave de API fornecida pelo IBM Watson. Os cabeçalhos da requisição incluem o tipo de conteúdo `Content-Type: audio/webm`, especificando que o arquivo de áudio está no formato correto.

<div align="center">
	<sub>Imagem X - Tela do Postman mostrando os cabeçalhos da requisição configurados corretamente para o envio do arquivo de áudio</sub>
	<img src="../assets/postman2.png"/>
</div>

&emsp;&emsp; No código, o arquivo de áudio é lido e enviado na requisição. Se a transcrição for bem-sucedida, o servidor retorna um JSON contendo a transcrição do áudio. A resposta pode ser acessada e exibida no terminal. Em caso de erro, o código de status HTTP e a mensagem de erro são exibidos, ajudando a identificar problemas na requisição.

<div align="center">
	<sub>Imagem X - Tela do Postman mostrando a resposta da API, incluindo o JSON com a transcrição do áudio</sub>
	<img src="../assets/postman3.png"/>
</div>

<div align="center">
	<sub>Imagem X - Tela do Postman mostrando um exemplo de erro, onde a API retorna um código de status HTTP diferente de 200, como 400 ou 500, acompanhado por uma mensagem de erro detalhando o problema</sub>
	<img src="../assets/postman3.png"/>
</div>

&emsp;&emsp; A utilização desta API no projeto proporciona uma solução robusta e eficiente para integrar a funcionalidade de transcrição de áudio, essencial em aplicações de Processamento de Linguagem Natural (PLN).

## 4.2 Algoritmo de NLP utilizado e sua implementação

&emsp;&emsp;O algorítimo de NLP foi desenvolvido com base no modelo de desenvolvimento TDD (Test Driven Development). Dessa forma, a arquitetura principal foi guiada em pré-processamento e pipeline, treinamento e testes guiados que possibilitaram a refatoração do modelo ao longo de outros testes.

## 4.2.1 Pipeline e testes

&emsp;&emsp;No pré-processamento, utilizamos técnicas de Processamento de Linguagem Natural (PLN) para melhorar a compreensão dos textos pelo computador. As principais etapas realizadas incluem:

- Extração de Sentenças: O texto é segmentado em orações para facilitar a análise e o processamento.
- Tokenização: Separação das palavras de uma frase, por exemplo, "Eu te amo" torna-se ["Eu", "te", "amo"].
- Remoção de Stop Words: Palavras comuns, que não contribuem significativamente para o significado da frase, são removidas (ex.: "de", "o", "a").
- Lematização: Palavras são convertidas para suas formas base ou raiz, como verbos no infinitivo ("correr", "amar") e substantivos no singular.
- Remoção de Pontuação: Caracteres de pontuação são eliminados, já que não são necessários para a análise semântica do texto.
- POS-Tagging: Identificação das categorias gramaticais de cada palavra, como adjetivos, substantivos e pronomes. Também detecta entidades nomeadas, como nomes de empresas e organizações.

&emsp;&emsp;A seguir, é apresentado, respectivamente, as funções de pré-processamento do input do usuário, pré-processamento do modelo, configuração do modelo e suas bibliotecas, a aplicação do pré-processamento no modelo, a avaliação, teste do pré-processamento, teste da predição do modelo, regex - entidade, regex entidade de data, tests de remoção de entidades, Bag of Words, testes do Bag of Words e os resultados da integração da API de NLP via Postman.

### Função

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Funções do pré-processamento</sub> 
	<img src="../assets/preprocessamento.png"/>
</div>

### Função

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Funções do pré-processamento do moedlo</sub>
	<img src="../assets/preprocessamentomodelo.png"/>
</div>

### Teste

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Resultado do pré-processamento</sub>
	<img src="../assets/testepreprocessamento.png"/>
</div>

### Configuração

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Configuração do modelo</sub>
	<img src="../assets/modelo.png"/>
</div>

### Pré-processamento

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Aplicando pré-processamento ao modelo</sub>
	<img src="../assets/aplicandopreprocessamento.png"/>
</div>

### Avaliação do modelo

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Avaliação do modelo</sub>
	<img src="../assets/avaliacao.png"/>
</div>

### Teste do modelo

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Teste do modelo</sub>
	<img src="../assets/testemodelo.png"/>
</div>

### Função

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Funções Regex para extração de informações do Input do usuário</sub>
	<img src="../assets/regex.png"/>
</div>

### Função

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Funções Regex Data para extração de informações do Input</sub>
	<img src="../assets/regexdata.png"/>
</div>

### Teste

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Testes da extração de entidades com regex</sub>
	<img src="../assets/testeentidade.png"/>
</div>

### Função

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Funções para aplicar o Bag of Words ao Input do usuário</sub>
	<img src="../assets/funcoesbag.png"/>
</div>

### Avaliação Bag of Words

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Resultados do Bag of Words aplicado</sub>
	<img src="../assets/bag.png"/>
</div>

### Teste de integração

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Resultados da integração do modelo PLN via Postman</sub>
	<img src="../assets/teste1.png"/>
</div>

### Teste de integração

<div align="center">
	<sub>Imagem X - Tela do Jupyter Notebook com o modelo PLN - Resultados da integração do modelo PLN via Postman</sub>
	<img src="../assets/teset2.png"/>
</div>

&emsp;&emsp;O pré-processamento é uma etapa fundamental no desenvolvimento de modelos de Processamento de Linguagem Natural, pois garante que os dados sejam adequadamente estruturados para análise. As técnicas aplicadas, como tokenização, remoção de stop words, lematização e POS-tagging, ajudam o modelo a capturar as informações mais relevantes, descartando ruídos desnecessários. Além disso, o uso de regex para a extração de entidades e a implementação de Bag of Words permitem uma análise eficiente e precisa dos textos. O processo foi baseado na arquitetura TDD por meio de testes e avaliações, integrando-se perfeitamente com ferramentas como o Postman para consultas e automações futuras.

## 4.3 Processo de deploy do algoritmo em nuvem

&emsp;&emsp;Este documento detalha o processo de implantação do algoritmo de Processamento de Linguagem Natural (NLP) em uma API desenvolvida em Flask, utilizando a Amazon Web Services (AWS) como plataforma de nuvem comercial. O objetivo é oferecer um guia passo a passo que possibilite a replicação desse processo em ambientes semelhantes.

#### Passo 1: Criar uma Conta na AWS

1. Acessar o site da AWS: Navegue até aws.amazon.com.
2. Criar uma conta: Clique em "Criar uma conta da AWS" e siga as instruções na tela.

#### Passo 2: Criar e Configurar a Instância EC2

1. Acessar o Console da AWS: Após criar sua conta, faça login no console da AWS.
2. Criar uma instância EC2:
   - No console da AWS, navegue até o serviço EC2.
   - Clique em **Executar instância**.
   - Dê um nome a instância.
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-2.png"/>
   </div>
   - Escolha "Ubuntu" como a imagem de máquina Amazon (AMI).
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image.png"/>
   </div>
   - Selecione um tipo de instância com base em suas necessidades de processamento.
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-1.png"/>
   </div>
   - Crie um par de chaves **.ppk** clicando em **Criar novo par de chaves**
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-3.png"/>
   </div>
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-4.png"/>
   </div>
   - Permita todos os tráfegos
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-5.png"/>
   </div>
   - Clique em **Executar instância**

#### Passo 3: Adicionar regra de segurança

1. Clique na instância e depois em **Segurança**
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-9.png"/>
   </div>

2. Selecione o grupo de segurança
3. Clique em **Editar regras de entrada**
4. Adicione uma regra com o tipo **Todo o tráfego** e para todos os blocos CIDR **0.0.0.0/0**
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-10.png"/>
   </div>
5. Clique em **Salvar regras**

#### Passo 4: Conectar na EC2

1. Volte para a página inicial da instância e clique em **Conectar**
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-6.png"/>
   </div>
2. Digite "ubuntu" no **Nome de usuário**
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-7.png"/>
   </div>
3. Clique em **Conectar** e você vai ser redirecionado a uma pagina com um terminal
   <div align="center">
    <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/image-8.png"/>
   </div>

#### Passo 5: Implantar o Algoritmo de NLP

1. Clone o repositório contendo o código do algoritmo usando o Git:
   `git clone git@github.com:seu_usuario/seu_repositorio.git`

_É necessário ter acesso a este repositório e provavelmente a uma chave SSH de autenticação pública para conseguir clonar._

2. Navegue até o diretório da aplicação:
   `cd seu_repositorio/src/backend`
3. Crie um ambiente virtual e instale as dependências necessárias:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

#### Passo 6: Configurar Variáveis de Ambiente

1. Adicione um arquivo .env:

   ```
   nano .env
   ```

2. Defina as variáveis de ambiente
3. Finalize com os seguintes comandos do teclado:
   - **CTRL + x** para finalizar a edição;
   - **y** para salvar as mudanças;
   - **ENTER** para sair.

#### Passo 7: Executar a aplicação

&emsp;&emsp;Para servir a aplicação Flask, é necessário o servidor WSGI Gunicorn. Ao “executar” o Flask, está, na verdade, rodando o servidor WSGI de desenvolvimento do Werkzeug, que encaminha as solicitações de um servidor web. Como o Werkzeug é destinado apenas ao desenvolvimento, é necessário utilizar o Gunicorn, um servidor WSGI preparado para produção, para atender a aplicação.

1. Instale o Gunicorn usando o comando abaixo:
   `pip install gunicorn`
2. Execute o Gunicorn:
   `diretório/gunicorn -b 0.0.0.0:8000 nome_do_arquivo_de_execução:app `

_Aqui, é necessário substituir "nome_do_arquivo_de_execução" para o nome do arquivo que se encontra a inicialização do Flask, como o app.py, ou run.py (sem o .py). Exemplo: `~/backend/venv/bin/gunicorn -b 0.0.0.0:8000 run:app`._

Pronto, a aplicação já estará rodando, podendo ser acessada no navegador em:
**http://<dns_publica>:8000** ou **http://<ip_publico>:8000**

#### Conclusão

&emsp;&emsp;O guia fornece instruções detalhadas que possibilitam a configuração e a execução do algoritmo em um ambiente de nuvem comercial. A escolha da AWS proporciona escalabilidade e flexibilidade, além da possibilidade de integração com uma variedade de serviços que podem potencializar o desempenho da aplicação.

&emsp;&emsp;A replicação deste processo em outros ambientes de nuvem pode ser realizada de acordo com as diretrizes apresentadas. Espera-se que este guia sirva como um recurso útil para a aplicação do conhecimento adquirido em projetos futuros, contribuindo para a evolução contínua das aplicações de NLP.

### 4.3.1 Teste do deploy

**Objetivo:** Verificar se o algoritmo de Processamento de Linguagem Natural (PLN) está funcionando corretamente no ambiente de produção, acessando a DNS pública e retornando a intenção do usuário.

**Pré-condição:**

- A aplicação deve estar em execução na DNS pública na porta 8000.
- O endpoint deve estar acessível no URL `http://<dns-publica>:8000/pln`.
- Um JSON deve ser enviado no corpo da requisição, contendo a estrutura necessária.

**Etapas do Teste:**

1. Utilizar uma ferramenta como Postman ou cURL para enviar uma requisição POST.
2. Configurar o endpoint como `http://<dns-publica>:8000/pln`.
3. No corpo da requisição, enviar um JSON no seguinte formato:

```
{
  "input": "Texto que representa a solicitação do usuário"
}
```

4. Enviar a requisição.
5. Verificar a resposta retornada pelo servidor.

**Pós-condição:**

- A resposta da API deve conter um código de status 200 OK.
- O corpo da resposta deve incluir um JSON que representa a intenção do usuário.

**Resultados Esperados:**
O corpo da resposta deve ser algo como:

```
{
  "resultado": "consulta_normativa"
}
```

**Captura de Tela do Postman:**
Abaixo está uma captura de tela do Postman mostrando a requisição bem-sucedida:

<div align="center">
  <img src="../assets/4.3 Processo de deploy do algoritmo em nuvem/postman-test.png"/>
</div>

## 4.4 API para receber os áudios enviados pelo usuário

&emsp;&emsp;A API de recepção de áudio é projetada para permitir que os usuários gravem áudio diretamente no navegador e enviem esse áudio para o backend para processamento adicional. O objetivo é capturar o áudio do usuário, convertê-lo em um formato adequado e, posteriormente, utilizá-lo para transcrição de voz para texto. Esta seção fornece detalhes sobre o endpoint disponível, os formatos de áudio suportados, os requisitos de entrada e os exemplos de chamadas.

### Endpoint

&emsp;&emsp;A API de recepção de áudio possui um único endpoint, `/transcribe`, que é responsável por receber arquivos de áudio enviados pelo frontend, processá-los e enviar esses dados para a API de transcrição de fala. Este endpoint utiliza o método `HTTP POST` para receber arquivos de áudio. Quando o frontend envia um arquivo de áudio, ele é encapsulado em um formulário usando o formato `multipart/form-data`, que é automaticamente gerado pelo navegador ao utilizar o objeto `FormData`. Este formato permite a transferência eficiente de arquivos e dados binários na requisição HTTP, garantindo que o backend possa acessar o arquivo de áudio diretamente através de `request.files`.

&emsp;&emsp;Ao receber a solicitação, o backend Flask verifica se o arquivo de áudio está presente e, se estiver, processa o arquivo de acordo com seu tipo MIME. A API suporta arquivos de áudio no formato `audio/webm;codecs=opus`, um formato altamente compatível com navegadores modernos. Atualmente, arquivos de áudio em outros formatos, como `audio/mp3` ou `audio/wav`, não são aceitos. Além disso, o tamanho máximo de arquivo suportado é de 5MB. Arquivos que excedem este limite resultarão em uma resposta de erro.

| Código de Status  | Descrição                         | Exemplo de corpo de resposta                                                                                      |
| ----------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `200 OK`          | Transcrição realizada com sucesso | json {"results": [{"alternatives": [{"confidence": x "transcript": texto transcrito"}], "final": true or false}]} |
| `400 Bad Request` | Nenhum arquivo de áudio enviado   | json {"error": "No audio file sent"}                                                                              |

&emsp;&emsp;Esta tabela resume os códigos de status HTTP que podem ser retornados pela API, junto com a descrição do que cada código significa e exemplos dos corpos de resposta que acompanham cada código. Essas informações ajudam os desenvolvedores a entender como lidar com diferentes respostas e como integrar corretamente suas aplicações.

### Exemplos de Chamadas à API

&emsp;&emsp;A seguir, vamos fornecer exemplos de como a API pode ser chamada para enviar um arquivo de áudio gravado pelo usuário. Estes exemplos são apresentados usando JavaScript, simulando como o frontend da aplicação interage com a API para enviar arquivos de áudio e receber a transcrição. Para enviar um arquivo de áudio gravado pelo usuário para a API de transcrição, seguimos um processo simples de gravação e upload utilizando a `fetch API` do JavaScript. O arquivo de áudio é capturado no formato webm e enviado usando um formulário `multipart/form-data`.

**1. Gravar o Áudio do Usuário:**

- O usuário clica no botão "Gravar" para iniciar a captura de áudio. O navegador solicita permissão para acessar o microfone.
- O áudio é gravado em chunks utilizando o `MediaRecorder API` do navegador.

**2. Parar a Gravação e Criar o Blob de Áudio:**

- Ao clicar no botão "Parar", a gravação é interrompida.
- Os chunks de áudio capturados são combinados em um único arquivo Blob (audioBlob).

**3. Enviar o Áudio para a API:**

- O Blob de áudio é anexado a um objeto FormData e enviado para o endpoint /transcribe da API usando o método HTTP POST.

&emsp;&emsp;Abaixo está um exemplo de como a aplicação frontend realiza essa operação:

```
const uploadAudio = async (audioBlob) => {
  try {
    // Cria um objeto FormData e anexa o arquivo de áudio
    const formData = new FormData();
    formData.append('audio', audioBlob, 'recording.webm');

    // Faz a solicitação POST para a API de transcrição
    const response = await fetch('http://localhost:5001/transcribe', {
      method: 'POST',
      body: formData,
    });

    // Verifica se a resposta é bem-sucedida e exibe a transcrição
    if (response.ok) {
      const data = await response.json();
      const transcriptText = data.results[0].alternatives[0].transcript;
      console.log('Transcrição:', transcriptText);
    } else {
      console.error('Erro ao enviar o arquivo:', response.status, response.statusText);
    }
  } catch (error) {
    console.error('Erro ao fazer upload do áudio:', error);
  }
};
```

- **Criação do FormData:** Um objeto `FormData` é criado para armazenar o Blob de áudio. O método append é usado para adicionar o Blob ao formulário com o nome do campo 'audio' e o nome do arquivo 'recording.webm'.

- **Envio da Requisição:** A função `fetch` é usada para enviar o formulário para a API. O método POST é especificado, e o corpo da requisição é o FormData que contém o arquivo de áudio.

- **Tratamento da Resposta:** Após o envio, verificamos se a resposta é bem-sucedida (response.ok). Se for, a transcrição recebida da API é extraída e exibida no console. Em caso de erro, a mensagem de erro é exibida para o desenvolvedor.

&emsp;&emsp;Quando a API recebe um arquivo de áudio válido, a resposta esperada é um JSON contendo a transcrição do áudio, como por exemplo:

```
{
    "result_index": 0,
    "results": [
        {
            "alternatives": [
                {
                    "confidence": 0.99,
                    "transcript": "transcri\u00e7\u00e3o funcionando perfeitamente "
                }
            ],
            "final": true
        }
    ]
}
```

### Testes da API

&emsp;&emsp; A seguir, detalhamos os testes realizados para verificar a funcionalidade e qualidade da API de recepção de áudio. Cada teste é descrito com suas pré-condições, etapas, resultados esperados, resultados obtidos e evidências visuais para demonstrar seu funcionamento correto.

#### Teste 1: Envio de um Arquivo de Áudio Válido

- **Objetivo**: Verificar se a API aceita um arquivo de áudio válido enviado pelo frontend e retorna a transcrição correta.

&emsp;&emsp;**Pré-condição**:

- A aplicação frontend (React) deve estar em execução (npm run dev ou yarn dev).
- A API em Flask deve estar em execução e acessível no endpoint http://localhost:5001/transcribe.
- O navegador suporta o tipo MIME `audio/webm;codecs=opus`.

&emsp;&emsp;**Etapas do Teste:**

- Abrir o navegador e acessar a aplicação frontend em http://localhost:3000.
- Clicar no botão "Gravar" para iniciar a gravação de áudio.
- Falar no microfone para gravar uma mensagem de teste.
- Clicar no botão "Parar" para interromper a gravação.
- Verificar se o console exibe a transcrição retornada.

&emsp;&emsp;**Pós-condição:**

- A resposta da API deve conter um código de status `200 OK`.
- O console do navegador deve mostrar uma mensagem de sucesso com a transcrição do áudio.

&emsp;&emsp;**Resultados Esperados:**

- O corpo da resposta deve ser algo como:

```
{
    "result_index": 0,
    "results": [
        {
            "alternatives": [
                {
                    "confidence": x,
                    "transcript": "texto transcrito"
                }
            ],
            "final": true
        }
    ]
}
```

&emsp;&emsp;**Resultados Obtidos:**

<div align="center">
  <sub>Figura X: Teste 1</sub>
  <img src="../assets/teste1.png" alt=“Teste1 width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

#### Teste 2: Envio de um Arquivo de Áudio Vazio

- **Objetivo**: Verificar se a API retorna um erro apropriado quando um arquivo de áudio vazio é enviado.

&emsp;&emsp;**Pré-condição:**

- A aplicação frontend deve estar em execução.
- A API Flask deve estar em execução e acessível no endpoint http://localhost:5001/transcribe.
- O usuário inicia e para a gravação muito rapidamente.

&emsp;&emsp;**Etapas do Teste:**

- Abrir o navegador e acessar a aplicação frontend em http://localhost:3000.
- Clicar no botão "Gravar" e rapidamente clicar em "Parar".
- Verificar o console do navegador para mensagens indicando que o áudio gravado é vazio.

&emsp;&emsp;**Pós-condição:**

- O console do navegador deve mostrar uma mensagem de erro indicando que o arquivo de áudio está vazio.

&emsp;&emsp;**Resultados Esperados:**

- O console deve exibir uma mensagem semelhante a:

`Nenhum chunk de áudio disponível para criar o Blob.`

&emsp;&emsp;**Resultados Obtidos:**

<div align="center">
  <sub>Figura X: Teste 2</sub>
  <img src="../assets/teste2.png" alt=“Teste2 width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

#### Teste 3: Usuário Não Autoriza o Uso do Microfone

- **Objetivo:** Verificar se a aplicação lida corretamente com a situação em que o usuário não autoriza o uso do microfone, fornecendo uma mensagem de erro clara e informativa.

- **Pré-condição:**
- O navegador deve ser capaz de solicitar permissão para acessar o microfone.
- O usuário deve estar ciente de que precisa conceder permissão para o uso do microfone.
- A aplicação frontend deve estar em execução.

- **Etapas do Teste:**
- Abrir o navegador e acessar a aplicação frontend em http://localhost:3000.
- Iniciar a gravação de audio clicando no botão "Gravar" na interface do usuário.
- Negar permissão para o microfone
- Verificar o console do navegador para ver a mensagem de erro correspondente.

- **Pós-condição:**
- A aplicação deve exibir uma mensagem clara para o usuário, indicando que a gravação de áudio não pode ser iniciada sem a permissão para o microfone.
- O console do navegador deve mostrar um erro, como DOMException: Permission denied.

- **Resultados Esperados:**
- Deve haver uma mensagem de erro no console:
  `VoiceRecorder.js:68 Erro ao acessar o microfone: DOMException: Permission denied`

- **Resultados Obtidos:**

<div align="center">
  <sub>Figura X: Teste 3</sub>
  <img src="../assets/teste3.png" alt=“Teste3 width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

&emsp;&emsp;Os testes realizados diretamente pelo frontend mostram que a API de recepção de áudio responde corretamente a diferentes cenários de uso, incluindo arquivos de áudio válidos e arquivos vazios. A API retorna códigos de status HTTP apropriados e mensagens de erro informativas conforme esperado.

# 5. Construção do Banco de Dados

&emsp;&emsp; Nesta seção, será abordada a construção do banco de dados para o projeto Vox. O banco de dados é uma parte essencial do sistema, responsável por armazenar e gerenciar os dados de forma eficiente e segura. A arquitetura do banco de dados foi projetada para atender às necessidades do sistema de NLP e da aplicação para busca e armazenamento de regulamentações.

## 5.1 Modelagem do Banco de Dados

&emsp;&emsp; A modelagem do banco de dados foi realizada com base nos requisitos do projeto, considerando as entidades e relacionamentos necessários para armazenar e gerenciar os dados de forma eficiente. O modelo do banco de dados foi elaborado utilizando a ferramenta dbdiagram.io, que permite a criação de diagramas de banco de dados de forma visual e intuitiva.

<div align="center">
  <sub>Figura X - Modelo do Banco de Dados</sub>
  <img src="./assets/vox-dbdiagram.png" width="100%" alt='Modelo do Banco de Dados'>
  <sup>Fonte: Os autores (2024) | <a href="https://dbdiagram.io/home">dbdiagram.io</a></sup>
</div>

<br>

&emsp;&emsp; Dentro do modelo do banco de dados, foram definidas as seguintes entidades principais, cada uma representando um aspecto específico do sistema:

<br>

| **Entidade**             | **Descrição**                                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ScrapingLog**          | Registra as informações sobre o scraping de dados de regulamentações, incluindo a data e hora da execução, o status da operação e mensagens de erro, se houver.         |
| **Regulator**            | Representa as entidades reguladoras responsáveis por emitir e manter as regulamentações, contendo informações como nome e o link do website onde o scraping será feito. |
| **Regulation**           | Armazena as informações sobre as regulamentações, incluindo o título, a data de publicação, sobre o que a norma se trata e o link para o documento original.            |
| **RegulationBacklink**   | Registra os links de referência para as regulamentações, permitindo associar normas relacionadas, seja por atualização, revogação ou complementação.                    |
| **RegulationCategories** | Tabela intermediária que associa as regulamentações com as categorias correspondentes, permitindo a classificação e organização das normas por temas.                   |
| **Tags**                 | Representa as tags associadas às regulamentações, permitindo a categorização e a busca por temas específicos.                                                           |
| **Notifications**        | Armazena as notificações enviadas aos usuários, incluindo o conteúdo da mensagem, a data de envio e o status de leitura.                                                |

<br>

&emsp;&emsp; Tendo as entidades, atributos e relacionamentos definidos, o modelo do banco de dados pode ser devidamente implementado em um banco de dado real, como o PostgreSQL, para armazenar e gerenciar os dados do projeto Vox de forma eficiente.

## 5.2 Implementação do Banco de Dados

&emsp;&emsp; O banco de dados foi implementado utilizando o PostgreSQL, que foi escolhido devido à sua robustez, escalabilidade e conformidade com os padrões SQL, além de oferecer recursos avançados como suporte a transações, replicação, e extensões para funções específicas, o que o torna ideal para aplicações de monitoramento de dados e análise regulatória.

&emsp;&emsp; Para o armazenamento e gerenciamento dos dados, utilizamos a plataforma [Supabase](https://supabase.com), que oferece fácil integração com o PostgreSQL, permite o desenvolvimento rápido de APIs RESTful a partir de tabelas do banco de dados, possibilidade de desenvolvimento colaborativo e seu suporte a recursos avançados, como autenticação integrada e auditoria de logs.

&emsp;&emsp; Ao configurar o banco de dados no Supabase, foram definidos esquemas e tabelas para armazenar regulamentos, notificações, logs de scraping, e outras informações relevantes de forma estruturada e segura, garantindo a conformidade com os requisitos do projeto.

&emsp;&emsp; Importante ressaltar que, após a finalização do projeto, a conexão com o supabase deve ser alterada para um banco de dados em uma RDS (Relational Database Service) da AWS.

<div align="center">
  <sub>Figura X - Projeto Vox no Supabase</sub>
  <img src="./assets/vox-supabase.png" width="100%" alt='Projeto Vox no Supabase'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Em conclusão, a implementação do banco de dados no PostgreSQL via Supabase proporciona uma solução robusta e escalável para o armazenamento e gerenciamento dos dados do projeto Vox, garantindo a integridade e segurança das informações.

# 6. Construção do Backend da Solução

&emsp;&emsp;Nesta seção, são descritos os principais endpoints utilizados para o processamento de linguagem natural (PLN) e o webhook de scraping de regulamentações no backend. Os endpoints permitem o processamento de textos e a integração dos dados com o banco de dados, utilizando um modelo de PLN.

### Estrutura geral

&emsp;&emsp;O backend da aplicação foi construído utilizando o Flask, um micro-framework para Python. A arquitetura do projeto segue uma estrutura modular, dividida em diversos componentes essenciais que visam manter a organização e facilitar a manutenção da aplicação. O diagrama básico da estrutura do projeto é:

```
backend/
│
├── app/
│   ├── pln/                   # Módulo para Processamento de Linguagem Natural (PLN)
│   ├── regulator/             # Módulo regulador
│   ├── scraping/              # Módulo de scraping para coleta de dados
│   ├── __init__.py            # Arquivo inicializador do módulo Flask
│   ├── config.py              # Arquivo de configuração (gerencia variáveis de ambiente e configurações do app)
│   └── database.py            # Arquivo responsável pela conexão com o banco de dados
│
├── venv/                      # Ambiente virtual Python
├── run.py                     # Arquivo principal para rodar o servidor Flask
```

### Descrição dos Módulos

#### app/

&emsp;&emsp;A pasta app/ contém os principais componentes da aplicação Flask. Dentro desta pasta, encontramos os seguintes módulos:

- pln/: Módulo dedicado ao Processamento de Linguagem Natural (PLN). Aqui, são implementados os algoritmos ou integrações para interpretar e processar texto, uma vez que o backend parece envolver interação com PLN.

- regulator/: Este módulo provavelmente contém as regras de negócio e regulações específicas da solução. Pode incluir funções que controlam o fluxo de dados ou a lógica condicional da aplicação.

- scraping/: Módulo responsável por tarefas de scraping (coleta de dados na web). Este componente interage com páginas externas para extrair informações que serão posteriormente processadas.

- \_\_init\_\_.py: Arquivo que inicializa a aplicação Flask e os módulos necessários para seu funcionamento. Ele configura o Flask e integra as dependências de módulos.

&emsp;&emsp;Cada módulo do backend contém três componentes principais:

1. **Controller:** Responsável por definir as rotas e interagir diretamente com as requisições HTTP. O controller recebe as requisições, chama os serviços necessários, e envia as respostas para o cliente.
2. **Service:** Implementa a lógica de negócio do módulo. Ele realiza o processamento dos dados, interage com outros serviços e faz uso dos modelos para acessar o banco de dados.
3. **Model:** Define as estruturas de dados que representam as tabelas do banco de dados. Cada model é mapeado para uma tabela no banco e contém métodos para interagir com os dados.

#### config.py

&emsp;&emsp;Este arquivo contém as configurações da aplicação, como variáveis de ambiente, chaves secretas, e opções de configuração do Flask. Normalmente, este arquivo utiliza variáveis definidas em um arquivo .env para configurar o ambiente de desenvolvimento e produção de forma separada.

#### database.py

&emsp;&emsp;O arquivo database.py é responsável por gerenciar a conexão com o banco de dados. Utilizando a ORM **SQLAlchemy**, ela define a estrutura dos dados e gerencia as operações no banco.

### Ambiente Virtual (venv/)

&emsp;&emsp;O ambiente virtual (venv/) é utilizado para isolar as dependências da aplicação. Ele garante que as bibliotecas e pacotes utilizados no projeto sejam gerenciados de forma independente, evitando conflitos com outras versões de pacotes instalados no sistema.

### Script Principal (run.py)

&emsp;&emsp;O arquivo run.py é o ponto de entrada da aplicação. Ele inicia o servidor Flask, configurando as rotas e dependências iniciais necessárias para o funcionamento da aplicação.

### Fluxo de Desenvolvimento

&emsp;&emsp;O fluxo de desenvolvimento básico inclui:

1. **Configuração do ambiente:** Certifique-se de que o ambiente virtual (venv/) esteja ativo e instale as dependências listadas no arquivo requirements.txt.
   `pip install -r requirements.txt`

2. **Execução da aplicação:** Após a configuração, a aplicação pode ser iniciada com o comando:
   `python run.py`

&emsp;&emsp;A arquitetura modular do projeto torna o desenvolvimento escalável e permite a adição de novas funcionalidades sem comprometer o funcionamento atual. A organização clara em módulos facilita a manutenção e possibilita que diferentes equipes trabalhem de forma independente em diferentes partes da aplicação.

## 6.1 Endpoints do backend

&emsp;&emsp;Esta seção apresenta a descrição dos endpoints disponíveis no backend do sistema. Cada endpoint corresponde a uma funcionalidade específica, abrangendo desde o processamento de linguagem natural (PLN) até a transcrição de áudios e o gerenciamento de regulamentações. A seguir, são fornecidas informações detalhadas sobre os métodos HTTP, os formatos de requisição, exemplos de corpos de requisição e as respostas possíveis para cada endpoint.

### 1. Endpoint: `POST /pln/`

#### Descrição

&emsp;&emsp;Este endpoint recebe um texto de entrada, processa o texto utilizando técnicas de PLN e faz uma previsão com base em um modelo treinado de PLN. O resultado da previsão é retornado na resposta.

#### Método HTTP

- **POST**

#### Body da Requisição (JSON)

- `input` (string): O texto que será processado e classificado pelo modelo.

```json
{
  "input": "Este é um exemplo de texto para processamento."
}
```

#### Resposta de Sucesso (200 OK):

```json
{
  "resultado": "categoria_predita"
}
```

### 2. Endpoint: `POST /pln/webhook-scraping`

#### Descrição

&emsp;&emsp;Este endpoint recebe um webhook com dados e os envia para o banco de dados. Ele é utilizado para processar e registrar informações relacionadas a novas regulamentações.

#### Método HTTP

- **POST**

#### Body da Requisição (JSON)

- JSON contendo os dados da regulamentação a serem enviados ao banco de dados.

```json
{
  "regulatorid": 201,
  "title": "New Regulation Title",
  "topic": "Financial Services",
  "description": "This is a description of the new regulation regarding financial services.",
  "documenturl": "https://example.com/regulation.pdf",
  "status": true,
  "publicationdate": "2024-09-13T00:00:00Z",
  "tags": [
    {
      "name": "Finance",
      "color": "#434343"
    }
  ]
}
```

#### Resposta de Sucesso (200 OK)

```json
{
  "status": "Data enviada para o banco com sucesso",
  "dados_enviados": {
    "regulatorid": 201,
    "title": "New Regulation Title",
    "topic": "Financial Services",
    "description": "This is a description of the new regulation regarding financial services.",
    "documenturl": "https://example.com/regulation.pdf",
    "status": true,
    "publicationdate": "2024-09-13T00:00:00Z",
    "tags": [
      {
        "name": "Finance",
        "color": "#434343"
      }
    ]
  }
}
```

#### Resposta de Erro(500 Internal Server Error)

```json
{
  "error": "Falha ao enviar para o banco: (Detalhes do erro)"
}
```

### 3. Endpoint: `GET /regulations/<int:id>`

#### Descrição

&emsp;&emsp;Este endpoint retorna uma regulação específica com base no ID fornecido.

#### Método HTTP

- **GET**

#### Parâmetros da URL

- `id` (inteiro): O ID da regulação que se deseja buscar.

#### Resposta de Sucesso (200 OK):

```json
{
  "regulatorid": 201,
  "title": "Regulation Title",
  "topic": "Financial Services",
  "description": "This is a description of the regulation.",
  "documenturl": "https://example.com/regulation.pdf",
  "status": true,
  "publicationdate": "2024-09-13T00:00:00Z",
  "tags": [
    {
      "name": "Finance",
      "color": "#434343"
    }
  ]
}
```

#### Resposta de Erro(404 Not Found)

```json
{
  "error": "Regulamento não encontrado"
}
```

### 4. Endpoint: `GET /regulations`

#### Descrição

&emsp;&emsp;Este endpoint retorna uma lista de todas as regulações.

#### Método HTTP

GET

#### Resposta de Sucesso (200 OK):

```json
[
  {
    "regulatorid": 201,
    "title": "Regulation Title 1",
    "topic": "Financial Services",
    "description": "Description for regulation 1.",
    "documenturl": "https://example.com/regulation1.pdf",
    "status": true,
    "publicationdate": "2024-09-13T00:00:00Z",
    "tags": [
      {
        "name": "Finance",
        "color": "#434343"
      }
    ]
  },
  {
    "regulatorid": 202,
    "title": "Regulation Title 2",
    "topic": "Health Services",
    "description": "Description for regulation 2.",
    "documenturl": "https://example.com/regulation2.pdf",
    "status": false,
    "publicationdate": "2024-09-14T00:00:00Z",
    "tags": [
      {
        "name": "Health",
        "color": "#123456"
      }
    ]
  }
]
```

### 5. Endpoint: `POST /regulations`

#### Descrição

&emsp;&emsp;Este endpoint cria uma nova regulação com base nos dados fornecidos no corpo da requisição.

#### Método HTTP

- **POST**

#### Body da Requisição (JSON)

- `regulatorid` (inteiro): O ID do regulador.
- `title` (string): O título da regulação.
- `topic` (string): O tópico da regulação.
- `description` (string): A descrição da regulação.
- `documenturl` (string): A URL do documento da regulação.
- `status` (booleano): O status da regulação (ativo/inativo).
- `publicationdate` (string, formato ISO 8601): A data de publicação da regulação.
- `tags` (array): Lista de tags associadas à regulação.

Exemplo de body:

```json
{
  "regulatorid": 203,
  "title": "New Regulation Title",
  "topic": "Education",
  "description": "This is a description of the new regulation regarding education.",
  "documenturl": "https://example.com/education.pdf",
  "status": true,
  "publicationdate": "2024-10-01T00:00:00Z",
  "tags": [
    {
      "name": "Education",
      "color": "#abcdef"
    }
  ]
}
```

#### Respostas de Sucesso (202 Created)

```json
{
  "regulatorid": 203,
  "title": "New Regulation Title",
  "topic": "Education",
  "description": "This is a description of the new regulation regarding education.",
  "documenturl": "https://example.com/education.pdf",
  "status": true,
  "publicationdate": "2024-10-01T00:00:00Z",
  "tags": [
    {
      "name": "Education",
      "color": "#abcdef"
    }
  ]
}
```

#### Resposta de Erro (400 Bad Request):

```json
{
  "error": "Missing field: 'title'"
}
```

#### Resposta de Erro (500 Internal Server Error):

```json
{
  "error": "Erro interno no servidor"
}
```

### 6. Endpoint: `POST /audio/transcribe`

#### Descrição

&emsp;&emsp;Este endpoint recebe um arquivo de áudio, valida o tamanho do arquivo e o tipo de conteúdo, e o envia para um serviço externo de transcrição de áudio (IBM Speech to Text). A transcrição é armazenada no banco de dados e o resultado é retornado na resposta.

#### Método HTTP

- **POST**

#### Body da Requisição (multipart/form-data)

- `audio` (file): O arquivo de áudio a ser transcrito. Suporta arquivos `.webm` ou `.l16`.

Exemplo de body:

```multipart/form-data
Content-Type: multipart/form-data; boundary=---boundary
---boundary
Content-Disposition: form-data; name="audio"; filename="audio_sample.webm"
Content-Type: audio/webm
```

#### Regras de validação:

- Tamanho máximo do arquivo: 5 MB.
- Tipos de arquivos suportados: .webm e .l16 (16 kHz

#### Resposta de Sucesso (200 OK)

```json
{
  "results": [
    {
      "alternatives": [
        {
          "transcript": "Este é o texto transcrito do áudio."
        }
      ]
    }
  ]
}
```

#### Resposta de Erro (413 Payload Too Large):

```json
{
  "error": "File too large",
  "message": "O arquivo excede o limite de 5 MB."
}
```

#### Resposta de Erro (400 Bad Request):

```json
{
  "error": "No audio file sent"
}
```

#### Resposta de Erro (500 Internal Server Error):

```json
{
  "error": "Error uploading file",
  "status_code": 500,
  "message": "Detalhes do erro"
}
```

## 6.2 Integração do Speech-to-text

&emsp;&emsp;Este sistema realiza a gravação de áudio no frontend, envia o arquivo para o backend e, em seguida, o backend processa o arquivo de áudio utilizando a API **IBM Watson Speech to Text** para converter a fala em texto. A transcrição do áudio é então armazenada em um banco de dados para futuras consultas.

### Funcionalidade

1. **Frontend**: O componente `VoiceRecorder` grava o áudio no navegador do usuário e o envia para o backend em formato `audio/webm` utilizando `FormData` via uma requisição POST.
2. **Backend**: O backend recebe o arquivo de áudio e o encaminha para a API IBM Watson Speech to Text, que processa o arquivo e retorna a transcrição.
3. **Banco de Dados**: A transcrição é armazenada em uma tabela no banco de dados com informações sobre o arquivo e o texto transcrito.

### Como Funciona a Integração

#### Fluxo de Dados

1. O áudio é capturado pelo navegador utilizando a API `MediaRecorder` e enviado para o backend via uma requisição POST para o endpoint `/transcribe`.
2. O backend recebe o arquivo de áudio e verifica se ele está dentro do tamanho máximo permitido de 5 MB.
3. O backend então faz uma requisição POST para o serviço **IBM Watson Speech to Text**, enviando o arquivo de áudio e utilizando autenticação básica.
4. A API da IBM retorna um objeto JSON contendo a transcrição do áudio.
5. O backend armazena essa transcrição no banco de dados.
6. A resposta do backend inclui a transcrição que é exibida no frontend para o usuário.

#### Requisição para a API IBM Watson Speech to Text

&emsp;&emsp;No backend, a integração com o serviço de transcrição de voz é feita através de uma requisição POST para a API da IBM. A requisição contém o arquivo de áudio no corpo e inclui as credenciais de autenticação.

**Exemplo de Requisição:**

```python
response = requests.post(
    IMB_SPEECH_TO_TEXT_URL,
    headers={
        "Content-Type": content_type
    },
    data=audio_file,
    auth=HTTPBasicAuth(IMB_SPEECH_TO_TEXT_USERNAME, IMB_SPEECH_TO_TEXT_PASSWORD)
)
```

#### Estrutura de Armazenamento no Banco de Dados

&emsp;&emsp;As transcrições são salvas na tabela `transcription` com as seguintes informações:

- `audio_name`: O nome do arquivo de áudio.
- `transcription_text`: O texto transcrito a partir do áudio.
- `created_at`: Data e hora da criação da transcrição.

**Exemplo de Registro no Banco de Dados:**

```python
transcription = Transcription(
    audio_name=filename,
    transcription_text=transcription_text
)
db.session.add(transcription)
db.session.commit()
```

#### Exemplo de Uso no Frontend

&emsp;&emsp;No frontend, o componente React `VoiceRecorder` gerencia a gravação do áudio e a comunicação com o backend. Após o envio do áudio, o backend retorna a transcrição, que é exibida ao usuário.

**Trecho de Código do Frontend:**

```javascript
const uploadAudio = async (audioBlob) => {
  const formData = new FormData();
  formData.append("audio", audioBlob, "recording.webm");

  const response = await fetch("http://localhost:5001/transcribe", {
    method: "POST",
    body: formData,
  });

  if (response.ok) {
    const data = await response.json();
    const transcriptText = data.results[0].alternatives[0].transcript;
    setTranscript(transcriptText);
  }
};
```

&emsp;&emsp;Essa integração permite que o áudio gravado no frontend seja transcrito automaticamente utilizando a API IBM Watson Speech to Text, com as transcrições sendo armazenadas no banco de dados para consultas futuras.

## 6.3 Webhook

&emsp;&emsp;Um webhook é um método de comunicação entre sistemas que permite que uma aplicação envie dados em tempo real para outra, em resposta a um evento específico. Diferente das requisições tradicionais, onde um cliente consulta um servidor periodicamente, o webhook funciona de maneira "reativa", ou seja, ele envia automaticamente os dados para um endpoint configurado sempre que o evento é disparado. Na prática, webhooks são amplamente utilizados para notificar sistemas externos sobre atualizações, mudanças de estado ou eventos, como quando uma nova mensagem é recebida, uma transação é concluída ou um novo dado é coletado.

&emsp;&emsp;No contexto deste projeto, o webhook é responsável por processar e distribuir os dados capturados durante o processo de Scraping, Tagging e envio ao banco de dados, garantindo que os sistemas conectados recebam as informações de forma eficiente e em tempo real.

&emsp;&emsp;O fluxo de interação do Webhook é responsável por intermediar os serviços de Scraping, Tagueamento e envio dos dados ao banco de dados. A seguir, é apresentado a arquitetura do Webhook e seus respectivos serviços:

<sub>Figura X - Arquitetura Webhook</sub>
<img src="./assets/arquiteturawebhook.png" width="100%" alt='Arquitetura Webhook'>
<sup>Fonte: Os autores (2024)</sup>

</div>

&emsp;&emsp;O serviço de Scraping, integrado ao AWS Lambda, realiza diariamente a coleta de dados, que são então enviados ao servidor de mensageria (RabbitMQ). Após o recebimento, os dados entram em uma fila e são encaminhados para uma função de callback na nossa API. A seguir, o Webhook é acionado para processar essas requisições uma a uma, distribuindo-as entre os serviços apropriados até que o processo seja concluído e o resultado final seja retornado ao cliente com um status 200 OK.

&emsp;&emsp;O fluxo funciona da seguinte maneira: o Webhook aciona o serviço de Tag, e após o sucesso deste, os dados são enviados para o serviço de Regulamentação, que processa e armazena a norma 'tagueada' no banco de dados. Com a conclusão bem-sucedida de todas as etapas, o nosso servidor principal recebe o código de status 200 OK.

**Trecho de Código da callback:**

```Python
def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

        webhook_url = 'http://127.0.0.1:5000/pln/webhook-scraping'

        try:
            # Converte o corpo da mensagem de bytes para string e depois para JSON
            body_str = body.decode('utf-8')
            body_json = json.loads(body_str)
            # Enviar os dados para o webhook
            webhook_response = requests.post(webhook_url, json=body_json)
            webhook_response.raise_for_status()

            print("Webhook processado com sucesso")
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except requests.exceptions.RequestException as e:
            print(f"Falha no webhook, erro: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"Erro ao processar mensagem: {str(e)}")
            ch.basic_nack(delivery_tag=method.delivery_tag)
```

&emsp;&emsp;O Webhook espera receber um conjunto de dados com os seguintes itens:

- "regulatorid": Identificador da entidade reguladora (exemplo: 201).
- "title": Título da nova regulamentação (exemplo: "New Regulation Title").
- "topic": Tema relacionado à regulamentação (exemplo:"Financial Services").
- "description": Descrição detalhada da nova regulamentação (exemplo: "This is a description of the new regulation regarding financial services").
- "documenturl": URL do documento da regulamentação (exemplo: "https://example.com/regulation.pdf").
- "status": Status da regulamentação (exemplo: True).
- "publicationdate": Data de publicação da regulamentação (exemplo: "2024-09-13T00:00:00Z").
- "tags": Lista de tags associadas à regulamentação, contendo:
- "name": Nome da tag (exemplo: "Finance").
- "color": Cor da tag no formato hexadecimal (exemplo: "#434343").

**Trecho de Código do Webhook:**

```Python
# Rota para processamento do webhook
@pln_blueprint.route('/webhook-scraping', methods=['POST'])
def webhook_scraping():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Nenhum dado JSON enviado'}), 400

    webhook_database_url = 'http://127.0.0.1:5000/regulations'

    # Exemplo de dados para enviar ao banco de dados
    data_base_send = {
        "regulatorid": 201,
        "title": "New Regulation Title",
        "topic": "Financial Services",
        "description": "This is a description of the new regulation regarding financial services.",
        "documenturl": "https://example.com/regulation.pdf",
        "status": True,
        "publicationdate": "2024-09-13T00:00:00Z",
        "tags": [
            {
                "name": "Finance",
                "color": "#434343"
            }
        ]
    }

    try:
        # Enviar os dados para o banco de dados
        webhook_database_response = requests.post(webhook_database_url, json=data_base_send)
        webhook_database_response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP 4xx/5xx

        print("Webhook enviou para o banco com sucesso")
        return jsonify({'status': 'Data enviada para o banco com sucesso', 'dados_enviados': data_base_send}), 200

    except requests.exceptions.RequestException as e:
        print(f"Falha ao enviar para o banco: {e}")
        return jsonify({'error': f'Falha ao enviar para o banco: {e}'}), 500
```

&emsp;&emsp;Ao final da execução, se tudo deu certo, o serviço do Webhook retorna um código de status 200 ao servidor.

<sub>Figura X - Resposta Servidor Webhook</sub>
<img src="./assets/retorno200webhook.png" width="100%" alt='Resposta Servidor Webhook'>
<sup>Fonte: Os autores (2024)</sup>

</div>

## 6.4 Serviço de mensageria (RabbitMQ)

&emsp;&emsp; O RabbitMQ é um software de mensageria open-source que implementa o protocolo AMQP (Advanced Message Queuing Protocol) para troca de mensagens entre aplicações. Ele é amplamente utilizado em sistemas distribuídos para comunicação assíncrona entre componentes, permitindo a escalabilidade e a resiliência da aplicação.

&emsp;&emsp; Para rodar o RabbitMQ, é necessário rodar o container Docker com o seguinte comando:

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

Após isso, o RabbitMQ estará disponível em `http://localhost:15672` com as credenciais padrão `guest:guest`.

<div align="center">
  <sub>Figura X - Fila do RabbitMQ</sub>
  <img src="./assets/rabbitmq-queue.jpg" width="100%" alt='Fila do RabbitMQ'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

### Utilização do RabbitMQ

&emsp;&emsp; Na aplicação Vox, o RabbitMQ é utilizado para facilitar a comunicação entre o serviço de scraping e o serviço de processamento de linguagem natural (PLN), responsável pelo tagueamento de normas e regulamentações. A fila "scraping_queue" foi criada para armazenar as mensagens contendo os dados capturados pelo serviço de scraping, antes que esses dados sejam enviados para o serviço de PLN. Essa arquitetura permite que os serviços sejam desacoplados e que o processamento seja realizado de forma assíncrona, aumentando a resiliência do sistema.

<div align="center">
  <sub>Figura X - Funcionamento do RabbitMQ</sub>
  <img src="./assets/rabbitmq-routing.png" width="100%" alt='Funcionamento do RabbitMQ'>
  <sup>Fonte: RabbitMQ</sup>
</div>

<br>

### Produção de Mensagens (Serviço de Scraping)

&emsp;&emsp; O serviço de scraping atua como publisher no sistema de mensageria, sendo responsável por coletar dados de diversas fontes e publicar essas informações na fila "scraping_queue". O publisher é configurado para enviar as mensagens de forma eficiente e segura, garantindo que os dados cheguem ao serviço de processamento de linguagem natural (PLN).

&emsp;&emsp; O publisher segue um fluxo de produção de mensagens que inclui:

- **Coleta de Dados**: O serviço de scraping deverá extrair dados brutos do site da BACEN a cada 24 horas, coletando informações referentes a novas normas e regulamentações publicadas.
- **Formato da Mensagem**: Cada mensagem enviada pelo publisher contém os dados capturados e é estruturada em um JSON, garantindo que o consumidor (serviço de PLN) possa interpretar e processar as informações corretamente.

- **Envio para a Fila**: O publisher publica as mensagens diretamente na fila "scraping_queue", utilizando uma exchange configurada para rotear as mensagens para a fila correta. Isso garante que as mensagens sejam entregues de forma confiável ao serviço de PLN.

```python
channel.queue_declare(queue='scraping_queue', durable=True)
```

- **Persistência**: Para garantir confiabilidade para o sistema, as mensagens são publicadas com a opção de persistência ativada, o que faz com que as mensagens sejam armazenadas em disco até serem processadas, evitando a perda de dados em caso de falhas no sistema.

- **Confirmação de Publicação**: O RabbitMQ foi configurado para fornecer um mecanismo de confirmação, no qual o publisher recebe um **acknowledgment** (confirmação) assim que o RabbitMQ garantir que a mensagem foi escrita em disco e roteada corretamente para a fila. Com isso, o publisher pode ter certeza de que a mensagem foi entregue.

### Consumo de Mensagens (Serviço de PLN)

&emsp;&emsp; O serviço de PLN atua como consumer no sistema de mensageria, sendo responsável por recuperar as mensagens da fila "scraping_queue" e processar os dados capturados pelo serviço de scraping.

&emsp;&emsp; É configurado para garantir o processamento confiável e eficiente das mensagens, utilizando controle de fluxo e mecanismos de confirmação para assegurar que as mensagens sejam processadas corretamente e não sejam perdidas em caso de falhas.

&emsp;&emsp; O consumer segue um fluxo de consumo de mensagens que inclui:

- **Consumo de Mensagens (Serviço de PLN)**: O serviço de PLN recupera as mensagens da fila e realiza o processamento de linguagem natural, como a extração de tags ou análise de conteúdo Esse processamento ocorre de forma assíncrona, permitindo que o serviço de scraping continue funcionando sem esperar pela conclusão do
  processamento no PLN.

```python
channel.queue_declare(queue='scraping_queue', durable=False)

channel.basic_consume(queue='scraping_queue', on_message_callback=callback)
```

- **Controle de Fluxo com basic_qos**: Para evitar que o serviço de PLN seja sobrecarregado ao receber muitas mensagens de uma vez, é utilizado o parâmetro `basic_qos` para controlar a quantidade de mensagens que o consumidor processa simultaneamente.

- **Confirmação de Mensagem com basic_ack**: Após o processamento bem-sucedido de uma mensagem, o consumidor envia uma confirmação (acknowledgment) para o RabbitMQ usando o comando `basic_ack`. Esse ack garante que as mensagens sejam removidas apenas após o processamento bem-sucedido, evitando que mensagens não processadas sejam perdidas.

- **Tratamento de Erros com basic_nack**: Caso ocorra um erro durante o processamento, o consumidor usa o comando `basic_nack` para rejeitar a mensagem. Com isso, ela é reencaminhada para a fila para tentar processá-la posteriormente e evitando perda de dados.

```python
try:
  webhook_response = requests.post(webhook_url, json=body_json)
  ch.basic_ack(delivery_tag=method.delivery_tag)

except requests.exceptions.RequestException as e:
  ch.basic_nack(delivery_tag=method.delivery_tag)
```

&emsp;&emsp; A utilização do RabbitMQ no projeto Vox permite a comunicação assíncrona e confiável entre os serviços de scraping e PLN, garantindo a escalabilidade e a resiliência do sistema.

# 7. Construção do Frontend da Solução

&emsp;&emsp; Esta seção aborda os aspectos do frontend da aplicação Vox, desenvolvida para otimizar a busca e acompanhamento de atualizações regulatórias no setor financeiro. A interface foi projetada com foco na simplicidade, intuitividade e na utilização de tecnologias como processamento de linguagem natural (PLN) para oferecer uma experiência eficiente tanto para interações via texto quanto por voz. A seguir, será detalhada a estrutura da interface, seus componentes principais e como eles se integram para oferecer uma navegação otimizada aos usuários.

## 7.1 Descrição da interface do usuário

&emsp;&emsp; A seguir, detalhamos os componentes que formam a interface de usuário da aplicação Vox, construída com foco na otimização da experiência de navegação e consulta de regulamentações financeiras. A interface foi projetada para oferecer uma interação simplificada, permitindo tanto buscas rápidas quanto consultas mais aprofundadas, utilizando tecnologias como reconhecimento de voz e PLN. Os elementos visuais foram cuidadosamente estruturados para garantir que os usuários encontrem as informações de forma intuitiva, seja através de buscas diretas, filtros avançados ou navegação entre temas relacionados. A seguir, abordamos a funcionalidade de cada componente da interface em suas respectivas telas.

### Tela Inicial (_Home_)

&emsp;&emsp;A tela inicial serve como ponto de entrada para as principais funcionalidades da aplicação. Ela oferece duas formas de interação para pesquisa de regulamentações: por texto e por comando de voz. A interface é composta pelos seguintes elementos principais:

<div align="center">
  <sub>Figura X: Tela inicial</sub>
  <img src="./assets/Interface/home.png" alt=“telainicial width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

1. **_Sidebar_ fixa:** Presente em todas as telas da aplicação, oferece uma navegação simplificada com links para:

- Adicionar regulamentações (ícone de "+" no topo da sidebar);
- Home (ícone de casa), que retorna o usuário à tela inicial;
- Explorar (ícone de lupa), que direciona à página de busca de regulamentações;
- Tags (ícone de etiqueta), que permite a categorização de regulamentações por tags específicas;
- Reguladores: Lista de órgãos reguladores (ex: BACEN, CVM, B3), permitindo que o usuário acesse diretamente as últimas modificações de cada um desses órgãos.

2. **Campo de pesquisa (_search bar_):** No centro da tela, permite ao usuário digitar sua pesquisa ou, clicando no ícone de microfone, realizar buscas utilizando PLN. O campo de pesquisa apresenta uma animação visual quando o comando de voz é ativado, conforme descrito na subseção a seguir.

3. **VUI (_Voice User Interface_):** Quando o usuário interage por comando de voz, o sistema oferece feedback visual em tempo real, possível visualizar nas imagens a seguir:

<div align="center">
  <sub>Figura X: Gravando áudio</sub>
  <img src="./assets/Interface/feedback-positive.png" alt=“GravandoÁudio width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

<div align="center">
  <sub>Figura X: Erro ao processar o áudio</sub>
  <img src="./assets/Interface/feedback-negative.png" alt=“ErroAoProcessarOÁudio width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

- A borda da search bar pisca em azul quando o sistema está gravando o áudio.
- Uma vez que a captura de áudio é concluída com sucesso, a borda permanece azul e o sistema processa o comando.
- Caso o sistema enfrente problemas na transcrição do áudio, a borda da search bar fica vermelha e uma mensagem de erro é exibida, sugerindo ao usuário que tente novamente.

4. **Botões de ação rápida:** Abaixo da barra de pesquisa, existem botões que oferecem atalhos para comandos populares, como: "Mostre as atualizações do dia", "Mostre as últimas normas do BACEN". Esses botões facilitam o acesso a informações rotineiras sem a necessidade de o usuário realizar uma pesquisa manual.

### Tela de Resultados

&emsp;&emsp;Após realizar uma pesquisa ou clicar no ícone de busca na _sidebar_, o usuário é direcionado para a tela de resultados. Essa página exibe as regulamentações encontradas de acordo com os termos pesquisados e/ou filtros aplicados. Os componentes principais desta tela incluem:

<div align="center">
  <sub>Figura X: Tela de Resultados</sub>
  <img src="./assets/Interface/search.png" alt=“TelaDeRegulamentações width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

1. **Quantidade de resultados:** Logo abaixo da barra de pesquisa, é exibido o número total de regulamentações que atendem ao critério de busca do usuário, por exemplo, "1.637 regulamentações encontradas".

2. **Filtros:** Permite o usuário selecionar atributos específicos como:

- Regulador: Permite selecionar o órgão regulador relevante (BACEN, CVM, B3);
- Período: Define o intervalo de datas para as regulamentações a serem exibidas;
- Tags: Facilita a segmentação das regulamentações por categorias, como "Segurança", "Transparência", entre outras.

3. **Lista de regulamentações:** Cada regulamentação é exibida em um cartão com os seguintes detalhes:

- Número do comunicado (por exemplo, Comunicado nº 42.030);
- Resumo da regulamentação com informações como o objetivo do comunicado e sua aplicação;
- Data de publicação;
- Categoria da regulação

&emsp;&emsp;Ao clicar em uma regulamentação específica, o usuário é direcionado para uma página detalhada, conforme descrito a seguir.

### Tela de Regulamentação Detalhada

&emsp;&emsp;Quando o usuário seleciona uma regulamentação na lista de resultados, ele é redirecionado para uma página dedicada, onde todos os detalhes da regulamentação são exibidos de maneira clara e acessível. Os principais elementos dessa tela incluem:

<div align="center">
  <sub>Figura X: Tela de Regulamentação</sub>
  <img src="./assets/Interface/regulamentation.png" alt=“TelaDeRegulamentação width="100%">
  <sup>Fonte: Elaborado pelo grupo Vox</sup>
</div>

1. **Título da regulamentação**: Apresentado no topo da página, com o número do comunicado e o órgão regulador responsável, seguido da data de publicação.

2. **Descrição completa**: Texto integral da regulamentação, permitindo ao usuário compreender o contexto e as implicações da nova regra.

3. **Informações adicionais**:

- Assunto: Indica a área temática da regulamentação (por exemplo, "Regulação Financeira");
- Tags: Exibe as tags associadas, ajudando na categorização e navegação entre regulamentações similares;
- Regulamentações relacionadas: Uma lista de links para outras regulamentações com temas correlatos, que facilita a exploração de documentos adicionais.

&emsp;&emsp;Além disso, um ícone de seta de retorno permite que o usuário volte rapidamente para a lista de resultados, otimizando a navegação.

&emsp;&emsp;Portanto, a interface de usuário foi desenvolvida com foco na usabilidade, integrando elementos visuais e funcionais que facilitam o acompanhamento de mudanças regulatórias. Com a presença de uma sidebar fixa e opções de pesquisa textual e por voz, a aplicação oferece uma experiência de uso eficiente para diferentes perfis de usuários. Além disso, a tela de resultados e a navegação por filtros avançados garantem que o usuário possa encontrar e visualizar regulamentações de forma rápida e organizada. Com o design centrado no usuário, a solução visa otimizar a interação com informações regulatórias no contexto da indústria financeira.

# 8. Integração Front e Back

&emsp;&emsp; Esta seção aborda como a aplicação Vox foi projetada para otimizar o processo de busca e acompanhamento de regulamentações financeiras, com foco na interação por voz. O sistema permite que os usuários façam pesquisas de regulamentações de forma intuitiva, utilizando comandos de voz que são transcritos e automaticamente convertidos em buscas no backend. Para proporcionar uma experiência fluida e eficiente, o frontend da aplicação se comunica com o backend por meio de chamadas de API, que permitem o envio de dados de áudio para transcrição e a realização de buscas automáticas com o texto transcrito. A seguir, serão descritos em detalhe os fluxos de transcrição de áudio e busca automática de regulamentações, destacando como essas interações são estruturadas para garantir um processamento ágil e preciso.

## Transcrição de áudio

&emsp;&emsp; A funcionalidade de transcrição de áudio permite que os usuários façam uma busca por voz. O áudio capturado é enviado para o backend, onde é transcrito para texto e utilizado como entrada para a pesquisa de regulamentações. Esse processo é fundamental para a busca automática, pois converte os comandos de voz do usuário em um formato processável pelo sistema.

1. **Frontend**: O componente `Microphone.tsx` é responsável por gerenciar a gravação de áudio do usuário. Ao clicar no ícone de microfone, o áudio é gravado e enviado ao backend para transcrição. O estado da interface é controlado pelas variáveis `isRecording`, `isProcessing` e `hasError`, que fornecem feedback visual ao usuário sobre o status da gravação e transcrição.

```javascript
const startRecording = async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const recorder = new MediaRecorder(stream, {
    mimeType: "audio/webm;codecs=opus",
  });

  recorder.ondataavailable = (event) => {
    audioChunks.push(event.data);
  };

  setIsRecording(true);
  setHasError(false);

  recorder.onstop = () => {
    if (audioChunks.length > 0) {
      const audioBlob = new Blob(audioChunks, {
        type: "audio/webm;codecs=opus",
      });
      setIsProcessing(true);
      transcribe(audioBlob);
      audioChunks = [];
    }

    stream.getTracks().forEach((track) => track.stop());
  };

  setMediaRecorder(recorder);
  recorder.start();
};
```

- O áudio gravado é transformado em um `Blob` e enviado ao backend para transcrição usando o método `transcribe()`.

2. **Backend**: O áudio é recebido pelo endpoint `/audio/transcribe`, que chama o serviço de áudio responsável pela transcrição, no caso do Vox, a IBM Watson

```javascript
@audio_blueprint.route('transcribe', methods=['POST'])
def send():
    return audio_service.send(request=request)
```

- O `AudioService` lida com o processamento do arquivo de áudio e faz a transcrição. Após transcrever o áudio, ele retorna o texto para o frontend.

3. **Processamento e resposta**: O backend retorna um JSON contendo o texto transcrito. Esse texto é automaticamente inserido no estado `audioText`, que armazena o resultado da transcrição. Uma vez que o texto transcrito é recebido, ele é tratado como um termo de busca, e o sistema realiza a busca automaticamente. O código que lida com a transcrição e atualização do campo de busca no frontend é:

```javascript
async function transcribe(audioUrl: Blob) {
  try {
    const formData = new FormData();
    formData.append("audio", audioUrl, "recording.webm");

    const response = await fetch("http://localhost:5000/audio/transcribe", {
      method: "POST",
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      const transcriptText = data.results[0].alternatives[0].transcript;
      setAudioText(transcriptText);
      setIsProcessing(false);
      router.push("/regulations");
    } else {
      setIsProcessing(false);
      setHasError(true);
    }
  } catch (error) {
    setIsProcessing(false);
    setHasError(true);
  }
}
```

## Busca automática de regulamentações

&emsp;&emsp; Após a transcrição do áudio, o texto transcrito é usado para realizar uma busca automática de regulamentações no sistema. Neste momento, o usuário não precisa realizar nenhuma ação adicional, pois o sistema trata o texto transcrito como uma entrada de busca e dispara a pesquisa automaticamente.

1. **Frontend**: Quando o texto transcrito é recebido, o frontend redireciona o usuário automaticamente para a página de regulamentações. O `router.push('/regulations')` é utilizado para navegar até a página que lista os resultados da busca. O texto transcrito é tratado como se fosse um termo digitado manualmente pelo usuário, embora ele tenha sido gerado por uma transcrição de voz.

```javascript
if (response.ok) {
  const data = await response.json();
  const transcriptText = data.results[0].alternatives[0].transcript;
  setAudioText(transcriptText);
  setIsProcessing(false);
  router.push("/regulations");
}
```

2. **Backend**: O termo de busca (texto transcrito) é enviado para o endpoint `/regulations`. O backend utiliza o serviço de regulamentações para buscar todas as correspondências no banco de dados ou em uma API externa, retornando os resultados em formato JSON.

```javascript
@regulation_blueprint.route('', methods=['GET'])
def get_all_regulations():
    regulations = RegulationService.get_all_regulations()
    return jsonify(regulations)
```

3. **Processamento e resposta**: Quando o backend retorna os resultados da busca, o frontend exibe a lista de regulamentações na página correspondente. A resposta do backend é um JSON contendo os detalhes das regulamentações, que são então processados e exibidos para o usuário. Exemplo de JSON:

```javascript
[
  {
    id: 1,
    title: "Regulação 42.030",
    description: "Atualiza as diretrizes do mercado financeiro...",
    publication_date: "2024-11-10",
  },
  {
    id: 2,
    title: "Regulação 42.031",
    description: "Estabelece novos critérios para a atuação...",
    publication_date: "2024-10-15",
  },
];
```

- No frontend, esses dados são renderizados na página de regulamentações para que o usuário possa visualizar as informações relevantes.

&emsp;&emsp; Portanto, a aplicação Vox integra de forma eficiente as funcionalidades de busca por voz e transcrição de áudio com a busca automática de regulamentações. O sistema captura a voz do usuário, transcreve o áudio no backend, e utiliza o texto transcrito para realizar uma busca automática de regulamentações. Essa abordagem permite uma interação intuitiva, onde o usuário simplesmente fala o termo de busca e o sistema realiza todo o processamento necessário para fornecer os resultados sem que nenhuma ação adicional seja necessária.

## 8.1 Intruções para integração

&emsp;&emsp;Esta seção detalha a integração do frontend (Next.js) com o backend (Flask) de uma aplicação que realiza scraping de documentos normativos, processamento desses documentos via PLN (Processamento de Linguagem Natural) e permite que usuários pesquisem documentos utilizando entradas de texto ou áudio.

## 1. Arquitetura e Fluxo Geral

&emsp;&emsp;A arquitetura da aplicação é composta por duas partes principais:

1. **Backend (Flask)**: O backend é responsável por realizar scraping de documentos normativos, processá-los com PLN e armazená-los na plataforma. Ele também fornece rotas para que o frontend possa realizar consultas por texto ou áudio.
   
2. **Frontend (Next.js)**: O frontend consome as APIs do backend, permitindo que os usuários pesquisem por documentos e visualizem os resultados em uma interface amigável.


## 2. Configuração das Chamadas à API

&emsp;&emsp;O frontend faz chamadas à API fornecida pelo backend para várias funcionalidades, como scraping, processamento de documentos e pesquisa por texto ou áudio. As chamadas são feitas utilizando a função `fetch()` no frontend, como mostrado nos exemplos de código.

### 2.1. Endpoints Disponíveis

#### 1. **GET `/regulators`**
   - **Descrição**: Retorna todos os reguladores disponíveis na plataforma.
   - **Uso no Frontend**: Utilizado para popular opções de filtro no frontend, como selecionar o regulador (ex.: BACEN, CVM).
   
   **Exemplo de Chamada no Frontend**:
   ```javascript
   async function getRegulators() {
      const response = await fetch('http://127.0.0.1:5000/regulators', {
         method: 'GET',
         headers: {
            'Content-Type': 'application/json',
         },
      });
      const data = await response.json();
      return data;  // Retorna uma lista de reguladores
   }
   ```

#### 2. **GET `/regulations`**
   - **Descrição**: Retorna todas as regulamentações disponíveis na plataforma.
   - **Uso no Frontend**: Utilizado para exibir todas as regulamentações na interface do usuário.
   
   **Exemplo de Chamada no Frontend**:
   ```javascript
   async function getAllRegulations() {
      const response = await fetch('http://127.0.0.1:5000/regulations', {
         method: 'GET',
         headers: {
            'Content-Type': 'application/json',
         },
      });
      const data = await response.json();
      return data;  // Retorna uma lista de regulamentações
   }
   ```

#### 3. **GET `/regulators/{id}`**
   - **Descrição**: Retorna os detalhes de um regulador específico.
   - **Parâmetros**:
     - `id`: O ID do regulador que se deseja consultar.
   - **Uso no Frontend**: Exibe detalhes de um regulador ao usuário quando solicitado.
   
   **Exemplo de Chamada no Frontend**:
   ```javascript
   async function getRegulatorById(id) {
      const response = await fetch(`http://127.0.0.1:5000/regulators/${id}`, {
         method: 'GET',
         headers: {
            'Content-Type': 'application/json',
         },
      });
      if (!response.ok) {
         throw new Error(`Erro HTTP! status: ${response.status}`);
      }
      const data = await response.json();
      return data;
   }
   ```

#### 4. **POST `/pln/query`**
   - **Descrição**: Processa uma consulta de texto ou áudio e retorna os documentos normativos correspondentes usando PLN.
   - **Corpo da Requisição**:
     ```json
     {
       "input": "texto ou consulta do usuário"
     }
     ```
   - **Uso no Frontend**: Esta rota é usada para enviar uma consulta de texto e buscar os documentos normativos processados pelo PLN.
   
   **Exemplo de Chamada no Frontend**:
   ```javascript
   async function getRegulationsByQuery(query) {
      const response = await fetch('http://127.0.0.1:5000/pln/query', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json',
         },
         body: JSON.stringify({
            input: query,
         }),
      });
      if (!response.ok) {
         throw new Error(`Erro HTTP! status: ${response.status}`);
      }
      const data = await response.json();
      return data;
   }
   ```

#### 5. **POST `/scraping/bacen`**
   - **Descrição**: Executa o scraping de documentos normativos a partir de uma URL do site do BACEN e retorna os dados.
   - **Corpo da Requisição**:
     ```json
     {
       "url": "URL da página de onde o scraping será realizado"
     }
     ```
   - **Uso no Frontend**: Pode ser usada quando o frontend deseja que o backend realize scraping de uma nova página do BACEN e insira novos dados na plataforma.
   
   **Exemplo de Chamada no Frontend**:
   ```javascript
   async function scrapeBacenData(url) {
      const response = await fetch('http://127.0.0.1:5000/scraping/bacen', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json',
         },
         body: JSON.stringify({ url }),
      });
      if (!response.ok) {
         throw new Error(`Erro HTTP! status: ${response.status}`);
      }
      const data = await response.json();
      return data;
   }
   ```

## 3. Tratamento de Erros

&emsp;&emsp;O frontend precisa estar preparado para lidar com vários tipos de erros que podem ocorrer durante a comunicação com o backend. Aqui estão os tipos mais comuns de erros e como tratá-los.

### 3.1. Erros HTTP Comuns

- **404 Not Found**: Geralmente ocorre quando a rota solicitada não existe.
- **500 Internal Server Error**: Indica que algo deu errado no lado do servidor.
- **400 Bad Request**: Ocorre quando a solicitação feita pelo frontend é inválida ou contém parâmetros incorretos.

### 3.2. Exemplo de Tratamento de Erros

**Exemplo de tratamento de erro no frontend**:
```javascript
fetch('http://127.0.0.1:5000/pln/query', {
   method: 'POST',
   headers: {
      'Content-Type': 'application/json',
   },
   body: JSON.stringify({ input: query }),
})
   .then(response => {
      if (!response.ok) {
         throw new Error(`Erro HTTP! status: ${response.status}`);
      }
      return response.json();
   })
   .then(data => {
      console.log('Dados recebidos:', data);
   })
   .catch(error => {
      console.error('Erro ao buscar os dados:', error);
      alert('Ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde.');
   });
```

**Dicas para tratamento de erros no frontend**:
- Exibir uma mensagem amigável ao usuário caso ocorra um erro.
- Registrar o erro no console para facilitar a depuração.
- Adicionar lógica de reintento para chamadas de rede em falha, dependendo da importância da operação.

## 4. Paginação e Exibição de Resultados

&emsp;&emsp;No frontend, a exibição dos resultados de regulamentações processadas segue um modelo de paginação. O backend retorna todos os resultados, e o frontend controla a paginação localmente.

### 4.1. Paginação no Frontend

&emsp;&emsp;A paginação é controlada através do estado da página atual e do número de itens por página. No exemplo abaixo, a quantidade de regulamentações exibidas por página é limitada a `ITEMS_PER_PAGE`.

```javascript
const ITEMS_PER_PAGE = 10;
const indexOfLastItem = currentPage * ITEMS_PER_PAGE;
const indexOfFirstItem = indexOfLastItem - ITEMS_PER_PAGE;
const currentItems = data.regulations.slice(indexOfFirstItem, indexOfLastItem);
```

&emsp;&emsp;A navegação entre páginas é controlada pela atualização do estado `currentPage`, que ajusta quais itens serão exibidos.

&emsp;&emsp;A integração entre o frontend e o backend do sistema segue uma arquitetura clara e bem definida, facilitando a comunicação entre ambas as partes. Além de proporcionar uma interface amigável, o Vox mostra eficiência no tratamento de dados e consultas, tornando a solução eficaz para a pesquisa de documentos normativos.

# 9. Guia de Configuração

&emsp;&emsp;Este guia é destinado à configuração e teste da solução de desenvolvimento, abrangendo tanto o frontend quanto o backend. O objetivo é fornecer instruções claras e detalhadas para garantir a instalação e configuração adequadas de todos os componentes, desde dependências até variáveis de ambiente.

## Configuração do Frontend

&emsp;&emsp;Para garantir o funcionamento adequado do frontend, siga os passos abaixo.

### Passo 1: Instalação das Dependências

Utilize o comando abaixo para instalar todas as dependências especificadas no arquivo de configuração. Isso é essencial para assegurar que o ambiente tenha as ferramentas necessárias configuradas corretamente.

```bash
npm install
```

### Passo 2: Iniciando o Frontend

Execute o comando a seguir para iniciar o servidor de desenvolvimento. Isso permitirá que o código do frontend seja executado localmente e forneça feedback em tempo real.

```bash
npm run dev
```

## Configuração do Backend

Para configurar o ambiente de desenvolvimento do backend, siga os passos abaixo.

### Passo 1: Criando e Ativando o Ambiente Virtual

Crie um ambiente virtual com o comando a seguir. Isso proporciona um espaço isolado para instalar pacotes específicos do projeto.

```bash
python -m venv venv
```

Após a criação, ative o ambiente virtual:

- **No Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **No MacOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Passo 2: Instalando as Dependências

Com o ambiente virtual ativo, instale as dependências necessárias com o comando abaixo. Esse passo é crucial para garantir que o backend funcione corretamente.

```bash
pip install -r requirements.txt
```

### Passo 3: Configurando Variáveis de Ambiente

O arquivo `.env` deve ser configurado para armazenar variáveis de ambiente específicas do backend, como chaves de API e credenciais. Certifique-se de que as informações estejam corretas e que o arquivo esteja preparado antes de iniciar o backend.

Exemplo de configuração do arquivo `.env`:

```
DATABASE_URL=postgres://user:password@localhost:5432/mydatabase
IMB_SPEECH_TO_TEXT_URL = "https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/your_api_key_here/v1/models/pt-BR_BroadbandModel/recognize"
IMB_SPEECH_TO_TEXT_USERNAME = "apikey"
IMB_SPEECH_TO_TEXT_PASSWORD = "your_password_here"
```

---

## Resumo dos Comandos

### Frontend:

1. **Instalar dependências**:
   ```bash
   npm install
   ```
2. **Iniciar o servidor de desenvolvimento**:
   ```bash
   npm run dev
   ```

### Backend:

1. **Criar ambiente virtual**:
   ```bash
   python -m venv venv
   ```
2. **Ativar ambiente virtual**:
   - Windows: `venv\Scripts\activate`
   - MacOS/Linux: `source venv/bin/activate`
3. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configurar variáveis de ambiente**:
   Certifique-se de editar ou criar o arquivo `.env` conforme necessário.

&emsp;&emsp;Ao seguir os passos descritos, será possível configurar corretamente o ambiente de desenvolvimento para frontend e backend, garantindo que todas as dependências estejam instaladas e as variáveis de ambiente configuradas. Isso permitirá um desenvolvimento consistente e eficiente, pronto para as fases subsequentes de testes e implementação.

# 10. Testes de Software

&emsp;&emsp; Os testes de software são uma etapa fundamental no ciclo de desenvolvimento de sistemas, especialmente em projetos de soluções tecnológicas para a indústria financeira. Eles visam garantir a qualidade, confiabilidade e segurança do software, validando se a solução atende aos requisitos funcionais e não funcionais definidos. Em um ambiente altamente regulado, como o setor bancário, os testes são essenciais para assegurar que a aplicação cumpre com as normativas vigentes e que falhas críticas, como vulnerabilidades de segurança ou erros de conformidade, sejam identificadas e corrigidas antes da implementação.

## 10.1. Plano de testes

&emsp;&emsp; O plano de testes tem como objetivo descrever as estratégias a serem aplicadas para garantir a qualidade do software desenvolvido. Nosso foco estará em testar diferentes camadas do sistema, desde componentes individuais até a integração entre módulos, assegurando que o comportamento da aplicação esteja de acordo com os requisitos definidos. A seguir, detalhamos as abordagens para os diferentes tipos de testes que serão utilizados no projeto.

### 1. Testes Unitários de Frontend

&emsp;&emsp; Para os testes unitários do front-end, utilizaremos o _Jest_, uma biblioteca de testes em JavaScript amplamente usada para validar a funcionalidade de componentes de interface de usuário em aplicações web. O foco dos testes unitários será garantir que cada componente funcione isoladamente e conforme o esperado. Testaremos os seguintes casos de uso:

1. **Microfone:** Testaremos a ativação e desativação do microfone, além de verificar se o componente é capaz de capturar e armazenar o áudio corretamente.

2. **Detalhamento de Normas:** Verificaremos se o componente responsável pelo detalhamento das normas exibe as informações corretas, de acordo com os dados fornecidos, e se ele lida adequadamente com diferentes formatos e tamanhos de conteúdo.

3. **Navegação da Sidebar:** Testaremos o comportamento da sidebar, validando a navegação entre diferentes seções da aplicação, garantindo que o estado ativo seja destacado e que não ocorram erros ao alternar entre as opções.

4. **Paginação:** Verificaremos a correta exibição e funcionalidade da paginação, garantindo que o sistema carregue as páginas de maneira sequencial e consistente, e que o usuário consiga navegar entre diferentes páginas sem erros.

&emsp;&emsp; Esses testes unitários serão executados automaticamente durante o processo de desenvolvimento, fornecendo feedback rápido sobre o funcionamento dos componentes.

### 2. Testes de Integração

&emsp;&emsp; Os testes de integração serão realizados para garantir que diferentes partes do sistema funcionem corretamente em conjunto, com foco na comunicação entre o frontend e o backend. Utilizaremos _Jest_ no frontend para verificar a captura e o envio de dados, e _Postman_ para testar o processamento e a resposta do backend. O objetivo é garantir que os dados sejam trocados corretamente entre as camadas e que as funcionalidades funcionem conforme o esperado, incluindo cenários de sucesso e falha.

1. **Transcrição de Áudio para Texto:** Testaremos desde a captura do áudio no frontend até o processamento e retorno da transcrição pelo backend. O teste começará com a simulação da gravação de áudio, seguida do envio do arquivo para o servidor. Em seguida, verificaremos se o backend recebe o arquivo corretamente, processa o áudio através do serviço de transcrição e retorna a transcrição esperada ao frontend. Também serão cobertos cenários de erro, como o envio de arquivos que excedem o tamanho permitido, a ausência de um arquivo de áudio ou falhas no serviço de transcrição externo. O teste garantirá que, em todas as situações, o sistema lida corretamente com as respostas e exibe as mensagens apropriadas ao usuário.

2. **Busca de Normas:** Realizaremos consultas com palavras-chave ou filtros específicos no frontend. Verificaremos se o backend processa essas consultas corretamente e retorna os resultados esperados do banco de dados. O teste cobrirá cenários de busca simples e complexa, com grandes volumes de dados, além de garantir que o sistema lide adequadamente com consultas sem resultados ou com parâmetros inválidos. O objetivo é garantir que as respostas sejam corretamente processadas e exibidas no frontend, proporcionando uma experiência fluida ao usuário.

&emsp;&emsp; Esses testes são essenciais para garantir que o sistema, em sua totalidade, funcione de forma integrada e sem falhas, assegurando a correta comunicação entre suas diferentes partes e o tratamento adequado de erros.

## 10.2. Casos de uso - Testes unitários

&emsp;&emsp;Nesta seção, são descritos os casos de uso testados no sistema, abrangendo componentes críticos da aplicação. Cada caso de uso é cuidadosamente validado por meio de testes unitários utilizando o _Jest_, garantindo que as funcionalidades esperadas sejam executadas corretamente sob diferentes cenários. Cada caso de uso é descrito com base nas entradas esperadas, resultados obtidos e os passos necessários para a reprodução dos testes. Esses cenários garantem que a aplicação funcione de maneira eficiente, proporcionando uma experiência de usuário consistente e livre de erros.

### 1. Microfone

&emsp;&emsp;O componente `Microfone` é responsável por iniciar, parar e processar gravações de áudio, sendo uma parte essencial da aplicação. Os testes realizados cobrem o ciclo completo do seu uso: desde a renderização do botão, o início e a parada da gravação, até o tratamento de erros, como a negação de permissões de acesso ao microfone. Com esses testes, asseguramos que o componente responde adequadamente às interações do usuário e lida corretamente com situações adversas, como erros de permissão.

&emsp;&emsp;**Teste 1. Renderização do Botão do Microfone** - Verifica se o mesmo é renderizado corretamente no componente.

&emsp;&emsp;**Entrada esperada:** O componente do microphone é renderizado.

&emsp;&emsp;**Resultados esperados:** O botão do microfone deve estar visível na interface.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente Microphone.

&emsp;&emsp;II. Verifique se o botão do microfone é exibido corretamente.

```javascript
test("should render microphone button", () => {
  render(
    <Microphone
      setIsRecording={mockSetIsRecording}
      setIsProcessing={mockSetIsProcessing}
      setHasError={mockSetHasError}
    />
  );

  const micButton = screen.getByRole("button");
  expect(micButton).toBeInTheDocument();
});
```

&emsp;&emsp;**Teste 2. Iniciar Gravação ao Clicar** - Verifica se a gravação do áudio começa quando o usuário clica no botão do microfone.

&emsp;&emsp;**Entrada esperada:** O usuário clica no botão de gravação e a função `getUserMedia` é resolvida com sucesso, concedendo acesso ao microfone.

&emsp;&emsp; **Resultados esperados:** A gravação começa, o estado `setIsRecording(true)` é chamado e o `getUserMedia` é invocado com `{ audio: true }`.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Simule o clique no botão do microfone.

&emsp;&emsp;II. Verifique se a gravação é iniciada e se o estado de gravação foi atualizado.

```javascript
test("should start recording on click", async () => {
  const mockStream = { getTracks: jest.fn(() => [{ stop: jest.fn() }]) };
  mockGetUserMedia.mockResolvedValue(mockStream);

  render(
    <Microphone
      setIsRecording={mockSetIsRecording}
      setIsProcessing={mockSetIsProcessing}
      setHasError={mockSetHasError}
    />
  );

  const micButton = screen.getByRole("button");
  fireEvent.click(micButton);

  await waitFor(() => {
    expect(mockSetIsRecording).toHaveBeenCalledWith(true);
    expect(mockGetUserMedia).toHaveBeenCalledWith({ audio: true });
  });
});
```

&emsp;&emsp;**Teste 3. Parar Gravação ao Clicar Novamente** - Verifica se a gravação do áudio para corretamente quando o botão do microfone é clicado novamente após o inicio da gravação.

&emsp;&emsp;**Entrada esperada:** O usuário inicia a gravação e clica no botão do microfone novamente para interromper a gravação e o `MediaRecorder` está ativo e gravando.

&emsp;&emsp;**Resultados esperados:** A gravação para e o estado `setIsRecording(false)` é chamado.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Simule o clique inicial no botão do microfone para começar a gravação.

&emsp;&emsp;II. Simule outro clique no botão para parar a gravação.

&emsp;&emsp;III. Verifique se a gravação foi interrompida e o estado foi atualizado.

```javascript
test("should stop recording on click when already recording", async () => {
  const mockStream = { getTracks: jest.fn(() => [{ stop: jest.fn() }]) };
  mockGetUserMedia.mockResolvedValue(mockStream);

  render(
    <Microphone
      setIsRecording={mockSetIsRecording}
      setIsProcessing={mockSetIsProcessing}
      setHasError={mockSetHasError}
    />
  );

  const micButton = screen.getByRole("button");

  fireEvent.click(micButton); // Start recording
  await waitFor(() => {
    expect(mockSetIsRecording).toHaveBeenCalledWith(true);
  });

  fireEvent.click(micButton); // Stop recording
  await waitFor(() => {
    expect(mockSetIsRecording).toHaveBeenCalledWith(false);
  });
});
```

&emsp;&emsp;**Teste 4. Lidar com Erros de Permissão do Microfone** - Verifica se o componente trata corretamente o erro de "_Permission denied_" ao tentar acessar o microfone.

&emsp;&emsp;**Entrada esperada:** O usuário tenta acessar o microfone, mas o acesso é negado (simulado com `mockRejectedValueOnce`).

&emsp;&emsp;**Resultados esperados:** A gravação não é iniciada, o estado de erro é ativado com `setHasError(true)` e o estado `setIsRecording(false)` é chamado.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Simule o clique no botão de gravação.

&emsp;&emsp;II. Simule a negação de permissão para o microfone.

&emsp;&emsp;III. Verifique se o estado de erro foi acionado e a gravação foi corretamente interrompida.

```javascript
test("should handle media recorder errors", async () => {
  mockGetUserMedia.mockRejectedValueOnce(new Error("Permission denied"));

  render(
    <Microphone
      setIsRecording={mockSetIsRecording}
      setIsProcessing={mockSetIsProcessing}
      setHasError={mockSetHasError}
    />
  );

  const micButton = screen.getByRole("button");

  // Simulando o clique no botão de gravação
  fireEvent.click(micButton);

  // Verificando se o erro foi tratado corretamente
  await waitFor(() => {
    expect(mockSetIsRecording).toHaveBeenCalledWith(false);
    expect(mockSetHasError).toHaveBeenCalledWith(true);
  });
});
```

### 2. Paginação

&emsp;&emsp;**Teste 1. Renderização da Paginação com Numeração Correta** - Verifica se o componente de paginação é renderizado corretamente com a numeração esperada.

&emsp;&emsp;**Entrada esperada:** O componente de paginação deve ser renderizado com a numeração correta.

&emsp;&emsp;**Resultados esperados:** A página 1 de 14 deve ser exibida corretamente.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `PaginationWrapper`.

&emsp;&emsp;II. Verifique se a numeração da página está correta ("Página 1 de 14").

```javascript
test("renders pagination with correct numeration and handles page changes", () => {
  const totalPages = 14;

  const PaginationWrapper = () => {
    const [currentPage, setCurrentPage] = useState(1);
    return (
      <Pagination
        current={currentPage}
        total={totalPages}
        setCurrent={setCurrentPage}
      />
    );
  };

  const { getByText } = render(<PaginationWrapper />);
  expect(getByText("Página 1 de 14")).toBeInTheDocument();
});
```

&emsp;&emsp;**Teste 2. Mudar de Página Anterior e Próxima** - Verifica se é possível navegar entre páginas usando os botões de "próxima" e "anterior".

&emsp;&emsp;**Entrada esperada:** O botão "próxima página" deve estar funcional.

&emsp;&emsp;**Resultados esperados:** A navegação entre as páginas deve atualizar a numeração visível.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `PaginationWrapper`.

&emsp;&emsp;II. Clique no botão de próxima página e verifique a mudança.

&emsp;&emsp;III. Clique no botão de página anterior e verifique a mudança.

```javascript
test("go to previous and next page", () => {
  const totalPages = 3;

  const PaginationWrapper = () => {
    const [currentPage, setCurrentPage] = useState(1);
    return (
      <Pagination
        current={currentPage}
        total={totalPages}
        setCurrent={setCurrentPage}
      />
    );
  };

  const { getByText, getByTestId } = render(<PaginationWrapper />);
  const leftButton = getByTestId("left-button");
  const rightButton = getByTestId("right-button");

  expect(getByText(`Página 1 de ${totalPages}`)).toBeInTheDocument();

  fireEvent.click(rightButton);
  expect(getByText(`Página 2 de ${totalPages}`)).toBeInTheDocument();

  fireEvent.click(leftButton);
  expect(getByText(`Página 1 de ${totalPages}`)).toBeInTheDocument();
});
```

&emsp;&emsp;**Teste 3. Tentar Voltar para a Primeira Página** - Verifica se o botão de página anterior não faz nada quando já está na primeira página.

&emsp;&emsp;**Entrada esperada:** O botão "anterior" não deve mudar a página se já estiver na primeira.

&emsp;&emsp;**Resultados esperados:** A página deve permanecer como "Página 1 de 3".

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `PaginationWrapper`.

&emsp;&emsp;II. Clique no botão de página anterior.

```javascript
test("tries to go to previous page - (it's already the first page)", () => {
  const totalPages = 3;

  const PaginationWrapper = () => {
    const [currentPage, setCurrentPage] = useState(1);
    return (
      <Pagination
        current={currentPage}
        total={totalPages}
        setCurrent={setCurrentPage}
      />
    );
  };

  const { getByText, getByTestId } = render(<PaginationWrapper />);
  const leftButton = getByTestId("left-button");

  expect(getByText(`Página 1 de ${totalPages}`)).toBeInTheDocument();
  fireEvent.click(leftButton);
  expect(getByText(`Página 1 de ${totalPages}`)).toBeInTheDocument();
});
```

&emsp;&emsp;**Teste 4. Tentar Avançar para a Última Página** - Verifica se o botão de próxima página não faz nada quando já está na última página.

&emsp;&emsp;**Entrada esperada:** O botão "próxima" não deve mudar a página se já estiver na última.

&emsp;&emsp;**Resultados esperados:** A página deve permanecer como "Página 3 de 3".

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `PaginationWrapper` já na última página.

&emsp;&emsp;II. Clique no botão de próxima página.

```javascript
test("tries to go to next page - (it's already the last page)", () => {
  const totalPages = 3;

  const PaginationWrapper = () => {
    const [currentPage, setCurrentPage] = useState(3);
    return (
      <Pagination
        current={currentPage}
        total={totalPages}
        setCurrent={setCurrentPage}
      />
    );
  };

  const { getByText, getByTestId } = render(<PaginationWrapper />);
  const rightButton = getByTestId("right-button");

  expect(getByText(`Página 3 de ${totalPages}`)).toBeInTheDocument();
  fireEvent.click(rightButton);
  expect(getByText(`Página 3 de ${totalPages}`)).toBeInTheDocument();
});
```

### 3. Sidebar

**Teste 1. Renderização da Sidebar com Botões e Itens** - Verifica se a sidebar e todos os botões são renderizados corretamente.

**Entrada esperada:** O componente Sidebar é renderizado.

**Resultados esperados:** O botão de menu, os botões Home, Explorer e Tag, além da div `regulators`, devem estar visíveis na interface.

**Passos para reproduzir:**

I. Renderize o componente Sidebar.

II. Verifique se o botão de menu, Home, Explorer e Tag, além da div `regulators`, são exibidos corretamente.

```javascript
test("renders sidebar with menu button and all items", () => {
  const { container, getByTestId } = render(<Sidebar />);
  const sidebar = container.querySelector(`.${styles.sidebar}`);
  const toggleButton = container.querySelector(`.${styles.menuBtn}`);
  const homeButton = getByTestId("home-button");
  const explorerButton = getByTestId("explorer-button");
  const tagButton = getByTestId("tag-button");
  const regulatorsDiv = container.querySelector(`.${styles.regulators}`);

  expect(toggleButton).toBeInTheDocument();
  expect(homeButton).toBeInTheDocument();
  expect(explorerButton).toBeInTheDocument();
  expect(tagButton).toBeInTheDocument();
  expect(sidebar).toBeInTheDocument();
  expect(regulatorsDiv).toBeInTheDocument();
});
```

**Teste 2. Abrir e Fechar Sidebar** - Verifica se a sidebar abre e fecha corretamente quando o botão de menu é clicado.

**Entrada esperada:** O componente Sidebar é renderizado com o botão de menu.

**Resultados esperados:** A sidebar deve expandir quando o botão de menu é clicado e fechar quando o botão é clicado novamente.

**Passos para reproduzir:**

I. Renderize o componente Sidebar.

II. Clique no botão de menu para expandir a sidebar e clique novamente para fechá-la.

```javascript
test('open and close sidebar', () => {
    const { container } = render(<Sidebar />);
    const sidebar = container.querySelector(`.${styles.sidebar}`);
    const toggleButton = container.querySelector(`.${styles.menuBtn}`);

    expect(sidebar).not.toHaveClass(styles.expanded);
    fireEvent.click(toggleButton!);
    expect(sidebar).toHaveClass(styles.expanded);
    fireEvent.click(toggleButton!);
    expect(sidebar).not.toHaveClass(styles.expanded);
});
```

**Teste 3. Navegar para a Página do Explorador** - Verifica se o clique no botão do Explorador redireciona corretamente para a página de regulamentos.

**Entrada esperada:** O componente Sidebar é renderizado com o botão do Explorador.

**Resultados esperados:** A função de navegação deve ser chamada com o caminho correto ao clicar no botão do Explorador.

**Passos para reproduzir:**

I. Renderize o componente Sidebar.

II. Clique no botão do Explorador.

```javascript
test('go to explorer', () => {
    const pushMock = jest.fn(); // Criar uma função mock para o router push

    // Mockando useRouter para simular o comportamento de navegação
    (useRouter as jest.Mock).mockImplementation(() => ({
        route: '/',
        pathname: '/',
        query: {},
        asPath: '/',
        push: pushMock, // Atribuir a função mock ao push
    }));

    const { getByTestId } = render(<Sidebar />);
    const explorerButton = getByTestId('explorer-button');
    fireEvent.click(explorerButton!); // Simular clique no botão do Explorador

    // Verificar se a função push foi chamada com o caminho correto
    expect(pushMock).toHaveBeenCalledWith('/regulations');
});
```

**Teste 4. Navegar para a Página Inicial** - Verifica se o clique no botão da Página Inicial redireciona corretamente para a página inicial.

**Entrada esperada:** O componente Sidebar é renderizado com o botão da Página Inicial.

**Resultados esperados:** A função de navegação deve ser chamada com o caminho correto ao clicar no botão da Página Inicial.

**Passos para reproduzir:**

I. Renderize o componente Sidebar.

II. Clique no botão da Página Inicial.

```javascript
test('go to home', () => {
    const pushMock = jest.fn(); // Criar uma função mock para o router push

    // Mockando useRouter com a rota atual definida como '/regulations'
    (useRouter as jest.Mock).mockImplementation(() => ({
        route: '/regulations',
        pathname: '/regulations',
        query: {},
        asPath: '/regulations',
        push: pushMock,
    }));

    const { getByTestId } = render(<Sidebar />);
    const homeButton = getByTestId('home-button');
    fireEvent.click(homeButton!); // Simular clique no botão da Página Inicial

    // Verificar se a função push foi chamada para navegar para a página inicial
    expect(pushMock).toHaveBeenCalledWith('/');
});
```

**Teste 5. Navegar para a Página de Tags** - Verifica se o clique no botão de Tags redireciona corretamente para a página de tags.

**Entrada esperada:** O componente Sidebar é renderizado com o botão de Tags.

**Resultados esperados:** A função de navegação deve ser chamada com o caminho correto ao clicar no botão de Tags.

**Passos para reproduzir:**

I. Renderize o componente Sidebar.

II. Clique no botão de Tags.

```javascript
test('go to tag page', () => {
    const pushMock = jest.fn(); // Criar uma função mock para o router push

    // Mockando useRouter para simular o comportamento de navegação
    (useRouter as jest.Mock).mockImplementation(() => ({
        route: '/',
        pathname: '/',
        query: {},
        asPath: '/',
        push: pushMock,
    }));

    const { getByTestId } = render(<Sidebar />);
    const tagButton = getByTestId('tag-button');
    fireEvent.click(tagButton!); // Simular clique no botão de Tags

    // Verificar se a função push foi chamada com o caminho correto
    expect(pushMock).toHaveBeenCalledWith('/tags');
});
```

**Teste 6. Navegar para a Página de Reguladores** - Verifica se o clique no botão de Reguladores abre a URL correta em uma nova aba.

**Entrada esperada:** O componente Sidebar é renderizado com o botão de Reguladores.

**Resultados esperados:** A função `window.open` deve ser chamada com a URL e o alvo corretos ao clicar no botão de Reguladores.

**Passos para reproduzir:**

I. Renderize o componente Sidebar.

II. Clique no botão de Reguladores.

```javascript
test('go to regulator page', () => {
    const openMock = jest.fn(); // Função mock para window.open
    window.open = openMock; // Sobrescrevendo o método window.open

    const { getByTestId } = render(<Sidebar />);
    const regulatorButton = getByTestId('regulator-button');
    fireEvent.click(regulatorButton!); // Simular clique no botão de Reguladores

    // Verificar se window.open foi chamada com a URL e o alvo corretos
    expect(openMock).toHaveBeenCalledWith('https://www.bcb.gov.br/', '_blank');
});
```

### 4. Regulation Component

&emsp;&emsp;O componente `Regulation` é responsável por exibir informações detalhadas sobre uma regulamentação, incluindo título, data de publicação, texto e tags associadas. Os testes realizados cobrem a renderização correta dos dados e a exibição dos detalhes esperados da regulamentação. Com esses testes, garantimos que os dados fornecidos pelo backend são exibidos corretamente no frontend.

&emsp;&emsp;**Teste 1. Renderização do componente Regulation** - Verifica se os detalhes da regulamentação são renderizados corretamente no componente.

&emsp;&emsp;**Entrada esperada:** Um objeto `regulation` é passado como propriedade para o componente, contendo detalhes como título, texto, tags e data de publicação.

&emsp;&emsp;**Resultados esperados:** O título, texto, tags e a data de publicação devem ser exibidos corretamente na interface.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `Regulation` com um objeto de regulamentação simulado. 

&emsp;&emsp;II. Verifique se o título, a data de publicação, o texto do XML e as tags são exibidos corretamente.

```javascript
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
```

### 5. RegulationInformationCard Component

&emsp;&emsp;O componente `RegulationInformationCard` é utilizado para exibir as informações detalhadas de uma regulamentação em um card, permitindo ao usuário visualizar o título, a data de publicação, as tags e regulamentações relacionadas. Este componente também permite que o usuário abra a URL do documento diretamente em uma nova aba do navegador. Os testes garantem que todos os elementos sejam exibidos e interajam corretamente.

&emsp;&emsp;**Teste 1. Renderização do tópico e das tags** - Verifica se o tópico e as tags da regulamentação são exibidos corretamente no componente.

&emsp;&emsp;**Entrada esperada:** Um objeto `regulation` com o campo `topic` e uma lista de `tags` é passado para o componente.

&emsp;&emsp;**Resultados esperados:** O tópico e as tags devem ser exibidos corretamente na interface.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `RegulationInformationCard` com um objeto de regulamentação contendo tópico e tags.

&emsp;&emsp;II. Verifique se o tópico e as tags são exibidos corretamente na interface.

```javascript
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
```

&emsp;&emsp;**Teste 2. Renderização de regulamentações relacionadas** - Verifica se as regulamentações relacionadas são exibidas corretamente quando disponíveis.

&emsp;&emsp;**Entrada esperada:** Um objeto `regulation` contendo regulamentações relacionadas (no campo `relations`).

&emsp;&emsp;**Resultados esperados:** As regulamentações relacionadas devem ser exibidas corretamente na interface.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `RegulationInformationCard` com um objeto de regulamentação contendo relações.

&emsp;&emsp;II. Verifique se o título das regulamentações relacionadas é exibido corretamente.

```javascript
it('renders related regulations when available', () => {
  render(<RegulationInformationCard regulation={mockRegulation} />);
  expect(screen.getByText(mockRegulation.relations[0].title)).toBeInTheDocument();
});
```

&emsp;&emsp;**Teste 3. Mensagem quando não há regulamentações relacionadas** - Verifica se a mensagem correta é exibida quando não há regulamentações relacionadas disponíveis.

&emsp;&emsp;**Entrada esperada:** Um objeto `regulation` sem relações (lista `relations` vazia).

&emsp;&emsp;**Resultados esperados:** Uma mensagem indicando que não há regulamentações relacionadas deve ser exibida.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `RegulationInformationCard` com um objeto de regulamentação sem relações.

&emsp;&emsp;II. Verifique se a mensagem de "Nenhuma regulamentação relacionada encontrada" é exibida corretamente.

```javascript
it('shows message when no related regulations are found', () => {
  render(<RegulationInformationCard regulation={{ ...mockRegulation, relations: [] }} />);
  expect(screen.getByText('Nenhuma regulamentação relacionada encontrada.')).toBeInTheDocument();
});
```

&emsp;&emsp;**Teste 4. Abrir URL do documento em uma nova aba** - Verifica se a URL do documento é aberta em uma nova aba ao clicar no botão apropriado.

&emsp;&emsp;**Entrada esperada:** O usuário clica no botão "Visualizar norma pelo site".

&emsp;&emsp;**Resultados esperados:** O link para o documento é aberto em uma nova aba do navegador.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente `RegulationInformationCard`.

&emsp;&emsp;II. Simule o clique no botão "Visualizar norma pelo site".

&emsp;&emsp;III. Verifique se a função `window.open` é chamada com a URL correta.

```javascript
it('opens document URL in a new tab when button is clicked', () => {
  const { getByText } = render(<RegulationInformationCard regulation={mockRegulation} />);
  const openSpy = jest.spyOn(window, 'open').mockImplementation(() => null);
  getByText('Visualizar norma pelo site').click();
  expect(openSpy).toHaveBeenCalledWith(mockRegulation.documenturl, '_blank');
});
```

## 10.3. Casos de uso - Testes de integração de frontend e backend

&emsp;&emsp;Os testes de integração têm como objetivo verificar se diferentes módulos ou componentes de uma aplicação funcionam corretamente em conjunto. Diferentemente dos testes unitários, que avaliam funcionalidades isoladas, os testes de integração focam na interação entre esses componentes, assegurando que a comunicação entre eles ocorra como esperado.

&emsp;&emsp;No contexto de uma aplicação que envolve tanto o frontend quanto o backend, os testes de integração podem incluir a verificação de chamadas de API (em mock), o comportamento do roteamento e a manipulação de estados. Esses testes são essenciais para garantir a consistência dos fluxos de dados e que as interações do usuário resultem nas respostas corretas do sistema.

### 1. Pesquisa por normas

&emsp;&emsp;**Teste 1: Renderização da Barra de Busca** - Verifica se a barra de busca é renderizada corretamente.

&emsp;&emsp;**Entrada esperada:** O usuário visualiza a barra de busca com o campo de entrada e o botão de busca.

&emsp;&emsp;**Resultados esperados:** O campo de entrada e o botão de busca estão presentes no componente renderizado.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente da barra de busca.

&emsp;&emsp;II. Verifique se o campo de entrada e o botão de busca estão presentes no DOM.

```javascript
    test('renders search bar', () => {
        const { getByTestId } = render(<SearchBar />);

        const input: HTMLInputElement = getByTestId('input') as HTMLInputElement;
        const searchButton: HTMLElement = getByTestId('search-button');

        expect(input).toBeInTheDocument();
        expect(searchButton).toBeInTheDocument();
    });
```

&emsp;&emsp;**Teste 2: Busca de Regulamentações** - Verifica se a busca é realizada ao pressionar "Enter" e se a chamada da API mockada retorna os dados esperados.

&emsp;&emsp;**Entrada esperada:** O usuário digita "Quero comunicados" na barra de busca e pressiona a tecla "Enter".

&emsp;&emsp;**Resultados esperados:** A função de configuração de texto de entrada é chamada com "Quero comunicados", a função de configuração de busca automática é chamada com `true`, o roteador é redirecionado para a página de regulamentações, e a chamada da API mockada retorna dados relacionados à busca.

&emsp;&emsp;**Passos para reproduzir:**

&emsp;&emsp;I. Renderize o componente da barra de busca.

&emsp;&emsp;II. Simule a digitação de "Quero comunicados" no campo de entrada.

&emsp;&emsp;III. Simule a pressão da tecla "Enter".

&emsp;&emsp;IV. Verifique se as funções de configuração foram chamadas com os parâmetros corretos e se o roteador foi redirecionado para a URL correta.

&emsp;&emsp;V. Simule a chamada da API com o input "Quero comunicados" e verifique se os dados retornados correspondem ao esperado.

```javascript
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
```

## 10.4 Relatório de testes

&emsp;&emsp;A aplicação web realiza o scraping de documentos normativos de fontes externas e usa PLN para processar o conteúdo extraído. Após o processamento, os documentos são armazenados na plataforma. Usuários podem pesquisar documentos usando entradas de texto ou áudio, e a aplicação retorna os documentos correspondentes com base nas palavras-chave ou transcrições de áudio. O objetivo dos testes foi validar o funcionamento das principais funcionalidades da aplicação:

1. **Scraping de Documentos Normativos:** Testar a coleta de documentos a partir de fontes externas.
2. **Processamento de Documentos por PLN:** Verificar a análise de documentos por PLN, tanto com entradas de texto quanto de áudio.
3. **Armazenamento de Documentos na Plataforma:** Confirmar o armazenamento correto de documentos e suas metadatas após o processamento.
4. **Pesquisa por Texto e Áudio:** Garantir que o sistema retorna o documento correto com base em entradas de texto e áudio.

&emsp;&emsp;Os testes cobriram cenários de sucesso e falha para identificar possíveis problemas e garantir a eficiência da aplicação. Foram realizadas ações corretivas nos casos em que problemas foram encontrados.

### Cenários de Teste

| Número | Cenário | Descrição | Resultado Esperado | Resultado Obtido | Ação Corretiva |
|--------|---------|-----------|--------------------|------------------|----------------|
| 1      | URL Ausente no Scraping                    | Verificar se o sistema retorna um erro ao tentar realizar scraping sem fornecer uma URL.            | O sistema deve retornar um código de erro 400, indicando que o campo `url` está ausente.                                                                                                                                                                               | O sistema retornou o código 400 com uma mensagem de erro clara.                                                             | Nenhuma ação corretiva necessária.                                                                                                                     |
| 2      | Sucesso no Scraping                        | Testar a extração de conteúdo de uma URL válida.                                                    | O scraping deve retornar o conteúdo da página com título e texto extraídos corretamente.                                                                                                                                                                                | Scraping bem-sucedido para páginas estáticas, mas falhou em páginas com conteúdo dinâmico.                                    | Integrar uma solução de scraping headless (Selenium/Playwright) para lidar com páginas que utilizam JavaScript para carregar conteúdo dinâmico.          |
| 3      | Erro no Scraping                           | Simular uma falha no processo de scraping.                                                          | O sistema deve retornar um erro 500 com uma mensagem clara e registrar a falha adequadamente.                                                                                                                                                                           | O sistema retornou erro 500, mas o log de erro não continha informações detalhadas.                                           | Melhorar o log de erros para capturar informações detalhadas, como a URL que falhou e o status do servidor externo.                                      |
| 4      | Processamento de Texto por PLN             | Verificar se o texto do documento é processado corretamente pelo modelo PLN.                        | O texto deve ser corretamente classificado, e o modelo PLN deve retornar a categoria apropriada.                                                                                                                                                                       | O modelo PLN processou o texto corretamente e retornou a categoria esperada.                                                 | Nenhuma ação corretiva necessária.                                                                                                                     |
| 5      | Processamento de Áudio por PLN             | Simular uma entrada de áudio e verificar se o sistema transcreve e processa o áudio corretamente.   | O áudio deve ser transcrito corretamente e a pesquisa deve mapear a transcrição para o documento correspondente.                                                                                                                                                       | Áudio de alta qualidade foi transcrito corretamente; áudios de baixa qualidade resultaram em transcrições imprecisas.         | Melhorar o pré-processamento de áudio e/ou utilizar um serviço de transcrição mais robusto para lidar com áudios de baixa qualidade.                     |
| 6      | Armazenamento após Processamento           | Verificar se os documentos processados por PLN são armazenados corretamente no banco de dados.      | Todos os documentos devem ser salvos no banco de dados com os metadados corretos, incluindo transcrições de áudio.                                                                                                                                                      | Os documentos foram armazenados corretamente no banco de dados com as transcrições e metadados.                              | Nenhuma ação corretiva necessária.                                                                                                                     |
| 7      | Pesquisa de Documentos por Texto           | Verificar se a aplicação retorna o documento correto com base em uma pesquisa de texto.             | A busca deve retornar os documentos corretos para consultas simples e complexas (incluindo sinônimos).                                                                                                                                                                | A pesquisa por texto funcionou bem para consultas simples, mas falhou em consultas complexas e com sinônimos.                 | Treinar o modelo PLN com um corpus maior e mais diversificado. Implementar uma camada de pré-processamento semântico para consultas mais complexas.     |
| 8      | Pesquisa de Documentos por Áudio           | Testar se a pesquisa por áudio funciona corretamente e retorna o documento correspondente.          | O áudio deve ser transcrito corretamente, e o sistema deve retornar o documento correto.                                                                                                                                                                                | Transcrições de áudios de alta qualidade funcionaram bem; áudios com ruídos ou de baixa qualidade resultaram em falhas.       | Implementar técnicas de redução de ruído no áudio ou permitir ao usuário revisar e corrigir a transcrição antes de executar a pesquisa.                 |

---

### Resultados Detalhados dos Testes

#### 1. Scraping de Documentos Normativos

&emsp;&emsp;Os testes para a funcionalidade de scraping foram realizados para verificar a capacidade da aplicação de extrair documentos normativos de fontes externas. O processo de scraping é crítico, pois fornece os dados iniciais que alimentam o pipeline de PLN e a plataforma de documentos.

- **Cenário 1: URL Ausente**:  
O sistema foi testado para verificar se lida corretamente com solicitações malformadas. Ao enviar uma requisição sem o campo `url`, o sistema respondeu com um código 400 e uma mensagem de erro apropriada, indicando que o campo estava ausente. Não foi identificado nenhum problema neste cenário.

- **Cenário 2: Sucesso no Scraping**:  
Quando uma URL válida de uma página estática foi fornecida, o sistema conseguiu realizar o scraping corretamente, extraindo o título e o conteúdo da página. No entanto, observou-se que a aplicação falhou ao processar páginas com conteúdo dinâmico, carregadas via JavaScript. Isso resultou em dados incompletos. Foi recomendado o uso de uma solução de scraping headless para lidar com esse tipo de conteúdo.

- **Cenário 3: Erro no Scraping**:  
Simulamos uma falha no processo de scraping para verificar como o sistema responde a erros externos, como a falta de conectividade ou bloqueios por parte do servidor remoto. O sistema retornou um código 500, mas o log de erro não continha informações suficientes para diagnosticar o problema. A sugestão foi melhorar o log para capturar mais detalhes técnicos sobre a falha, como o código de resposta do servidor externo e a URL envolvida.

#### 2. Processamento de Documentos por PLN

&emsp;&emsp;Os testes de processamento via PLN envolveram tanto entradas de texto quanto de áudio. O objetivo era verificar se o sistema de PLN estava processando corretamente o conteúdo extraído pelo scraping e se as consultas realizadas pelos usuários estavam retornando os documentos corretos.

- **Cenário 1: Processamento de Texto**:  
O modelo PLN foi testado para verificar se o conteúdo do documento era classificado corretamente com base no texto inserido. O resultado foi satisfatório, com o modelo retornando as categorias esperadas. Não houve problemas identificados neste cenário.

- **Cenário 2: Processamento de Áudio**:  
O teste de processamento de áudio revelou que a aplicação conseguiu transcrever e processar corretamente áudios de alta qualidade, resultando na recuperação bem-sucedida de documentos. Entretanto, áudios de baixa qualidade, com ruído ou falhas na gravação, causaram transcrições imprecisas, levando à falha na recuperação de documentos. A ação corretiva sugerida foi melhorar o processamento de áudio e considerar o uso de serviços mais robustos de transcrição para lidar melhor com variabilidade na qualidade de gravação.

- **Cenário 3: Armazenamento após Processamento**:  
Os documentos processados foram corretamente armazenados no banco de dados, incluindo suas transcrições de áudio e metadados. Todos os dados esperados estavam presentes, e não foram observados problemas neste cenário.

#### 3. Pesquisa de Documentos (Texto e Áudio)

&emsp;&emsp;A pesquisa é uma das funcionalidades principais da aplicação, permitindo que os usuários encontrem documentos normativos com base em consultas de texto ou áudio.

- **Cenário 1: Pesquisa por Texto**:  
A pesquisa por texto funcionou corretamente em consultas simples e retornou os documentos relevantes. No entanto, em consultas mais complexas, como frases longas ou uso de sinônimos, o modelo PLN falhou em identificar os documentos corretos. A sugestão foi reforçar o treinamento do modelo PLN com mais dados, além de implementar técnicas de pré-processamento semântico que ajudem o sistema a lidar melhor com variações de linguagem.

- **Cenário 2: Pesquisa por Áudio**:  
A pesquisa por áudio foi bem-sucedida quando foram fornecidos áudios de alta qualidade. O sistema conseguiu transcrever o áudio e realizar a busca corretamente. Entretanto, áudios com ruído ou baixa qualidade levaram a transcrições imprecisas e falhas na pesquisa. A ação corretiva proposta foi melhorar o feedback para o usuário, permitindo que ele revisasse ou editasse a transcrição antes de prosseguir com a busca.

&emsp;&emsp;Portando, os testes demonstraram que a aplicação está funcional na maior parte dos casos e cumpre seu objetivo principal de realizar scraping, processar documentos via PLN e permitir pesquisas de texto e áudio. No entanto, alguns problemas foram identificados, especialmente em cenários envolvendo páginas com conteúdo dinâmico e áudios de baixa qualidade. As seguintes ações corretivas foram recomendadas:

1. **Melhorar o suporte para scraping de páginas dinâmicas** utilizando uma ferramenta de scraping headless.
2. **Aprimorar a qualidade dos logs de erro** para facilitar o diagnóstico de problemas.
3. **Melhorar o processamento de áudio** para lidar com gravações de baixa qualidade e permitir feedback mais robusto para o usuário.
4. **Reforçar o treinamento do modelo PLN** e implementar técnicas de pré-processamento semântico para melhorar a precisão em consultas mais complexas.

&emsp;&emsp;Com essas melhorias, a aplicação estará mais preparada para lidar com uma gama maior de cenários e entradas, oferecendo uma experiência mais confiável e eficiente para os usuários.

# 11. Deploy da Solução

&emsp;&emsp;Para o deploy dessa solução, foi utilizado do Software de containers, `Docker`.*Docker* é uma plataforma que permite desenvolver, enviar e executar aplicações em containers. Esses, são pacotes que incluem tudo o que é necessário para executar uma aplicação, garantindo que ela funcione de forma consistente em qualquer ambiente. Para isso, foi utilizado imagens Docker. Esse é um modelo que contém o código da aplicação, bibliotecas, dependências e configurações necessárias. As imagens são construídas a partir de um Dockerfile, que especifica como a imagem deve ser criada.

&emsp;&emsp;Já um container, é uma instância em execução de uma imagem Docker. Ele é isolado do sistema *host* e pode ser iniciado, parado, movido ou excluído. Cada container tem seu próprio sistema de arquivos, rede e processo. Por fim, o *Docker Compose* é uma ferramenta para definir e executar aplicações Docker multi-containers. Com um arquivo de configuração docker-compose.yml, você pode especificar todos os containers necessários, suas redes e volumes.

## 11.1. Monitoramento
&emsp;&emsp;Com o objetivo de monitorar e analisar o desempenho da EC2 na aplicação, a AWS fornece instrumentos de log e o AWS CloudWatch, um serviço de monitoramento para recursos e aplicações que permite coletar e rastrear métricas, coletar e monitorar arquivos de log e definir alarmes. Com o CloudWatch, é possível monitorar o desempenho da aplicação em tempo real e receber notificações em caso de problemas.

&emsp;&emsp;As métricas de importante análise, são:
- Uso de CPU: Monitorar o uso de CPU do container para identificar se a aplicação está sobrecarregada.
- Uso de Memória: Monitorar a utilização de memória para evitar problemas de desempenho.
- Tempo de Resposta: Medir o tempo que leva para as solicitações serem processadas.
- Taxa de Erros: Monitorar a porcentagem de solicitações que resultam em erros.

## 11.2. Testes de produção

&emsp;&emsp;Com o laboratório da AWS Academy em execução, validamos o endereço público (AWS IP ELASTIC - http://34.231.209.40/) 

<div align="center">
	<sub>Imagem x - Get all regulations</sub>
	<img src="./assets/deploy_regulations.png"/>
</div>

--- 

<div align="center">
	<sub>Imagem x - Get all pln</sub>
	<img src="./assets/deploy_pln.png"/>
</div>

## 11.3. Como Utilizar o Docker Compose

&emsp;&emsp;Para iniciar a aplicação usando Docker Compose, siga estas etapas:

- Instalação do Docker Compose
- Execute 'docker-compose up'
- Para fechar, execute 'docker-compose down'
- Para visualizar os logs, execute 'docker-compose logs'

# 12. Benefícios entregues pelo projeto

&emsp;&emsp;O projeto Vox traz uma série de benefícios significativos para o Bank of America, otimizando processos relacionados ao acompanhamento das mudanças regulatórias na indústria financeira. A solução permitirá uma agilidade considerável na busca por regulamentações atualizadas, proporcionando maior velocidade e precisão na identificação de normativas relevantes. Além disso, o Vox oferece facilidade de acesso às consultas normativas, com uma interface centralizada que reunirá todas as informações sobre atualizações regulatórias em um só lugar.

&emsp;&emsp;Esses benefícios impactarão diretamente o trabalho dos analistas, reduzindo o tempo gasto em consultas, aumentando a eficiência das análises e garantindo maior precisão nas tomadas de decisão. Como resultado, o Vox contribuirá para uma gestão regulatória mais ágil e assertiva, alinhada às necessidades de compliance do banco.

## Detalhamento:

- Agilidade na busca por regulamentações atualizadas: O sistema permite que os analistas encontrem rapidamente as regulamentações mais recentes, eliminando a necessidade de pesquisas manuais extensas, permitindo assim, que as decisões sejam sempre baseadas nas normas mais atuais.

- Facilidade na identificação de regulamentações relacionadas: Por meio de um sistema de interligação automática, é destacado regulamentações correlacionadas, o que facilita a análise de normas interdependentes e permite uma visão mais abrangente do cenário regulatório.

- Praticidade nas consultas normativas: Por meio de uma interface intuitiva e recursos avançados de filtragem com PLN, os usuários podem realizar consultas específicas com maior facilidade, seja por data, órgão regulador ou palavra-chave, reduzindo o tempo gasto em buscas.

- Centralização de informações sobre políticas regulatórias: O projeto VOX consolida todas as informações regulamentares em um único local, proporcionando uma fonte confiável e única de consulta. Isso reduz a fragmentação das informações e garante que todos os analistas acessem as mesmas referências.

- Aumento da precisão e redução de erros: Ao automatizar parte do processo de consulta e cruzamento de normas, o sistema minimiza erros humanos e aumenta a precisão nas análises, o que é crucial em um ambiente de compliance, onde a preocupação sobre a integridade das normas é essencial.

- Eficiência operacional e otimização de tempo: Com a automação de processos e a facilitação de consultas, os analistas podem dedicar mais tempo às tarefas estratégicas, otimizando sua produtividade e reduzindo o esforço repetitivo de pesquisa e interpretação.

- Atualizações diárias: O sistema está configurado para fornecer atualizações automáticas diáriamente sempre que uma nova regulamentação for publicada ou alterada, permitindo que os analistas se mantenham informados.

&emsp;&emsp;Esses benefícios não apenas melhoram a eficiência operacional, mas também garantem maior conformidade regulatória e suporte às tomadas de decisão estratégicas no ambiente bancário.

# 13. Aperfeiçoamentos Futuros

O projeto atual foi desenvolvido em apenas 10 semanas, o que naturalmente implicou na necessidade de priorizar entregas dentro de um curto período de tempo. É compreensível que a solução ainda não esteja no estado mais refinado possível, mas já oferece uma base sólida. Dessa forma, algumas ideias de aperfeiçoamento foram identificadas e serão discutidas para futuros ciclos de desenvolvimento. 

## 13.1 Possíveis aperfeiçoamentos futuros

A seguir, listamos sugestões para evoluir a arquitetura e as tecnologias empregadas, visando otimizar o sistema em termos de escalabilidade, segurança e desempenho.

**Migração para Banco de Dados NoSQL (DynamoDB)**

Atualmente, o sistema utiliza o **PostgreSQL** no Amazon RDS como banco de dados relacional. No entanto, à medida que o volume de dados cresce, pode ser vantajoso migrar algumas partes do sistema para uma solução de banco de dados **NoSQL** como o **Amazon DynamoDB**, especialmente para dados não estruturados ou que necessitem de alta escalabilidade e baixa latência.

Benefícios dessa migração incluem:
- **Escalabilidade Horizontal Automática**: O DynamoDB ajusta sua capacidade automaticamente com base na demanda, sem necessidade de intervenção manual.
- **Desempenho Consistente**: É altamente eficiente para operações de leitura e gravação com baixa latência, ideal para grandes volumes de dados e acessos concorrentes.
- **Modelo Flexível de Dados**: Permite a armazenagem de dados sem a rigidez de um esquema pré-definido, sendo ideal para cenários de dados em evolução.

**Aprimoramento da Segurança com AWS Secrets Manager e KMS**

Embora o sistema já utilize boas práticas de segurança, há sempre margem para aprimorar ainda mais esse aspecto crítico. A utilização do **AWS Secrets Manager** e do **AWS Key Management Service (KMS)** pode ajudar a gerenciar credenciais e chaves de criptografia de forma mais segura e escalável.

Principais benefícios:
- **Gerenciamento Seguro de Credenciais**: O Secrets Manager permite armazenar e rotacionar automaticamente credenciais, como senhas, chaves de API e tokens.
- **Criptografia mais Segura**: O KMS possibilita a criptografia de dados com chaves gerenciadas centralmente, oferecendo mais controle e auditabilidade sobre as chaves criptográficas.
- **Conformidade com Padrões de Segurança**: A adoção dessas soluções facilita a conformidade com padrões de segurança como ISO 27001, PCI-DSS e HIPAA.

**Integração de Machine Learning para Previsões e Análises Preditivas**

Com a quantidade de dados regulatórios e transcrições que o sistema processa, há um potencial para integrar funcionalidades de **Machine Learning (ML)**, aproveitando serviços como **Amazon SageMaker**. Isso possibilitaria previsões e análises preditivas mais avançadas, como:
- **Análise Preditiva de Mudanças Regulatórias**: Prever mudanças futuras com base em padrões históricos e tendências.
- **Classificação Automática de Regulações**: Utilizar modelos de aprendizado supervisionado para melhorar a classificação automática de regulações, minimizando a intervenção manual.
- **Detecção de Anomalias**: Identificar automaticamente padrões incomuns em dados transcritos ou regulatórios que possam indicar problemas ou novas oportunidades.

**Monitoramento e Observabilidade Avançados com AWS X-Ray e Prometheus**

O sistema já possui monitoramento básico, mas poderia se beneficiar da implementação de ferramentas avançadas de monitoramento e rastreamento como o **AWS X-Ray** e o **Prometheus** para obter maior visibilidade e controle sobre o comportamento dos serviços.

- **AWS X-Ray** permite rastrear solicitações de ponta a ponta através do sistema distribuído, facilitando a identificação de gargalos de desempenho e a análise de falhas em serviços individuais.
- **Prometheus**, aliado ao **Grafana**, possibilita o monitoramento em tempo real de métricas detalhadas dos serviços e dos recursos de infraestrutura, fornecendo alertas em caso de incidentes.

**Redundância Geográfica e Multi-Region Failover**

Para aumentar a resiliência do sistema contra falhas catastróficas, uma evolução seria a implementação de uma **arquitetura multi-regional**. Isso implica replicar os serviços e bancos de dados em múltiplas regiões da AWS, garantindo continuidade de serviço mesmo em caso de falhas em uma região específica.

Benefícios dessa abordagem incluem:
- **Alta Disponibilidade**: Com redundância geográfica, o sistema pode continuar operando mesmo em caso de falha de uma região inteira da AWS.
- **Melhor Performance Global**: Serviços distribuídos em várias regiões podem reduzir a latência para usuários localizados em diferentes partes do mundo.
- **Failover Automatizado**: Em caso de falha, o tráfego pode ser redirecionado automaticamente para a região saudável, minimizando interrupções no serviço.

**Adoção de Arquitetura Serverless para Algumas Funções**

Embora a arquitetura atual seja baseada em instâncias EC2 e microserviços, alguns componentes do sistema podem ser convertidos para uma arquitetura **serverless** utilizando **AWS Lambda** para reduzir custos e melhorar a escalabilidade em cargas de trabalho variáveis.

Componentes que poderiam ser serverless:
- **Serviço de Transcrição de Áudio**: Migrar o processamento de transcrições de áudio para funções Lambda, que são executadas sob demanda.
- **Processamento de Eventos**: Utilizar Lambda para acionar processamento de eventos regulatórios ou de PLN, permitindo uma execução mais eficiente e elástica conforme a demanda.

Todas essas tecnologias combinadas tem como intuito tornar o projeto cada vez melhor, dessa maneira, tornando mais alinhado as tecnologias atuais e sustentáveis em termos de custos, ciclo de vida e alinhamento ao mercado.

# Referências

[Seção 1.3.3](#133-estimativa-de-investimentos):

[Média salarial Desenvolvedor Júnior](https://www.glassdoor.com.br/Sal%C3%A1rios/desenvolvedor-junior-sal%C3%A1rio-SRCH_KO0,20.htm)

[Média salarial Desenvolvedor Sênior](https://br.indeed.com/career/desenvolvedor-java-s%C3%AAnior/salaries/Estado-de-S%C3%A3o-Paulo)

[Média salarial _Product owner_](https://www.glassdoor.com.br/Sal%C3%A1rios/product-owner-po-sal%C3%A1rio-SRCH_KO0,16.htm#:~:text=A%20remunera%C3%A7%C3%A3o%20vari%C3%A1vel%20do%20cargo)

1. DAM, R.; SIANG, T. Personas – A Simple Introduction. Disponível em: https://www.interaction-design.org/literature/article/personas-why-and-how-you-should-use-them. Acesso em: 12 fev. 2024.

# Apêndice

<conteúdo>
