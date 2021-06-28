import tkinter as tk
import tkinter.font as tkFont
from classes import RESTAURANT, ITEM, ADMIN, EMPLOYEE
from tkinter import messagebox
import sqlite3 as sql

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
        ft = tkFont.Font(family='Roboto',size=25)
        
        root.title("Restraunt Management System")
        width=750
        height=320
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = bg_main)
        
        ft = tkFont.Font(family='Roboto',size=30, weight = "bold")
        self.name_restraunt=tk.Label(root)
        self.name_restraunt["font"] = ft
        self.name_restraunt["fg"] = fg_panel
        self.name_restraunt["bg"] = bg_panel
        self.name_restraunt["justify"] = "center"
        self.name_restraunt["text"] = myRest.name.upper()
        self.name_restraunt.place(x=0,y=0,width=750,height=80)
        
        ft = tkFont.Font(family='Roboto',size=15, weight = "bold")
        self.name_restraunt=tk.Label(root)
        self.name_restraunt["font"] = ft
        self.name_restraunt["fg"] = "black"
        self.name_restraunt["bg"] = bg_main
        self.name_restraunt["justify"] = "center"
        self.name_restraunt["text"] = "LOG IN TO CONTINUE"
        self.name_restraunt.place(x=10,y=100,width=729,height=30)
        
        ft = tkFont.Font(family='Roboto',size=12, weight = "bold")
        self.username=tk.Entry(root)
        self.username["borderwidth"] = "1px"
        self.username["font"] = ft
        self.username["fg"] = "#333333"
        self.username["text"] = "User Name"
        self.username.place(x=160,y=140,width=494,height=30)

        self.password=tk.Entry(root)
        self.password["borderwidth"] = "1px"
        self.password["font"] = ft
        self.password["fg"] = "#333333"
        self.password["text"] = "Password"
        self.password.place(x=160,y=220,width=493,height=30)
        self.password['show'] = '*'

        self.label_username=tk.Label(root)
        self.label_username["font"] = ft
        self.label_username["fg"] = "#333333"
        self.label_username["bg"] = bg_main
        self.label_username["justify"] = "center"
        self.label_username["text"] = "User ID:"
        self.label_username.place(x=80,y=140,width=70,height=25)

        self.label_password=tk.Label(root)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["bg"] = bg_main
        self.label_password["justify"] = "center"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=70,y=220,width=80,height=25)        
        
        self.login_btn=tk.Button(root)
        self.login_btn["bg"] = btn_bg
        self.login_btn["font"] = ft
        self.login_btn["fg"] = "black"
        self.login_btn["justify"] = "center"
        self.login_btn["text"] = "Admin Login"
        self.login_btn.place(x=200,y=280,width=150,height=30)
        self.login_btn["command"] = self.logAdmin
        # self.login_btn.bind()
        
        self.login_btn=tk.Button(root)
        self.login_btn["bg"] = btn_bg
        self.login_btn["font"] = ft
        self.login_btn["fg"] = "black"
        self.login_btn["justify"] = "center"
        self.login_btn["text"] = "Employee Login"
        self.login_btn.place(x=400,y=280,width=150,height=30)
        self.login_btn["command"] = self.logEMP
    
    def logAdmin(self):
        
        a = adminCon.cursor()
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
                tk.messagebox.showerror("Wrong Credentials", "Username/Password Incorrect")
        except:
            tk.messagebox.showerror("Record Not Found", "No Such User Found")  
        
    def logEMP(self):
        
        e = empCon.cursor()
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
                root.mainloop()
            else:
                tk.messagebox.showerror("Wrong Credentials", "Username/Password Incorrect")
        except:
            tk.messagebox.showerror("Record Not Found", "No Such User Found")


