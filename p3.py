#wapp to wish the user GM/GA/GE

from datetime import *

dt=datetime.now()
hr=dt.hour

msg=""
if hr<12:
	msg ="Gm"
elif hr<16:
	msg ="GA"
else:
	msg="GE"

print(msg)