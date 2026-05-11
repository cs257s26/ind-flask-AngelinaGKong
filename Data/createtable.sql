DROP TABLE IF EXISTS water_country_cleaned_again_again;
CREATE TABLE water_country_cleaned_again_again (
    country TEXT,
    year_n REAL,
    population_n REAL,
    urban_percent REAL,
    basic_percent REAL,
    limited REAL,
    unimproved REAL,
    safely_managed REAL,
    accessible REAL,
    available REAL,
    no_contamination REAL,
    piped REAL,
    not_piped REAL
);

DROP TABLE IF EXISTS water_region;
CREATE TABLE water_region (
    country TEXT,
    year_n REAL,
    population_n REAL,
    urban_percent REAL,
    basic_percent REAL,
    limited REAL,
    unimproved REAL,
    safely_managed REAL,
    accessible REAL,
    available REAL,
    no_contamination REAL,
    piped REAL,
    not_piped REAL
);