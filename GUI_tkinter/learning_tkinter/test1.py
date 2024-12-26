import tkinter as tk

# Create a simple window
root = tk.Tk()
root.title("My First Tkinter App")



# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()



label = tk.Label(root, text="This is a label", background="red", height="10", width="10")
label.pack()



def button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=button_click, background="green",width="10", height="10 " ,cursor="hand2")
button.pack()



entry = tk.Entry(root,cursor="hand2", show="*", width="10", background="yellow",font=("Arial", 12))
entry.pack()



text_widget = tk.Text(root, width=20, height=5,cursor="hand2",background= "pink"  )
text_widget.pack()



frame = tk.Frame(root, width=100, height=100, background="blue",cursor="hand2")
label = tk.Label(frame, text="Label in Frame", background="yellow", cursor="hand2"  ,font=("Arial", 12) )
label.pack()
frame.pack()

# Start the Tkinter event loop
root.mainloop()