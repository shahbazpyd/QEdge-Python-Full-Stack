# import tkinter as tk

# root = tk.Tk()
# root.geometry("300x200") # Width x Height
# root.title("My First Tkinter App")


# label1 = tk.Label(root, text="Label 1")
# label1.pack(side=tk.TOP)

# label2 = tk.Label(root, text="Label 2")
# label2.pack(side=tk.BOTTOM)

# button = tk.Button(root, text="Click Me")
# button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)




import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("My First Tkinter App")

top_frame = tk.Frame(root, bg="red")  # Create a container frame
top_frame.pack(side=tk.TOP, fill=tk.X) # Make frame expand horizontally


label1 = tk.Label(top_frame, text="Click button", name="label1")
label1.pack(side=tk.LEFT)  # Pack label on the left side of the frame

button = tk.Button(top_frame, text="Click Me")
button.pack(side=tk.LEFT, ipadx=20, ipady=20,padx=20, pady=20) # Pack button to the right of the label, within the frame





mid_frame=tk.Frame(root, bg="green")
mid_frame.pack(side=tk.TOP, fill=tk.X)

label2 = tk.Label(mid_frame, text="Click button")
label2.pack(side=tk.LEFT)

button2 = tk.Button(mid_frame, text="Click me")
button2.pack(side=tk.LEFT, ipadx=20, ipady=20,padx=20, pady=20)


root.mainloop()
