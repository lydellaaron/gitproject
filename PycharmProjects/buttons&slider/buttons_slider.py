import tkinter
import customtkinter  # import CustomTkinter module
from PIL import Image, ImageTk

root_tk = tkinter.Tk()  # create Tk window
root_tk.geometry("996x624")
root_tk.title("Drone Control")
root_tk.configure(bg="#ffffff")
#Adding transparent background property
root_tk.wm_attributes('-transparentcolor', '#ab23ff')
# Add image file
#bg = ImageTk.PhotoImage(file="/Users/toddjohnsgard/26970396.jpeg")

def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.grid(row=0, column=0, padx=20, pady=20, fg_color="transparent",bg_color="transparent")

button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.grid(row=0, column=1, padx=20, pady=20)

button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.grid(row=1, column=0, padx=20, pady=20)

button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.grid(row=1, column=1, padx=20, pady=20)

def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(master=root_tk, width=160, height=16, border_width=5.5, command=slider_event)
slider.place(relx=0.45, rely=0.7, anchor=tkinter.CENTER)

root_tk.mainloop()