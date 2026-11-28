
# EducaPE — Análise da Infraestrutura das Escolas Públicas em Pernambuco

## 1. Apresentação do projeto

O **EducaPE** é um projeto acadêmico desenvolvido na disciplina de Banco de Dados I, do curso de Análise e Desenvolvimento de Sistemas (ADS), da Autarquia de Ensino Superior de Arcoverde (AESA).

O projeto tem como objetivo organizar, explorar e analisar informações relacionadas à infraestrutura das escolas públicas de Pernambuco, utilizando dados oficiais do Censo Escolar da Educação Básica 2024, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

A pesquisa busca compreender como os recursos e serviços escolares estão distribuídos entre as localidades pernambucanas, identificando possíveis desigualdades nas condições de infraestrutura.

Entre os aspectos investigados estão o abastecimento de água, o fornecimento de energia elétrica, o acesso à internet, a disponibilidade de bibliotecas e a existência de laboratórios.

O projeto passou pela fase de Descoberta, com a obtenção, organização e análise exploratória dos dados. Posteriormente, foi desenvolvido o banco de dados relacional em PostgreSQL, incluindo a criação das tabelas, os relacionamentos, a importação dos dados e as consultas SQL para análise da infraestrutura escolar.
## 2. Objetivos

### Objetivo geral

Analisar a distribuição da infraestrutura das escolas públicas de Pernambuco, utilizando dados oficiais do Censo Escolar 2024, para identificar possíveis desigualdades entre as localidades.

### Objetivos específicos

- Obter e organizar os microdados oficiais do INEP.
- Identificar as escolas localizadas em Pernambuco.
- Separar as instituições públicas das escolas privadas.
- Investigar indicadores de abastecimento de água e energia elétrica.
- Analisar a disponibilidade de internet, bibliotecas e laboratórios.
- Identificar valores ausentes e possíveis limitações dos dados.
- Levantar perguntas relevantes para o desenvolvimento do banco de dados.
- Identificar preliminarmente as entidades e seus relacionamentos.

## 3. Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Leitura, tratamento e importação dos dados. |
| Pandas | Manipulação e análise dos arquivos CSV. |
| PostgreSQL | Armazenamento dos dados em um banco relacional. |
| SQL | Criação das tabelas e consultas de análise. |
| pgAdmin 4 | Administração do banco e execução das consultas SQL. |
| psycopg2 | Conexão entre Python e PostgreSQL. |
| python-dotenv | Carregamento das configurações de conexão por variáveis de ambiente. |
| Cursor | Edição e organização dos códigos Python e SQL. |
| Git e GitHub | Controle de versões e armazenamento do projeto. |
| Markdown | Elaboração da documentação.

## 4. Fonte dos dados

**Instituição:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

**Base de dados:** Censo Escolar da Educação Básica 2024.

**Formato:** CSV.

**Arquivo original:** `microdados_ed_basica_2024.csv`.

**Arquivo filtrado:** `escolas_pe_2024.csv`.

**Ano de referência:** 2024.

**Portal oficial:** [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos)

### Obtenção dos dados

Os microdados foram obtidos por download no portal oficial do INEP.

Após a extração dos arquivos, foi realizada a seleção dos registros correspondentes ao estado de Pernambuco, utilizando o código da unidade federativa.

O arquivo resultante foi armazenado separadamente para preservar os dados originais.


## 5. Estrutura do projeto

O projeto EducaPE está organizado nas seguintes pastas e arquivos:

```text
EducaPE/
│
├── banco_de_dados/
│   ├── 01_criar_tabelas.sql
│   ├── 02_importar_dados.py
│   ├── 03_consultas.sql
│   ├── 04_dicionario_dados.md
│   └── diagramas/
│
├── dados_originais/
│
├── dados_tratados/
│   └── escolas_pe_2024.csv
│
├── analise_py/
│
├── README.md
└── documentacao_tecnica_educape.md
```

### Responsabilidade das pastas e arquivos

banco_de_dados/: reúne os scripts SQL, o código de importação, o dicionário de dados e os diagramas.

dados_originais/: armazena os microdados originais disponibilizados pelo INEP.

dados_tratados/: contém os dados filtrados e preparados para análise.

analise_py/: reúne os códigos Python utilizados na exploração dos dados.

README.md: apresenta o projeto, seus objetivos, metodologia e resultados.

documentacao_tecnica_educape.md: descreve os aspectos técnicos do banco de dados e sua implementação.


