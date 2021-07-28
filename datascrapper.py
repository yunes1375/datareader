from flask import Flask,request,render_template, flash,redirect, send_file,url_for,jsonify
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup
import re
import os  
import time
from selenium import webdriver
from unidecode import unidecode
from werkzeug.utils import secure_filename
import mysql.connector
import datetime
cnx1 = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')

driver = webdriver.Chrome()
def readurls():
    cnx1 = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
    cursor7=cnx1.cursor(dictionary=True)
    urls=[]
    query="select id from tsetms;"
    cursor7.execute(query)
    
    for x in cursor7:
       for key,value in x.items():
           value='http://www.tsetmc.com/loader.aspx?ParTree=151311&i='+str(value)
           urls.append(value)
    cnx1.close()
    return urls
def datainserter(c):
  cnx1 = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
  cursor6=cnx1.cursor() 
#  print(c[1],c[2],c[3],c[4],c[5],c[6],int(c[7]),int(c[8]),int(c[9]),int(c[10]),c[0])
  query='update tsetms set namee=\'%s\', price=\'%s\', eps=\'%s\', pe=\'%s\', pegroup=\'%s\', ps=\'%s\', hakh=\'%s\', hokh=\'%s\', haf=\'%s\', hof=\'%s\', sarane=\'%s\', dateday=\'%s\', time=\'%s\' where id=\'%s\';'%(c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],str(c[12]),str(c[13]),c[0])
  cursor6.execute(query)
  cnx1.commit()
  cnx1.close()
def datainserter2(c):
  cnx1 = mysql.connector.connect(user='yunes', password='1290',
                              host='127.0.0.1',
                              database='learn')
  cursor8=cnx1.cursor() 
#  print(c[1],c[2],c[3],c[4],c[5],c[6],int(c[7]),int(c[8]),int(c[9]),int(c[10]),c[0])
  query='insert into tsetms2 values (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\' ,\'%s\');'%(str(c[0]),c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],str(c[12]),str(c[13]))
  cursor8.execute(query)
  cnx1.commit()
  cnx1.close()
def datascrapper(url):
  pages = driver.get(url)
  ids=url.split("=")
  id=ids[2]
  time.sleep(10)
  name=driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[1]").text.split('-')[0]
  text1=driver.find_element_by_xpath('/html/body/div[4]/form/div[3]/div[2]/div[1]').text
  if "NAV" in text1:
#####sandogh 
        try:
            price1 = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[1]/div[1]/table/tbody/tr[2]/td[2]").text
            price=price1.replace(" ","-").split("-")[0].replace(",","")
        except NoSuchElementException:
            price="None"
            pass
        try:
            time1 = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[1]/span").text
        except NoSuchElementException:
            time1="None"
            pass
        eps="None"
        pe="None"
        ps="None"
        pegroup="None"
        ps="None"
        try:
            hakh = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[6]/td[2]").text.replace(",","")
        except NoSuchElementException:
            hakh="None"
            pass
        try:
            hokh = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[7]/td[2]").text.replace(",","")
        except NoSuchElementException:
            hokh="None"
            pass
        try:
            haf = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[6]/td[3]").text.replace(",","")
        except NoSuchElementException:
            haf="None"
            pass
        try:
            hof = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[7]/td[3]").text.replace(",","")
        except NoSuchElementException:
            hof="None"
            pass
        try:
            dkhh = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div[2]").text
        except NoSuchElementException:
            dkhh="None"
            pass
        try:
            dfh = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[3]/div[2]").text
        except NoSuchElementException:
            dfh="None"
            pass
                
##### deafualt pages xpath
  else:
        try:
            price1 = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[2]").text
            price=price1.replace(" ","-").split("-")[0].replace(",","")
        except NoSuchElementException:
            pass
        try:
            time1 = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[1]/span").text
        except NoSuchElementException:
            time1="None"
            pass
        try:
            eps = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[6]/table/tbody/tr[1]/td[2]").text
        except NoSuchElementException:
            pass
        try:
            pe = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[6]/table/tbody/tr[1]/td[4]").text
        except NoSuchElementException:
            ps="None"
            pass
        try:
            pegroup = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[6]/table/tbody/tr[1]/td[6]").text
        except NoSuchElementException:
            ps="None"
            pass
        try:
            ps = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[2]/div[6]/table/tbody/tr[1]/td[8]").text
        except NoSuchElementException:
            ps="None"
            pass
#
        try:
            hakh = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[6]/td[2]").text.replace(",","")
        except NoSuchElementException:
            hakh="None"
            pass
        try:
            hokh = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[7]/td[2]").text.replace(",","")
        except NoSuchElementException:
            hokh="None"
            pass
        try:
            haf = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[5]/td[3]").text.replace(",","")
        except NoSuchElementException:
            haf="None"
            pass
        try:
            hof = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[7]/td[3]").text.replace(",","")
        except NoSuchElementException:
            hof="None"
            pass
        try:
            dkhh = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[2]/div[2]").text
        except NoSuchElementException:
            dkhh="None"
            pass
        try:
            dfh = driver.find_element_by_xpath("/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[3]/div[2]").text
        except NoSuchElementException:
            dfh="None"
            pass
  b=[]
  if dfh!="None":
     sarane=(float(haf)*float(dkhh))/(float(hakh)*float(dfh))
     sarane = str(round(sarane, 2))
  else:
     sarane="None"
  dd=str(datetime.datetime.now().date())
  a=[id,name,price,eps,pe,pegroup,ps,hakh,hokh,haf,hof,sarane,dd,time1]
  b=b+a;
  return b
while(1!=0):
  time.sleep(5)
  urls=readurls()
  for x in range(0,len(urls)):
    c=datascrapper(urls[x])
    datainserter(c)
    datainserter2(c)
