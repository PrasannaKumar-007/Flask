from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/forgotpwd')
def forgotpwd():
    return render_template('forgotpassword.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/hostelpricing')
def hostelpricing():
    return render_template('pricing.html')



#Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    try:
        email = request.form['email']
        password = request.form['password']

        if email == '' or password == '':
            return render_template('login.html', error='Missing form data')

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE email=?', (email,))
        user = cur.fetchone()

        if user is None:
            return render_template('login.html', error='User does not exist')

        if user[1] != password:
            return render_template('login.html', error='Incorrect password')

        return render_template('index.html', user=email)
    except:
        return render_template('login.html', error='Missing form data')

#signup
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    try:
        fname  = request.form['fname']
        lname  = request.form['lname']
        pin = request.form['pin']
        email = request.form['email']
        password = request.form['password']


        if email == '' or password == '' or pin=='' or fname=='' or lname=='':
            return render_template('register.html', error='Missing form data')

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE email=?', (email))
        user = cur.fetchone()

        if user is not None:
            return render_template('register.html', error='User already exists')

        cur.execute(
            'INSERT INTO users (fname, lname, email, password,pin) VALUES (?,?,?,?,?)', (fname, lname, email, password,pin))
        conn.commit()

        return render_template('login.html', user=email)
    except:
        return render_template('register.html', error='Missing form data')