## 6. Metodologia

O desenvolvimento da Fase 01 foi organizado nas seguintes atividades:

1. Definição do tema e do problema de pesquisa.
2. Identificação da fonte oficial de dados.
3. Download e extração dos microdados.
4. Filtragem das escolas de Pernambuco.
5. Organização dos arquivos originais e tratados.
6. Exploração inicial utilizando Python e Pandas.
7. Seleção das escolas públicas.
8. Análise preliminar dos indicadores de infraestrutura.
9. Identificação de possíveis entidades.
10. Levantamento de perguntas para as próximas etapas do projeto.

## 7. Análise exploratória dos dados

A análise exploratória tem como objetivo conhecer a estrutura dos microdados e identificar informações relevantes para a pesquisa.

### 7.1 Informações gerais

| Indicador                           | Resultado |
| ----------------------------------- | --------- |
| Colunas identificadas               | 426       |
| Escolas identificadas em Pernambuco | 9.936     |
| Escolas públicas identificadas      | 6.835     |
| Localidades identificadas           | 185       |

As 185 localidades correspondem aos 184 municípios pernambucanos e ao distrito estadual de Fernando de Noronha.

### 7.2 Distribuição das escolas

Entre as localidades com maior quantidade de escolas identificadas na base estão:

| Município               | Escolas |
| ----------------------- | ------- |
| Recife                  | 1.235   |
| Jaboatão dos Guararapes | 514     |
| Petrolina               | 379     |
| Olinda                  | 332     |
| Caruaru                 | 298     |

Esses valores consideram os registros gerais das escolas de Pernambuco, incluindo instituições públicas e privadas.

### 7.3 Seleção das escolas públicas

Para identificar as escolas públicas, foi utilizada a variável `TP_DEPENDENCIA`.

| Código | Dependência administrativa |
| ------ | -------------------------- |
| 1      | Federal                    |
| 2      | Estadual                   |
| 3      | Municipal                  |
| 4      | Privada                    |

Foram selecionados os registros com códigos 1, 2 e 3, resultando em 6.835 escolas públicas.

## 8. Indicadores de infraestrutura

As análises a seguir consideram as escolas públicas identificadas na base.

Em diversos indicadores, foram encontrados 993 registros sem informação. Esses valores foram contabilizados separadamente, sem serem interpretados como respostas negativas.

### 8.1 Abastecimento de água

| Indicador                 | Sim   | Não   | Sem informação |
| ------------------------- | ----- | ----- | -------------- |
| Água potável              | 5.663 | 179   | 993            |
| Água da rede pública      | 3.580 | 2.262 | 993            |
| Poço artesiano            | 674   | 5.168 | 993            |
| Cacimba                   | 1.990 | 3.852 | 993            |
| Fonte ou rio              | 71    | 5.771 | 993            |
| Carro-pipa                | 1.007 | 4.835 | 993            |
| Abastecimento inexistente | 111   | 5.731 | 993            |

**Observação preliminar:** embora a maioria das escolas com informações disponíveis declare possuir água potável, existem instituições sem esse recurso.

Também foram identificadas diferentes fontes de abastecimento, incluindo rede pública, cacimba e carro-pipa.

Uma escola pode utilizar mais de uma fonte de água, portanto os indicadores não devem ser somados como categorias exclusivas.

### 8.2 Energia elétrica

| Indicador           | Sim   | Não   | Sem informação |
| ------------------- | ----- | ----- | -------------- |
| Rede pública        | 5.832 | 10    | 993            |
| Gerador fóssil      | 3     | 5.839 | 993            |
| Energia renovável   | 40    | 5.802 | 993            |
| Energia inexistente | 8     | 5.834 | 993            |

**Observação preliminar:** a rede pública é a principal forma de fornecimento de energia elétrica entre as escolas com dados disponíveis.

### 8.3 Acesso à internet

| Indicador                  | Sim   | Não   | Sem informação |
| -------------------------- | ----- | ----- | -------------- |
| Internet na escola         | 5.391 | 451   | 993            |
| Internet para alunos       | 2.221 | 3.621 | 993            |
| Internet administrativa    | 4.966 | 876   | 993            |
| Internet para aprendizagem | 3.951 | 1.891 | 993            |
| Internet para comunidade   | 171   | 5.671 | 993            |

**Observação preliminar:** existe uma diferença entre a quantidade de escolas que declaram possuir internet e aquelas que registram acesso para os alunos.

