import tkinter as tk
import tkinter.font as tkFont

class Login:
    def __init__(self, root):
        
        ft = tkFont.Font(family='Times',size=10)
        
        root.title("Restraunt Management System")
        width=750
        height=320
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        username=tk.Entry(root)
        username["borderwidth"] = "1px"
        username["font"] = ft
        username["fg"] = "#333333"
        username["text"] = "User Name"
        username.place(x=160,y=140,width=494,height=30)
        username["show"] = "undefined"

        password=tk.Entry(root)
        password["borderwidth"] = "1px"
        password["font"] = ft
        password["fg"] = "#333333"
        password["text"] = "Password"
        password.place(x=160,y=220,width=493,height=30)

        name_restraunt=tk.Label(root)
        name_restraunt["font"] = ft
        name_restraunt["fg"] = "#333333"
        name_restraunt["justify"] = "center"
        name_restraunt["text"] = "Name of Restraunt"
        name_restraunt.place(x=10,y=20,width=729,height=31)

        type_login=tk.Listbox(root)
        type_login["borderwidth"] = "1px"
        type_login["font"] = ft
        type_login["fg"] = "#333333"
        type_login["justify"] = "center"
        type_login.place(x=220,y=80,width=274,height=30)

        label_username=tk.Label(root)
        label_username["font"] = ft
        label_username["fg"] = "#333333"
        label_username["justify"] = "center"
        label_username["text"] = "User Id:"
        label_username.place(x=80,y=140,width=70,height=25)

        label_password=tk.Label(root)
        label_password["font"] = ft
        label_password["fg"] = "#333333"
        label_password["justify"] = "center"
        label_password["text"] = "Password:"
        label_password.place(x=70,y=220,width=70,height=25)
if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
