/*

This is a sample query, used for testing, that attempts to register a new player for a tournament.

Authors: Jaren Alexander, Yankun Chen, Brett Fox, Kevin Truong, Sam Windheim

Group Name: TournamentsEZ

Last Modification Date: 6/9/2023

*/

-- SQLite
-- Registering a user for a tournament
INSERT INTO Player (email, fname, lname, phonenum, address)
VALUES ("bobj@sampletext.com", "Bob", "Jones", "1112224444", "123 Bobby Street, Nowheresville NM");

INSERT INTO PlayerTournament (player_email, tournament_name)
VALUES ("bobj@sampletext.com", "Super Smash Showdown");
