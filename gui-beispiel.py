from tkinter import *

def action():
    print("Aua!")

def exit():
    quit()

root = Tk()
root.attributes('-fullscreen', True)
root.title('Hit me')

button = Button(root, text = "Hit me!", command = action)
button.pack()

button = Button(root, text = "Exit", command = exit)
button.pack()

mainloop()