Esse resultado motiva uma investigação sobre a finalidade e a disponibilidade dos recursos tecnológicos.

### 8.4 Bibliotecas e laboratórios

| Indicador                            | Sim   | Não   | Sem informação |
| ------------------------------------ | ----- | ----- | -------------- |
| Biblioteca                           | 2.268 | 3.574 | 993            |
| Biblioteca ou sala de leitura        | 3.035 | 2.807 | 993            |
| Laboratório de ciências              | 583   | 5.259 | 993            |
| Laboratório de informática           | 1.186 | 4.656 | 993            |
| Laboratório de educação profissional | 44    | 5.798 | 993            |

**Observação preliminar:** os dados apontam diferenças na disponibilidade de espaços e recursos pedagógicos, especialmente laboratórios de ciências e informática.

Essas informações poderão ser aprofundadas por município e dependência administrativa.

## 9. Qualidade e limitações dos dados

Durante a exploração inicial, foram observados os seguintes aspectos:

- Existência de valores ausentes em indicadores de infraestrutura.
- Necessidade de diferenciar respostas negativas de registros sem informação.
- Presença de escolas públicas e privadas no arquivo filtrado por estado.
- Possibilidade de múltiplas fontes de abastecimento de água para uma mesma escola.
- Necessidade de considerar a quantidade de escolas por município ao realizar comparações.

Os resultados apresentados são preliminares e descritivos. Ainda não representam uma avaliação definitiva da qualidade da infraestrutura escolar.

## 10. Dicionário inicial de dados

| Variável                     | Descrição                                     |
| ---------------------------- | --------------------------------------------- |
| `CO_ENTIDADE`                | Código de identificação da escola             |
| `NO_ENTIDADE`                | Nome da escola                                |
| `CO_MUNICIPIO`               | Código da localidade                          |
| `NO_MUNICIPIO`               | Nome da localidade                            |
| `TP_DEPENDENCIA`             | Dependência administrativa da escola          |
| `IN_AGUA_POTAVEL`            | Indicador de água potável                     |
| `IN_AGUA_REDE_PUBLICA`       | Indicador de abastecimento pela rede pública  |
| `IN_ENERGIA_REDE_PUBLICA`    | Indicador de energia da rede pública          |
| `IN_ENERGIA_INEXISTENTE`     | Indicador de inexistência de energia elétrica |
| `IN_INTERNET`                | Indicador de disponibilidade de internet      |
| `IN_INTERNET_ALUNOS`         | Indicador de acesso à internet para alunos    |
| `IN_BIBLIOTECA`              | Indicador de biblioteca                       |
| `IN_LABORATORIO_CIENCIAS`    | Indicador de laboratório de ciências          |
| `IN_LABORATORIO_INFORMATICA` | Indicador de laboratório de informática       |

Este dicionário é preliminar e poderá ser ampliado e validado com a documentação oficial do INEP nas próximas etapas.

## 11. Identificação preliminar das entidades

A partir da análise dos dados e da modelagem do banco de dados, foram definidas três entidades principais.

1. Município

Representa as localidades onde as escolas estão situadas.

Atributos:

Código do município (co_municipio).

Nome do município (no_municipio).

2. Escola

Representa as instituições públicas de ensino cadastradas no projeto.

Atributos:

Código da escola (co_entidade).

Nome da escola (no_entidade).

Código do município (co_municipio).

Tipo de dependência administrativa (tp_dependencia).

3. Infraestrutura

Armazena informações sobre os recursos e serviços disponíveis nas escolas.

Atributos:

Código da escola (co_entidade).
Indicador de água potável.
Indicador de abastecimento pela rede pública.
Indicador de energia elétrica da rede pública.
Indicador de internet.
Indicador de internet para alunos.
Indicador de biblioteca.
Indicador de laboratório de informática.
Indicador de laboratório de ciências.

### Relacionamentos

- **Município (1:N) Escola:** um município pode possuir várias escolas.
- **Escola (1:1) Infraestrutura:** cada registro de infraestrutura está associado a uma única escola.

Esses relacionamentos são implementados por meio de chaves primárias (PK) e chaves estrangeiras (FK).


## 12. Subtemas do projeto

O EducaPE aborda três subtemas com a mesma importância na análise da infraestrutura das escolas públicas de Pernambuco.

### 1. Abastecimento de água

