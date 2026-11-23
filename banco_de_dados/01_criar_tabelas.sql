
CREATE TABLE municipios (
    co_municipio INTEGER PRIMARY KEY,
    no_municipio VARCHAR(150) NOT NULL
);


CREATE TABLE escolas (
    co_entidade INTEGER PRIMARY KEY,
    no_entidade VARCHAR(255) NOT NULL,
    co_municipio INTEGER NOT NULL,
    tp_dependencia INTEGER,

    FOREIGN KEY (co_municipio)
        REFERENCES municipios(co_municipio)
);



CREATE TABLE infraestrutura (
    co_entidade INTEGER PRIMARY KEY,

    in_agua_potavel INTEGER,
    in_agua_rede_publica INTEGER,
    in_energia_rede_publica INTEGER,
    in_internet INTEGER,
    in_internet_alunos INTEGER,
    in_biblioteca INTEGER,
    in_laboratorio_informatica INTEGER,
    in_laboratorio_ciencias INTEGER,

    FOREIGN KEY (co_entidade)
        REFERENCES escolas(co_entidade)
);
