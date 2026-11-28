
-- Consulta 1: Quantidade de escolas públicas
SELECT COUNT(*) AS total_escolas
FROM escolas;

-- Consulta 2: Existência de internet nas escolas
SELECT
    COUNT(*) AS total_escolas,
    COUNT(*) FILTER (WHERE in_internet = 1) AS com_internet,
    COUNT(*) FILTER (WHERE in_internet = 0) AS sem_internet,
    COUNT(*) FILTER (WHERE in_internet IS NULL) AS sem_informacao
FROM infraestrutura;

-- Consulta 3: Internet disponível para alunos
SELECT
    COUNT(*) AS total_escolas,
    COUNT(*) FILTER (WHERE in_internet_alunos = 1) AS alunos_com_acesso,
    COUNT(*) FILTER (WHERE in_internet_alunos = 0) AS alunos_sem_acesso,
    COUNT(*) FILTER (WHERE in_internet_alunos IS NULL) AS sem_informacao
FROM infraestrutura;


-- Consulta 4: Infraestrutura das escolas públicas por município
SELECT
    m.no_municipio AS municipio,
    COUNT(e.co_entidade) AS total_escolas,
    COUNT(*) FILTER (WHERE i.in_internet = 1) AS com_internet,
    COUNT(*) FILTER (WHERE i.in_agua_potavel = 1) AS com_agua_potavel,
    COUNT(*) FILTER (WHERE i.in_biblioteca = 1) AS com_biblioteca
FROM municipios m
INNER JOIN escolas e
    ON m.co_municipio = e.co_municipio
LEFT JOIN infraestrutura i
    ON e.co_entidade = i.co_entidade
GROUP BY m.co_municipio, m.no_municipio
ORDER BY m.no_municipio;