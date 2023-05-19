from tkinter import *


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry('1440x720')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(root, bg='red', 
    # Change later to black, 
    width=1400,
    height=180)
top_frame.place()

# Run the Window
root.mainloop()
