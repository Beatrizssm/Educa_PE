
# Dicionário de Dados — EducaPE

## 1. Tabela: municipios

**Descrição:** Armazena os municípios de Pernambuco presentes na base de dados do projeto.

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| co_municipio | INTEGER | PK | Código de identificação do município no INEP. |
| no_municipio | VARCHAR(150) | NOT NULL | Nome do município. |


## 2. Tabela: escolas

**Descrição:** Armazena as informações de identificação das escolas públicas de Pernambuco.

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| co_entidade | INTEGER | PK | Código único de identificação da escola no INEP. |
| no_entidade | VARCHAR(255) | NOT NULL | Nome da escola. |
| co_municipio | INTEGER | FK, NOT NULL | Código do município onde a escola está localizada. |
| tp_dependencia | INTEGER | — | Código da dependência administrativa da escola. |


## 3. Tabela: infraestrutura

**Descrição:** Armazena informações sobre os recursos e serviços disponíveis nas escolas públicas de Pernambuco.

| Campo | Tipo | Restrição | Descrição |
|---|---|---|---|
| co_entidade | INTEGER | PK, FK | Código da escola à qual pertencem os dados de infraestrutura. |
| in_agua_potavel | INTEGER | — | Indica se a escola possui água potável. |
| in_agua_rede_publica | INTEGER | — | Indica se a escola recebe água da rede pública. |
| in_energia_rede_publica | INTEGER | — | Indica se a escola possui energia elétrica da rede pública. |
| in_internet | INTEGER | — | Indica se a escola possui internet. |
| in_internet_alunos | INTEGER | — | Indica se a escola disponibiliza internet para os alunos. |
| in_biblioteca | INTEGER | — | Indica se a escola possui biblioteca. |
| in_laboratorio_informatica | INTEGER | — | Indica se a escola possui laboratório de informática. |
| in_laboratorio_ciencias | INTEGER | — | Indica se a escola possui laboratório de ciências. |

### Interpretação dos indicadores

Para os campos que começam com `in_`:

- **1:** Sim.
- **0:** Não.
- **NULL:** Informação ausente ou não aplicável, conforme a base original.

### Relacionamento

O campo `co_entidade` funciona como chave primária (PK) e chave estrangeira (FK).

Ele identifica o registro de infraestrutura e o relaciona à escola correspondente na tabela `escolas`.
