-- Criação da tabela somente se não existir
CREATE TABLE IF NOT EXISTS covid_stats (
    id SERIAL PRIMARY KEY,
    code VARCHAR(100),
    country VARCHAR(100),
    continent VARCHAR(100),
    date DATE,
    new_cases INT,
    new_deaths INT,
    population INT,
    cases_per_100k FLOAT,
    deaths_per_100k FLOAT
);
