from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()  # Create a window object
root.geometry(f'{settings.Width}x{settings.Height}')  # Set the size
# ('WIDTH x HEIGHT')
root.title('Minesweeper - by pietr-o')  # Set the title for our windows
root.resizable(False, False)  # Make the window (not) resizable in width and height

top_frame = Frame(
    root,
    background='black',  # set background colour, CHANGE IT TO BLACK LATER
    width=settings.Width,
    height=utils.height_percentage(22)
)
top_frame.place(x=0, y=0)
left_frame = Frame(
    root,
    background='black',  # Set it later to light grey
    width=utils.width_percentage(25),
    height=utils.height_percentage(78)
)
left_frame.place(x=0, y=utils.height_percentage(22))

center_frame = Frame(
    root,
    background='black',
    width=utils.width_percentage(75),
    height=utils.height_percentage(78)
)
center_frame.place(x=utils.width_percentage(25), y=utils.height_percentage(22))

for x in range(settings.Grid_Size):
    for y in range(settings.Grid_Size):
        c = Cell()
        c.create_btn_obj(center_frame)
        c.cell_btn_obj.grid(column=x, row=y)
# Run the window
root.mainloop()  # All code in this loop will be into the created window
