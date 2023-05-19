from tkinter import *
import settings
import utils


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(root, bg='red', 
    # Change later to black, 
    width=1400,
    height=180)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',# Change later to black
    width=360,
    height=540
)
let_flame.place(x=0, y=180)
# Run the Window
root.mainloop()
