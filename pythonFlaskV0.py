from flask import Flask,  render_template
import sqlite3

app = Flask(__name__)
app = Flask(__name__, template_folder='public')

DATABASE = 'database.db'



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/host')
def host():
    return render_template('host.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/tournament')
def tournament():
    return render_template('tournament.html')
