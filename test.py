import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3 as sql
bg_main = "#d8c3a5"
btn_bg = "#eae7dc"
bg_panel = "#565958"
fg_panel = "#e85a4f"

class ManageEmployee:
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
        
        # ---------------------------------------x---------------------------------------------
        
        self.lable_ecode = tk.Label(root)
        self.lable_ecode["font"] = ft
        self.lable_ecode["fg"] = "#333333"
        self.lable_ecode["bg"] = bg_main
        self.lable_ecode["justify"] = "center"
        self.lable_ecode["text"] = "Price:"
        self.lable_ecode.place(x=10, y=350, width=170, height=40)

        # ---------------------------------------x---------------------------------------------
        
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

        
        # ---------------------------------------x---------------------------------------------
        

        # ---------------------------------------x---------------------------------------------
        self.add_price = tk.Entry(root)
        self.add_price["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_price["font"] = ft
        self.add_price["fg"] = "#333333"
        self.add_price["justify"] = "left"
        self.add_price["text"] = ""
        self.add_price.place(x=190, y=410, width=250, height=33)
        
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
            selfprice = self.admin_confirm_pricesword.get()
            if len(name) == 0 or len(icode) == 0 or len(selfprice) == 0:
                tk.messagebox.showerror("Error", "Fields Cannot be Empty")  
            else:
                c = itemCon.cursor()
                c.execute("SELECT * FROM items WHERE icode = (?)", (icode, ))
                exist = c.fetchone()
                if exist == None:
                    if selfprice == currAdmin.password:
                        choice = messagebox.askyesno(
                            "Confirm", "Do you want to proceed?")
                        if choice:
                            a = itemCon.cursor()
                            a.execute("INSERT INTO items VALUES (?, ?, ?)",
                                      (icode, name, price))
                            itemCon.commit()
                            messagebox.showinfo(
                                "Success!", "New Item Succesfully Created")
                    else:
                        tk.messagebox.showerror("Error", "Wrong Icode")
                else:
                    messagebox.showerror(
                        "Error", "Item with icode exists already!")
        except:
            messagebox.showerror("Error", "Price Has to be a valid number.")

    def btn_view_report_command(self):
        c = empCon.cursor()
        c.execute("SELECT * FROM employee ORDER BY name ASC")
        data = c.fetchall()        
        htmlContent ='''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="shortcut icon" href="./icon/icon2.ico">
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
                    background-color: #F371D1;
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

        webbrowser.open_new_tab('empData.html')

    def btn_delete_command(self):
        global currAdmin
        user = self.delete_username.get()
        selfPas = self.admin_confirm_password.get()

        if len(user) == 0 or len(selfPas) == 0:
            tk.messagebox.showerror("Error", "Fields Cannot be Empty")
        else:
            c = empCon.cursor()
            c.execute("SELECT * FROM employee WHERE username = (?)", (user, ))
            exist = c.fetchone()

            if exist != None:
                
                if selfPas == currAdmin.password:
                    choice = messagebox.askyesno(
                        "Confirm", "Do you want to proceed?")
                    if choice:
                        a = empCon.cursor()
                        a.execute(
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