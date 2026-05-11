DROP TABLE IF EXISTS water_country_cleaned_again_again_with_utf8;
CREATE TABLE water_country_cleaned_again_again_with_utf8 (
    country TEXT,
    year_n TEXT,
    population_n TEXT,
    urban_percent TEXT,
    basic_percent TEXT,
    limited TEXT,
    unimproved TEXT,
    safely_managed TEXT,
    accessible TEXT,
    available TEXT,
    no_contamination TEXT,
    piped TEXT,
    not_piped TEXT
);

DROP TABLE IF EXISTS water_region;
CREATE TABLE water_region (
    country TEXT,
    year_n TEXT,
    population_n TEXT,
    urban_percent TEXT,
    basic_percent TEXT,
    limited TEXT,
    unimproved TEXT,
    safely_managed TEXT,
    accessible TEXT,
    available TEXT,
    no_contamination TEXT,
    piped TEXT,
    not_piped TEXT
);

DROP TABLE IF EXISTS water_country_cleaned_again_again_with_comma_dil;
