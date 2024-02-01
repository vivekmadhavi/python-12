#wapp to shpow number of days in current month

from datetime import *
dt=datetime.now()
month=dt.month

if month in (1,3,5,7,8,10,12) :
	print("31 days")
elif month in (4,6,9,11):
	print("30 days")
else:
	print("28/29 days")
print(month)