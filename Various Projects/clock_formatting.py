import datetime

time_entry = input('Enter a time in hh:mm:ss format:')
hours, minutes, second = map(int, time_entry.split(':'))
t = datetime.time(hours, minutes, second)

h = int(input('Hours:'))
m = int(input('Minutes:'))
s = int(input('Seconds:'))

print('Current time is:',t)

t1 = datetime.time(hours + h, minutes + m, second + s)
print('New time is:',t1)