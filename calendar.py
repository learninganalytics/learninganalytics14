import datetime

date1 = datetime.date(2014, 8, 24)
date2 = datetime.date(2014, 10, 05)
day = datetime.timedelta (days=1)
list_dates=[]

while date1 <= date2:
	list_dates.append(date1)
	date1 = date1 +day

print list_dates



