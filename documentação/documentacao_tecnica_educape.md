
# Documentação Técnica — EducaPE

## 1. Introdução

O EducaPE é um projeto acadêmico desenvolvido na disciplina de Banco de Dados I, do curso de Análise e Desenvolvimento de Sistemas.

O projeto tem como finalidade analisar a infraestrutura das escolas públicas de Pernambuco, utilizando dados oficiais do Censo Escolar da Educação Básica de 2024, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

A proposta consiste em organizar os dados em um banco de dados relacional PostgreSQL, permitindo realizar consultas sobre os recursos e serviços disponíveis nas instituições de ensino.

## 2. Objetivos

### 2.1. Objetivo geral

Desenvolver um banco de dados relacional para armazenar, organizar e analisar informações sobre a infraestrutura das escolas públicas de Pernambuco.

### 2.2. Objetivos específicos

- Obter dados oficiais do Censo Escolar 2024.
- Explorar e tratar os dados utilizando Python e pandas.
- Identificar as entidades e seus relacionamentos.
- Modelar e implementar o banco de dados no PostgreSQL.
- Importar os registros das escolas públicas.
- Desenvolver consultas SQL para analisar a infraestrutura escolar.
- Investigar a disponibilidade de recursos educacionais, com destaque para o município de Verdejante.


## 3. Fonte dos Dados

### 3.1. Origem dos dados

Os dados utilizados no EducaPE foram obtidos do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), por meio dos microdados do Censo Escolar da Educação Básica de 2024.

O Censo Escolar reúne informações sobre instituições de ensino, matrículas, profissionais e infraestrutura escolar.

### 3.2. Forma de obtenção

Os dados foram obtidos por download no portal oficial do INEP, em formato CSV (Comma-Separated Values).

O arquivo original utilizado foi:

`microdados_ed_basica_2024.csv`

Após o tratamento, foi gerado o arquivo:

`escolas_pe_2024.csv`

### 3.3. Organização dos arquivos

Os arquivos estão organizados nas seguintes pastas:

- `dados_originais/`: contém o arquivo original do INEP.
- `dados_tratados/`: contém os dados filtrados de Pernambuco.
- `analise_py/`: contém os códigos Python utilizados na exploração dos dados.

### 3.4. Características da base

Na exploração inicial, foram identificados:

- 9.936 registros de escolas em Pernambuco.
- 426 colunas no arquivo analisado.
- 185 localidades identificadas, incluindo Fernando de Noronha.

Posteriormente, foram selecionadas 6.835 escolas públicas para importação no PostgreSQL.


## 4. Tecnologias Utilizadas

O desenvolvimento do EducaPE utiliza ferramentas para exploração, tratamento, armazenamento e consulta dos dados.

### 4.1. Python

Linguagem de programação utilizada para realizar a leitura, o tratamento e a importação dos dados do Censo Escolar.

### 4.2. Pandas

Biblioteca Python utilizada para manipular os arquivos CSV, selecionar colunas, filtrar registros e analisar os dados escolares.

### 4.3. PostgreSQL

Sistema Gerenciador de Banco de Dados Relacional (SGBD) utilizado para armazenar as informações das escolas públicas de Pernambuco.

### 4.4. pgAdmin 4

Ferramenta gráfica utilizada para administrar o PostgreSQL, executar consultas SQL e verificar os registros armazenados.

### 4.5. Cursor

Editor de código utilizado para desenvolver os scripts Python e SQL e organizar os arquivos do projeto.

### 4.6. Git e GitHub

Ferramentas utilizadas para controlar as versões do projeto e armazenar os códigos e a documentação em um repositório remoto.


## 5. Exploração e Tratamento dos Dados

### 5.1. Leitura dos arquivos

Os dados do Censo Escolar 2024 foram analisados utilizando Python e a biblioteca pandas.

O arquivo CSV foi lido utilizando ponto e vírgula (`;`) como separador e a codificação `utf-8-sig`.

### 5.2. Seleção dos dados de Pernambuco

A partir dos microdados nacionais do INEP, foi criado o arquivo `escolas_pe_2024.csv`, contendo os registros das escolas de Pernambuco.

Na exploração inicial, foram identificadas 9.936 escolas e 426 colunas.

### 5.3. Filtragem das escolas públicas

Para a importação no PostgreSQL, foram selecionadas as escolas com os seguintes códigos de dependência administrativa:

- 1 — Federal
- 2 — Estadual
- 3 — Municipal

A filtragem foi realizada utilizando a coluna `TP_DEPENDENCIA`.

Após essa seleção, foram identificadas 6.835 escolas públicas.

### 5.4. Seleção das informações

