-- SQLite
-- Registering a user for a tournament
INSERT INTO Player (email, fname, lname, phonenum, address)
VALUES ("bobj@sampletext.com", "Bob", "Jones", "1112224444", "123 Bobby Street, Nowheresville NM");

INSERT INTO PlayerTournament (player_email, tournament_name)
VALUES ("bobj@sampletext.com", "Super Smash Showdown");
