import tkinter as tk

# root = tk.Tk()

# label1 = tk.Label(root, text="enter your name", bg="red")
# label1.grid(row=0, column=0)

# entry = tk.Entry(root)
# entry.grid(row=0, column=1)



# button = tk.Button(root, text="Click Me", bg="green" command=entry.get())
# button.grid(row=2, column=0, columnspan=2)



# label2 = tk.Label(root, text="Label 2", bg="blue")
# label2.grid(row=1, column=0)

# root.mainloop()


import tkinter as tk

def greet_user():
    name = entry.get()
    greeting_label.config(text=f"Hello, {name}!")

root = tk.Tk()

label1 = tk.Label(root, text="Enter your name:")
label1.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

button = tk.Button(root, text="Click Me", command=greet_user)
button.grid(row=1, column=0, columnspan=2)

greeting_label = tk.Label(root, text="") # Initially empty
greeting_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
