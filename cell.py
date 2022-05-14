from tkinter import Button

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #append object to cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=6,
            height=1,
            text=f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print("Left clicked")

    def right_click_actions(self, event):
        print(event)
        print("Right clicked")

    @staticmethod
    def randomize_mines(self):
        pass

    def __repr__(self):
        return f"Cell({self.x},{self.y})"