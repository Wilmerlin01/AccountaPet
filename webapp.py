from flask import Flask, abort, render_template, request, redirect, url_for, session
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'webapp_secret_key'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()
    # Retrieve the current user's name and id from the current_user table
    c.execute("SELECT user_name, user_id FROM current_user")
    result = c.fetchone()
    user_name, user_id = result[0], result[1] if result else ('', '')
    
    # Retrieve all goals for the current user
    c.execute("SELECT goal_id, goal_description, time_remaining FROM goal WHERE user_id=?", (user_id,))
    goals = c.fetchall()

    c.close()
    conn.close()

    print("Webapp username: " + user_name)

    return render_template('home.html', user_name=user_name, goals=goals)


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
