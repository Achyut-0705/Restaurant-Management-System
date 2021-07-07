#import os
#os.chdir('c:/Users/Anupam/Documents/GitHub/Restaurant-Management-System')

import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from classes import *
import sqlite3 as sql
from tkinter import messagebox
from tkinter import Toplevel, ttk
from tkinter import *
import threading


myRest = None
currAdmin = None
currEmp = None

bg_main = "#d8c3a5"
btn_bg = "#eae7dc"
bg_panel = "#565958"
fg_panel = "#e85a4f"

class Login:
    def __init__(self, root):

        self.window = root

        global bg_main
        global btn_bg
        ft = tkFont.Font(family='Roboto', size=25)

        root.title("Restraunt Management System")
        width = 750
        height = 320
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background=bg_main)

        ft = tkFont.Font(family='Roboto', size=30, weight="bold")
        self.name_restraunt = tk.Label(root)
        self.name_restraunt["font"] = ft
        self.name_restraunt["fg"] = fg_panel
        self.name_restraunt["bg"] = bg_panel
        self.name_restraunt["justify"] = "center"
        self.name_restraunt["text"] = myRest.name.upper()
        self.name_restraunt.place(x=0, y=0, width=750, height=80)

        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.name_restraunt = tk.Label(root)
        self.name_restraunt["font"] = ft
        self.name_restraunt["fg"] = "black"
        self.name_restraunt["bg"] = bg_main
        self.name_restraunt["justify"] = "center"
        self.name_restraunt["text"] = "LOG IN TO CONTINUE"
        self.name_restraunt.place(x=10, y=100, width=729, height=30)

        ft = tkFont.Font(family='Roboto', size=12, weight="bold")
        self.username = tk.Entry(root)
        self.username["borderwidth"] = "1px"
        self.username["font"] = ft
        self.username["fg"] = "#333333"
        self.username["text"] = "User Name"
        self.username.place(x=160, y=140, width=494, height=30)
        self.username.focus()

        self.password = tk.Entry(root)
        self.password["borderwidth"] = "1px"
        self.password["font"] = ft
        self.password["fg"] = "#333333"
        self.password["text"] = "Password"
        self.password["show"] = "*"
        self.password.place(x=160, y=220, width=493, height=30)
        self.password['show'] = '*'

        self.label_username = tk.Label(root)
        self.label_username["font"] = ft
        self.label_username["fg"] = "#333333"
        self.label_username["bg"] = bg_main
        self.label_username["justify"] = "center"
        self.label_username["text"] = "User ID:"
        self.label_username.place(x=80, y=140, width=70, height=25)

        self.label_password = tk.Label(root)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["bg"] = bg_main
        self.label_password["justify"] = "center"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=70, y=220, width=80, height=25)

        self.login_btn = tk.Button(root)
        self.login_btn["bg"] = btn_bg
        self.login_btn["font"] = ft
        self.login_btn["fg"] = "black"
        self.login_btn["justify"] = "center"
        self.login_btn["text"] = "Admin Login"
        self.login_btn.place(x=200, y=280, width=150, height=30)
        self.login_btn["command"] = self.logAdmin

        self.login_btn = tk.Button(root)
        self.login_btn["bg"] = btn_bg
        self.login_btn["font"] = ft
        self.login_btn["fg"] = "black"
        self.login_btn["justify"] = "center"
        self.login_btn["text"] = "Employee Login"
        self.login_btn.place(x=400, y=280, width=150, height=30)
        self.login_btn["command"] = self.logEMP

    def logAdmin(self):
        user = self.username.get()
        try:
            a.execute("SELECT * FROM admin WHERE username = (?)", (user, ))
            data = a.fetchone()
            pas = self.password.get()
            if data[2] == pas:
                global currAdmin
                currAdmin = ADMIN(data[0], data[1], data[2])
                tk.messagebox.showinfo("Logged In", "Successfully Logged In")
                self.window.destroy()
                root = tk.Tk()
                app = AdminPanel(root)
                root.mainloop()
            else:
                tk.messagebox.showerror(
                    "Wrong Credentials", "Username/Password Incorrect")
        except:
            tk.messagebox.showerror("Record Not Found", "No Such User Found")
        

    def logEMP(self):
        
        user = self.username.get()
        try:
            e.execute("SELECT * FROM employee WHERE username = (?)", (user, ))
            data = e.fetchone()
            pas = self.password.get()
            if data[3] == pas:
                global currEmp
                currEmp = EMPLOYEE(data[0], data[1], data[2], data[3])
                tk.messagebox.showinfo("Logged In", "Successfully Logged In")
                self.window.destroy()
                root = tk.Tk()
                app = SalesPanel(root)
                root.attributes('-topmost', 1)
                root.focus_force()
                root.mainloop()
            else:
                tk.messagebox.showerror(
                    "Wrong Credentials", "Username/Password Incorrect")
        except:
            tk.messagebox.showerror("Record Not Found", "No Such User Found")
        

class AdminPanel:
    def __init__(self, root):
        global bg_main
        global btn_bg
        global bg_main
        global fg_panel

        self.window = root

        root.title("Admin Panel")
        root.configure(background=bg_main)
        width = 900
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background=bg_main)

        self.admin = tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=60, weight="bold")
        self.admin["font"] = ft
        self.admin["fg"] = fg_panel
        self.admin["justify"] = "center"
        self.admin["text"] = "ADMIN PANEL"
        self.admin["bg"] = bg_panel
        self.admin.place(x=0, y=0, width=900, height=180)

        self.name_admin_panel = tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=20, weight="bold")
        self.name_admin_panel["font"] = ft
        self.name_admin_panel["fg"] = "#333333"
        self.name_admin_panel["justify"] = "left"
        self.name_admin_panel["text"] = "Name: " + currAdmin.name
        self.name_admin_panel["bg"] = bg_main
        self.name_admin_panel.place(x=10, y=200, width=400)

        self.name_admin_panel = tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=20, weight="bold")
        self.name_admin_panel["font"] = ft
        self.name_admin_panel["fg"] = "#333333"
        self.name_admin_panel['justify'] = 'left'
        self.name_admin_panel["text"] = "Username: " + currAdmin.username
        self.name_admin_panel["bg"] = bg_main
        self.name_admin_panel.place(x=450, y=200, width=400)

        self.btn_emp_mng = tk.Button(root)
        self.btn_emp_mng["bg"] = btn_bg
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_emp_mng["font"] = ft
        self.btn_emp_mng["fg"] = "#000000"
        self.btn_emp_mng["justify"] = "center"
        self.btn_emp_mng["text"] = "MANAGE EMPLOYEE"
        self.btn_emp_mng.place(x=525, y=260, width=300, height=50)
        self.btn_emp_mng["command"] = self.btn_emp_mng_command

        self.btn_reset = tk.Button(root)
        self.btn_reset["bg"] = btn_bg
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_reset["font"] = ft
        self.btn_reset["fg"] = "#000000"
        self.btn_reset["justify"] = "center"
        self.btn_reset["text"] = "RESET DATABASE"
        self.btn_reset.place(x=125, y=260, width=300, height=50)
        self.btn_reset["command"] = self.btn_reset_command

        self.btn_logout = tk.Button(root)
        self.btn_logout["bg"] = btn_bg
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_logout["font"] = ft
        self.btn_logout["fg"] = "#000000"
        self.btn_logout["justify"] = "center"
        self.btn_logout["text"] = "LOG OUT"
        self.btn_logout.place(x=375, y=420, width=200, height=50)
        self.btn_logout["command"] = self.btn_logout_command

        self.btn_manage_item = tk.Button(root)
        self.btn_manage_item["bg"] = btn_bg
        self.btn_manage_item["font"] = ft
        self.btn_manage_item["fg"] = "#000000"
        self.btn_manage_item["justify"] = "center"
        self.btn_manage_item["text"] = "MANAGE ITEMS"
        self.btn_manage_item.place(x=525, y=350, width=300, height=50)
        self.btn_manage_item["command"] = self.btn_manage_item_command

        self.btn_reset = tk.Button(root)
        self.btn_reset["bg"] = btn_bg
        self.btn_reset["font"] = ft
        self.btn_reset["fg"] = "#000000"
        self.btn_reset["justify"] = "center"
        self.btn_reset["text"] = "MANAGE ADMIN"
        self.btn_reset.place(x=125, y=350, width=300, height=50)
        self.btn_reset["command"] = self.btn_manage_admin_command

    def btn_emp_mng_command(self):
        top = Toplevel(self.window)
        app = ManageEmployee(top)
        top.mainloop()

    def btn_reset_command(self):
        self.window.destroy()
        root = tk.Tk()
        app = ResetDatabase(root)
        root.mainloop()

    def btn_logout_command(self):
        self.window.destroy()
        global currEmp
        currEmp = None
        root = tk.Tk()
        app = Login(root)
        root.focus_force()
        root.mainloop()

    def btn_manage_item_command(self):
        top = Toplevel(self.window)
        app = ManageItem(top)
        top.mainloop()

    def btn_manage_admin_command(self):
        top = Toplevel(self.window)
        app = ManageAdmin(top)
        top.mainloop()


