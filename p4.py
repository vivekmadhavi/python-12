#wapp to show ot or pt


from datetime import *

dt = datetime.now()
wd=dt.weekday()

if wd <5:
	print("office time")
else:
	print("party")