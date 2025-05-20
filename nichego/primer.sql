--
-- File generated with SQLiteStudio v3.4.4 on Вс май 18 17:00:51 2025
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: gay_clubs
CREATE TABLE IF NOT EXISTS gay_clubs (pk INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);

-- Table: porno
CREATE TABLE IF NOT EXISTS porno (pk INTEGER PRIMARY KEY AUTOINCREMENT, pidor TEXT, gay_club REFERENCES gay_clubs (pk));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
