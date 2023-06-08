-- SQLite
SELECT Tournament.name
FROM Tournament
    JOIN PlayerTournament ON (Tournament.name=PlayerTournament.tournament_name)
    JOIN Player ON (PlayerTournament.player_email=Player.email)
WHERE Player.email = "player9@example.com";
