/*

This is a sample query, used for testing, that checks which players are participating in the tournament Super Smash Showdown.

Authors: Jaren Alexander, Yankun Chen, Brett Fox, Kevin Truong, Sam Windheim

Group Name: TournamentsEZ

Last Modification Date: 6/9/2023

*/

-- Checking which users are participating in Super Smash Showdown
SELECT Player.fname, Player.lname, Player.email
FROM Player 
    JOIN PlayerTournament ON (Player.email = PlayerTournament.player_email)
    JOIN Tournament ON (PlayerTournament.tournament_name = Tournament.name)
WHERE Tournament.name = "Super Smash Showdown";
