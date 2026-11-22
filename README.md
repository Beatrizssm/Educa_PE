Aqui está o **README completo e atualizado do EducaPE**, com os nomes de Maria Beatriz e Edcalos França, a informação de que vocês realizaram todas as atividades juntos e as reuniões presenciais às segundas e quartas-feiras, sem mencionar WhatsApp.

Você pode copiar o conteúdo abaixo e substituir o texto do seu `README.md` no Cursor.

# EducaPE — Análise da Infraestrutura das Escolas Públicas em Pernambuco

## 1. Apresentação do projeto

O **EducaPE** é um projeto acadêmico desenvolvido na disciplina de Banco de Dados I, do curso de Análise e Desenvolvimento de Sistemas (ADS), da Autarquia de Ensino Superior de Arcoverde (AESA).

O projeto tem como objetivo organizar, explorar e analisar informações relacionadas à infraestrutura das escolas públicas de Pernambuco, utilizando dados oficiais do Censo Escolar da Educação Básica 2024, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

A pesquisa busca compreender como os recursos e serviços escolares estão distribuídos entre as localidades pernambucanas, identificando possíveis desigualdades nas condições de infraestrutura.

Entre os aspectos investigados estão o abastecimento de água, o fornecimento de energia elétrica, o acesso à internet, a disponibilidade de bibliotecas e a existência de laboratórios.

Nesta primeira fase, denominada **Descoberta**, o trabalho concentra-se na obtenção, organização e análise exploratória dos dados, estabelecendo uma base para as próximas etapas de desenvolvimento do banco de dados.

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

| Tecnologia | Aplicação                                                  |
| ---------- | ---------------------------------------------------------- |
| Python     | Processamento e análise exploratória dos dados             |
| Pandas     | Leitura, filtragem, agrupamento e contagem das informações |
| CSV        | Formato dos arquivos de dados originais e tratados         |
| Cursor     | Ambiente de desenvolvimento e execução do código           |
| Markdown   | Documentação do projeto                                    |

O projeto encontra-se na Fase 01. Nesta etapa, ainda não foram implementados frontend, backend, API ou banco de dados relacional.

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

```
EducaPE/
│
├── dados_originais/
│   └── microdados_ed_basica_2024.csv
│
├── dados_tratados/
│   └── escolas_pe_2024.csv
│
├── analise.py
│
└── README.md
```

### Responsabilidade de cada arquivo