Foram selecionados os campos necessários para a identificação das escolas, dos municípios e dos indicadores de infraestrutura.

Entre os indicadores utilizados estão:

- Disponibilidade de água potável.
- Abastecimento de água pela rede pública.
- Energia elétrica da rede pública.
- Acesso à internet.
- Internet disponível para os alunos.
- Existência de bibliotecas.
- Laboratórios de informática.
- Laboratórios de ciências.

### 5.5. Tratamento de valores ausentes

Durante a exploração, foram identificados campos sem informação.

Esses valores foram preservados como `NULL` no PostgreSQL, permitindo diferenciá-los dos registros que indicam ausência de determinado recurso.

### 5.6. Resultado do processamento

Após a preparação e importação, o banco de dados passou a armazenar:

- 185 localidades.
- 6.835 escolas públicas.
- 6.835 registros de infraestrutura.


## 6. Modelagem do Banco de Dados

### 6.1. Modelo relacional

O banco de dados EducaPE foi desenvolvido no PostgreSQL e organizado em três tabelas relacionadas: `municipios`, `escolas` e `infraestrutura`.

Essa estrutura permite armazenar os dados de maneira organizada e realizar consultas sobre as condições das escolas públicas de Pernambuco.

### 6.2. Entidades do banco de dados

**Tabela municipios**

Armazena o código e o nome dos municípios presentes na base de dados.

- Chave primária (PK): `co_municipio`

**Tabela escolas**

Armazena a identificação das escolas públicas e o município ao qual cada escola pertence.

- Chave primária (PK): `co_entidade`
- Chave estrangeira (FK): `co_municipio`

**Tabela infraestrutura**

Armazena os indicadores de infraestrutura das escolas, como internet, água potável, energia elétrica, bibliotecas e laboratórios.

- Chave primária (PK): `co_entidade`
- Chave estrangeira (FK): `co_entidade`

### 6.3. Relacionamentos

**Municípios e escolas — 1:N**

Um município pode possuir várias escolas, mas cada escola está vinculada a um único município.

**Escolas e infraestrutura — 1:1**

Cada escola possui um registro correspondente na tabela de infraestrutura.

O relacionamento é realizado pelo campo `co_entidade`.

### 6.4. Diagrama Entidade-Relacionamento

O diagrama representa visualmente as entidades, seus atributos e os relacionamentos existentes no banco de dados.

O arquivo do diagrama está disponível em:

`banco_de_dados/diagramas/`

### 6.5. Dicionário de Dados

A descrição dos campos, tipos de dados e restrições das tabelas está documentada no arquivo:

`banco_de_dados/04_dicionario_dados.md`


## 7. Implementação do Banco de Dados

### 7.1. Criação do banco

O banco de dados `educape` foi criado no PostgreSQL para armazenar as informações das escolas públicas de Pernambuco.

A administração do banco e a execução das consultas SQL foram realizadas utilizando o pgAdmin 4.

### 7.2. Criação das tabelas

Foram criadas três tabelas:

- `municipios`
- `escolas`
- `infraestrutura`

A criação das tabelas foi realizada por meio de comandos SQL, utilizando chaves primárias (PK) e estrangeiras (FK) para estabelecer os relacionamentos.

O script está disponível em:

`banco_de_dados/01_criar_tabelas.sql`

### 7.3. Importação dos dados

A importação foi realizada utilizando Python, pandas e psycopg2.

O script lê o arquivo CSV tratado, seleciona as escolas públicas e insere os registros nas tabelas do PostgreSQL.

O código está disponível em:

`banco_de_dados/02_importar_dados.py`

### 7.4. Dados armazenados

Após a importação, foram registrados:

| Tabela | Quantidade de registros |
|---|---:|
| municipios | 185 |
| escolas | 6.835 |
| infraestrutura | 6.835 |

### 7.5. Integridade referencial

A integridade referencial é mantida por meio das chaves estrangeiras.

A tabela `escolas` referencia `municipios` pelo campo `co_municipio`.

A tabela `infraestrutura` referencia `escolas` pelo campo `co_entidade`.

Esses relacionamentos ajudam a evitar registros associados a municípios ou escolas inexistentes.


## 8. Consultas SQL e Análise dos Resultados

### 8.1. Objetivo das consultas

As consultas SQL foram desenvolvidas para analisar as informações armazenadas no PostgreSQL, permitindo identificar a disponibilidade de recursos nas escolas públicas de Pernambuco.

As consultas estão disponíveis no arquivo:

`banco_de_dados/03_consultas.sql`

### 8.2. Quantidade de escolas públicas

A consulta de contagem identificou 6.835 escolas públicas cadastradas no banco de dados.

