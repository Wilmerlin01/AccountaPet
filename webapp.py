from flask import Flask, abort, render_template, request, redirect, url_for
import os
import sqlite3

app = Flask(__name__)

# connect to the database
conn = sqlite3.connect('db/accountapet.db')
c = conn.cursor()

# close the database connection
conn.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/pet_status')
def pet_status():

    return render_template('pet_status.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
