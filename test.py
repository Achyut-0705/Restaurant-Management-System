import tkinter as tk
import tkinter.font as tkFont

class EmpLogin:
    def __init__(self, root):
        root.title("Sales Panel")
        width=1200
        height=740
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.empLoginHead=tk.Label(root)
        ft = tkFont.Font(family='Times',size=115)
        self.empLoginHead["font"] = ft
        self.empLoginHead["fg"] = "#333333"
        self.empLoginHead["justify"] = "center"
        self.empLoginHead["text"] = "Place an order !"
        self.empLoginHead.place(x=80,y=50,width=1068,height=125)

        self.label_name=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        self.label_name["font"] = ft
        self.label_name["fg"] = "#333333"
        self.label_name["justify"] = "center"
        self.label_name["text"] = "Name:"
        self.label_name.place(x=260,y=190,width=115,height=51)

        self.name_emp=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        self.name_emp["font"] = ft
        self.name_emp["fg"] = "#333333"
        self.name_emp["justify"] = "left"
        self.name_emp["text"] = "Achyut Shukla"
        self.name_emp.place(x=420,y=180,width=731,height=90)

        self.label_username=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        self.label_username["font"] = ft
        self.label_username["fg"] = "#333333"
        self.label_username["justify"] = "center"
        self.label_username["text"] = "Username:"
        self.label_username.place(x=200,y=270,width=166,height=53)

        self.username_emp=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        self.username_emp["font"] = ft
        self.username_emp["fg"] = "#333333"
        self.username_emp["justify"] = "left"
        self.username_emp["text"] = "Achyut007"
        self.username_emp.place(x=420,y=270,width=731,height=56)

        self.label_name_customer=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        self.label_name_customer["font"] = ft
        self.label_name_customer["fg"] = "#333333"
        self.label_name_customer["justify"] = "center"
        self.label_name_customer["text"] = "Enter Customer Name:"
        self.label_name_customer.place(x=30,y=350,width=351,height=54)

        self.name_customer=tk.Entry(root)
        self.name_customer["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=28)
        self.name_customer["font"] = ft
        self.name_customer["fg"] = "#333333"
        self.name_customer["justify"] = "left"
        self.name_customer["text"] = ""
        self.name_customer.place(x=420,y=360,width=760,height=40)

        self.label_email=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        self.label_email["font"] = ft
        self.label_email["fg"] = "#333333"
        self.label_email["justify"] = "center"
        self.label_email["text"] = "Enter E-mail ID:"
        self.label_email.place(x=140,y=430,width=229,height=48)

        self.email_customer=tk.Entry(root)
        self.email_customer["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=28)
        self.email_customer["font"] = ft
        self.email_customer["fg"] = "#333333"
        self.email_customer["justify"] = "left"
        self.email_customer["text"] = ""
        self.email_customer.place(x=420,y=430,width=760,height=40)

        self.list_item=tk.Listbox(root)
        self.list_item["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=28)
        self.list_item["font"] = ft
        self.list_item["fg"] = "#333333"
        self.list_item["justify"] = "left"
        self.list_item.place(x=750,y=490,width=374,height=208)

        self.btn_add_item=tk.Button(root)
        self.btn_add_item["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=28)
        self.btn_add_item["font"] = ft
        self.btn_add_item["fg"] = "#000000"
        self.btn_add_item["justify"] = "center"
        self.btn_add_item["text"] = "Add Item"
        self.btn_add_item.place(x=140,y=620,width=150,height=50)
        self.btn_add_item["command"] = self.btn_add_item_command

        self.btn_remove_item=tk.Button(root)
        self.btn_remove_item["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=28)
        self.btn_remove_item["font"] = ft
        self.btn_remove_item["fg"] = "#000000"
        self.btn_remove_item["justify"] = "center"
        self.btn_remove_item["text"] = "Remove"
        self.btn_remove_item.place(x=390,y=620,width=150,height=50)
        self.btn_remove_item["command"] = self.btn_remove_item_command

    def btn_add_item_command(self):
        pass

    def btn_remove_item_command(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = EmpLogin(root)
    root.mainloop()
