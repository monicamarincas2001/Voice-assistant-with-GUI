import tkinter as tk
import main


# styling the main window and the button
class FreidaUI:
    def __init__(self):
        self.top = tk.Tk()
        self.top.minsize(700, 700)
        self.top.maxsize(700, 700)
        self.loadimage = tk.PhotoImage(file="freida-button.PNG")
        self.B = tk.Button(self.top, image=self.loadimage, height=420, width=420, command=main.speakingFreida,
                           activebackground="#F5CDAA")
        self.top["bg"] = "#F5CDAA"
        self.B["bg"] = "#F5CDAA"
        self.B["border"] = "0"
        self.B.pack()
        self.B.place(relx=0.2, rely=0.2)
        self.top.mainloop()


app = FreidaUI()

