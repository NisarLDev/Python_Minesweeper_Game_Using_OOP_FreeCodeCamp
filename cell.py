from tkinter import Button
class Cell:
    def __init__(self,is_mine=False)
        self.is_mine = is_mine
        self.cell_btn_object = None
    def create_btn_object(self, location):
        btn = Button(
            localtion,
            text='Text'
        )
        self.cell_btn_object = btn
        btn.bind('<Button-1>', self.left_click_actions )
        self.cell_btn_object = btn

    defleft_click_actions(self):
        print("I am left clicked!")
