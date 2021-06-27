import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1196
        height=725
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_881=tk.Label(root)
        ft = tkFont.Font(family='Times',size=115)
        GLabel_881["font"] = ft
        GLabel_881["fg"] = "#333333"
        GLabel_881["justify"] = "center"
        GLabel_881["text"] = "Place an order !"
        GLabel_881.place(x=80,y=50,width=1068,height=125)

        GLabel_463=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_463["font"] = ft
        GLabel_463["fg"] = "#333333"
        GLabel_463["justify"] = "center"
        GLabel_463["text"] = "Name:"
        GLabel_463.place(x=200,y=190,width=170,height=53)

        GLabel_478=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_478["font"] = ft
        GLabel_478["fg"] = "#333333"
        GLabel_478["justify"] = "left"
        GLabel_478["text"] = "Achyut Shukla"
        GLabel_478.place(x=420,y=180,width=731,height=90)

        GLabel_502=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_502["font"] = ft
        GLabel_502["fg"] = "#333333"
        GLabel_502["justify"] = "center"
        GLabel_502["text"] = "Username:"
        GLabel_502.place(x=80,y=260,width=304,height=78)

        GLabel_806=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_806["font"] = ft
        GLabel_806["fg"] = "#333333"
        GLabel_806["justify"] = "left"
        GLabel_806["text"] = "Achyut007"
        GLabel_806.place(x=420,y=270,width=731,height=56)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
