/*

This is a sample query, used for testing, that checks which host has the email 'host4@example.com'

Authors: Jaren Alexander, Yankun Chen, Brett Fox, Kevin Truong, Sam Windheim

Group Name: TournamentsEZ

Last Modification Date: 6/9/2023

*/

-- SQLite
SELECT Tournament.name
FROM Tournament
    JOIN Host ON (Tournament.host_email = Host.email)
WHERE Host.email = "host4@example.com";
