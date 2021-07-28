from flask import Flask,request,render_template, flash,redirect, send_file,url_for,jsonify
from selenium.common.exceptions import NoSuchElementException
import requests
import re
import time
from selenium import webdriver
from unidecode import unidecode
from werkzeug.utils import secure_filename
import mysql.connector
import datetime
import json
def insertsql(data):
    cnx = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
    cursor4=cnx.cursor()
    query="insert into tsetms values (\'%s\' ,'Null','Null','Null','Null','Null','Null','0','0','0','0','Null','Null','Null');"%str(data)
    cursor4.execute(query)
    cnx.commit()
    cnx.close()
def sqldatadel(id):
    cnx = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
    cursor3=cnx.cursor(dictionary=True)
    query="delete from tsetms where id =\'%s\';"%str(id)
    cursor3.execute(query)
    cnx.commit()
    cnx.close()
def sqldataids():
    cnx = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
    cursor2=cnx.cursor(dictionary=True)
    values=[]
    query="select id, namee from tsetms;"
    cursor2.execute(query)
    for x in cursor2:
        values.append(x.items())
    cnx.close()
    return values
def sqldata():
    cnx = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
    cursor1=cnx.cursor(dictionary=True)
    values=[]
    query="select * from tsetms;"
    cursor1.execute(query)
    for x in cursor1:
        values.append(x.items())
    cnx.close()
    return values
app = Flask(__name__)
@app.route('/insert',methods = ['POST','GET'])
def insert():
      data=request.form['description']
      insertsql(data)
      return redirect('/addurls')
@app.route('/addurls',methods = ['POST','GET'])
def home1():
      c=sqldataids()
      return render_template('index.html',c=c)
@app.route('/<id>',methods = ['POST','GET'])
def delete(id):
    sqldatadel(id)
    return redirect('/addurls')
@app.route('/',methods = ['POST','GET'])
def home():
      values=sqldata()
      return(render_template('home.html',values=values))


@app.route('/test/', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        # print('Recieved from JS')
        b=sqldata()
        jsonf=[]
        i=1;
        for x in b:
            json_data=[]
            for a in x:
                z=list(a)
                aa=str(z[0])
                bb=str(z[1])
                json_data.append({aa:bb})
            jsonf.append({"data":json_data})
            i=i+1
        return jsonify(jsonf)
        # print(jsonf)
          # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        # print(request.get_json())  # parse as JSON
        return 'Sucesss', 200
if __name__ == "__main__":
       app.run(host='127.0.0.1',port=80)