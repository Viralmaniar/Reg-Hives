# Import tkinter library
from tkinter import *

# Define empty outer window
window=Tk()

window.title("Reghive-Dumper")
window.geometry('800x400')
window.configure(bg='black')

# sam command function. Need better structure to pass values to text.
def sam():
    print("debug")

def exit():
    print("Goodbye!")
    window.quit()

def logo():
    logo='''
    ____                __     _                      ____
   / __ \ ___   ____ _ / /_   (_)_   __ ___          / __ \ __  __ ____ ___   ____   ___   _____
  / /_/ // _ \ / __ `// __ \ / /| | / // _ \ ______ / / / // / / // __ `__ \ / __ \ / _ \ / ___/
 / _, _//  __// /_/ // / / // / | |/ //  __//_____// /_/ // /_/ // / / / / // /_/ //  __// /
/_/ |_| \___/ \__, //_/ /_//_/  |___/ \___/       /_____/ \__,_//_/ /_/ /_// .___/ \___//_/
             /____/                                                       /_/
[+] Author: Viral Maniar
[+] Twitter: @ManiarViral
    '''
    print (logo())

t1 = Text(window, text="")
t1.grid()

# Creating button for the SAM key
b1 = Button(window, text="Save SAM",command=sam)
b1.grid(row=10,column=1)

# Creating button for the SECURITY key
b2 = Button(window, text="Save SECURITY")
b2.grid(row=10,column=2)

# Creating button for the SYSTEM key
b3 = Button(window, text="Save SYSTEM")
b3.grid(row=10,column=3)

b4 = Button(window, text="EXIT",command=exit)
b4.grid(row=10,column=4)

# Adding widgets to the window
'''t1=Text(window)
t1.grid(row=1,column=2)'''

# Call mainloop
window.mainloop()