Análise da disponibilidade de água potável e das diferentes fontes de abastecimento utilizadas pelas escolas.

### 2. Energia elétrica

Análise da disponibilidade de energia da rede pública, geradores e fontes renováveis.

### 3. Internet e conectividade

Análise da disponibilidade de internet nas escolas e do acesso oferecido aos alunos.

### Indicadores complementares

Também são considerados indicadores relacionados à existência de bibliotecas, salas de leitura e laboratórios.

### Tema selecionado

**Análise da Infraestrutura das Escolas Públicas em Pernambuco.**

O tema foi escolhido por permitir uma análise mais abrangente, relacionando diferentes indicadores e possibilitando comparações entre localidades.

## 13. Perguntas que o banco de dados deverá responder

1. Quais municípios apresentam maior proporção de escolas públicas sem água potável?
2. A disponibilidade de internet nas escolas está associada ao acesso dos alunos?
3. Quais municípios apresentam menor disponibilidade de bibliotecas e laboratórios?
4. Existem diferenças na infraestrutura entre escolas municipais, estaduais e federais?
5. Como os recursos escolares estão distribuídos entre as localidades pernambucanas?
6. Quais indicadores apresentam maiores diferenças entre os municípios?

Essas perguntas orientarão o levantamento de requisitos e o desenvolvimento do banco de dados nas próximas fases.

## Requisitos Funcionais

- **RF001:** O banco de dados deverá permitir consultar as escolas públicas cadastradas.
- **RF002:** O banco de dados deverá permitir consultar as escolas por município.
- **RF003:** O banco de dados deverá permitir consultar a disponibilidade de internet nas escolas.
- **RF004:** O banco de dados deverá permitir consultar informações sobre abastecimento de água, energia elétrica, bibliotecas e laboratórios.
- **RF005:** O banco de dados deverá permitir obter resultados quantitativos sobre os indicadores de infraestrutura escolar.

## Requisitos Não Funcionais

- **RNF001 — Banco de Dados:** O projeto deverá utilizar PostgreSQL para armazenar os dados das escolas públicas.
- **RNF002 — Integridade:** O banco deverá utilizar chaves primárias e estrangeiras para garantir a integridade dos relacionamentos entre as tabelas.
- **RNF003 — Segurança:** As credenciais de acesso ao banco deverão ser armazenadas em variáveis de ambiente, sem publicação no GitHub.
- **RNF004 — Organização:** Os scripts SQL, códigos Python e documentos deverão ser organizados em pastas específicas.
- **RNF005 — Desempenho:** As consultas deverão apresentar desempenho adequado para a análise dos dados escolares.

## 14. Instalação e configuração

### Pré-requisitos

Para executar o projeto EducaPE, são necessárias as seguintes ferramentas:

- Python 3.
- PostgreSQL.
- pgAdmin 4.
- Bibliotecas Pandas, psycopg2 e python-dotenv.
- Arquivo CSV tratado do Censo Escolar 2024.
- Arquivo .env configurado com os dados de conexão ao PostgreSQL.

### Instalação das bibliotecas

No terminal, execute:

pip install pandas psycopg2-binary python-dotenv

### Configuração

O projeto utiliza um arquivo .env para armazenar as configurações de conexão com o PostgreSQL.

As credenciais devem permanecer privadas e não devem ser publicadas no GitHub.

### Estrutura necessária

Antes da execução, confira se o arquivo `escolas_pe_2024.csv` está dentro da pasta `dados_tratados`.

## 15. Executando a análise

Para executar o projeto EducaPE, siga as etapas abaixo.

### Preparação do banco de dados

Abra o pgAdmin 4, conecte-se ao PostgreSQL e acesse o banco de dados educape.

Para criar as tabelas, execute o script:
**banco_de_dados/01_criar_tabelas.sql**

### Importação dos dados

Com o banco de dados preparado e o arquivo .env configurado, execute no terminal, a partir da pasta principal do projeto:

**python banco_de_dados/02_importar_dados.py**

Esse script realiza a conexão com o PostgreSQL e importa os dados dos municípios, escolas públicas e infraestrutura.

### Execução das consultas SQL

No pgAdmin 4, abra o Query Tool e execute as consultas disponíveis no arquivo:

**banco_de_dados/03_consultas.sql**

As consultas permitem analisar a quantidade de escolas públicas e a disponibilidade de recursos de infraestrutura.

### Análise exploratória

Para executar a análise exploratória dos dados, utilize o terminal:

