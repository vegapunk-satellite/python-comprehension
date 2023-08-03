# Datetime module:
# Working with dates using python:
# Naive dates and times don't have enough information to determine things like timezones or daylight savings.
# While on the other hand, aware dates and times let users access those values.


# In simple cases using naive dates and times tend to be more convenient.
import datetime


# Will be using years, months, days when working with dates.
d = datetime.date(
    1524, 5, 5
)  # (year, month, day) Month and day must not have leading 0. Have to be regular integers.
print(d)
today = datetime.date.today()  # Built-in method to access date of today.
print(today)
print(d.year)  # Accessing the desired date's year individually.
print(
    today.day
)  # Accessing the number of a day within its calendar month individually.
print(d.month)  # Accessing the desired date's month individually.


#'.weekday()' and '.isoweekday()' both return a number for each day:
print(today.weekday())  # Indexes start from 0. Monday: 0, ..., Sunday: 6
print(today.isoweekday())  # Indexes start from 1. Monday: 1, ..., Sunday: 7


# Time Deltas are simply the difference between dates or times.
# 'date2 = date1 + timedelta'
tdelta = datetime.timedelta(days=7)  # Setting the duration difference to seven days.
print(today + tdelta)  # One week later.
print(today - tdelta)  # One week before.


# Calculating how many days until user's birthday in that year:
# 'timedelta = date1 + date2'
birthday = datetime.date(2024, 5, 18)
till_bday = birthday - today
print(till_bday)  # Returns the time delta between two dates.
print(till_bday.days)  # Returns total duration measured in days.
print(till_bday.total_seconds())  # Returns total duration measured in seconds.


# Working with times using python: (Less frequently used.)
# Will be using hours, minutes, seconds and microseconds when working with times.
# No timezone information is given within these examples yet, so still counted as 'naive' datetime.
import datetime


t = datetime.time(8, 24, 12, 10004)  # (hour, minute, second and microsecond)
print(t)
print(t.hour)  # Accessing the hour variable individually.


# Most of the real life problems that require the time information, will require the date information as well.
# 'datetime.datetime()' lets users access both 'date' and 'time' information at once. (More convenient way.)
import datetime


d_t = datetime.datetime(
    1524, 4, 21, 9, 15, 54, 100011
)  # (year, month, day, hour, minute, second and microsecond)
print(d_t)  # Returns the entire date and time values.
print(d_t.year)  # Returns only the year value.
print(d_t.time())  # Returns only the time values.
tdelta = datetime.timedelta(hours=12)  # Setting the time delta to twelve hours.
print(
    d_t + tdelta
)  # Adding time delta to the specific date. (Any other arithmetic operation can be applied.)


# Alternative constructors that come with '.datetime()':
dt_today = (
    datetime.datetime.today()
)  # Returns the local date and time without a timezone value.
dt_now = (
    datetime.datetime.now()
)  # Returns a naive date time when the timezone value is left empty such as in current example.
dt_utcnow = (
    datetime.datetime.utcnow()
)  # Returns the time of the UTC-0 but without a timezone value.


print(dt_today)
print(dt_now)
print(dt_utcnow)
