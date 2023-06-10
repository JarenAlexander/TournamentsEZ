/*

This is a sample query, used for testing, that checks which player has the email 'player9@example.com'

Authors: Jaren Alexander, Yankun Chen, Brett Fox, Kevin Truong, Sam Windheim

Group Name: TournamentsEZ

Last Modification Date: 6/9/2023

*/

-- SQLite
SELECT Tournament.name
FROM Tournament
    JOIN PlayerTournament ON (Tournament.name=PlayerTournament.tournament_name)
    JOIN Player ON (PlayerTournament.player_email=Player.email)
WHERE Player.email = "player9@example.com";
