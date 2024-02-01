
from tkinter import *
from datetime import *
root = Tk()
root.title("Greeting app")
root.geometry("1000x400")
f = ("Times New Roman", 100, "bold")

dt = datetime.now()
hr = dt.hour
msg=""
if hr < 12:
	msg="Good Morning"
elif hr <16:
	msg="Good Afternoon"
else:
	msg="Good Evening"

lab = Label(root, text=msg,font=f,fg="red")
lab.pack(pady=50)
root.mainloop()