**dados_originais/**

Contém o arquivo original do Censo Escolar 2024, preservando os dados disponibilizados pelo INEP.

**dados_tratados/**

Armazena o arquivo CSV com os registros das escolas de Pernambuco, obtidos após a filtragem por unidade federativa.

O arquivo contém escolas de diferentes dependências administrativas. A seleção das escolas públicas é realizada posteriormente pelo código Python.

**analise.py**

Script Python responsável pela exploração inicial dos dados, incluindo contagens, agrupamentos, filtragens e análise dos indicadores de infraestrutura.

**README.md**

Documentação do projeto, contendo objetivos, fonte dos dados, organização, metodologia, resultados e instruções de execução.

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

A partir da estrutura dos dados, foram identificadas duas entidades principais.

### Município

Representa a localidade onde as escolas estão situadas.

Atributos preliminares:

- Código do município.
- Nome do município.

### Escola

Representa a instituição de ensino.

Atributos preliminares:

- Código da escola.
- Nome da escola.
- Município.
- Dependência administrativa.
- Indicadores de infraestrutura.

### Relacionamento inicial

Um município pode possuir várias escolas, enquanto cada escola está associada a uma localidade na base analisada.

**Município (1) — (N) Escola**

Esse relacionamento será detalhado na etapa de modelagem conceitual.

## 12. Subtemas considerados

Durante a definição do projeto, foram considerados três possíveis subtemas:

**1. Abastecimento de água nas escolas públicas**

Investigação da disponibilidade de água potável e das diferentes fontes de abastecimento.

**2. Acesso à tecnologia e à internet**

Análise da disponibilidade de conexão, acesso dos alunos e laboratórios de informática.

**3. Infraestrutura física e acessibilidade**

Investigação dos espaços e recursos escolares, incluindo bibliotecas, laboratórios e condições de acessibilidade.

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

## 14. Instalação e configuração

### Pré-requisitos

- Python 3 instalado.
- Biblioteca Pandas.
- Arquivo CSV tratado disponível na pasta correspondente.

### Instalar a biblioteca necessária

No terminal, execute:

```
pip install pandas
```

### Estrutura necessária

Antes da execução, confira se o arquivo `escolas_pe_2024.csv` está dentro da pasta `dados_tratados`.

## 15. Executando a análise

Abra o projeto EducaPE no Cursor ou em outro editor compatível com Python.

No terminal, a partir da pasta principal do projeto, execute:

```
python analise.py
```

O script apresentará no terminal:

- Informações iniciais sobre os dados.
- Quantidade de escolas e localidades.
- Distribuição das escolas por município.
- Quantidade de escolas públicas.
- Resultados dos indicadores de água.
- Identificação das variáveis de infraestrutura.
- Resultados de energia, internet, bibliotecas e laboratórios.

A análise atual é realizada por linha de comando, sem interface gráfica.

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

A equipe do projeto EducaPE, formada por **Maria Beatriz e Edcalos França**, realiza reuniões presenciais todas as segundas e quartas-feiras, na faculdade.

Durante esses encontros, os integrantes discutem o andamento do projeto, compartilham os resultados das análises, esclarecem dúvidas e definem as próximas atividades.

O desenvolvimento é realizado de forma colaborativa, com participação de ambos os integrantes em todas as etapas.

### Registro das reuniões

As reuniões presenciais são utilizadas para acompanhar o desenvolvimento do projeto e organizar as atividades da Fase 01.

As datas específicas, os assuntos discutidos e as decisões tomadas serão registrados conforme os encontros efetivamente realizados.

**Registro pendente:** inserir as datas e decisões reais das reuniões realizadas pela equipe.

## 18. Utilização de inteligência artificial

A inteligência artificial foi utilizada como ferramenta de apoio durante o desenvolvimento do projeto, auxiliando na organização das atividades, elaboração e revisão do código Python, interpretação dos resultados e estruturação da documentação.

O código foi executado e testado durante o desenvolvimento.

**Link público da conversa utilizada:** PENDENTE DE INSERÇÃO.

## 19. Próximas etapas

Após a conclusão da Fase 01, o projeto poderá avançar para:

- Levantamento e formalização dos requisitos.
- Definição do escopo do banco de dados.
- Elaboração do Diagrama Entidade-Relacionamento (DER).
- Desenvolvimento do modelo lógico relacional.
- Definição de chaves primárias e estrangeiras.
- Estruturação das tabelas.
- Implementação do banco de dados, conforme as próximas orientações da disciplina.
- Desenvolvimento de consultas para responder às perguntas de pesquisa.

Essas atividades ainda não fazem parte da implementação concluída nesta fase.

## 20. Considerações finais

A primeira etapa do EducaPE permitiu conhecer a estrutura dos microdados do Censo Escolar 2024 e identificar informações relevantes sobre as condições de infraestrutura das escolas públicas de Pernambuco.

A análise preliminar revelou diferenças na disponibilidade de recursos, especialmente no acesso dos alunos à internet, na presença de bibliotecas e na existência de laboratórios.

Os resultados também evidenciaram a importância de tratar adequadamente os registros sem informação e de considerar as características de cada localidade.

O projeto estabelece uma base inicial para as próximas etapas de levantamento de requisitos e modelagem de banco de dados, contribuindo para a aplicação prática dos conhecimentos da disciplina.

## 21. Autores

**Projeto:** EducaPE — Análise da Infraestrutura das Escolas Públicas em Pernambuco

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

**Instituição:** Autarquia de Ensino Superior de Arcoverde (AESA)

**Disciplina:** Banco de Dados I

**Integrantes:**

- Maria Beatriz
- Edcalos França

---

**EducaPE — Dados educacionais para compreender a infraestrutura das escolas públicas de Pernambuco.**

