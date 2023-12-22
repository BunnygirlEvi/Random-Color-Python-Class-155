from tkinter import *
import random
root = Tk()
root.title("Random Colors")
root.geometry("500x500")

dictionary = {"colour" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}

def randomColor(): 
    print(3)
    random_number = random.randint(0,7)
    root.configure(background = dictionary["colour"][random_number])
    
button = Button(root,text = "Click me", command= randomColor)
button.place(relx= 0.5, rely= 0.5, anchor= CENTER)
root.mainloop()