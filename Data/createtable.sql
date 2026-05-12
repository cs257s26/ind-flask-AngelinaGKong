DROP TABLE IF EXISTS water_country;
CREATE TABLE water_country (
    country TEXT,
    year_n INT,
    population_n INT,
    urban_percent REAL,
    basic_percent REAL,
    limited INT,
    unimproved INT,
    safely_managed INT,
    accessible INT,
    available INT,
    no_contamination INT,
    piped INT,
    not_piped INT
);

DROP TABLE IF EXISTS water_region;
CREATE TABLE water_region (
    country TEXT,
    year_n INT,
    population_n INT,
    urban_percent REAL,
    basic_percent REAL,
    limited INT,
    unimproved INT,
    safely_managed INT,
    accessible INT,
    available INT,
    no_contamination INT,
    piped INT,
    not_piped INT
);
