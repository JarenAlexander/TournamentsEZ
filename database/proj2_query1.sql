-- SQLite
SELECT Player.fname, Player.lname, Player.email
FROM Player 
    JOIN PlayerTournament ON (Player.email = PlayerTournament.player_email)
    JOIN Tournament ON (PlayerTournament.tournament_name = Tournament.name)
WHERE Tournament.name = "Super Smash Showdown";
