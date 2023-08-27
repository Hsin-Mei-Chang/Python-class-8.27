import sqlite3
import json
from typing import Text
from flask import session, redirect, Flask, render_template, request
from log_utils import *
import logging

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        try:
            account = request.values['Account']
            password = request.values['Password']
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            print("Insert Start")
            cursor.execute("INSERT INTO %s (account,password) VALUES (:1,:2)" % "userdata", [
                           account, password])
            conn.commit()
            print("Insert End")
            conn.close()

        except:
            return render_template('register.html')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.values['send'] == '登入':

            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            print("Selete Start")
            print(request.values["Account"])
            rows = cursor.execute("""
            SELECT COUNT(*) FROM userdata WHERE password = '%s'
            """ % (request.values["Password"]))
            conn.commit()
            print("Selete End")
            conn.close()
            if rows:
                return render_template('login.html')
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s ', level=logging.DEBUG)
    # logging.INFO()
    app.run(host='0.0.0.0', port='5000')
'''2023-07-30 21:01:54,208 INFO: [31m[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.[0m
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.189:5000
2023-07-30 21:01:54,209 INFO: [33mPress CTRL+C to quit[0m'''