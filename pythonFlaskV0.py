from flask import Flask,  render_template, url_for, request
import sqlite3

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

DATABASE = 'database.db'

app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")

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

@app.route("/host", methods=["GET", "POST"])
def host():
    if request.method == "POST":
        # Tournament info
        tournament_name = request.form.get("tournament_name")
        location = request.form.get("location")
        date = request.form.get("date")
        game = request.form.get("game")
        # Host info
        host_name = request.form.get("host_name")
        host_email = request.form.get("host_email")
        host_phone = request.form.get("host_phone")
        
        # Do something with the form data (e.g., save it to the database)

        return "Form submitted successfully!"  # Or redirect to another page
    else:
        return render_template("host.html")

@app.route("/tournament")
def tournament():
    return render_template("tournament.html")

@app.route("/bracket")
def bracket():
    return render_template("bracket.html")
    

if __name__ == '__main__':
    app.run()
