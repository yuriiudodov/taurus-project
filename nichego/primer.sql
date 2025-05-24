--
-- File generated with SQLiteStudio v3.4.4 on ѕт май 23 14:03:10 2025
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: animal_docs
CREATE TABLE IF NOT EXISTS animal_docs (pk INTEGER PRIMARY KEY ASC AUTOINCREMENT, animal_or_cattle INTEGER, animal REFERENCES animals_simple (pk), cattle REFERENCES cattle (pk), document TEXT);

-- Table: animals_simple
CREATE TABLE IF NOT EXISTS animals_simple (pk INTEGER PRIMARY KEY ASC AUTOINCREMENT, specie TEXT, count INTEGER, belongs_to_household REFERENCES household (pk) ON UPDATE CASCADE, timestamp TEXT);

-- Table: cattle
CREATE TABLE IF NOT EXISTS cattle (pk INTEGER PRIMARY KEY ASC AUTOINCREMENT, name TEXT, specie TEXT, inventory_num INTEGER UNIQUE ON CONFLICT ABORT, belongs_to_household REFERENCES household (pk) ON UPDATE CASCADE, timestamp TEXT);

-- Table: city
CREATE TABLE IF NOT EXISTS city (pk INTEGER PRIMARY KEY ASC AUTOINCREMENT, name TEXT, belongs_to_settlement INTEGER REFERENCES settlement (pk) ON DELETE CASCADE ON UPDATE CASCADE);

-- Table: household
CREATE TABLE IF NOT EXISTS household (pk INTEGER PRIMARY KEY ASC AUTOINCREMENT, owner TEXT, address TEXT, belongs_to_city INTEGER REFERENCES city (pk));

-- Table: report_entries
CREATE TABLE IF NOT EXISTS report_entries (pk INTEGER PRIMARY KEY ASC AUTOINCREMENT, belongs_to_report INTEGER REFERENCES reports (pk), household INTEGER REFERENCES household (pk), specie TEXT, count INTEGER, is_conditions_good TEXT, data_from_administration INTEGER, prevous_count INTEGER);

-- Table: reports
CREATE TABLE IF NOT EXISTS reports (pk INTEGER PRIMARY KEY ASC AUTOINCREMENT, datetime TEXT, city REFERENCES city (pk), file TEXT);

-- Table: settlement
CREATE TABLE IF NOT EXISTS settlement (pk INTEGER PRIMARY KEY ASC AUTOINCREMENT, name TEXT, belongs_to_vet_station REFERENCES vet_station (pk));

-- Table: vet_administration
CREATE TABLE IF NOT EXISTS vet_administration (pk INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, info TEXT, is_chosen INTEGER);

-- Table: vet_station
CREATE TABLE IF NOT EXISTS vet_station (pk INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, info TEXT, belongs_to_vet_administration REFERENCES vet_administration (pk), is_chosen INTEGER);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
