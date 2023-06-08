from flask import Flask, render_template, url_for, request
from BracketTree import Tree, insertPlayer, loadPlayerData, test
import sqlite3

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

DATABASE = 'database/proj2_db.sqlite3'

app.static_folder = 'static'

# Establish a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Fetch all tournaments from the database
def fetch_tournaments():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM Tournament")
    tournaments = cursor.fetchall()
    cursor.close()
    conn.close()
    return tournaments

def generate_tournament_bracket(selected_tournament):
    # Fetch the players for the selected tournament from the database
    player_list = loadPlayerData(selected_tournament)  # Assuming selected_tournament is the database name
    player_tree = insertPlayer(player_list)

    # Perform any required operations on the player_tree

    return player_tree



# Route for home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Fetch the tournaments from the database
    tournaments = fetch_tournaments()

    if request.method == 'POST':
        # Get the form data
        tournament_name = request.form.get('tournament-select')
        player_email = request.form.get('email')
        phonenum = request.form.get('phone')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        address = request.form.get('address')
        
        # Save the player data to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the player already exists in the Player table
        cursor.execute("SELECT * FROM Player WHERE email = ?", (player_email,))
        existing_player = cursor.fetchone()

        if existing_player is None:
            # Create a new player
            cursor.execute("INSERT INTO Player (email, fname, lname, phonenum, address) VALUES (?, ?, ?, ?, ?)",
                           (player_email, fname, lname, phonenum, address))

        # Save the player-tournament association to the PlayerTournament table
        print(f"Inserting email into PlayerTournament: {player_email}")
        print(f"Inserting tournament name into PlayerTournament: {tournament_name}")
        cursor.execute("INSERT INTO PlayerTournament (player_email, tournament_name) VALUES (?, ?)",
                       (player_email, tournament_name))

        conn.commit()
        cursor.close()
        conn.close()

        # Fetch the updated tournament list
        tournaments = fetch_tournaments()

        # Render the signup.html template with the updated tournaments and reset the form
        return render_template('signup.html', tournaments=tournaments)

    elif request.method == 'GET':
        # Handle the GET method (display the form with the tournaments)
        return render_template('signup.html', tournaments=tournaments)

    # Handle the case when the method is not allowed
    else:
        return "Method Not Allowed", 405

 

# Route for host page
@app.route("/host", methods=["GET", "POST"])
def host():
    if request.method == 'POST':
        # Get the form data
        tournament_name = request.form.get('tournament_name')
        host_email = request.form.get('host_email')
        fname = request.form.get('host_fname')
        lname = request.form.get('host_lname')
        phonenum = request.form.get('host_phone')
        location = request.form.get('location')
        date = request.form.get('date')
        game = request.form.get('game')
        
        # Save the host data to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if the host already exists in the Host table
        cursor.execute("SELECT * FROM Host WHERE email = ?", (host_email,))
        existing_host = cursor.fetchone()
        
        if existing_host is None:
            # Create a new host
            cursor.execute("INSERT INTO Host (email, fname, lname, phonenum, address) VALUES (?, ?, ?, ?, ?)",
                           (host_email, fname, lname, phonenum, ''))
        
        # Save the tournament data to the Tournament table
        cursor.execute("INSERT INTO Tournament (name, email, phonenum, address, url, date, game, host_email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (tournament_name, '', '', location, '', date, game, host_email))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        # Fetch the updated tournament list
        tournaments = fetch_tournaments()
        
        # Render the host.html template with the updated tournaments and reset the form
        return render_template('host.html', tournaments=tournaments)

    elif request.method == 'GET':
        # Fetch the tournament list
        tournaments = fetch_tournaments()
        
        # Handle the GET method (display the form with the tournaments)
        return render_template('host.html', tournaments=tournaments)

    # Handle the case when the method is not allowed
    else:
        return "Method Not Allowed", 405


@app.route('/tournament', methods=['GET', 'POST'])
def tournament():
    # Fetch the tournaments from the database
    tournaments = fetch_tournaments()
    
    if request.method == 'POST':
        # Get the selected tournament name from the form
        selected_tournament = request.form.get('tournament_name')

        # Fetch the players in the selected tournament from the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Player.* FROM Player JOIN PlayerTournament ON Player.email = PlayerTournament.player_email WHERE PlayerTournament.tournament_name = ?", (selected_tournament,))
        players = cursor.fetchall()
        cursor.close()
        conn.close()

        # Check if the tournament already exists
        if selected_tournament in [tournament['name'] for tournament in tournaments]:
            # Tournament already exists, display the players in the tournament
            return render_template('tournament.html', tournaments=tournaments, selected_tournament=selected_tournament, players=players)

        # Tournament is new, add it to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tournament (name) VALUES (?)", (selected_tournament,))
        conn.commit()
        cursor.close()
        conn.close()

        # Display an empty player list for the new tournament
        return render_template('tournament.html', tournaments=tournaments, selected_tournament=selected_tournament, players=[])
    
    # Handle GET request, display the tournaments
    return render_template('tournament.html', tournaments=tournaments)



@app.route('/bracket', methods=['GET', 'POST'])
def bracket():
    # Fetch the tournaments from the database
    tournaments = fetch_tournaments()

    if request.method == 'POST':
        # Get the selected tournament name from the form
        selected_tournament = request.form.get('tournament_name')

        # Load player data for the selected tournament
        player_list = loadPlayerData(selected_tournament)

        # Generate the tournament bracket using the Tree class
        player_tree = insertPlayer(player_list)

        # Perform any required operations on the player_tree

        # Render the bracket.html template with the tournament data and bracket
        return render_template('bracket.html', tournaments=tournaments, selected_tournament=selected_tournament)

    # Handle GET request, display the tournaments
    return render_template('bracket.html', tournaments=tournaments)


    

if __name__ == '__main__':
    app.run(debug=True)
