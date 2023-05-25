import sqlite3

connection = sqlite3.connect("./proj2_db.sqlite3") # Connecting to database

my_cursor = connection.cursor()

with open("./loadscript.sql") as fin:
    sql_script = fin.read()

my_cursor.execute("PRAGMA foreign_keys = ON;")

# my_cursor.executescript(sql_script) # Creating database

# Host/player format: (email, fname, lname, phonenum, address)
# Tournament format: (name, email, phonenum, address, url, date, game, host_email)

player_list = [
    ("player1@example.com", "John", "Doe", "1234567890", "123 Main Street, Cityville"),
    ("player2@example.com", "Jane", "Smith", "9876543210", "456 Elm Avenue, Townsville"),
    ("player3@example.com", "Mike", "Johnson", "5555545555", "789 Oak Road, Villagetown"),
    ("player4@example.com", "Emily", "Williams", "1111311111", "321 Cedar Lane, Cityville"),
    ("player5@example.com", "Chris", "Brown", "9999999299", "654 Pine Street, Townsville"),
    ("player6@example.com", "Jessica", "Davis", "7779777777", "987 Maple Avenue, Villagetown"),
    ("player7@example.com", "Andrew", "Wilson", "4444442444", "456 Oak Road, Cityville"),
    ("player8@example.com", "Olivia", "Anderson", "2222262222", "123 Elm Street, Townsville"),
    ("player9@example.com", "David", "Martinez", "8883888888", "789 Cedar Lane, Villagetown"),
    ("player10@example.com", "Sophia", "Taylor", "6666966666", "321 Maple Street, Cityville")
]

my_cursor.executemany("""INSERT INTO Player (email, fname, lname, phonenum, address) VALUES
    (?, ?, ?, ?, ?)""", player_list)

host_list = [
    ("host1@example.com", "Adam", "Smith", "1234533890", "123 Main Street, Cityville"),
    ("host2@example.com", "Laura", "Johnson", "9876543280", "456 Elm Avenue, Townsville"),
    ("host3@example.com", "Michael", "Brown", "5565555555", "789 Oak Road, Villagetown"),
    ("host4@example.com", "Emily", "Wilson", "1111112111", "321 Cedar Lane, Cityville"),
    ("host5@example.com", "Daniel", "Taylor", "9999899999", "654 Pine Street, Townsville")
]

my_cursor.executemany("""INSERT INTO Host (email, fname, lname, phonenum, address) VALUES
    (?, ?, ?, ?, ?)""", host_list)

tournament_list = [
    ("Summer Slam Tournament", "summerslam@example.com", "1234567690", "123 Main Street, Cityville", "http://www.summerslam.com", "2023-07-15", "Street Fighter V", "host4@example.com"),
    ("Battle Royale Championship", "championship@example.com", "9871543210", "456 Oak Avenue, Townsville", "http://www.battleroyalechampionship.com", "2023-09-05", "Fortnite", "host1@example.com"),
    ("Super Smash Showdown", "showdown@example.com", "5500555555", "789 Elm Street, Villagetown", "http://www.smashshowdown.com", "2023-08-20", "Super Smash Bros. Ultimate", "host2@example.com"),
    ("League of Legends Clash", "clash@example.com", "1113411111", "321 Cedar Road, Cityville", "http://www.clashlol.com", "2023-10-10", "League of Legends", "host3@example.com"),
    ("FIFA World Tournament", "fifatournament@example.com", "9924999999", "654 Maple Lane, Townsville", "http://www.fifaworldtournament.com", "2023-07-30", "FIFA 22", "host5@example.com"),
    ("Call of Duty Championship", "codchampionship@example.com", "7777777277", "987 Pine Avenue, Villagetown", "http://www.codchampionship.com", "2023-08-10", "Call of Duty: Warzone", "host5@example.com"),
    ("Overwatch Mayhem", "mayhem@example.com", "4444934444", "456 Oak Avenue, Cityville", "http://www.overwatchmayhem.com", "2023-09-15", "Overwatch", "host1@example.com"),
    ("Rocket League Rumble", "rumble@example.com", "2220422222", "123 Elm Street, Townsville", "http://www.rocketleaguerumble.com", "2023-08-05", "Rocket League", "host2@example.com"),
    ("Dota 2 Battle", "dota2battle@example.com", "8888881988", "789 Cedar Road, Villagetown", "http://www.dota2battle.com", "2023-09-25", "Dota 2", "host1@example.com"),
    ("Mortal Kombat Klash", "klash@example.com", "6666726666", "321 Maple Lane, Cityville", "http://www.mkk.com", "2023-10-20", "Mortal Kombat 11", "host3@example.com")
    ]

my_cursor.executemany("""INSERT INTO Tournament (name, email, phonenum, address, url, date, game, host_email) VALUES
    (?, ?, ?, ?, ?, ?, ?, ?)""", tournament_list)

playertournament_list = [
    ("Summer Slam Tournament", "player1@example.com"),
    ("Battle Royale Championship", "player2@example.com"),
    ("Super Smash Showdown", "player3@example.com"),
    ("League of Legends Clash", "player4@example.com"),
    ("FIFA World Tournament", "player5@example.com"),
    ("Call of Duty Championship", "player6@example.com"),
    ("Overwatch Mayhem", "player7@example.com"),
    ("Rocket League Rumble", "player8@example.com"),
    ("Dota 2 Battle", "player9@example.com"),
    ("Mortal Kombat Klash", "player10@example.com"),
    ("Summer Slam Tournament", "player2@example.com"),
    ("Battle Royale Championship", "player3@example.com"),
    ("Super Smash Showdown", "player4@example.com"),
    ("League of Legends Clash", "player5@example.com"),
    ("FIFA World Tournament", "player6@example.com"),
    ("Call of Duty Championship", "player7@example.com"),
    ("Overwatch Mayhem", "player8@example.com"),
    ("Rocket League Rumble", "player9@example.com"),
    ("Dota 2 Battle", "player10@example.com"),
    ("Mortal Kombat Klash", "player1@example.com")
]

my_cursor.executemany("""INSERT INTO PlayerTournament (tournament_name, player_email) VALUES
    (?, ?)""", playertournament_list)

# connection.commit() # Uncomment this to actually commit the changes to the DB

# DEBUG TODO: Try inputting a non-int value as a phone number


my_cursor.close()
connection.close() # Disconnecting from database