class AdminPanel:
    def __init__(self, root):
        global bg_main
        global btn_bg
        self.window = root
        bg_main = "#d8c3a5"
        btn_bg = "#eae7dc"
        
        root.title("Admin Panel")
        root.configure(background = bg_main)
        width=1160
        height=615
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = bg_main)
        

        self.admin=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=60,weight = "bold")
        self.admin["font"] = ft
        self.admin["fg"] = "#e85a4f"
        self.admin["justify"] = "center"
        self.admin["text"] = "ADMIN PANEL"
        self.admin["bg"] = "#565958"
        self.admin.place(x=0,y=0,width=1160,height=180)


        self.name_admin_panel=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=20, weight = "bold")
        self.name_admin_panel["font"] = ft
        self.name_admin_panel["fg"] = "#333333"
        self.name_admin_panel["justify"] = "left"
        self.name_admin_panel["text"] = "Name: " + currAdmin.name
        self.name_admin_panel["bg"] = bg_main
        self.name_admin_panel.place(x=100,y=230,width=200)

        self.name_admin_panel=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=20, weight = "bold")
        self.name_admin_panel["font"] = ft
        self.name_admin_panel["fg"] = "#333333"
        self.name_admin_panel["justify"] = "left"
        self.name_admin_panel["text"] = "Username: " + currAdmin.username
        self.name_admin_panel["bg"] = bg_main
        self.name_admin_panel.place(x=800,y=230,width=250)

        self.btn_emp_mng=tk.Button(root)
        self.btn_emp_mng["bg"] = btn_bg
        ft = tkFont.Font(family='Roboto',size=18)
        self.btn_emp_mng["font"] = ft
        self.btn_emp_mng["fg"] = "#000000"
        self.btn_emp_mng["justify"] = "center"
        self.btn_emp_mng["text"] = "MANAGE EMPLOYEE"
        self.btn_emp_mng.place(x=650,y=320,width=400,height=62)
        self.btn_emp_mng["command"] = self.btn_emp_mng_command

        self.btn_reset=tk.Button(root)
        self.btn_reset["bg"] = btn_bg
        
        ft = tkFont.Font(family='Roboto',size=18)
        self.btn_reset["font"] = ft
        self.btn_reset["fg"] = "#000000"
        self.btn_reset["justify"] = "center"
        self.btn_reset["text"] = "RESET DATABASE"
        self.btn_reset.place(x=100,y=320,width=400,height=62)
        self.btn_reset["command"] = self.btn_reset_command

        self.btn_logout=tk.Button(root)
        self.btn_logout["bg"] = btn_bg
        
        ft = tkFont.Font(family='Roboto',size=18)
        self.btn_logout["font"] = ft
        self.btn_logout["fg"] = "#000000"
        self.btn_logout["justify"] = "center"
        self.btn_logout["text"] = "LOG OUT"
        self.btn_logout.place(x=440,y=550,width=300,height=45)
        self.btn_logout["command"] = self.btn_logout_command

        self.btn_manage_item=tk.Button(root)
        self.btn_manage_item["bg"] = btn_bg
        
        ft = tkFont.Font(family='Roboto',size=18)
        self.btn_manage_item["font"] = ft
        self.btn_manage_item["fg"] = "#000000"
        self.btn_manage_item["justify"] = "center"
        self.btn_manage_item["text"] = "MANAGE ITEMS"
        self.btn_manage_item.place(x=650,y=430,width=400,height=62)
        self.btn_manage_item["command"] = self.btn_manage_item_command
        
        self.btn_reset=tk.Button(root)
        self.btn_reset["bg"] = btn_bg
        ft = tkFont.Font(family='Roboto',size=18)
        self.btn_reset["font"] = ft
        self.btn_reset["fg"] = "#000000"
        self.btn_reset["justify"] = "center"
        self.btn_reset["text"] = "MANAGE ADMIN"
        self.btn_reset.place(x=100,y=430,width=400,height=62)
        self.btn_reset["command"] = self.btn_manage_admin_command

    def btn_emp_mng_command(self):
        print("command")


    def btn_reset_command(self):
        print("command")

    def btn_logout_command(self):
        self.window.destroy()
        root = tk.Tk()
        app = Login(root)
        root.mainloop()

    def btn_manage_item_command(self):
        print("command")
    
    def btn_manage_admin_command(self):
        print("command")


