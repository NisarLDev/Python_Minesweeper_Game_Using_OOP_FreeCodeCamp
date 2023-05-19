from tkinter import Button
import random
import settings


class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        #Append the object tothe Cell.all list
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        self.cell_btn_object = btn
        btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click

        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            
    
    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
    def show_cell(self):
        print(self.get_cell_by_axis(0,0))
    
    def show_mine(self):
        #A logic do interrupt thegame anddisplay a message that player lost!
        self.cell_btn_object.configure(bg='red')
    
    def right_click_actions(selft, event):
        print(event)
        print("I am right clicked!")
    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
            
            
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
