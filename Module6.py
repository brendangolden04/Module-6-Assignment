import sys
for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 6:
        data = date, time, store, item, cost, payment = data
        print('0}\t{1}'.format(item, cost))

from datetime import datetime
from datetime import timedelta

# add 1 day

print(datetime.now() + timedelta(days=1))

# Subtract 60 seconds
print(datetime.now() - timedelta(seconds=60))

# add 2 years
print(datetime.now() + timedelta(days=730))

d = timedelta(microseconds=-1)
print(d.days, d.seconds, d.microseconds)
g = timedelta(minutes=144613)
print(g.days, g.seconds)

datetime_object = datetime.now()
def heightandtime(x, y, z):
    print('The height is ',x,' feet and ',y,' inches.')
    print(z)


x = input('Enter Feet - ')
y = input('Enter Inches - ')
heightandtime(x, y, datetime_object)