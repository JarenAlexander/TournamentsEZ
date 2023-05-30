from flask import Flask,  render_template
import sqlite3

app = Flask(__name__)
app = Flask(__name__, template_folder='public')

DATABASE = 'database.db'



@app.route('/')

def index():
    return render_template('index.html')
