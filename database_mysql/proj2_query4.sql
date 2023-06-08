-- SQLite
SELECT Tournament.name
FROM Tournament
    JOIN Host ON (Tournament.host_email = Host.email)
WHERE Host.email = "host4@example.com";
