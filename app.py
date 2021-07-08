
from flask import Flask, render_template, request, jsonify
import mysql.connector




app = Flask(__name__)

conn = mysql.connector.connect(  host="localhost",  user="root",  password="root",  database="alpha")
	



@app.route('/signup', methods=['GET', 'POST'])
 
def signup():
    return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])

def register():
    if request.method == "POST":
        details = request.form
        Username = details['name']
        Email_address = details['email']
        password = details['password']
        Confirm_Password = details['password1']
        if password == Confirm_Password :
           print("password matched")
        else :
            
            return({"error": "password does not match"})
       
        cur = conn.cursor()
        cur.execute("INSERT INTO userdet(Username, Email, Password) VALUES (%s, %s, %s)", (Username, Email_address, password))
        conn.commit()
        cur.close()

        resp = jsonify(details)
        resp.status_code = 200
        return resp
    



@app.route('/signin', methods=['GET', 'POST'])
 
def signin():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == "POST":
        details = request.form
        Email_address = details['email']
        password = details['password']

        cur = conn.cursor()
        cur.execute('SELECT * FROM userdet WHERE email="{}"'.format(Email_address))
        rows_fetch = cur.fetchall()
        cur.close()
        is_valid = False
        for row in rows_fetch:
            if Email_address in row[1] and password in row[2] :
                is_valid = True
                break

        if is_valid:
            
            json_userexist  = jsonify({"status": "user is valid"})
            json_userexist.status_code = 200
        else:
            json_userexist  = jsonify({"error": "user is not valid"})
            json_userexist.status_code = 404

        return json_userexist
    









