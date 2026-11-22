
# PROJETO EDUCAPЕ
# Análise da Infraestrutura das Escolas Públicas em Pernambuco
# Fonte: Censo Escolar 2024 - INEP
# UTILIZÇÃO DE INTELIGÊNCIA ARTIFICIAL
# A IA foi utilizada como ferramenta de apoio durante o desenvolvimento do projeto,
#auxiliando na organização e revisão de erros e do códigco Python.
# Link público da conversa: 

import pandas as pd

# 1. CARREGAMENTO DOS DADOS
# Abre o arquivo CSV com os dados das escolas de Pernambuco.

arquivo = "dados_tratados/escolas_pe_2024.csv"

dados = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\n===== INFORMAÇÕES INICIAIS =====")
print(dados.head())
print("Quantidade de colunas:", len(dados.columns))


# 2. IDENTIFICAÇÃO DAS ESCOLAS E MUNICÍPIOS
# Conta escolas e localidades presentes na base.

print("\nEscolas identificadas:", dados["CO_ENTIDADE"].nunique())
print("Localidades encontradas:", dados["CO_MUNICIPIO"].nunique())

municipios = dados[
    ["CO_MUNICIPIO", "NO_MUNICIPIO"]
].drop_duplicates()

print("\nRelação de municípios e códigos:")
print(municipios.sort_values("NO_MUNICIPIO").to_string(index=False))

print("\nMunicípios sem código:", dados["CO_MUNICIPIO"].isna().sum())
print("Municípios sem nome:", dados["NO_MUNICIPIO"].isna().sum())


# 3. QUANTIDADE DE ESCOLAS POR MUNICÍPIO
# Identifica a distribuição das escolas nas localidades.

escolas_por_municipio = (
    dados.groupby("NO_MUNICIPIO")["CO_ENTIDADE"]
    .nunique()
    .sort_values(ascending=False)
)

print("\n===== ESCOLAS POR MUNICÍPIO =====")
print(escolas_por_municipio.to_string())


# 4. SEPARAÇÃO DAS ESCOLAS PÚBLICAS
# Dependência 1: Federal
# Dependência 2: Estadual
# Dependência 3: Municipal

dados_publicos = dados[
    dados["TP_DEPENDENCIA"].isin([1, 2, 3])
].copy()

print("\n===== ESCOLAS PÚBLICAS =====")
print(
    "Total de escolas públicas:",
    dados_publicos["CO_ENTIDADE"].nunique()
)


# 5. ANÁLISE DO ABASTECIMENTO DE ÁGUA
# Verifica as condições de abastecimento de água.

colunas_agua = [
    "IN_AGUA_POTAVEL",
    "IN_AGUA_REDE_PUBLICA",
    "IN_AGUA_POCO_ARTESIANO",
    "IN_AGUA_CACIMBA",
    "IN_AGUA_FONTE_RIO",
    "IN_AGUA_CARRO_PIPA",
    "IN_AGUA_INEXISTENTE"
]

print("\n===== ANÁLISE DA ÁGUA =====")

for coluna in colunas_agua:
    valores = dados_publicos[coluna]
    validos = valores.dropna()

    print(f"\n{coluna}")
    print("Sim:", (validos == 1).sum())
    print("Não:", (validos == 0).sum())
    print("Sem informação:", valores.isna().sum())


# 6. IDENTIFICAÇÃO DAS VARIÁVEIS DE INFRAESTRUTURA
# Localiza colunas relacionadas a energia, internet,
# bibliotecas e laboratórios.

termos = [
    "ENERGIA",
    "INTERNET",
    "BIBLIOTECA",
    "LABORATORIO"
]

print("\n===== VARIÁVEIS DE INFRAESTRUTURA =====")

for termo in termos:
    print(f"\n{termo}:")
    print([
        coluna
        for coluna in dados_publicos.columns
        if termo in coluna
    ])


# 7. ANÁLISE DE ENERGIA, INTERNET, BIBLIOTECAS
# E LABORATÓRIOS
# Conta respostas positivas, negativas e sem informação.

grupos = {
    "ENERGIA": [
        "IN_ENERGIA_REDE_PUBLICA",
        "IN_ENERGIA_GERADOR_FOSSIL",
        "IN_ENERGIA_RENOVAVEL",
        "IN_ENERGIA_INEXISTENTE"
    ],

    "INTERNET": [
        "IN_INTERNET",
        "IN_INTERNET_ALUNOS",
        "IN_INTERNET_ADMINISTRATIVO",
        "IN_INTERNET_APRENDIZAGEM",
        "IN_INTERNET_COMUNIDADE"
    ],

    "BIBLIOTECAS": [
        "IN_BIBLIOTECA",
        "IN_BIBLIOTECA_SALA_LEITURA"
    ],

    "LABORATORIOS": [
        "IN_LABORATORIO_CIENCIAS",
        "IN_LABORATORIO_INFORMATICA",
        "IN_LABORATORIO_EDUC_PROF"
    ]
}

for grupo, colunas in grupos.items():
    print(f"\n===== {grupo} =====")

    for coluna in colunas:
        valores = dados_publicos[coluna]
        validos = valores.dropna()

        print(f"\n{coluna}")
        print("Sim:", (validos == 1).sum())
        print("Não:", (validos == 0).sum())
        print("Sem informação:", valores.isna().sum())

# FIM DA ANÁLISE PRELIMINAR

