#!/usr/bin/python3
import pymysql
kdb = pymysql.connect(host='localhost',user='kube',password='placement',db='kubeplacement')
kcursor = kdb.cursor()

sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT )"""

kcursor.execute(sql)
kdb.close()

