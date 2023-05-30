from flask import Flask,  render_template
import sqlite3

app = Flask(__name__, template_folder='public')
app = Flask(__name__)

DATABASE = 'database.db'



@app.route('/')

def index():
    return render_template('index.html')