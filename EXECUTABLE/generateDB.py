"""
Set Up DataBase
"""

import sqlite3 as sql
import os
def genDB():
    if not os.path.isdir("Database"):
        os.mkdir("Database")
    adminCon = sql.connect("Database/admin.db")
    restCon = sql.connect("Database/rest.db")
    empCon = sql.connect("Database/emp.db")
    itemCon = sql.connect("Database/item.db")
    orderCon = sql.connect("Database/order.db")
    
    a = adminCon.cursor()
    a.execute(""" CREATE TABLE admin (
                  name text,
                  username text,
                  password blob 
                  )""")
    
    r = restCon.cursor()
    r.execute(""" CREATE TABLE restaurant (
                  name text,
                  address text,
                  owner text 
                  )""")
    
    e = empCon.cursor()
    e.execute(""" CREATE TABLE employee (
                  ecode blob,
                  name text,
                  username text,
                  password blob 
                  )""")  
    
    i = itemCon.cursor()
    i.execute(""" CREATE TABLE items (
                  icode blob,
                  name text,
                  price real 
                  )""")
    
    o = orderCon.cursor()
    o.execute(""" CREATE TABLE orders (
                  onum INTEGER PRIMARY KEY AUTOINCREMENT,
                  cust_name TEXT,
                  cust_email TEXT,
                  total REAL
                  )""")
    
    adminCon.commit()
    restCon.commit()
    empCon.commit()
    itemCon.commit()
    orderCon.commit()
    
    a.close()
    o.close()
    i.close()
    e.close()
    r.close()
    
    adminCon.close()
    restCon.close()
    empCon.close()
    itemCon.close()
    orderCon.close()
