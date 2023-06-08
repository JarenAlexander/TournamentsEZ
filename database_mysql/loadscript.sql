CREATE TABLE IF NOT EXISTS Player (email VARCHAR(254) PRIMARY KEY, fname TEXT NOT NULL, lname TEXT NOT NULL, phonenum TEXT, address TEXT);
CREATE TABLE IF NOT EXISTS Host (email VARCHAR(254) PRIMARY KEY, fname TEXT NOT NULL, lname TEXT NOT NULL, phonenum TEXT, address TEXT);
CREATE TABLE IF NOT EXISTS Tournament (name VARCHAR(300) PRIMARY KEY, email VARCHAR(254), phonenum TEXT, address TEXT, url TEXT, date TEXT, game TEXT, host_email VARCHAR(254),
    FOREIGN KEY (host_email) REFERENCES Host(email) ON DELETE CASCADE);
CREATE TABLE IF NOT EXISTS PlayerTournament (player_email VARCHAR(254), tournament_name VARCHAR(300),
    FOREIGN KEY(tournament_name) REFERENCES Tournament(name) ON DELETE CASCADE,
    FOREIGN KEY (player_email) REFERENCES Player(email) ON DELETE CASCADE,
    PRIMARY KEY (tournament_name, player_email));
