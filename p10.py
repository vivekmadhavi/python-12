from tkinter import *

root = Tk()
root.title("app by me")
root.geometry("1000x600")
f =("Arial",50,"bold")
labtitle= Label(root , text="Even odd finder by me",font=f)
labtitle.pack(pady=20)
def check():
	try:
		num=int(entNumber.get())
		msg=""
		if num %2==0:
			msg="even"
		else:
			msg="odd"
		labMsg.configure(text=msg)
	except ValueError:
		labMsg.configure(text="enter integer only")

labNumber= Label(root, text="enter integer",font=f)
entNumber = Entry(root, font=f)
btncheck= Button(root, text="find", font=f,command=check)
labMsg = Label(root, font=f)			

labNumber.pack(pady=10)
entNumber.pack(pady=10)
btncheck.pack(pady=10)
labMsg.pack(pady=10)
root.mainloop()