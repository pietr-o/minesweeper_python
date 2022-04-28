from tkinter import Button

# Dynamic class definition


class Cell:  # Define class 'Cell'
    def __init__(self, is_mine=False):  # Initialization method
        self.is_mine = is_mine  # Passes args to self (the class itself)
        self.cell_btn_obj = None

    def create_btn_obj(self, position):  # Defines a new method
        btn = Button(
            position,
            width=12,
            height=4,
            text="\U0001F611"
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Double-1>', self.right_click_action)
        # Passes the object created to self (the method itself)
        self.cell_btn_obj = btn

    def left_click_action(self, event):
        print(event)
        print('You triggered the click')

    def right_click_action(self, event):
        print(event)
        print('You triggered the double click')
