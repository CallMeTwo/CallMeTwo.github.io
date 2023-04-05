from re import M
from flask import Flask, redirect, url_for, request, render_template, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pandas as pd
import numpy as np


app = Flask(__name__)

app.secret_key = '\xef\x0e\xaa\xd2@\x18\xe9\xf0\x17~u\x89W\x04\xce\xb4\xccK\xb4h\xbc*\x91\xf7'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'two'
app.config['MYSQL_PASSWORD'] = 'two14239'
app.config['MYSQL_DB'] = 'database1'

mysql = MySQL(app)

#---------

@app.route('/')
def index():    
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      sec = request.form['sec']
      return redirect(url_for(sec))

@app.route('/ped', methods = ['POST', 'GET'])
def ped():
    if request.method == 'POST':
        getage = request.form['age']
        getga = int(request.form['ga'])
        if getga>38 :
            getga=38
        getga=str(getga)
        getrisk = request.form['risk']
        if getrisk=='low' :
            risk='a'
        else:
            risk='b'
        gettcb = request.form['mb']
        cursor = mysql.connection.cursor()
        cursor.execute(''.join(['select a',
                               risk,
                               getga,
                               ' from jaundice where age = ',
                               getage]))
        photo = cursor.fetchone()[0]
        cursor.execute(''.join(['select b',
                               risk,
                               getga,
                               ' from jaundice where age = ',
                               getage]))
        transfu = cursor.fetchone()[0]
        return render_template('ped.html',
                               photo = photo,
                               transfu = transfu,
                               age = getage,
                               ga = getga,
                               tcb = gettcb,
                               risk = getrisk)
    else:
        return render_template('ped.html')

@app.route('/med')
def med():
   return render_template('med.html')


if __name__ == '__main__':
   app.run(debug = True)