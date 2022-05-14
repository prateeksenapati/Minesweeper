from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
# Settings
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(FALSE, FALSE)
root.configure(bg='black')

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_perc(20)
)

top_frame.place(x=0, y=0)

side_frame = Frame(
    root,
    bg='black',
    width=utils.width_perc(20),
    height=utils.height_perc(80)
)

side_frame.place(x=0, y=utils.height_perc(20))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_perc(80),
    height=utils.height_perc(80)
)

center_frame.place(x=utils.width_perc(20), y=utils.height_perc(20))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )
print(Cell.all)

root.mainloop()
