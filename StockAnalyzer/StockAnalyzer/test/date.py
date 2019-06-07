#datetime object structure
#object
#    timedelta
#    tzinfo
#    time
#    date
#        datetime

import datetime

# current date
print "Finding today's dates"
now = datetime.datetime.now()
print now.hour
print now.minute
print now.year
print now.day
print now.month
print now.strftime("%Y-%m-%d %H:%M")

# previous date
print 'Creating previous dates'
previous = datetime.datetime(2003, 8, 4, 21, 41, 43)
print previous.hour
print previous.minute
print previous.year
print previous.day
print previous.month
print previous.strftime("%Y-%m-%d %H:%M")

print 'Looping through dates'
from datetime import date
from dateutil.rrule import rrule, DAILY # install python-dateutil

a = date(2009, 5, 30)
b = date(2009, 6, 9)

for dt in rrule(DAILY, dtstart=a, until=b):
    print dt.strftime("%Y-%m-%d")
    
# using timedelta
print 'Using timedelta'
# timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
from datetime import timedelta

td = timedelta(weeks=52)
c = a - td
print a, ' - ', td, ' = ', c