### 8.3. Disponibilidade de internet

A análise da disponibilidade de internet apresentou:

| Indicador | Quantidade |
|---|---:|
| Total de escolas | 6.835 |
| Com internet | 5.391 |
| Sem internet | 451 |
| Sem informação | 993 |

### 8.4. Internet disponível para os alunos

A consulta sobre o acesso dos alunos à internet apresentou:

| Indicador | Quantidade |
|---|---:|
| Total de escolas | 6.835 |
| Com acesso para alunos | 2.221 |
| Sem acesso para alunos | 3.621 |
| Sem informação | 993 |

### 8.5. Análise do município de Verdejante

Foi realizada uma consulta específica para analisar a infraestrutura das escolas públicas do município de Verdejante, identificado pelo código `2616100`.

Os resultados foram:

| Indicador | Quantidade |
|---|---:|
| Escolas públicas | 12 |
| Escolas com internet | 11 |
| Escolas com água potável | 12 |
| Escolas com biblioteca | 3 |

### 8.6. Interpretação dos resultados

Os resultados demonstram que a disponibilidade de internet nas escolas não significa necessariamente que os alunos tenham acesso a esse recurso.

Em Verdejante, 11 das 12 escolas registram disponibilidade de internet, enquanto apenas 3 possuem biblioteca.

Essas informações permitem identificar diferenças na disponibilidade de recursos educacionais e contribuem para a análise da infraestrutura escolar.


## 9. Requisitos do Projeto

### 9.1. Requisitos Funcionais

Os requisitos funcionais descrevem as funcionalidades previstas para o EducaPE.

| Código | Descrição |
|---|---|
| RF001 | Permitir consultar as escolas públicas cadastradas. |
| RF002 | Permitir consultar escolas por município. |
| RF003 | Permitir consultar a disponibilidade de internet nas escolas. |
| RF004 | Permitir consultar informações sobre água, energia, bibliotecas e laboratórios. |
| RF005 | Permitir gerar resultados quantitativos sobre a infraestrutura escolar. |

### 9.2. Requisitos Não Funcionais

Os requisitos não funcionais descrevem características técnicas e de qualidade esperadas para o projeto.

| Código | Descrição |
|---|---|
| RNF001 | Utilizar PostgreSQL para armazenar os dados. |
| RNF002 | Utilizar chaves primárias e estrangeiras para garantir a integridade referencial. |
| RNF003 | Proteger as credenciais de acesso ao banco por meio de variáveis de ambiente. |
| RNF004 | Manter os scripts e documentos organizados em pastas específicas. |
| RNF005 | Apresentar desempenho adequado nas consultas SQL. |

### 9.3. Situação da Implementação

O EducaPE possui um banco de dados PostgreSQL implementado, com dados reais importados e consultas SQL para análise da infraestrutura escolar.

As funcionalidades de consulta são realizadas diretamente no banco de dados.

O desenvolvimento de uma interface gráfica e de uma API ainda não faz parte da implementação atual.

O requisito de desempenho deverá ser validado por meio de testes específicos.


## 10. Conclusão

O desenvolvimento do EducaPE permitiu aplicar conhecimentos de Banco de Dados I na organização e análise de dados reais da educação pública de Pernambuco.

A partir dos microdados do Censo Escolar 2024, disponibilizados pelo INEP, foi possível explorar, tratar e importar informações de 6.835 escolas públicas para um banco de dados relacional PostgreSQL.

A implementação das tabelas, dos relacionamentos e das consultas SQL possibilitou analisar indicadores de infraestrutura escolar, como acesso à internet, água potável e disponibilidade de bibliotecas.

A análise específica do município de Verdejante demonstrou a aplicação prática do banco de dados na identificação de recursos disponíveis nas escolas.

O projeto também contribuiu para o desenvolvimento de conhecimentos sobre modelagem de dados, integridade referencial, tratamento de arquivos CSV e consultas SQL.

## 11. Limitações e Possíveis Melhorias

### 11.1. Limitações

- Os dados utilizados correspondem ao Censo Escolar de 2024.
- Algumas informações apresentam valores ausentes.
- O banco contempla apenas uma seleção dos indicadores disponíveis na base original.
- As consultas são realizadas diretamente no PostgreSQL, sem uma interface gráfica.
- Ainda não foram realizados testes específicos de desempenho.

### 11.2. Possíveis Melhorias

- Ampliar a quantidade de indicadores analisados.
- Incorporar dados de outros anos para permitir comparações.
- Desenvolver visualizações gráficas dos resultados.
- Criar uma interface para facilitar as consultas.
- Implementar uma API para disponibilizar os dados do projeto.
