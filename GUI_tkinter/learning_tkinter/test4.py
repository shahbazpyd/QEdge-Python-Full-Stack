import tkinter as tk
from tkinter import ttk



def message():
    msglabel.config(text="Hello! "+enty.get())


root=tk.Tk()
root.title="my app"

enty=tk.Entry(root)
enty.grid(row=0, column=0)



btn=tk.Button(root, text="click me",command=message)
btn.grid(row=1, column=0)

msglabel=tk.Label(root, text="")
msglabel.grid(row=2, column=0)



root.mainloop()