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
    width=settings.WIDTH,
    height=utils.height_pctr(25)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',# Change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
let_flame.place(x=0, y=utils.height_prct(25))
                  
center_frame= Frame(
    root,
    bg='green', # Change laterto black
    width=utils.width_prct(75)
    height=utils.height_prct(75)
)
                  
# Run the Window
root.mainloop()