class SalesPanel:
    def __init__(self, root):

        global bg_main
        global btn_bg
        global currEmp

        self.root = root
        
        root.title("Sales Panel")
        width = 1280
        height = 720
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background=bg_main)

        self.empLoginHead = tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=50, weight="bold")
        self.empLoginHead["font"] = ft
        self.empLoginHead["fg"] = fg_panel
        self.empLoginHead["justify"] = "center"
        self.empLoginHead["bg"] = bg_panel
        self.empLoginHead["text"] = "PLACE AN ORDER!"
        self.empLoginHead.place(x=0, y=0, width=1280, height=150)

        ft = tkFont.Font(family='Roboto', size=15, weight="bold")

        self.name_emp = tk.Label(root)
        self.name_emp["font"] = ft
        self.name_emp["fg"] = "#333333"
        self.name_emp["justify"] = "left"
        self.name_emp["bg"] = bg_main
        self.name_emp["text"] = "Name: " + currEmp.Name
        self.name_emp.place(x=400, y=160, width=250, height=50)

        self.username_emp = tk.Label(root)
        self.username_emp["font"] = ft
        self.username_emp["fg"] = "#333333"
        self.username_emp["justify"] = "left"
        self.username_emp["bg"] = bg_main
        self.username_emp["text"] = "Username: " + currEmp.Username
        self.username_emp.place(x=650, y=160, width=250, height=50)

        self.label_name_customer = tk.Label(root)
        self.label_name_customer["font"] = ft
        self.label_name_customer["fg"] = "#333333"
        self.label_name_customer["justify"] = "left"
        self.label_name_customer["bg"] = bg_main
        self.label_name_customer["text"] = "Customer Name:"
        self.label_name_customer.place(x=35, y=250, width=200, height=54)

        self.name_customer = tk.Entry(root)
        self.name_customer["borderwidth"] = "1px"
        self.name_customer["font"] = ft
        self.name_customer["fg"] = "#333333"
        self.name_customer["justify"] = "left"
        self.name_customer.place(x=250, y=260, width=400, height=35)
        self.name_customer.focus()

        self.label_email = tk.Label(root)
        self.label_email["font"] = ft
        self.label_email["fg"] = "#333333"
        self.label_email["justify"] = "center"
        self.label_email["bg"] = bg_main
        self.label_email["text"] = "E-mail ID:"
        self.label_email.place(x=600, y=250, width=230, height=48)

        self.email_customer = tk.Entry(root)
        self.email_customer["borderwidth"] = "1px"
        self.email_customer["font"] = ft
        self.email_customer["fg"] = "#333333"
        self.email_customer["justify"] = "left"
        self.email_customer["text"] = ""
        self.email_customer.place(x=830, y=260, width=400, height=35)

        self.list_item = tk.Listbox(root)
        self.list_item["borderwidth"] = "1px"
        self.list_item["font"] = ft
        self.list_item["fg"] = "#333333"
        self.list_item["justify"] = "left"
        self.list_item["state"] = tk.DISABLED
        self.list_item.place(x=500, y=350, width=725, height=267)

        self.btn_add_item = tk.Button(root)
        self.btn_add_item["bg"] = "#efefef"
        self.btn_add_item["font"] = ft
        self.btn_add_item["fg"] = "#000000"
        self.btn_add_item["justify"] = "center"
        self.btn_add_item["bg"] = btn_bg
        self.btn_add_item["text"] = "Add Item"
        self.btn_add_item.place(x=50, y=430, width=400, height=50)
        self.btn_add_item["command"] = self.btn_add_item_command

        self.btn_remove_item = tk.Button(root)
        self.btn_remove_item["bg"] = "#efefef"
        self.btn_remove_item["font"] = ft
        self.btn_remove_item["fg"] = "#000000"
        self.btn_remove_item["justify"] = "center"
        self.btn_remove_item["bg"] = btn_bg
        self.btn_remove_item["text"] = "Clear Items"
        self.btn_remove_item.place(x=50, y=500, width=400, height=50)
        self.btn_remove_item["command"] = self.btn_remove_item_command

        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        
        """
        Loading Items into the Menu
        """
        i.execute("SELECT * FROM items")
        INVENTORY = i.fetchall()
        items = [thisItem[1] for thisItem in INVENTORY]
        self.item_count = dict()
        for item in items:
            self.item_count[item] = 0
        self.clicked = tk.StringVar()
        self.clicked.set('Choose')
        self.item_list = tk.OptionMenu(root, self.clicked, *items)
        self.item_list['bg'] = btn_bg
        self.item_list['font'] = ft
        self.item_list['menu']['bg'] = btn_bg
        self.item_list.config(width=400)
        self.item_list.place(x=50, y=350, width=200, height=50)

        ft = tkFont.Font(family='Roboto', size=13, weight="bold")
        menu = root.nametowidget(self.item_list.menuname)
        menu.config(font=ft)

        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        qty = [1, 2, 3, 4, 5]
        self.clicked_qty = tk.IntVar()
        self.clicked_qty.set(1)
        self.qty_list = tk.OptionMenu(root, self.clicked_qty, *qty)
        self.qty_list['bg'] = btn_bg
        self.qty_list['font'] = ft
        self.qty_list['menu']['bg'] = btn_bg
        self.qty_list.config(width=400)
        self.qty_list.place(x=260, y=350, width=196, height=50)

        ft = tkFont.Font(family='Roboto', size=13, weight="bold")
        menu = root.nametowidget(self.item_list.menuname)
        menu.config(font=ft)

        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.btn_new_order = tk.Button(root)
        self.btn_new_order["bg"] = "#efefef"
        self.btn_new_order["font"] = ft
        self.btn_new_order["fg"] = "#000000"
        self.btn_new_order["justify"] = "center"
        self.btn_new_order["bg"] = btn_bg
        self.btn_new_order["text"] = "New Order"
        self.btn_new_order.place(x=50, y=570, width=400, height=50)
        self.btn_new_order["command"] = self.btn_new_order_command

        self.btn_prev_order = tk.Button(root)
        self.btn_prev_order["bg"] = "#efefef"
        self.btn_prev_order["font"] = ft
        self.btn_prev_order["fg"] = "#000000"
        self.btn_prev_order["justify"] = "center"
        self.btn_prev_order["bg"] = btn_bg
        self.btn_prev_order["text"] = "View Previous Orders"
        self.btn_prev_order.place(x=50, y=640, width=400, height=50)
        self.btn_prev_order["command"] = self.btn_prev_order_command

        self.btn_gen_receipt = tk.Button(root)
        self.btn_gen_receipt["bg"] = "#efefef"
        self.btn_gen_receipt["font"] = ft
        self.btn_gen_receipt["fg"] = "#000000"
        self.btn_gen_receipt["justify"] = "center"
        self.btn_gen_receipt["bg"] = btn_bg
        self.btn_gen_receipt["text"] = "Generate Receipt"
        self.btn_gen_receipt.place(x=500, y=640, width=380, height=50)
        self.btn_gen_receipt["command"] =  self.btn_gen_receipt_command
        #self.btn_gen_receipt["command"] =  self.btn_gen_receipt_command_part1

        self.receipt = tk.Label(root)
        self.receipt["font"] = ft
        self.receipt["fg"] = "white"
        self.receipt["justify"] = "center"
        self.receipt["bg"] = bg_panel
        self.receipt["text"] = "RECEIPT"
        #self.receipt.place(x=900, y=350, width=330, height=267)

        self.btn_print = tk.Button(root)
        self.btn_print["bg"] = "#efefef"
        self.btn_print["font"] = ft
        self.btn_print["fg"] = "#000000"
        self.btn_print["justify"] = "center"
        self.btn_print["bg"] = btn_bg
        self.btn_print["text"] = "Print Receipt"
        self.btn_print.place(x=900, y=640, width=160, height=50)
        self.btn_print["command"] = self.btn_print_command

        self.btn_logout = tk.Button(root)
        self.btn_logout["bg"] = "#efefef"
        self.btn_logout["font"] = ft
        self.btn_logout["fg"] = "#000000"
        self.btn_logout["justify"] = "center"
        self.btn_logout["bg"] = btn_bg
        self.btn_logout["text"] = "Log Out"
        self.btn_logout.place(x=1070, y=640, width=160, height=50)
        self.btn_logout["command"] = self.btn_logout_command
        
    
    def btn_add_item_command(self):
        itemChosen = self.clicked.get()
        if itemChosen == "Choose":
            messagebox.showerror("Error", "Choose an item")
        else:
            qty = self.clicked_qty.get()
            i.execute("SELECT price FROM items where name = (?)", (itemChosen, ))
            price = i.fetchone()[0]
            self.item_count[itemChosen] +=  qty
            self.list_item["state"] = tk.NORMAL
            
            self.list_item.delete(0,tk.END)
            
            for j in self.item_count:
                if self.item_count[j] != 0:
                    self.list_item.insert(tk.END, f"{j} - {self.item_count[j]} -- {price*self.item_count[j]}/-")
                
            self.list_item["state"] = tk.DISABLED

    def btn_remove_item_command(self):
        self.list_item["state"] = tk.NORMAL
        self.list_item.delete(0,tk.END)
        for i in self.item_count:
            self.item_count[i] = 0
        self.list_item["state"] = tk.DISABLED

    def btn_new_order_command(self):
        self.root.destroy()
        root = tk.Tk()
        app = SalesPanel(root)
        root.focus_force()
        root.mainloop()

    def btn_prev_order_command(self):
    
        o.execute("SELECT * FROM orders ORDER BY onum")
        data = o.fetchall()        
        htmlContent ='''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="shortcut icon" href="./icon/icon2.ico">
            <title> Order Database </title>
            <style> table, th, tr 
                { font-size: 30px; padding: 5px; }
                th {
                     border: 2px solid black;
                     background-color: #f9dbf1;
                    }
                table {
                    border: 5px solid black;
                    }
                body {
                     
                    font-family: "Arial";
                    }
            </style> 
        </head>
        <body>
            <table>
                <tr>
                    <th> Order Number </th>
                    <th> Customer Name </th>
                    <th> Customer Email </th>
                    <th> Total </th>
                </tr>
        '''
        with open('empData.html','w') as file:
            file.write(htmlContent)
            for record in data:
                code = f"<tr> <th> { record[0] } </th> <th> { record[1] } </th><th> { record[2] } </th> <th> { record[3] } </th> </tr>"
                file.write(code)
            file.write("</table> </body> </html>")
        import webbrowser
        webbrowser.open_new_tab('empData.html')        
        
    def validEmail(self,em):
        if em.count('@') != 1:
            return False
        i = em.index('@')
        domain = em[i+1:]
        if domain == "" or '.' not in domain or '.' == domain[-1] or '.' == domain[0]:
            return False
        return True        
    
    def btn_gen_receipt_command_part1(self):
        a = threading.Thread(target=self.btn_gen_receipt)
        a.daemon(True)
        a.start()    
    
    def btn_gen_receipt_command(self):
        name = self.name_customer.get()
        email = self.email_customer.get()
        
        if self.list_item.size() > 4:
            ft = tkFont.Font(family='Roboto', size=10, weight="bold")
            self.receipt["font"] = ft
        if not self.validEmail(email):
            messagebox.showerror("Error", "Invalid E-mail!")
        elif len(name)==0 or len(email)==0:
            messagebox("Error", "Fields cannot be empty")
        else:
            self.receipt["justify"] = "left"
            rec = f"-------------RECEIPT-------------\nName: {name}\nEmail: {email}\nServed By: {currEmp.Name}\n\nItem\tQty\tPrice"
            total =0
            # item_list = i.execute('select * from items').fetchall()
            
            item_list = self.list_item.get(0,tk.END) 
            
            for it in item_list:
                # rec += f"\n{it[0]}\t{it[1]}\t{it[2]}/-"
                # name - quantity - price
                temp = it.replace(' -- ','-').replace('/-','').replace(' - ','-').strip()
                item, count, total_price = temp.split('-')
                total_price = float(total_price)
                total += total_price
                rec += f"\n{item}\t{count}\t{total_price}/-"
        
            rec += f"\n-----------------\nTotal: {total}/- (Tax Inclusive)"
            self.receipt["text"] = rec
            
