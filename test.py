import tkinter as tk
import tkinter.font as tkFont
bg_main = "#d8c3a5"
btn_bg = "#eae7dc"
bg_panel = "#565958"
fg_panel = "#e85a4f"
class AdminPanel:
    def __init__(self, root):
        global bg_main
        global btn_bg
        global bg_main
        global fg_panel
        
        self.window = root
        
        root.title("Admin Panel")
        root.configure(background = bg_main)
        width=900
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = bg_main)
        

        self.admin=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=60,weight = "bold")
        self.admin["font"] = ft
        self.admin["fg"] = fg_panel
        self.admin["justify"] = "center"
        self.admin["text"] = "ADMIN PANEL"
        self.admin["bg"] = bg_panel
        self.admin.place(x=0,y=0,width=900,height=180)

        self.name_admin_panel=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=20, weight = "bold")
        self.name_admin_panel["font"] = ft
        self.name_admin_panel["fg"] = "#333333"
        self.name_admin_panel["justify"] = "left"
        self.name_admin_panel["text"] = "Name: " + currAdmin.name
        self.name_admin_panel["bg"] = bg_main
        self.name_admin_panel.place(x=10,y=200,width=400)

        self.name_admin_panel=tk.Label(root)
        ft = tkFont.Font(family='Roboto',size=20, weight = "bold")
        self.name_admin_panel["font"] = ft
        self.name_admin_panel["fg"] = "#333333"
        # self.name_admin_panel.
        self.name_admin_panel['justify'] = 'left'
        self.name_admin_panel["text"] = "Username: " + currAdmin.username
        self.name_admin_panel["bg"] = bg_main
        self.name_admin_panel.place(x=450,y=200,width=400)

        self.btn_emp_mng=tk.Button(root)
        self.btn_emp_mng["bg"] = btn_bg
        ft = tkFont.Font(family='Roboto',size=18)
        self.btn_emp_mng["font"] = ft
        self.btn_emp_mng["fg"] = "#000000"
        self.btn_emp_mng["justify"] = "center"
        self.btn_emp_mng["text"] = "MANAGE EMPLOYEE"
        self.btn_emp_mng.place(x=525,y=260,width=300,height=50)
        self.btn_emp_mng["command"] = self.btn_emp_mng_command

        self.btn_reset=tk.Button(root)
        self.btn_reset["bg"] = btn_bg        
        ft = tkFont.Font(family='Roboto',size=18)
        self.btn_reset["font"] = ft
        self.btn_reset["fg"] = "#000000"
        self.btn_reset["justify"] = "center"
        self.btn_reset["text"] = "RESET DATABASE"
        self.btn_reset.place(x=125,y=260,width=300,height=50)
        self.btn_reset["command"] = self.btn_reset_command

        self.btn_logout=tk.Button(root)
        self.btn_logout["bg"] = btn_bg        
        ft = tkFont.Font(family='Roboto',size=18)
        self.btn_logout["font"] = ft
        self.btn_logout["fg"] = "#000000"
        self.btn_logout["justify"] = "center"
        self.btn_logout["text"] = "LOG OUT"
        self.btn_logout.place(x=375,y=420,width=200,height=50)
        self.btn_logout["command"] = self.btn_logout_command

        self.btn_manage_item=tk.Button(root)
        self.btn_manage_item["bg"] = btn_bg        
        self.btn_manage_item["font"] = ft
        self.btn_manage_item["fg"] = "#000000"
        self.btn_manage_item["justify"] = "center"
        self.btn_manage_item["text"] = "MANAGE ITEMS"
        self.btn_manage_item.place(x=525,y=350,width=300,height=50)
        self.btn_manage_item["command"] = self.btn_manage_item_command
        
        self.btn_reset=tk.Button(root)
        self.btn_reset["bg"] = btn_bg
        self.btn_reset["font"] = ft
        self.btn_reset["fg"] = "#000000"
        self.btn_reset["justify"] = "center"
        self.btn_reset["text"] = "MANAGE ADMIN"
        self.btn_reset.place(x=125,y=350,width=300,height=50)
        self.btn_reset["command"] = self.btn_manage_admin_command

    def btn_emp_mng_command(self):
        # top = Toplevel(self.window)
        # app = ManageEmployee(top)
        # top.mainloop()
        pass


    def btn_reset_command(self):
        pass

    def btn_logout_command(self):
        # self.window.destroy()
        # root = tk.Tk()
        # app = Login(root)
        # root.mainloop()
        pass

    def btn_manage_item_command(self):
        pass
    
    def btn_manage_admin_command(self):
        # top = Toplevel(self.window)
        # app = ManageAdmin(top)
        # top.mainloop()
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminPanel(root)
    root.mainloop()
