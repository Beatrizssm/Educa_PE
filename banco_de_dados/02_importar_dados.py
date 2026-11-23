
# EducaPE — Importação dos dados
# Código desenvolvido com auxílio de IA (ChatGPT).

import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv

# Carrega as configurações do arquivo .env
load_dotenv(override=True)



# Conecta ao banco de dados PostgreSQL
try:
    conexao = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    print("Conexão com o EducaPE realizada com sucesso!")
    conexao.close()

except Exception as erro:
    print("Erro ao conectar ao PostgreSQL:")
    print(erro)


# Lê os dados tratados do Censo Escolar 2024
arquivo = "dados_tratados/escolas_pe_2024.csv"

dados = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig",
    low_memory=False
)

# Seleciona apenas as escolas públicas:
# 1 = Federal, 2 = Estadual, 3 = Municipal
escolas_publicas = dados[
    dados["TP_DEPENDENCIA"].isin([1, 2, 3])
].copy()
# Seleciona as informações necessárias das escolas públicas
escolas = escolas_publicas[
    [
        "CO_ENTIDADE",
        "NO_ENTIDADE",
        "CO_MUNICIPIO",
        "TP_DEPENDENCIA"
    ]
].drop_duplicates(subset=["CO_ENTIDADE"])

print("Escolas preparadas para importação:", len(escolas))

# Lê os dados tratados do Censo Escolar 2024
arquivo = "dados_tratados/escolas_pe_2024.csv"

dados = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig",
    low_memory=False
)

# Seleciona apenas as escolas públicas:
# 1 = Federal, 2 = Estadual, 3 = Municipal
escolas_publicas = dados[
    dados["TP_DEPENDENCIA"].isin([1, 2, 3])
].copy()

print("Total de escolas públicas:", len(escolas_publicas))


# Seleciona o código e o nome dos municípios
municipios = escolas_publicas[
    ["CO_MUNICIPIO", "NO_MUNICIPIO"]
].drop_duplicates(subset=["CO_MUNICIPIO"])

# Organiza os municípios pelo nome
municipios = municipios.sort_values("NO_MUNICIPIO")

print("Municípios encontrado:", len(municipios))
# Conecta ao PostgreSQL para importar as escolas
with psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
) as conexao:

    with conexao.cursor() as cursor:

        for _, escola in escolas.iterrows():
            cursor.execute(
                """
                INSERT INTO escolas (
                    co_entidade,
                    no_entidade,
                    co_municipio,
                    tp_dependencia
                )
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (co_entidade) DO NOTHING;
                """,
                (
                    int(escola["CO_ENTIDADE"]),
                    escola["NO_ENTIDADE"],
                    int(escola["CO_MUNICIPIO"]),
                    int(escola["TP_DEPENDENCIA"])
                )
            )

    conexao.commit()

print("Escolas importadas com sucesso!")

print(municipios.head())


# Seleciona os dados de infraestrutura das escolas públicas
colunas_infraestrutura = [
    "CO_ENTIDADE",
    "IN_AGUA_POTAVEL",
    "IN_AGUA_REDE_PUBLICA",
    "IN_ENERGIA_REDE_PUBLICA",
    "IN_INTERNET",
    "IN_INTERNET_ALUNOS",
    "IN_BIBLIOTECA",
    "IN_LABORATORIO_INFORMATICA",
    "IN_LABORATORIO_CIENCIAS"
]

infraestrutura = escolas_publicas[
    colunas_infraestrutura
].drop_duplicates(subset=["CO_ENTIDADE"]).copy()

print(
    "Registros de infraestrutura preparados:",
    len(infraestrutura)
)

print(infraestrutura.head())


# Importa os dados de infraestrutura para o PostgreSQL
with psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
) as conexao:

    with conexao.cursor() as cursor:

        for registro in infraestrutura.itertuples(index=False, name=None):

            # Converte valores ausentes (NaN) para NULL
            valores = [
                None if pd.isna(valor) else int(valor)
                for valor in registro
            ]

            cursor.execute(
                """
                INSERT INTO infraestrutura (
                    co_entidade,
                    in_agua_potavel,
                    in_agua_rede_publica,
                    in_energia_rede_publica,
                    in_internet,
                    in_internet_alunos,
                    in_biblioteca,
                    in_laboratorio_informatica,
                    in_laboratorio_ciencias
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (co_entidade) DO NOTHING;
                """,
                valores
            )

    conexao.commit()

print("Infraestrutura importada com sucesso!")
