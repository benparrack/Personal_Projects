import tkinter as tk # tkinter is a library that is already included in python, which makes it easy bc we don't have to install it
# writing as tk makes it so we only have to write tk instead of tkinter when referencing it, basically just qol
root = tk.Tk() # creates the main/parent window

# Setting some window properties
root.title("Tk Example Window")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

# Create two labels
tk.Label(root, text="Nothing will work unless you do.").pack() # root means this code applies to the root window, .pack() makes it
# work with the geometry, i.e. "packs" the window
label2 = tk.Label(root, text="- Maya Angelou")
label2.pack() # can also pack like this

# Display an image
image = tk.PhotoImage(file="pika.png") # when using images, have to put in same folder as running file (makes sense)
tk.Label(root, image=image).pack()

root.mainloop() # handles mouse and cursor inputs
