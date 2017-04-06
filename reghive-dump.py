# Import tkinter library
from tkinter import *

# Define empty outer window
window=Tk()

# sam command function. Need better structure to pass values to text. 
def sam():
    print("debug")

# Creating button for the SAM key
b1 = Button(window, text="Save SAM",command=sam)
b1.grid(row=0,column=1)

# Creating button for the SECURITY key
b2 = Button(window, text="Save SECURITY")
b2.grid(row=1,column=1)

# Creating button for the SYSTEM key
b3 = Button(window, text="Save SYSTEM")
b3.grid(row=2,column=1)

# Adding widgets to the window
t1=Text(window)
t1.grid(row=1,column=2)

# Call mainloop
window.mainloop()
