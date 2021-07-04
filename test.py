import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3 as sql

bg_main = "#d8c3a5"
btn_bg = "#eae7dc"
bg_panel = "#565958"
fg_panel = "#e85a4f"

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
        self.password.place(x=208, y=280, width=335, height=30)
        self.password['show'] = '*'
        
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
        pass
        
root = tk.Tk()
app = ResetDatabase(root)
root.mainloop()