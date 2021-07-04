import tkinter as tk
import tkinter.font as tkFont
bg_main = "#d8c3a5"
btn_bg = "#eae7dc"
bg_panel = "#565958"
fg_panel = "#e85a4f"

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
        height = 650
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
        self.label_panel["text"] = "StartUp Mode"
        self.label_panel.place(x=0,y=0,width=1200,height=90)

        self.label_heading=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=30)
        self.label_heading["font"] = ft
        self.label_heading["fg"] = "#333333"
        self.label_heading["bg"] = bg_main
        self.label_heading["justify"] = "center"
        self.label_heading["text"] = "Enter Following details To SetUp you software"
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

        self.label_password_employee=tk.Label(root)
        ft = tkFont.Font(family='Roboto', size=18)
        self.label_password_employee["font"] = ft
        self.label_password_employee["fg"] = "#333333"
        self.label_password_employee["bg"] = bg_main
        self.label_password_employee["justify"] = "center"
        self.label_password_employee["text"] = "Password:"
        self.label_password_employee.place(x=30,y=520,width=160,height=50)

        self.password_employee=tk.Entry(root)
        self.password_employee["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.password_employee["font"] = ft
        self.password_employee["fg"] = "#333333"
        self.password_employee["justify"] = "left"
        self.password_employee["text"] = ""
        self.password_employee.place(x=220,y=530,width=305,height=30)

        self.btn_continue=tk.Button(root)
        self.btn_continue["bg"] = "#efefef"
        ft = tkFont.Font(family='Roboto', size=18)
        self.btn_continue["font"] = ft
        self.btn_continue["fg"] = "#000000"
        self.btn_continue["bg"] = btn_bg
        self.btn_continue["justify"] = "center"
        self.btn_continue["text"] = "Continue"
        self.btn_continue.place(x=400,y=600,width=368,height=41)
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

        self.name_restaurant=tk.Entry(root)
        self.name_restaurant["borderwidth"] = "1px"
        ft = tkFont.Font(family='Roboto', size=18)
        self.name_restaurant["font"] = ft
        self.name_restaurant["fg"] = "#333333"
        self.name_restaurant["justify"] = "left"
        self.name_restaurant["text"] = ""
        self.name_restaurant.place(x=830,y=270,width=305,height=30)

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
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()