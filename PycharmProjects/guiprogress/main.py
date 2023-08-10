import tkinter as tk
from tkinter import ttk
import time

def start_task():
    progress['maximum'] = 100
    for i in range(101):
        time.sleep(0.1)
        progress['value'] = i
        print(i)
        root.update_idletasks()  # Update GUI
    status_label.config(text="Cleaning Done!")

root = tk.Tk()
root.title("Progress Bar")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

start_button = tk.Button(frame, text="Start Cleaning", command=start_task)
start_button.pack()

progress = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
progress.pack()

status_label = tk.Label(frame, text="")
status_label.pack()

root.mainloop()
