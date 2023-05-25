BEGIN;
CREATE TABLE IF NOT EXISTS Player (email TEXT PRIMARY KEY, fname TEXT NOT NULL, lname TEXT NOT NULL, phonenum TEXT, address TEXT);
CREATE TABLE IF NOT EXISTS Host (email TEXT PRIMARY KEY, fname TEXT NOT NULL, lname TEXT NOT NULL, phonenum INT, address TEXT);
CREATE TABLE IF NOT EXISTS Tournament (name TEXT PRIMARY KEY, email TEXT, phonenum TEXT, address TEXT, url TEXT, date TEXT, game TEXT, host_email TEXT,
    FOREIGN KEY (host_email) REFERENCES Host(email) ON DELETE CASCADE);
CREATE TABLE IF NOT EXISTS PlayerTournament (player_email TEXT, tournament_name TEXT,
    FOREIGN KEY(tournament_name) REFERENCES Tournament(name) ON DELETE CASCADE,
    FOREIGN KEY (player_email) REFERENCES Player(email) ON DELETE CASCADE,
    PRIMARY KEY (tournament_name, player_email));
COMMIT;
