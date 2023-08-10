from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('Buttons With Images')
root.geometry("500x570")

# Define Images
#add_folder_image = ImageTk.PhotoImage(Image.open("/Users/toddjohnsgard/landing.png").resize((40,40)))
takeoff = ImageTk.PhotoImage(Image.open("/Users/toddjohnsgard/take-off.png").resize((40,40)))
land = ImageTk.PhotoImage(Image.open("/Users/toddjohnsgard/landing.png").resize((40,40)))

# Create Buttons
button_1 = customtkinter.CTkButton(master=root, image=land, text="Land", width=190, height=40, compound="top")
button_1.pack(pady=20, padx=20)

button_2 = customtkinter.CTkButton(master=root, image=takeoff, text="Takeoff", width=190, height=40, compound="right",
	fg_color="#D35B58", hover_color="#C77C78")
button_2.pack(pady=10, padx=20)

button_3 = customtkinter.CTkButton(master=root, image=land, text="Land", width=190, height=40, compound="top")
button_3.pack(pady=20, padx=20)

button_4 = customtkinter.CTkButton(master=root, image=land, text="Land", width=190, height=40, compound="right")
button_4.pack(pady=10, padx=20)

button_5 = customtkinter.CTkButton(master=root, image=land, text="Land", width=190, height=40, compound="left",
	fg_color="#D35B58", hover_color="#C77C78")
button_5.pack(pady=10, padx=20)

button_6 = customtkinter.CTkButton(master=root, image=land, text="", width=40, height=40, compound="right",
	fg_color="#D35B58", hover_color="#C77C78")
button_6.pack(pady=10, padx=20)

button_7 = customtkinter.CTkButton(master=root, image=land, text="", width=40, height=40, compound="left")
button_7.pack(pady=10, padx=20)

root.mainloop()