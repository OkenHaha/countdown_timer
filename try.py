from datetime import datetime, timedelta, time
import time as tm

d = datetime.now()
fr_data = "%H:%M:%S"
empty = time(0,0,0)
endT = d + timedelta(seconds=30)


def to_str(dateTime):
	dateSTR = dateTime.strftime(fr_data)
	return dateSTR

def to_dt(dateTime):
	dateDT = datetime.strptime(dateTime, fr_data)	
	return dateDT


while True:
	e = endT-datetime.now()
	print(e)
	print(type(e))
	# v = to_str(e)
	# print(v)
	#to_str(e)
	#print(to_dt(v))
	tm.sleep(1)
	if e<=timedelta(hours=0,minutes=0,seconds=0):
		print("done")
		break

c = to_str(endT)
print(type(c))
print(to_dt(c))
print(type(to_dt(c)))

# s = to_str(d)
# t = to_dt(s)
# print(s)
# print(t)
# print(type(s))
# print(type(t))



# print(d)
# print(endT)

# print(type(d))
# print(type(endT))

#e = endT - d

#print(e)
#print(type(e))

#f = str(e)
#print(f)
#print(type(f))

#g = datetime.strptime(f, fr_data)
#print(g)
#print(type(g))


#z = datetime.now().time()

#print(datetime.now().time())

#x = z.strftime(fr_data) + endT.strftime(fr_data)
#print(x)





