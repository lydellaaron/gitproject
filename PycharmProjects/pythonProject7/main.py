import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create window
app.geometry("400x240")

def button_callback():
    print("button pressed")

# create button
button = customtkinter.CTkButton(app, command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)
button = customtkinter.CTkButton(app, command=button_callback)
button.grid(row=0, column=1, padx=20, pady=20)
button = customtkinter.CTkButton(app, command=button_callback)
button.grid(row=1, column=0, padx=20, pady=20)
button = customtkinter.CTkButton(app, command=button_callback)
button.grid(row=1, column=1, padx=20, pady=20)

slider = customtkinter.CTkSlider(master=root_tk, width=160, height=16, border_width=5.5, command=slider_event)
slider.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



app.mainloop()