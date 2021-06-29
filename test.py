import tkinter as tk
import tkinter.font as tkFont
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
        root.title("Manage Employee Panel")
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
        
        # ---------------------------------------x---------------------------------------------
        
        self.lable_ecode = tk.Label(root)
        self.lable_ecode["font"] = ft
        self.lable_ecode["fg"] = "#333333"
        self.lable_ecode["bg"] = bg_main
        self.lable_ecode["justify"] = "center"
        self.lable_ecode["text"] = "Employee Code:"
        self.lable_ecode.place(x=10, y=350, width=170, height=40)

        # ---------------------------------------x---------------------------------------------
        
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

        
        # ---------------------------------------x---------------------------------------------
        
        self.add_emp_ecode = tk.Entry(root)
        self.add_emp_ecode["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=15, weight="bold")
        self.add_emp_ecode["font"] = ft
        self.add_emp_ecode["fg"] = "#333333"
        self.add_emp_ecode["justify"] = "left"
        self.add_emp_ecode["text"] = ""
        self.add_emp_ecode.place(x=190, y=360, width=250, height=33)

        # ---------------------------------------x---------------------------------------------
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
        pass

    def btn_view_report_command(self):
        pass

    def btn_delete_command(self):
        pass
