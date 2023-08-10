#Import required libraries
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import customtkinter  # <- import CustomTkinter module

# Create object
root = Tk()

# Define window geometry
root.geometry("996x624")

# Add image file
bg = ImageTk.PhotoImage(file="/Users/toddjohnsgard/26970396.jpeg")

# Create canvas
canvas = Canvas(root,width= 996, height= 624)
canvas.pack(fill= "both", expand=True)

# Display image
canvas.create_image(0, 0, image=bg, anchor="nw")

# Add canvas text
canvas.create_text(500,590,text="COMP 699: Introduction to Programming: Drone Project", font=("Times New Roman", 24))

# Execute tkinter
root.mainloop()