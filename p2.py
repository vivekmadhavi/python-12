#wapp to check the current year is a leap year
#leap year --> every 4yr ad 400yr
#century year --> 1900,2000,2100


from datetime import *

dt =datetime.now()
year=dt.year

year = 20024

# fresher

if year % 4 ==0:
	print("it is a leap year")
else:
	print("its not a leap year")

# expert

if ((year % 100 ==0) and (year % 400 ==0)) or ((year %100 !=0) and (year % 4 ==0)):
	print("it is a leap year")
else:
	print("it not a leap year")