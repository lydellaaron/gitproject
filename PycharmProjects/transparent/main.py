import tkinter as tk

def on_button_click():
    print("Button Clicked")

root = tk.Tk()
root.title("Transparent Button Example")
root.geometry("300x200")  # Set the initial window size

# Create a transparent button
button = tk.Button(root, text="Transparent Button", command=on_button_click, bg="blue", fg="white")
button.config(borderwidth=0)  # Remove border
button.place(x=50, y=50)  # Adjust the button position

# Set the transparency level (alpha value) of the button
#button.attributes("-alpha", 0.7)

root.mainloop()
