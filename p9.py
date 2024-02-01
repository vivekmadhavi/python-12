from tkinter import *
from datetime import *

root = Tk()
root.title("app by kamal sir")
root.geometry("2000x600")
f = ("arial",70,"bold","italic")

def show():
	name = entName.get()
	dt=datetime.now()
	hr =dt.hour
	msg = ""
	if hr <12:
		msg="Good Morning"
	elif hr <16:
		msg="Good Afternoon"
	else:
		msg="Good Evening"
	rep = msg + " " + name.title()
	labMsg.configure(text=rep)


labName = Label(root , text="enter  name",font=f)
entName = Entry(root,font=f)
btnSubmit = Button(root, text="Submit",font=f, command=show)
labMsg = Label(root, font=f)

labName.pack(pady=10)
entName.pack(pady=10)
btnSubmit.pack(pady=10)
labMsg.pack(pady=10)

root.mainloop()