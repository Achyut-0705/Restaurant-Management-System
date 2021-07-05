"""
Generate Sample DataBase
"""
import sqlite3 as sql

adminCon = sql.connect("admin.db")
restCon = sql.connect("rest.db")
empCon = sql.connect("emp.db")
itemCon = sql.connect("item.db")

c = adminCon.cursor()
c.execute(""" CREATE TABLE admin (
              name text,
              username text,
              password blob 
              )""")
adminCon.commit()
c.execute("INSERT INTO admin VALUES (?, ?, ?)", ("Admin", "admin", "admin"))
adminCon.commit()
adminCon.close()


r = restCon.cursor()
r.execute(""" CREATE TABLE restaurant (
              name text,
              address text,
              owner text 
              )""")
restCon.commit()
r.execute("INSERT INTO restaurant VALUES (?, ?, ?)", ("Fast Food Counter", "Pune", "Dinker Ahuja"))
restCon.commit()
restCon.close()

e = empCon.cursor()
e.execute(""" CREATE TABLE employee (
              ecode blob,
              name text,
              username text,
              password blob 
              )""")
empCon.commit()
e.execute("INSERT INTO employee VALUES (?, ?, ?, ?)", ("E001", "EMP1", "emp1", "password"))
empCon.commit()
e.execute("INSERT INTO employee VALUES (?, ?, ?, ?)", ("E002", "EMP2", "emp2", "password"))
empCon.commit()
e.execute("INSERT INTO employee VALUES (?, ?, ?, ?)", ("E002", "EMP2", "emp2", "password"))
empCon.commit()
empCon.close()


i = itemCon.cursor()
i.execute(""" CREATE TABLE items (
              icode blob,
              name text,
              price real 
              )""")

itemCon.commit()
i.execute("INSERT INTO items VALUES (?, ?, ?)", ("I001", "Burger", 100))
itemCon.commit()
i.execute("INSERT INTO items VALUES (?, ?, ?)", ("I002", "Pizza", 120))
itemCon.commit()
i.execute("INSERT INTO items VALUES (?, ?, ?)", ("I003", "Pepsi", 60))
itemCon.commit()
itemCon.close()

orderFile = "order.db"
orderCon = sql.connect(orderFile)
o = orderCon.cursor()
o.execute(""" CREATE TABLE orders (
              onum INTEGER PRIMARY KEY AUTOINCREMENT,
              cust_name TEXT,
              cust_email TEXT,
              total REAL
              )""")
o.execute("INSERT INTO orders (cust_name, cust_email, total) VALUES (:cust_name, :cust_email, :total)", {"cust_name":"Antriksh", "cust_email":"abc@gmail.com", "total":100})
orderCon.commit()

o.execute("SELECT * FROM orders")
print(o.fetchone())
orderCon.close()