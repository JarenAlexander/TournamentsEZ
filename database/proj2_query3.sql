/*

This is a sample query, used for testing, that checks which tournaments are on the date '2023-10-20'.

Authors: Jaren Alexander, Yankun Chen, Brett Fox, Kevin Truong, Sam Windheim

Group Name: TournamentsEZ

Last Modification Date: 6/9/2023

*/

-- SQLite
SELECT Tournament.name
FROM Tournament
WHERE Tournament.date = "2023-10-20";