<<<<<<< Updated upstream
            frame = ttk.Frame(self.root, width=300, height=267)
            frame.grid(row = 900,column = 350)
            canvas = Canvas(frame)
            canvas.pack(side = tk.LEFT)
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
            scrollbar.pack(side = tk.RIGHT, fill = 'y')
            canvas.configure(yscrollcommand = scrollbar.set)
            canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas2 = ttk.Frame(canvas)
            canvas.create_window((0,0),window = canvas2, anchor = 'nw')
            ttk.Label(canvas2, text = self.receipt['text']).pack()
=======
            

>>>>>>> Stashed changes
            
            o.execute("INSERT INTO orders (cust_name, cust_email, total) VALUES (?, ?, ?)", (name, email, total))
            orderCon.commit()
            
            import smtplib
            from email.message import EmailMessage
            import socket
            socket.getaddrinfo('localhost', 465)
            
            msg = EmailMessage()
            msg["Subject"] = f"Your Order from {myRest.name}"
            msg["From"] = myRest.name
            msg["To"] = email  
            msg.set_content(self.receipt.cget("text"))
            
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("restrolabs@gmail.com", "Restro@labs123")
            server.send_message(msg)
            server.quit()
            
            self.name_customer['state'] = 'disabled'            
            self.email_customer['state'] = 'disabled'  
            top = Toplevel(self.root)
            top.title("View Receipt")
            width = 400
            height = 267
            screenwidth = top.winfo_screenwidth()
            screenheight = top.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
            top.geometry(alignstr)
            top.resizable(width=False, height=False)
            top.configure(background=bg_main)
            frame = ttk.Frame(top, width=300, height=267)
            frame.grid(row = 900,column = 350)
            canvas = Canvas(frame)
            canvas.pack(side = tk.LEFT)
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
            scrollbar.pack(side = tk.RIGHT, fill = 'y')
            canvas.configure(yscrollcommand = scrollbar.set)
            canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas2 = ttk.Frame(canvas)
            canvas.create_window((0,0),window = canvas2, anchor = 'nw')
            ttk.Label(canvas2, text = self.receipt['text']).pack()
            top.attributes('-topmost', 1)
            top.focus_force()
            top.mainloop()
            
            
            
        
    def btn_print_command(self):
        
        import tempfile
        file = tempfile.mktemp(".txt")
        open(file, "w").write(self.receipt.cget("text"))
        os.startfile(file, "print")

    def btn_logout_command(self):
        self.root.destroy()
        root = tk.Tk()
        app = Login(root)
        root.focus_force()
        root.mainloop()

