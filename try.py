from datetime import datetime, timedelta, time #, strftime, strptime
import time as tm

d = datetime.now()
fr_data = "%Y-%m-%d %H:%M:%S"
empty = time(0,0,0)
endT = d + timedelta(seconds=3)

'''

So, I can convert timedelta object to str type
And string type datetime to datetime

But converting a timedelta or datetime object to string using str()
will require milliseconds

converting to datetime object requires two arguments. One the datetime and the other, the time format

'''
hms = "%H:%M:%S"
def to_str(dateTime):
	dateSTR = dateTime.strftime(fr_data)
	return dateSTR

def to_dt(dateTime):
	dateDT = datetime.strptime(dateTime, fr_data)	
	return dateDT

def to_HMS(dateTime):
	dateHMS = datetime.strptime(dateTime, hms)
	return dateHMS

while True:
	e = endT-datetime.now()
	#print(e)
	print(type(str(e)))
	print(str(e).split('.')[0])
	#print(e.split('.')[0])
	#print(cd[8:])
	# v = to_str(e)
	# print(v)
	#to_str(e)
	#print(to_dt(v))
	tm.sleep(1)
	de = e
	if e<timedelta(hours=0,minutes=0,seconds=1):
		# s = str(e)
		# print(to_str(s))
		print("done")
		break
	cc = e 


# dee = str(de).split('.')[0]
# print(dee, type(dee))
# print(de, type(de))
# cx = dee[8:]
# print(to_HMS(cx))
#print(to_HMS(str(dee)[0]))
# print(de)
# print(type(de))
# print(cc)
# print(type(cc))

#asd = str(cc)
#print(to_dt(asd))
#print(type(to_dt(asd)))

# c = str(endT)					This few lines represent on the fact that
# print(type(c), c)				datetime or timedelta can be converted
								#into datetime object
# cd = to_str(endT)
# print(type(cd), cd)

# de = to_dt(c)
# print(type(de), de)
