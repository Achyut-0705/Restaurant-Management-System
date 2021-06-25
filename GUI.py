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

        self.username=tk.Entry(root)
        self.username["borderwidth"] = "1px"
        self.username["font"] = ft
        self.username["fg"] = "#333333"
        self.username["text"] = "User Name"
        self.username.place(x=160,y=140,width=494,height=30)
        self.username["show"] = "undefined"

        self.password=tk.Entry(root)
        self.password["borderwidth"] = "1px"
        self.password["font"] = ft
        self.password["fg"] = "#333333"
        self.password["text"] = "Password"
        self.password.place(x=160,y=220,width=493,height=30)

        self.name_restraunt=tk.Label(root)
        self.name_restraunt["font"] = ft
        self.name_restraunt["fg"] = "#333333"
        self.name_restraunt["justify"] = "center"
        self.name_restraunt["text"] = "Name of Restraunt"
        self.name_restraunt.place(x=10,y=20,width=729,height=31)

        self.type_login=tk.Listbox(root)
        self.type_login["borderwidth"] = "1px"
        self.type_login["font"] = ft
        self.type_login["fg"] = "#333333"
        self.type_login["justify"] = "center"
        self.type_login.place(x=220,y=80,width=274,height=30)

        self.label_username=tk.Label(root)
        self.label_username["font"] = ft
        self.label_username["fg"] = "#333333"
        self.label_username["justify"] = "center"
        self.label_username["text"] = "User Id:"
        self.label_username.place(x=80,y=140,width=70,height=25)

        self.label_password=tk.Label(root)
        self.label_password["font"] = ft
        self.label_password["fg"] = "#333333"
        self.label_password["justify"] = "center"
        self.label_password["text"] = "Password:"
        self.label_password.place(x=70,y=220,width=70,height=25)        
        
        self.login_btn=tk.Button(root)
        self.login_btn["bg"] = "#efefef"
        self.login_btn["font"] = ft
        self.login_btn["fg"] = "#000000"
        self.login_btn["justify"] = "center"
        self.login_btn["text"] = "Login"
        self.login_btn.place(x=320,y=280,width=120,height=30)
        self.login_btn["command"] = self.logmein

    def logmein(self):
        print('login button clicked')
            
if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()