class ManageAdmin:
    def __init__(self, root):
        global bg_main
        global btn_bg
        global bg_panel
        global fg_panel

        self.window = root
        root.title("Manage Admin Panel")
        width = 988
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background=bg_main)

        self.manage_admin_head = tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=50, weight="bold")
        self.manage_admin_head["font"] = ft
        self.manage_admin_head["fg"] = fg_panel
        self.manage_admin_head["bg"] = bg_panel
        self.manage_admin_head["justify"] = "center"
        self.manage_admin_head["text"] = "Manage Admin"
        self.manage_admin_head.place(x=0, y=0, width=990, height=110)

        self.btn_view_report = tk.Button(root)
        self.btn_view_report["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_view_report["font"] = ft
        self.btn_view_report["fg"] = "#000000"
        self.btn_view_report["bg"] = btn_bg
        self.btn_view_report["justify"] = "center"
        self.btn_view_report["text"] = "View Admin DataBase"
        self.btn_view_report.place(x=350, y=120, width=270, height=40)
        self.btn_view_report["command"] = self.btn_view_report_command

        self.label_add_admin = tk.Label(root)
        self.label_add_admin["font"] = ft
        self.label_add_admin["fg"] = "#333333"
        self.label_add_admin["bg"] = bg_main
        self.label_add_admin["justify"] = "center"
        self.label_add_admin["text"] = "Add Admin"
        self.label_add_admin.place(x=160, y=150, width=189, height=50)

        self.label_delete = tk.Label(root)
        self.label_delete["font"] = ft
        self.label_delete["fg"] = "#333333"
        self.label_delete["bg"] = bg_main
        self.label_delete["justify"] = "center"
        self.label_delete["text"] = "Delete Admin"
        self.label_delete.place(x=630, y=150, width=237, height=52)

        self.label_add_name = tk.Label(root)
        self.label_add_name["font"] = ft
        self.label_add_name["fg"] = "#333333"
        self.label_add_name["bg"] = bg_main
        self.label_add_name["justify"] = "center"
        self.label_add_name["text"] = "Name:"
        self.label_add_name.place(x=60, y=230, width=115, height=40)

        self.label_add_username = tk.Label(root)
        self.label_add_username["font"] = ft
        self.label_add_username["fg"] = "#333333"
        self.label_add_username["bg"] = bg_main
        self.label_add_username["justify"] = "center"
        self.label_add_username["text"] = "Username:"
        self.label_add_username.place(x=10, y=290, width=156, height=40)

        self.label_password = tk.Label(root)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["bg"] = bg_main
        self.label_password["justify"] = "center"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=10, y=360, width=164, height=40)

        self.label_confirm_password = tk.Label(root)
        self.label_confirm_password["font"] = ft
        self.label_confirm_password["fg"] = "#333333"
        self.label_confirm_password["bg"] = bg_main
        self.label_confirm_password["justify"] = "center"
        self.label_confirm_password["text"] = "Enter your password to confirm"
        self.label_confirm_password.place(x=240, y=420, width=464, height=40)

        self.label_delete_username = tk.Label(root)
        self.label_delete_username["font"] = ft
        self.label_delete_username["fg"] = "#333333"
        self.label_delete_username["bg"] = bg_main
        self.label_delete_username["justify"] = "center"
        self.label_delete_username["text"] = "Username"
        self.label_delete_username.place(x=670, y=240, width=156, height=40)

        self.add_name = tk.Entry(root)
        self.add_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_name["font"] = ft
        self.add_name["fg"] = "#333333"
        self.add_name["justify"] = "left"
        self.add_name["text"] = ""
        self.add_name.place(x=190, y=230, width=250, height=33)
        self.add_name.focus()

        self.delete_username = tk.Entry(root)
        self.delete_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.delete_username["font"] = ft
        self.delete_username["fg"] = "#333333"
        self.delete_username["justify"] = "left"
        self.delete_username["text"] = ""
        self.delete_username.place(x=590, y=290, width=350, height=33)

        self.add_username = tk.Entry(root)
        self.add_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_username["font"] = ft
        self.add_username["fg"] = "#333333"
        self.add_username["justify"] = "left"
        self.add_username["text"] = ""
        self.add_username.place(x=190, y=290, width=250, height=33)

        self.add_password = tk.Entry(root)
        self.add_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_password["font"] = ft
        self.add_password["fg"] = "#333333"
        self.add_password["justify"] = "left"
        self.add_password["text"] = ""
        self.add_password["show"] = "*"
        self.add_password.place(x=190, y=360, width=250, height=33)

        self.admin_confirm_password = tk.Entry(root)
        self.admin_confirm_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.admin_confirm_password["font"] = ft
        self.admin_confirm_password["fg"] = "#333333"
        self.admin_confirm_password["justify"] = "left"
        self.admin_confirm_password["text"] = ""
        self.admin_confirm_password["show"] = "*"
        self.admin_confirm_password.place(x=250, y=480, width=450, height=30)

        self.btn_add = tk.Button(root)
        self.btn_add["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_add["font"] = ft
        self.btn_add["fg"] = "#000000"
        self.btn_add["bg"] = btn_bg
        self.btn_add["justify"] = "center"
        self.btn_add["text"] = "Add"
        self.btn_add.place(x=270, y=530, width=180, height=30)
        self.btn_add["command"] = self.btn_add_command

        self.btn_delete = tk.Button(root)
        self.btn_delete["bg"] = "#efefef"
        self.btn_delete["font"] = ft
        self.btn_delete["fg"] = "#000000"
        self.btn_delete["bg"] = btn_bg
        self.btn_delete["justify"] = "center"
        self.btn_delete["text"] = "Delete"
        self.btn_delete.place(x=500, y=530, width=180, height=30)
        self.btn_delete["command"] = self.btn_delete_command

    def btn_add_command(self):
        global currAdmin

        name = self.add_name.get()
        user = self.add_username.get()
        pas = self.add_password.get()

        selfPas = self.admin_confirm_password.get()
        if len(name) == 0 or len(user) == 0 or len(pas) == 0 or len(selfPas) == 0:
            tk.messagebox.showerror("Error", "Fields Cannot be Empty")
        else:
            
            a.execute("SELECT * FROM admin WHERE username = (?)", (user, ))
            exist = a.fetchone()
            if exist == None:
                if selfPas == currAdmin.password:
                    choice = messagebox.askyesno(
                        "Confirm", "Do you want to proceed?")
                    if choice:
                        
                        a.execute("INSERT INTO admin VALUES (?, ?, ?)",
                                  (name, user, pas))
                        adminCon.commit()
                        messagebox.showinfo(
                            "Success!", "New Admin Succesfully Created")
                        self.window.destroy()
                else:
                    tk.messagebox.showerror("Error", "Wrong Password")
            else:
                messagebox.showerror(
                    "Error", "Admin with username exists already!")

    def btn_delete_command(self):
        global currAdmin

        user = self.delete_username.get()
        selfPas = self.admin_confirm_password.get()

        if len(user) == 0 or len(selfPas) == 0:
            tk.messagebox.showerror("Error", "Fields Cannot be Empty")
        else:
            
            a.execute("SELECT * FROM admin WHERE username = (?)", (user, ))
            exist = a.fetchone()

            if exist != None:
                if currAdmin.username == exist[1]:
                    messagebox.showerror(
                        "Error!", "Admin Logged in currently. Can not proceed")
                else:
                    if selfPas == currAdmin.password:
                        choice = messagebox.askyesno(
                            "Confirm", "Do you want to proceed?")
                        if choice:
                            
                            a.execute(
                                "DELETE FROM admin WHERE username = (?)", (user, ))
                            adminCon.commit()
                            messagebox.showinfo(
                                "Success!", "Admin Records Deleted")
                            self.window.destroy()
                    else:
                        tk.messagebox.showerror("Error", "Wrong Password")
            else:
                messagebox.showerror(
                    "Error", "Admin with username does not exist!")

    def btn_view_report_command(self):

        
        a.execute("SELECT name, username FROM admin ORDER BY name ASC")
        data = a.fetchall()        
        htmlContent ='''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="shortcut icon" href="./icon/icon.ico">
            <title> Admin Database </title>
            <style> table, th, tr 
                { font-size: 30px; padding: 5px; }
                th {
                     border: 2px solid black;
                     background-color: #f9dbf1;
                    }
                table {
                    border: 5px solid black;
                    }
                body {
                     
                    font-family: "Arial";
                    }
            </style> 
        </head>
        <body>
            <table>
                <tr>
                    <th> NAME </th>
                    <th> USERNAME </th>
                </tr>
        '''
        with open('adminData.html','w') as file:
            file.write(htmlContent)
            for record in data:
                code = f"<tr> <th> { record[0] } </th> <th> { record[1] } </th> </tr>"
                file.write(code)
            file.write("</table> </body> </html>")
        import webbrowser
        webbrowser.open_new_tab('adminData.html')


class ManageEmployee:
    def __init__(self, root):
        global bg_main
        global btn_bg
        global bg_panel
        global fg_panel

        self.window = root
        root.title("Manage Employee Panel")
        width = 988
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background=bg_main)

        self.manage_admin_head = tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=50, weight="bold")
        self.manage_admin_head["font"] = ft
        self.manage_admin_head["fg"] = fg_panel
        self.manage_admin_head["bg"] = bg_panel
        self.manage_admin_head["justify"] = "center"
        self.manage_admin_head["text"] = "Manage Employee"
        self.manage_admin_head.place(x=0, y=0, width=990, height=110)

        self.btn_view_report = tk.Button(root)
        self.btn_view_report["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_view_report["font"] = ft
        self.btn_view_report["fg"] = "#000000"
        self.btn_view_report["bg"] = btn_bg
        self.btn_view_report["justify"] = "center"
        self.btn_view_report["text"] = "View Database"
        self.btn_view_report.place(x=370, y=120, width=214, height=40)
        self.btn_view_report["command"] = self.btn_view_report_command

        self.label_add_admin = tk.Label(root)
        self.label_add_admin["font"] = ft
        self.label_add_admin["fg"] = "#333333"
        self.label_add_admin["bg"] = bg_main
        self.label_add_admin["justify"] = "center"
        self.label_add_admin["text"] = "Add Employee"
        self.label_add_admin.place(x=160, y=150, width=189, height=50)
        
        self.label_delete = tk.Label(root)
        self.label_delete["font"] = ft
        self.label_delete["fg"] = "#333333"
        self.label_delete["bg"] = bg_main
        self.label_delete["justify"] = "center"
        self.label_delete["text"] = "Delete Employee"
        self.label_delete.place(x=630, y=150, width=237, height=52)

        self.label_add_name = tk.Label(root)
        self.label_add_name["font"] = ft
        self.label_add_name["fg"] = "#333333"
        self.label_add_name["bg"] = bg_main
        self.label_add_name["justify"] = "center"
        self.label_add_name["text"] = "Name:"
        self.label_add_name.place(x=60, y=230, width=115, height=40)

        self.label_add_username = tk.Label(root)
        self.label_add_username["font"] = ft
        self.label_add_username["fg"] = "#333333"
        self.label_add_username["bg"] = bg_main
        self.label_add_username["justify"] = "center"
        self.label_add_username["text"] = "Username:"
        self.label_add_username.place(x=10, y=290, width=156, height=40)
        
        self.lable_ecode = tk.Label(root)
        self.lable_ecode["font"] = ft
        self.lable_ecode["fg"] = "#333333"
        self.lable_ecode["bg"] = bg_main
        self.lable_ecode["justify"] = "center"
        self.lable_ecode["text"] = "Employee Code:"
        self.lable_ecode.place(x=10, y=350, width=170, height=40)

        self.label_password = tk.Label(root)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["bg"] = bg_main
        self.label_password["justify"] = "center"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=10, y=410, width=164, height=40)

        self.label_confirm_password = tk.Label(root)
        self.label_confirm_password["font"] = ft
        self.label_confirm_password["fg"] = "#333333"
        self.label_confirm_password["bg"] = bg_main
        self.label_confirm_password["justify"] = "center"
        self.label_confirm_password["text"] = "Enter your password to confirm"
        self.label_confirm_password.place(x=240, y=460, width=464, height=40)

        self.label_delete_username = tk.Label(root)
        self.label_delete_username["font"] = ft
        self.label_delete_username["fg"] = "#333333"
        self.label_delete_username["bg"] = bg_main
        self.label_delete_username["justify"] = "center"
        self.label_delete_username["text"] = "Username"
        self.label_delete_username.place(x=670, y=240, width=156, height=40)

        self.add_name = tk.Entry(root)
        self.add_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_name["font"] = ft
        self.add_name["fg"] = "#333333"
        self.add_name["justify"] = "left"
        self.add_name["text"] = ""
        self.add_name.place(x=190, y=230, width=250, height=33)
        self.add_name.focus()

        self.add_username = tk.Entry(root)
        self.add_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_username["font"] = ft
        self.add_username["fg"] = "#333333"
        self.add_username["justify"] = "left"
        self.add_username["text"] = ""
        self.add_username.place(x=190, y=290, width=250, height=33)

        self.add_emp_ecode = tk.Entry(root)
        self.add_emp_ecode["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_emp_ecode["font"] = ft
        self.add_emp_ecode["fg"] = "#333333"
        self.add_emp_ecode["justify"] = "left"
        self.add_emp_ecode["text"] = ""
        self.add_emp_ecode.place(x=190, y=360, width=250, height=33)

        self.add_password = tk.Entry(root)
        self.add_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_password["font"] = ft
        self.add_password["fg"] = "#333333"
        self.add_password["justify"] = "left"
        self.add_password["text"] = ""
        self.add_password["show"] = "*"
        self.add_password.place(x=190, y=410, width=250, height=33)
        
        self.delete_username = tk.Entry(root)
        self.delete_username["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.delete_username["font"] = ft
        self.delete_username["fg"] = "#333333"
        self.delete_username["justify"] = "left"
        self.delete_username["text"] = ""
        self.delete_username.place(x=590, y=290, width=350, height=33)
        
        self.admin_confirm_password = tk.Entry(root)
        self.admin_confirm_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.admin_confirm_password["font"] = ft
        self.admin_confirm_password["fg"] = "#333333"
        self.admin_confirm_password["justify"] = "left"
        self.admin_confirm_password["text"] = ""
        self.admin_confirm_password["show"] = "*"
        self.admin_confirm_password.place(x=250, y=500, width=450, height=30)
        
        self.btn_add = tk.Button(root)
        self.btn_add["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_add["font"] = ft
        self.btn_add["fg"] = "#000000"
        self.btn_add["bg"] = btn_bg
        self.btn_add["justify"] = "center"
        self.btn_add["text"] = "Add"
        self.btn_add.place(x=270, y=540, width=180, height=30)
        self.btn_add["command"] = self.btn_add_command

        self.btn_delete = tk.Button(root)
        self.btn_delete["bg"] = "#efefef"
        self.btn_delete["font"] = ft
        self.btn_delete["fg"] = "#000000"
        self.btn_delete["bg"] = btn_bg
        self.btn_delete["justify"] = "center"
        self.btn_delete["text"] = "Delete"
        self.btn_delete.place(x=500, y=540, width=180, height=30)
        self.btn_delete["command"] = self.btn_delete_command

    def btn_add_command(self):
        name = self.add_name.get()
        user = self.add_username.get()
        pas = self.add_password.get()
        ecode = self.add_emp_ecode.get()

        selfPas = self.admin_confirm_password.get()
        
        if len(name) == 0 or len(user) == 0 or len(pas) == 0 or len(selfPas) == 0:
            tk.messagebox.showerror("Error", "Fields Cannot be Empty")
        else:
            
            e.execute("SELECT * FROM employee WHERE username = (?)", (user, ))
            exist = e.fetchone()
            if exist == None:
                if selfPas == currAdmin.password:
                    choice = messagebox.askyesno(
                        "Confirm", "Do you want to proceed?")
                    if choice:
                        
                        e.execute("INSERT INTO employee VALUES (?, ?, ?,?)",
                                  (ecode,name, user, pas))
                        empCon.commit()
                        messagebox.showinfo(
                            "Success!", "New Employee Succesfully Created")
                        self.window.destroy()
                else:
                    tk.messagebox.showerror("Error", "Wrong Password")
            else:
                messagebox.showerror(
                    "Error", "Employee with username exists already!")

    def btn_view_report_command(self):
       
        e.execute("SELECT * FROM employee ORDER BY name ASC")
        data = e.fetchall()        
        htmlContent ='''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="shortcut icon" href="./icon/icon.ico">
            <title> Employee Database </title>
            <style> table, th, tr 
                { font-size: 30px; padding: 5px; }
                th {
                     border: 2px solid black;
                     background-color: #f9dbf1;
                    }
                table {
                    border: 5px solid black;
                    }
                body {
                     
                    font-family: "Arial";
                    }
            </style> 
        </head>
        <body>
            <table>
                <tr>
                    <th> Employee Code </th>
                    <th> NAME </th>
                    <th> USERNAME </th>
                </tr>
        '''
        with open('empData.html','w') as file:
            file.write(htmlContent)
            for record in data:
                code = f"<tr> <th> { record[0] } </th> <th> { record[1] } </th><th> { record[2] } </th> </tr>"
                file.write(code)
            file.write("</table> </body> </html>")
        import webbrowser
        webbrowser.open_new_tab('empData.html')

    def btn_delete_command(self):
        global currAdmin
        user = self.delete_username.get()
        selfPas = self.admin_confirm_password.get()

        if len(user) == 0 or len(selfPas) == 0:
            tk.messagebox.showerror("Error", "Fields Cannot be Empty")
        else:
            
            e.execute("SELECT * FROM employee WHERE username = (?)", (user, ))
            exist = e.fetchone()

            if exist != None:
                
                if selfPas == currAdmin.password:
                    choice = messagebox.askyesno(
                        "Confirm", "Do you want to proceed?")
                    if choice:
                        
                        e.execute(
                            "DELETE FROM employee WHERE username = (?)", (user, ))
                        empCon.commit()
                        messagebox.showinfo(
                            "Success!", "Employee Records Deleted")
                        self.window.destroy()
                else:
                    tk.messagebox.showerror("Error", "Wrong Password")
            else:
                messagebox.showerror(
                    "Error", "Employee with username does not exist!")

class ManageItem:
    def __init__(self, root):
        global bg_main
        global btn_bg
        global bg_panel
        global fg_panel

        self.window = root
        root.title("Manage Items Panel")
        width = 988
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background=bg_main)

        self.manage_admin_head = tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=50, weight="bold")
        self.manage_admin_head["font"] = ft
        self.manage_admin_head["fg"] = fg_panel
        self.manage_admin_head["bg"] = bg_panel
        self.manage_admin_head["justify"] = "center"
        self.manage_admin_head["text"] = "Manage Items"
        self.manage_admin_head.place(x=0, y=0, width=990, height=110)

        self.btn_view_report = tk.Button(root)
        self.btn_view_report["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_view_report["font"] = ft
        self.btn_view_report["fg"] = "#000000"
        self.btn_view_report["bg"] = btn_bg
        self.btn_view_report["justify"] = "center"
        self.btn_view_report["text"] = "View Database"
        self.btn_view_report.place(x=370, y=120, width=214, height=40)
        self.btn_view_report["command"] = self.btn_view_report_command

        self.label_add_admin = tk.Label(root)
        self.label_add_admin["font"] = ft
        self.label_add_admin["fg"] = "#333333"
        self.label_add_admin["bg"] = bg_main
        self.label_add_admin["justify"] = "center"
        self.label_add_admin["text"] = "Add Item"
        self.label_add_admin.place(x=160, y=150, width=189, height=50)

        self.label_delete = tk.Label(root)
        self.label_delete["font"] = ft
        self.label_delete["fg"] = "#333333"
        self.label_delete["bg"] = bg_main
        self.label_delete["justify"] = "center"
        self.label_delete["text"] = "Delete Item"
        self.label_delete.place(x=630, y=150, width=237, height=52)

        self.label_add_name = tk.Label(root)
        self.label_add_name["font"] = ft
        self.label_add_name["fg"] = "#333333"
        self.label_add_name["bg"] = bg_main
        self.label_add_name["justify"] = "center"
        self.label_add_name["text"] = "Name:"
        self.label_add_name.place(x=60, y=230, width=115, height=40)

        self.label_add_username = tk.Label(root)
        self.label_add_username["font"] = ft
        self.label_add_username["fg"] = "#333333"
        self.label_add_username["bg"] = bg_main
        self.label_add_username["justify"] = "center"
        self.label_add_username["text"] = "Item Code:"
        self.label_add_username.place(x=10, y=290, width=156, height=40)
        
        self.lable_ecode = tk.Label(root)
        self.lable_ecode["font"] = ft
        self.lable_ecode["fg"] = "#333333"
        self.lable_ecode["bg"] = bg_main
        self.lable_ecode["justify"] = "center"
        self.lable_ecode["text"] = "Price:"
        self.lable_ecode.place(x=10, y=350, width=170, height=40)
        
        self.label_confirm_password = tk.Label(root)
        self.label_confirm_password["font"] = ft
        self.label_confirm_password["fg"] = "#333333"
        self.label_confirm_password["bg"] = bg_main
        self.label_confirm_password["justify"] = "center"
        self.label_confirm_password["text"] = "Enter your password to confirm"
        self.label_confirm_password.place(x=240, y=460, width=464, height=40)

        self.label_delete_username = tk.Label(root)
        self.label_delete_username["font"] = ft
        self.label_delete_username["fg"] = "#333333"
        self.label_delete_username["bg"] = bg_main
        self.label_delete_username["justify"] = "center"
        self.label_delete_username["text"] = "Item Code"
        self.label_delete_username.place(x=670, y=240, width=156, height=40)
        
        self.add_name = tk.Entry(root)
        self.add_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_name["font"] = ft
        self.add_name["fg"] = "#333333"
        self.add_name["justify"] = "left"
        self.add_name["text"] = ""
        self.add_name.place(x=190, y=230, width=250, height=33)
        self.add_name.focus()

        self.add_icode = tk.Entry(root)
        self.add_icode["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_icode["font"] = ft
        self.add_icode["fg"] = "#333333"
        self.add_icode["justify"] = "left"
        self.add_icode["text"] = ""
        self.add_icode.place(x=190, y=290, width=250, height=33)

        self.add_price = tk.Entry(root)
        self.add_price["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_price["font"] = ft
        self.add_price["fg"] = "#333333"
        self.add_price["justify"] = "left"
        self.add_price["text"] = ""
        self.add_price.place(x=190, y=360, width=250, height=33)
        
        self.delete_icode = tk.Entry(root)
        self.delete_icode["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.delete_icode["font"] = ft
        self.delete_icode["fg"] = "#333333"
        self.delete_icode["justify"] = "left"
        self.delete_icode["text"] = ""
        self.delete_icode.place(x=590, y=290, width=350, height=33)
        
        self.admin_confirm_password = tk.Entry(root)
        self.admin_confirm_password["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.admin_confirm_password["font"] = ft
        self.admin_confirm_password["fg"] = "#333333"
        self.admin_confirm_password["justify"] = "left"
        self.admin_confirm_password["text"] = ""
        self.admin_confirm_password["show"] = "*"
        self.admin_confirm_password.place(x=250, y=500, width=450, height=30)
        
        self.btn_add = tk.Button(root)
        self.btn_add["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_add["font"] = ft
        self.btn_add["fg"] = "#000000"
        self.btn_add["bg"] = btn_bg
        self.btn_add["justify"] = "center"
        self.btn_add["text"] = "Add"
        self.btn_add.place(x=270, y=540, width=180, height=30)
        self.btn_add["command"] = self.btn_add_command

        self.btn_delete = tk.Button(root)
        self.btn_delete["bg"] = "#efefef"
        self.btn_delete["font"] = ft
        self.btn_delete["fg"] = "#000000"
        self.btn_delete["bg"] = btn_bg
        self.btn_delete["justify"] = "center"
        self.btn_delete["text"] = "Delete"
        self.btn_delete.place(x=500, y=540, width=180, height=30)
        self.btn_delete["command"] = self.btn_delete_command

    def btn_add_command(self):
        name = self.add_name.get()
        icode = self.add_icode.get()
        try:    
            price = int(self.add_price.get())
            selfprice = self.admin_confirm_password.get()
            if len(name) == 0 or len(icode) == 0 or len(selfprice) == 0:
                tk.messagebox.showerror("Error", "Fields Cannot be Empty")  
            else:
                
                i.execute("SELECT * FROM items WHERE icode = (?)", (icode, ))
                exist = i.fetchone()
                if exist == None:
                    name_isPresent = i.execute("SELECT * from items where name = (?)",(name, )).fetchone()
                    if name_isPresent == None:
                        if selfprice == currAdmin.password:
                            choice = messagebox.askyesno(
                                "Confirm", "Do you want to proceed?")
                            if choice:
                                
                                i.execute("INSERT INTO items VALUES (?, ?, ?)",
                                        (icode, name, price))
                                itemCon.commit()
                                messagebox.showinfo(
                                    "Success!", "New Item Succesfully Created")
                        else:
                            tk.messagebox.showerror("Error", "Wrong password")
                    else:
                        tk.messagebox.showerror("Error",'Item with same name already exists')
                    
                else:
                    messagebox.showerror(
                        "Error", "Item with icode exists already!")
        except:
            messagebox.showerror("Error", "Price Has to be a valid number.")
        
        self.window.destroy()

    def btn_view_report_command(self):
        
        i.execute("SELECT * FROM items ORDER BY icode ASC")
        data = i.fetchall()        
        htmlContent ='''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="shortcut icon" href="./icon/icon2.ico">
            <title> Item Database </title>
            <style> table, th, tr 
                { font-size: 30px; padding: 5px; }
                th {
                     border: 2px solid black;
                     background-color: #f9dbf1;
                    }
                table {
                    border: 5px solid black;
                    }
                body {
                     
                    font-family: "Arial";
                    }
            </style> 
        </head>
        <body>
            <table>
                <tr>
                    <th> Item Code </th>
                    <th> Name </th>
                    <th> Price </th>
                </tr>
        '''
        with open('itemData.html','w') as file:
            file.write(htmlContent)
            for record in data:
                code = f"<tr> <th> { record[0] } </th> <th> { record[1] } </th><th> { record[2] } </th> </tr>"
                file.write(code)
            file.write("</table> </body> </html>")
        import webbrowser
        webbrowser.open_new_tab('itemData.html')

    def btn_delete_command(self):
        global currAdmin
        icode = self.delete_icode.get()
        selfPas = self.admin_confirm_password.get()

        if len(icode) == 0 or len(selfPas) == 0:
            tk.messagebox.showerror("Error", "Fields Cannot be Empty")
        else:
            
            i.execute("SELECT * FROM items WHERE icode = (?)", (icode, ))
            exist = i.fetchone()

            if exist != None:
                
                if selfPas == currAdmin.password:
                    choice = messagebox.askyesno(
                        "Confirm", "Do you want to proceed?")
                    if choice:
                        
                        i.execute(
                            "DELETE FROM items WHERE icode = (?)", (icode, ))
                        itemCon.commit()
                        messagebox.showinfo(
                            "Success!", "Item Record Deleted")
                        self.window.destroy()
                else:
                    tk.messagebox.showerror("Error", "Wrong Password")
            else:
                messagebox.showerror(
                    "Error", "Item with Icode does not exist!")

class ResetDatabase:
    def __init__(self, root):
        
        global bg_main
        global btn_bg
        global bg_panel
        global fg_panel

        self.window = root

        ft = tkFont.Font(family='Roboto', size=25, weight = "bold")

        root.title("Restraunt Management System")
        width = 750
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background=bg_main)
        
        self.title_bar = tk.Label(root)
        self.title_bar["font"] = ft
        self.title_bar["fg"] = fg_panel
        self.title_bar["bg"] = bg_panel
        self.title_bar["justify"] = "center"
        self.title_bar["text"] = "RESET DATABASE"
        self.title_bar.place(x=0, y=0, width=750, height=80)
        
        ft = tkFont.Font(family='Roboto', size=18, weight = "bold")
        self.info_bar = tk.Label(root)
        self.info_bar["font"] = ft
        self.info_bar["fg"] = "#000000"
        self.info_bar["bg"] = bg_main
        self.info_bar["justify"] = "left"
        self.info_bar["wraplength"] = 700
        self.info_bar["text"] = "NOTE: This will reset all files, i.e., clear all the data in them and you will enter STARTUP MODE. The database can not be retreived once cleaned."
        self.info_bar.place(x=0, y=100, width=750, height=100)
        
        self.password_label = tk.Label(root)
        self.password_label["font"] = ft
        self.password_label["fg"] = "#000000"
        self.password_label["bg"] = bg_main
        self.password_label["justify"] = "center"
        self.password_label["text"] = "Enter Admin Password"
        self.password_label.place(x=248, y = 240, height = 30)
        
        self.password = tk.Entry(root)
        self.password["borderwidth"] = "1px"
        self.password["font"] = ft
        self.password["fg"] = "#333333"
        self.password["text"] = "Password"
        self.password["show"] = "*"
        self.password.place(x=208, y=280, width=335, height=30)
        
        ft = tkFont.Font(family='Roboto', size=15, weight = "bold")
        self.rest_btn = tk.Button(root)
        self.rest_btn["bg"] = btn_bg
        self.rest_btn["font"] = ft
        self.rest_btn["fg"] = "black"
        self.rest_btn["justify"] = "center"
        self.rest_btn["text"] = "RESET DATABASE"
        self.rest_btn.place(x=208, y=340, width=335, height=40)
        self.rest_btn["command"] = self.reset_btn_command
        
    def reset_btn_command(self):
        import os
        import sys
        import shutil
        
        pas = self.password.get()
        if pas == currAdmin.password:
            ans = messagebox.askyesno("Proceed", "Do you want to Continue?")
            if ans:
                
                a.close()
                e.close()
                i.close()
                o.close()
                r.close()
                
                adminCon.close()
                empCon.close()
                itemCon.close()
                orderCon.close()
                restCon.close()

                shutil.rmtree("Database")
                
                messagebox.showinfo("Success", "All files succesfully deleted!")
                self.window.destroy()
                
        else:
            messagebox.showerror("Error", "Wrong Password")
    
class StartUp:
    def __init__(self, root):
        
        global bg_main
        global btn_bg
        global bg_panel
        global fg_panel

        self.window = root

        ft = tkFont.Font(family='Roboto', size=25, weight = "bold")

        root.title("Restraunt Management System")
        width = 1200
        height = 700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)        
        root.configure(background=bg_main)

        self.label_panel=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=50, weight="bold")
        self.label_panel["font"] = ft
        self.label_panel["fg"] = fg_panel
        self.label_panel["bg"] = bg_panel
        self.label_panel["justify"] = "center"
        self.label_panel["text"] = "STARTUP MODE"
        self.label_panel.place(x=0,y=0,width=1200,height=90)

        self.label_heading=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=20)
        self.label_heading["font"] = ft
        self.label_heading["fg"] = "#333333"
        self.label_heading["bg"] = bg_main
        self.label_heading["justify"] = "center"
        self.label_heading["text"] = "Enter the following details To Setup you software"
        self.label_heading["wraplength"] = 1100
        self.label_heading.place(x=0,y=100,width=1200,height=50)

        self.label_admin=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=30)
        self.label_admin["font"] = ft
        self.label_admin["fg"] = "#333333"
        self.label_admin["bg"] = bg_main
        self.label_admin["justify"] = "center"
        self.label_admin["text"] = "Admin"
        self.label_admin.place(x=60,y=170,width=280,height=30)

        self.label_restaurant=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=30)
        self.label_restaurant["font"] = ft
        self.label_restaurant["fg"] = "#333333"
        self.label_restaurant["bg"] = bg_main
        self.label_restaurant["justify"] = "center"
        self.label_restaurant["text"] = "Restaurant"
        self.label_restaurant.place(x=790,y=170,width=260,height=30)

        self.label_name_admin=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_name_admin["font"] = ft
        self.label_name_admin["fg"] = "#333333"
        self.label_name_admin["bg"] = bg_main
        self.label_name_admin["justify"] = "center"
        self.label_name_admin["text"] = "Name: "
        self.label_name_admin.place(x=70,y=210,width=126,height=48)

        self.name_admin=tk.Entry(root)
        self.name_admin["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.name_admin["font"] = ft
        self.name_admin["fg"] = "#333333"
        self.name_admin["justify"] = "left"
        self.name_admin["text"] = ""
        self.name_admin.place(x=220,y=220,width=305,height=30)

        self.label_username_admin=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_username_admin["font"] = ft
        self.label_username_admin["fg"] = "#333333"
        self.label_username_admin["bg"] = bg_main
        self.label_username_admin["justify"] = "center"
        self.label_username_admin["text"] = "UserName:"
        self.label_username_admin.place(x=10,y=260,width=196,height=48)

        self.username_admin=tk.Entry(root)
        self.username_admin["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.username_admin["font"] = ft
        self.username_admin["fg"] = "#333333"
        self.username_admin["justify"] = "left"
        self.username_admin["text"] = ""
        self.username_admin.place(x=220,y=270,width=305,height=30)

        self.label_password_admin=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_password_admin["font"] = ft
        self.label_password_admin["fg"] = "#333333"
        self.label_password_admin["bg"] = bg_main
        self.label_password_admin["justify"] = "center"
        self.label_password_admin["text"] = "Password:"
        self.label_password_admin.place(x=30,y=310,width=162,height=48)

        self.password_admin=tk.Entry(root)
        self.password_admin["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.password_admin["font"] = ft
        self.password_admin["fg"] = "#333333"
        self.password_admin["justify"] = "left"
        self.password_admin["text"] = ""
        self.password_admin["show"] = "*"
        self.password_admin.place(x=220,y=320,width=305,height=30)

        self.label_employee=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=30)
        self.label_employee["font"] = ft
        self.label_employee["fg"] = "#333333"
        self.label_employee["bg"] = bg_main
        self.label_employee["justify"] = "center"
        self.label_employee["text"] = "Employee"
        self.label_employee.place(x=90,y=360,width=206,height=50)

        self.label_ecode_employee=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_ecode_employee["font"] = ft
        self.label_ecode_employee["fg"] = "#333333"
        self.label_ecode_employee["bg"] = bg_main
        self.label_ecode_employee["justify"] = "center"
        self.label_ecode_employee["text"] = "ECode:"
        self.label_ecode_employee.place(x=70,y=420,width=129,height=50)

        self.ecode_employee=tk.Entry(root)
        self.ecode_employee["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.ecode_employee["font"] = ft
        self.ecode_employee["fg"] = "#333333"
        self.ecode_employee["justify"] = "left"
        self.ecode_employee["text"] = ""
        self.ecode_employee.place(x=220,y=430,width=305,height=30)

        self.label_name_employee=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_name_employee["font"] = ft
        self.label_name_employee["fg"] = "#333333"
        self.label_name_employee["bg"] = bg_main
        self.label_name_employee["justify"] = "center"
        self.label_name_employee["text"] = "Name:"
        self.label_name_employee.place(x=80,y=470,width=110,height=40)

        self.name_employee=tk.Entry(root)
        self.name_employee["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.name_employee["font"] = ft
        self.name_employee["fg"] = "#333333"
        self.name_employee["justify"] = "left"
        self.name_employee["text"] = ""
        self.name_employee.place(x=220,y=480,width=305,height=30)
       
        self.label_usernmae_employee=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_usernmae_employee["font"] = ft
        self.label_usernmae_employee["fg"] = "#333333"
        self.label_usernmae_employee["bg"] = bg_main
        self.label_usernmae_employee["justify"] = "center"
        self.label_usernmae_employee["text"] = "Username:"
        self.label_usernmae_employee.place(x=57,y=520,width=110,height=40)
        
        self.username_employee=tk.Entry(root)
        self.username_employee["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.username_employee["font"] = ft
        self.username_employee["fg"] = "#333333"
        self.username_employee["justify"] = "left"
        self.username_employee["text"] = ""
        self.username_employee.place(x=220,y=530,width=305,height=30)
        
        self.label_password_employee=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_password_employee["font"] = ft
        self.label_password_employee["fg"] = "#333333"
        self.label_password_employee["bg"] = bg_main
        self.label_password_employee["justify"] = "center"
        self.label_password_employee["text"] = "Password:"
        self.label_password_employee.place(x=30,y=570,width=160,height=40)

        self.password_employee=tk.Entry(root)
        self.password_employee["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.password_employee["font"] = ft
        self.password_employee["fg"] = "#333333"
        self.password_employee["justify"] = "left"
        self.password_employee["text"] = ""
        self.password_employee["show"] = "*"
        self.password_employee.place(x=220,y=580,width=305,height=30)

        self.btn_continue=tk.Button(root)
        self.btn_continue["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_continue["font"] = ft
        self.btn_continue["fg"] = "#000000"
        self.btn_continue["bg"] = btn_bg
        self.btn_continue["justify"] = "center"
        self.btn_continue["text"] = "Continue"
        self.btn_continue.place(x=400,y=650,width=368,height=41)
        self.btn_continue["command"] = self.btn_continue_command

        self.label_name_restaurant=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_name_restaurant["font"] = ft
        self.label_name_restaurant["fg"] = "#333333"
        self.label_name_restaurant["bg"] = bg_main
        self.label_name_restaurant["justify"] = "center"
        self.label_name_restaurant["text"] = "Name:"
        self.label_name_restaurant.place(x=670,y=210,width=126,height=48)

        self.name_restaurant=tk.Entry(root)
        self.name_restaurant["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.name_restaurant["font"] = ft
        self.name_restaurant["fg"] = "#333333"
        self.name_restaurant["justify"] = "left"
        self.name_restaurant["text"] = ""
        self.name_restaurant.place(x=830,y=220,width=305,height=30)

        self.label_address_restaurant=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_address_restaurant["font"] = ft
        self.label_address_restaurant["fg"] = "#333333"
        self.label_address_restaurant["bg"] = bg_main
        self.label_address_restaurant["justify"] = "center"
        self.label_address_restaurant["text"] = "Address:"
        self.label_address_restaurant.place(x=650,y=260,width=143,height=46)

        self.address_restaurant=tk.Entry(root)
        self.address_restaurant["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.address_restaurant["font"] = ft
        self.address_restaurant["fg"] = "#333333"
        self.address_restaurant["justify"] = "left"
        self.address_restaurant["text"] = ""
        self.address_restaurant.place(x=830,y=270,width=305,height=30)

        self.label_owner_restaurant=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_owner_restaurant["font"] = ft
        self.label_owner_restaurant["fg"] = "#333333"
        self.label_owner_restaurant["bg"] = bg_main
        self.label_owner_restaurant["justify"] = "center"
        self.label_owner_restaurant["text"] = "Owner:"
        self.label_owner_restaurant.place(x=660,y=310,width=125,height=53)

        self.owner_restaurant=tk.Entry(root)
        self.owner_restaurant["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.owner_restaurant["font"] = ft
        self.owner_restaurant["fg"] = "#333333"
        self.owner_restaurant["justify"] = "left"
        self.owner_restaurant["text"] = ""
        self.owner_restaurant.place(x=830,y=320,width=305,height=30)

        self.label_item_details=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=30)
        self.label_item_details["font"] = ft
        self.label_item_details["fg"] = "#333333"
        self.label_item_details["bg"] = bg_main
        self.label_item_details["justify"] = "center"
        self.label_item_details["text"] = "Item Details"
        self.label_item_details.place(x=790,y=360,width=263,height=54)

        self.label_icode_item=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_icode_item["font"] = ft
        self.label_icode_item["fg"] = "#333333"
        self.label_icode_item["bg"] = bg_main
        self.label_icode_item["justify"] = "center"
        self.label_icode_item["text"] = "I-Code:"
        self.label_icode_item.place(x=660,y=420,width=129,height=50)

        self.icode_item=tk.Entry(root)
        self.icode_item["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.icode_item["font"] = ft
        self.icode_item["fg"] = "#333333"
        self.icode_item["justify"] = "left"
        self.icode_item["text"] = ""
        self.icode_item.place(x=830,y=430,width=305,height=30)

        self.label_name_item=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_name_item["font"] = ft
        self.label_name_item["fg"] = "#333333"
        self.label_name_item["bg"] = bg_main
        self.label_name_item["justify"] = "center"
        self.label_name_item["text"] = "Name:"
        self.label_name_item.place(x=670,y=480,width=114,height=49)

        self.name_item=tk.Entry(root)
        self.name_item["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.name_item["font"] = ft
        self.name_item["fg"] = "#333333"
        self.name_item["justify"] = "left"
        self.name_item["text"] = ""
        self.name_item.place(x=830,y=490,width=305,height=30)

        self.label_price_item=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_price_item["font"] = ft
        self.label_price_item["fg"] = "#333333"
        self.label_price_item["bg"] = bg_main
        self.label_price_item["justify"] = "center"
        self.label_price_item["text"] = "Price:"
        self.label_price_item.place(x=680,y=540,width=70,height=25)

        self.price_item=tk.Entry(root)
        self.price_item["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.price_item["font"] = ft
        self.price_item["fg"] = "#333333"
        self.price_item["justify"] = "left"
        self.price_item["text"] = ""
        self.price_item.place(x=830,y=550,width=305,height=30)
    
    def btn_continue_command(self):
        adminName = self.name_admin.get()
        adminUser = self.username_admin.get()
        adminPass = self.password_admin.get()
        
        empName = self.name_employee.get()
        empUser = self.username_employee.get()
        empCode = self.ecode_employee.get()
        empPass = self.password_employee.get()
        
        restName = self.name_restaurant.get()
        restAdd = self.address_restaurant.get()
        restOwner = self.owner_restaurant.get()
        
        icode = self.icode_item.get()
        iname = self.name_item.get()
        iprice = self.price_item.get()
        
        if adminName == "" or adminUser == "" or adminPass == "" \
            or empName == "" or empUser == "" or empCode == "" or empPass == "" \
                or restName == "" or restAdd == "" or restOwner == "" or icode == "" \
                    or iname == "" or iprice == "":
            messagebox.showerror("Error", "Some Records Are Empty!")
        else:
            try:
                iprice = float(iprice)
                from generateDB import genDB
                genDB()
                
                adminFile = "Database/admin.db"
                restFile = "Database/rest.db"
                empFile = "Database/emp.db"
                itemFile = "Database/item.db"
                
                if not os.path.isdir("Database"):
                    os.mkdir("Database")
                
                adminCon = sql.connect(adminFile)
                restCon = sql.connect(restFile)
                empCon = sql.connect(empFile)
                itemCon = sql.connect(itemFile)
        
                a=adminCon.cursor()
                r=restCon.cursor()
                i=itemCon.cursor()
                e=empCon.cursor()
                
                a.execute("INSERT INTO admin VALUES (?, ?, ?)", (adminName, adminUser, adminPass))
                r.execute("INSERT INTO restaurant VALUES (?, ?, ?)", (restName, restAdd, restOwner))
                e.execute("INSERT INTO employee VALUES (?, ?, ?, ?)", (empCode, empName, empUser, empPass))
                i.execute("INSERT INTO items VALUES (?, ?, ?)", (icode, iname, iprice))                
            
                adminCon.commit()
                empCon.commit()
                itemCon.commit()
                restCon.commit()
                
                messagebox.showinfo("Success!", "Your Sodtware Has been set up! Open the app again to use your software")
                
                a.close()
                r.close()
                i.close()
                e.close()
                
                self.window.destroy()

            except:
                messagebox.showerror("Error", "Price is not a real number")
                
        
              
if __name__ == "__main__":
    
    import os
    
    adminFile = "Database/admin.db"
    restFile = "Database/rest.db"
    empFile = "Database/emp.db"
    itemFile = "Database/item.db"
    orderFile = "Database/order.db"
    
    """
    
    Check if DataBase exists and determine 
    wether to enter startup mode or
    normal mode
    
    """
    
    startup = 0
    if not os.path.isdir("Database"):
        #database folder does not exist
        startup = 1
    
    file_exist = [os.path.isfile(adminFile), os.path.isfile(restFile), 
                  os.path.isfile(empFile), os.path.isfile(itemFile)]
    
    if not all(file_exist):
        #some or all files do not exist
        startup = 1
        
    if startup == 0:
        
        #enter normal login panel mode
        
        adminCon = sql.connect(adminFile)
        restCon = sql.connect(restFile)
        empCon = sql.connect(empFile)
        itemCon = sql.connect(itemFile)
        orderCon = sql.connect(orderFile)
        
        a = adminCon.cursor()
        r = restCon.cursor()
        o = orderCon.cursor()
        i = itemCon.cursor()
        e = empCon.cursor()
        
        
        r.execute("SELECT * FROM restaurant")
        rd = r.fetchone()
        myRest = RESTAURANT(rd[0], rd[1], rd[2])
        r.close()
        
        root = tk.Tk()
        app = Login(root)
        root.attributes('-topmost', 1)
        root.focus_force()
        ico = tk.PhotoImage(file='icon\icon.png')
        root.iconphoto(True, ico)
        root.mainloop()
    
        adminCon.close()
        restCon.close()
        empCon.close()
        itemCon.close()
        orderCon.close()
        
        if os.path.exists("adminData.html"):
            os.remove("adminData.html")
        if os.path.exists("empData.html"):
            os.remove("empData.html")
        if os.path.exists("orderData.html"):
            os.remove("orderData.html")
        if os.path.exists("itemData.html"):
            os.remove("itemData.html")
    else:
        #enter startup mode
        root = tk.Tk()
        app = StartUp(root)
        root.mainloop()
        