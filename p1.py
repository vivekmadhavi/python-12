#wapp to demo datetime module


from datetime import *

dt = datetime.now()
print(dt)

d= datetime.now().date()
print("date",d)

t = datetime.now().time()
print("time",t)


print(dt.day)
print(dt.month)
print(dt.year)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print(dt.weekday())
