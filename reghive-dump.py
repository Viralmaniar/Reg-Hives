# Import tkinter library
from tkinter import *

# Define empty outer window
window=Tk()

window.title("Reghive-Dumper")
window.geometry('450x450')
window.configure(bg='black')

# sam command function. Need better structure to pass values to text.
def sam():
    print("debug")

def exit():
    print("Goodbye!")
    window.quit()

logo=r"""
Reghive-Dumper
[+] Author: Viral Maniar
[+] Twitter: @ManiarViral
"""
l1 = Label(window,bg='green',justify=LEFT, text=logo, font=("Bauhaus 93", 25))
l1.pack()

# Creating button for the SAM key
b1 = Button(window, text="Save SAM",command=sam).pack()
#b1.grid(row=350,column=350)

# Creating button for the SECURITY key
b2 = Button(window, text="Save SECURITY").pack()
#b2.grid(row=150,column=2)

# Creating button for the SYSTEM key
b3 = Button(window, text="Save SYSTEM").pack()
#b3.grid(row=150,column=3)

b4 = Button(window, text="EXIT",command=exit).pack()
#b4.grid(row=150,column=4)

# Adding widgets to the window
'''t1=Text(window)
t1.grid(row=1,column=2)'''

# Call mainloop
window.mainloop()
