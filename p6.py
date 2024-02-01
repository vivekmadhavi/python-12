from tkinter import *


root =Tk()
root.title("my first app")
root.geometry("400x300")
f=("Arial", 30 ,"bold")

lab =  Label(root, text="welxome to GUI",font=f)

lab.pack(pady=100)

root.mainloop()