class SalesPanel:
    def __init__(self, root):
        global bg_main
        global btn_bg
        global currEmp
        
        root.title("Sales Panel")
        width=1280
        height=720
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        root.configure(background = bg_main)

        self.empLoginHead=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=50,weight = "bold")
        self.empLoginHead["font"] = ft
        self.empLoginHead["fg"] = fg_panel
        self.empLoginHead["justify"] = "center"
        self.empLoginHead["bg"] = bg_panel
        self.empLoginHead["text"] = "PLACE AN ORDER!"
        self.empLoginHead.place(x=0,y=0,width=1280,height=150)

        ft = tkFont.Font(family='Roboto',size=15, weight = "bold")

        self.name_emp=tk.Label(root)
        self.name_emp["font"] = ft
        self.name_emp["fg"] = "#333333"
        self.name_emp["justify"] = "left"
        self.name_emp["bg"] = bg_main
        self.name_emp["text"] = "Name: " + currEmp.Name
        self.name_emp.place(x=400,y=160,width=250,height=50)

        self.username_emp=tk.Label(root)
        self.username_emp["font"] = ft
        self.username_emp["fg"] = "#333333"
        self.username_emp["justify"] = "left"
        self.username_emp["bg"] = bg_main
        self.username_emp["text"] = "Username: " + currEmp.Username
        self.username_emp.place(x=650,y=160,width=250,height=50)

        self.label_name_customer=tk.Label(root)
        self.label_name_customer["font"] = ft
        self.label_name_customer["fg"] = "#333333"
        self.label_name_customer["justify"] = "left"
        self.label_name_customer["bg"] = bg_main
        self.label_name_customer["text"] = "Customer Name:"
        self.label_name_customer.place(x=35,y=250,width=200,height=54)

        self.name_customer=tk.Entry(root)
        self.name_customer["borderwidth"] = "1px"
        self.name_customer["font"] = ft
        self.name_customer["fg"] = "#333333"
        self.name_customer["justify"] = "left"
        self.name_customer.place(x=250,y=255, width=400,height=35)

        self.label_email=tk.Label(root)
        self.label_email["font"] = ft
        self.label_email["fg"] = "#333333"
        self.label_email["justify"] = "center"
        self.label_email["bg"] = bg_main
        self.label_email["text"] = "E-mail ID:"
        self.label_email.place(x=600,y=250,width=230,height=48)

        self.email_customer=tk.Entry(root)
        self.email_customer["borderwidth"] = "1px"
        self.email_customer["font"] = ft
        self.email_customer["fg"] = "#333333"
        self.email_customer["justify"] = "left"
        self.email_customer["text"] = ""
        self.email_customer.place(x=830,y=255,width=400,height=35)

        self.list_item=tk.Listbox(root)
        self.list_item["borderwidth"] = "1px"
        self.list_item["font"] = ft
        self.list_item["fg"] = "#333333"
        self.list_item["justify"] = "left"
        self.list_item["state"] = tk.DISABLED
        self.list_item.place(x=500,y=380,width=374,height=160)

        self.btn_add_item=tk.Button(root)
        self.btn_add_item["bg"] = "#efefef"
        self.btn_add_item["font"] = ft
        self.btn_add_item["fg"] = "#000000"
        self.btn_add_item["justify"] = "center"
        self.btn_add_item["bg"] = btn_bg
        self.btn_add_item["text"] = "Add Item"
        self.btn_add_item.place(x=50,y=430,width=400,height=50)
        self.btn_add_item["command"] = self.btn_add_item_command

        self.btn_remove_item=tk.Button(root)
        self.btn_remove_item["bg"] = "#efefef"
        self.btn_remove_item["font"] = ft
        self.btn_remove_item["fg"] = "#000000"
        self.btn_remove_item["justify"] = "center"
        self.btn_remove_item["bg"] = btn_bg
        self.btn_remove_item["text"] = "Remove"
        self.btn_remove_item.place(x=50,y=500,width=400,height=50)
        self.btn_remove_item["command"] = self.btn_remove_item_command
        
        items = ['maggie','momos','pizza']
        self.clicked = tk.StringVar()
        self.clicked.set('Select an item')
        self.item_list = tk.OptionMenu(root,self.clicked,*items)
        self.item_list['bg'] = btn_bg
        self.item_list['font'] = ft
        self.item_list['menu']['bg'] = btn_bg
        self.item_list.config(width = 400)
        self.item_list.place(x=50,y=350,width=400,height=50)

    def btn_add_item_command(self):
        pass

    def btn_remove_item_command(self):
        pass
        

if __name__ == "__main__":
    
    
    adminCon = sql.connect("SampleData/admin.db")
    restCon = sql.connect("SampleData/rest.db")
    empCon = sql.connect("SampleData/emp.db")
    itemCon = sql.connect("SampleData/item.db")
    
    #reading restaurant details
    r = restCon.cursor()
    r.execute("SELECT * FROM restaurant")
    rd = r.fetchone()
    myRest = RESTAURANT(rd[0], rd[1], rd[2])
    
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
    
    adminCon.close()
    restCon.close()
    empCon.close()
    itemCon.close()