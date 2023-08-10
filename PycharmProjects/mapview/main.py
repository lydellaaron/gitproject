from tkinter import *
import tkintermapview

root = Tk()
root.title('Tkinter MapView')
root.geometry("996x624")

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=966, height=624, corner_radius=0)

# Set Coordinates
map_widget.set_position(34.686787, -118.154160)

# Set Address
#map_widget.set_address("43000 20th Street East Lancaster, California, United States")

# Set Zoom
map_widget.set_zoom(20)

map_widget.pack()

root.mainloop()