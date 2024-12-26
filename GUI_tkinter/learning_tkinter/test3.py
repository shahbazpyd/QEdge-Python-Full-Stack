import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1", bg="red")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.grid(row=0, column=1)

entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=2)

button = tk.Button(root, text="Click Me", bg="green")
button.grid(row=2, column=0, columnspan=2)

root.mainloop()