**python analise_py/analise.py**

O script apresenta informações sobre as escolas, os municípios e os indicadores de infraestrutura.

### Observação

Os scripts SQL são executados no pgAdmin 4, enquanto os scripts Python são executados pelo terminal.

## 16. Organização e responsabilidades da equipe

O projeto EducaPE é desenvolvido pelos integrantes **Maria Beatriz e Edcalos França**, que participam conjuntamente de todas as etapas do trabalho.

### Atividades realizadas em conjunto

- Definição do tema e dos objetivos do projeto.
- Pesquisa e identificação da fonte oficial de dados.
- Download e organização dos microdados do INEP.
- Filtragem e tratamento inicial dos arquivos CSV.
- Desenvolvimento e execução do código Python.
- Análise exploratória dos indicadores de infraestrutura.
- Identificação preliminar das entidades e dos requisitos.
- Elaboração e revisão da documentação.
- Planejamento da apresentação acadêmica.

### Divisão de responsabilidades

As atividades são realizadas de maneira colaborativa, com participação de ambos os integrantes nas decisões, no desenvolvimento e na revisão do projeto.

Não houve divisão exclusiva de tarefas entre os integrantes.

## 17. Comunicação e acompanhamento da equipe

A equipe do projeto EducaPE, formada por Maria Beatriz e Edcalos França, realiza reuniões presenciais às segundas e quartas-feiras, na faculdade.

Durante esses encontros, os integrantes discutem o andamento do projeto, compartilham resultados, esclarecem dúvidas e definem as próximas atividades.

O desenvolvimento é realizado de forma colaborativa, com participação de ambos os integrantes nas decisões e em todas as etapas do trabalho.

## 18. Ferramentas de apoio ao desenvolvimento

Durante o desenvolvimento do EducaPE, foi utilizado o Cursor como ambiente de desenvolvimento, em substituição ao Visual Studio Code, devido às limitações de desempenho do notebook, que dificultavam a utilização do VS Code.

O Cursor também foi utilizado como ferramenta de apoio para identificar e corrigir erros nos códigos, auxiliando na resolução de dificuldades técnicas encontradas durante a implementação do projeto.

## 19. Próximas etapas

Com a estrutura do banco de dados implementada, as próximas atividades do EducaPE são:

- Revisar e validar os requisitos levantados.
- Conferir a consistência entre o DER, o modelo lógico e as tabelas implementadas.
- Validar as consultas SQL e os resultados obtidos.
- Finalizar a documentação técnica do projeto.
- Organizar os resultados das análises para a apresentação acadêmica.
- Realizar a revisão final do repositório no GitHub.

Essas atividades têm como objetivo consolidar o desenvolvimento e preparar o projeto para sua apresentação e avaliação.

## 20. Considerações finais

O desenvolvimento do EducaPE permitiu organizar, explorar e analisar os microdados do Censo Escolar 2024, disponibilizados pelo INEP, identificando informações relevantes sobre as condições de infraestrutura das escolas públicas de Pernambuco.

Durante o desenvolvimento, foram identificadas 6.835 escolas públicas distribuídas em 185 localidades. A análise exploratória revelou diferenças na disponibilidade de recursos, especialmente no abastecimento de água, no fornecimento de energia elétrica e no acesso à internet.

Também foi desenvolvido um banco de dados relacional utilizando PostgreSQL, composto pelas tabelas municipios, escolas e infraestrutura, com seus respectivos relacionamentos. Foram realizadas a importação dos dados, a elaboração do diagrama do banco e a criação de consultas SQL para investigar os indicadores de infraestrutura escolar.

Os resultados demonstram a importância da organização e análise dos dados educacionais para compreender as condições das escolas públicas e identificar possíveis diferenças entre as localidades pernambucanas.

Dessa forma, o EducaPE consolida a aplicação prática dos conhecimentos de Banco de Dados, envolvendo coleta, tratamento, modelagem, armazenamento e consulta de dados reais.

## 21. Autores

**Projeto:** EducaPE — Análise da Infraestrutura das Escolas Públicas em Pernambuco

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

**Instituição:** Autarquia de Ensino Superior de Arcoverde (AESA)

**Disciplina:** Banco de Dados I

**Integrantes:**

- Maria Beatriz Silva Santos
- Edcalos França da Silva

---

**EducaPE — Dados educacionais para compreender a infraestrutura das escolas públicas de Pernambuco.**

