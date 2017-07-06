import os
from flask import Flask, render_template, redirect, url_for, escape, request
from datetime import datetime
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def new():
   return render_template('home1.html')


@app.route('/enternew')
def new_entry():
   return render_template('entry1.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      
         name = request.form['name']
         age = request.form['age']
         timing=request.form['timing']
      
         
         with sql.connect("mydata.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO grp (name,age,timing)VALUES (?,?,?)",(name,age,timing))
          
            con.commit()
            ms = "Record  added"
      
      
      
         return render_template("result1.html",ms = ms)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("mydata.db")
   con.row_factory = sql.Row
   
   cur = con.cursor( )
   cur.execute("select * from grp")
   
   rows = cur.fetchall();
   return render_template("list1.html",rows = rows)

   
if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0', port=5000)

    
