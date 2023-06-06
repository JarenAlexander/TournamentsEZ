from flask import Flask, render_template, url_for, request
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

# Route for home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        tournament = request.form.get("tournament")
        name = request.form.get("name")
        address1 = request.form.get("address1")
        address2 = request.form.get("address2")
        mailing_address = request.form.get("mailingAddress")
        email = request.form.get("email")
        phone = request.form.get("phone")

        # Do something with the form data (e.g., save it to the database)

        return "Form submitted successfully!"  # Or redirect to another page
    else:
        return render_template("signup.html")

# Route for host page
@app.route("/host", methods=["GET", "POST"])
def host():
    if request.method == 'POST':
        # Get the form data
        tournament_name = request.form.get('tournament_name')
        host_email = request.form.get('host_email')
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
                           (host_email, '', '', phonenum, ''))
        
        # Save the tournament data to the Tournament table
        cursor.execute("INSERT INTO Tournament (name, email, phonenum, address, date, game, host_email) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (tournament_name, '', '', location, date, game, host_email))
        
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



# Route for tournament page
@app.route('/tournament')
def tournament():
    # Fetch the tournaments from the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tournament")
    tournaments = cursor.fetchall()
    cursor.close()
    conn.close()
    # Pass the tournaments to the template
    return render_template('tournament.html', tournaments=tournaments)

# Route for bracket page
@app.route("/bracket")
def bracket():
    return render_template("bracket.html")
    

if __name__ == '__main__':
    app.run(debug=True)
