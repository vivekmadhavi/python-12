from  tkinter import *
from datetime import *

root=Tk()
root.title("greeting app")
root.geometry("1000x600")
f = ("Arial",100,"bold") 

dt = datetime.now()

wd = dt.weekday()
msg=""
if wd < 5:
	msg="office time"
else:
	msg="party time"
lab = Label(root , text=msg , font=f , fg="red")
lab.pack(pady=50)
root.mainloop()