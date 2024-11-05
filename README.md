# VOX

# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="assets/inteli-logo.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width=40% height=40%></a>
</p>

<br>

# Automação com Reconhecimento de Voz

## Vox Group

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/bruna-brasil-alexandre/">Bruna Brasil</a>
- <a href="https://www.linkedin.com/in/claramohammad/">Clara Mohammad</a>
- <a href="https://www.linkedin.com/in/joselitojunior/">Joselito Junior</a>
- <a href="https://www.linkedin.com/in/luigiotavio/">Luigi Macedo</a>
- <a href="https://www.linkedin.com/in/renanfeit/">Renan Feitosa</a>



## 👩‍🏫 Professores:
### Orientador(a) 
- Hermano Peixoto

### Instrutores
- Reginaldo Arakaki
- Victor Hayashi
- Hermano Peixoto
- Francisco Escobar
- Geraldo Magela
- Lisane Valdo
- Ana Cristina dos Santos

## 📜 Descrição

&emsp;&emsp; O projeto Vox tem como objetivo criar uma solução tecnológica que facilite o processo de identificação, classificação e consulta de mudanças nas Leis, Regras e Regulamentações (LRRs) aplicáveis ao Bank of America utilizando técnicas de Processamento de Linguagem Natural. Esse processo auxilia a área de Compliance do BofA a manter-se atualizada com as normas vigentes, garantindo a conformidade com as regulamentações do mercado financeiro brasileiro.


## 📁 Estrutura de pastas

|--> assets<br>
  &emsp;| --> imagens <br>
|--> docs<br>
  &emsp;| --> assets <br>
  &emsp;|--> readme.md<br>
|--> src<br>
  &emsp;|--> backend<br>
  &emsp;&emsp;|--> database<br>
  &emsp;&emsp;|--> pln<br>
  &emsp;&emsp;|--> scraping<br>
  &emsp;&emsp;|--> tests<br>
  &emsp;|--> frontend<br>
    &emsp;&emsp;|--> src<br>
    &emsp;&emsp;|--> tests<br>
| readme.md<br>

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a parte gráfica do projeto, ou seja, as imagens e links de vídeos que os representam.

- <b>docs</b>: aqui está toda a documentação relacionada ao projeto. Inclui a documentação de todo o processo de desenvolvimento, desde a concepção da ideia até a entrega do produto final.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto, incluindo backend e frontend.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Instalação

### Pré-requisitos
- [Python](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en/download/)
- [Docker](https://docs.docker.com/get-docker/)

### Backend

1. Clone o repositório localmente
2. Rodar o docker compose com o comando `docker-compose up`, que instalará todas as dependências necessárias e iniciará o servidor.


### Frontend

1. Clone o repositório localmente
2. Instale as dependências dentro da pasta `frontend` com o comando `npm install`
3. Inicie o servidor com o comando `npm run dev`



## 🗃 Histórico de lançamentos

* 0.1.0 - 19/08/2024
  * DOCS | Organização e adição de seções.
  * DOCS | Stakeholders, matriz de riscos e diagrama de arquitetura.
  * DOCS | Canvas proposta de valor, modelo de negócios e requisitos funcionais.
  * DOCS | Padrões de trabalho, solução proposta, e pilha tecnológica.
  * DOCS | Seções de perfil de usuário, descrição do problema, persona, jornada do usuário.
  * DOCS | Requisitos não funcionais, estimativa de investimento, tendências na área.

* 0.2.0 - 31/08/2024
  * FEAT | Configuração inicial do backend.
  * FEAT | Integração da API Speech-to-text.
  * DOCS | Pilha tecnológica, documentação de banco de dados e mockups.

* 0.3.0 - 30/09/2024
  * DOCS | Backend e processo de deploy do algoritmo na nuvem.
  * FIX | Refatoração do backend e integração com APIs.
  * DOCS | Documentação de PLN e RabbitMQ.
  * FEAT | Frontend e integração.
  * FEAT | Scraping, serviço de mensageria e testes.
  * FEAT | Adição de docker-compose.

* 0.4.0 - 10/10/2024
  * DOCS | Instruções de integração, relatórios de testes, deploy e upgrades futuros.
  * FEAT | Adição de filtros funcionais, paginação e finalização de sidebar.
  * FEAT | Pipeline da criação de normas integrada.
  * FEAT | Tela de tags.
  * FEAT | Identificação de normas associadas.


## 📋 Licença/License

Vox by <a href="https://www.linkedin.com/in/bruna-brasil-alexandre/">Bruna Brasil</a>, <a href="https://www.linkedin.com/in/claramohammad/">Clara Mohammad</a>, <a href="https://www.linkedin.com/in/joselitojunior/">Joselito Junior</a>, <a href="https://www.linkedin.com/in/luigiotavio/">Luigi Macedo</a>, <a href="https://www.linkedin.com/in/renanfeit/">Renan Feitosa</a>. Licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>
