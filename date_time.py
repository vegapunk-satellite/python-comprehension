# Datetime module:
#'naive date and time' don't have enough information to determine things like time zone or daylight savings
# but they are easy to use in simple cases
# will be using years, months, days when working with 'date'
import datetime

d = datetime.date(1524, 5, 5)
print(d)
today = datetime.date.today()
print(today)
print(d.year)
print(today.day)
print(d.month)
print(today.weekday())  ##Monday: 0, ..., Sunday 6
print(today.isoweekday())  ##Monday: 1, ..., Sunday 7

# Time Delta
tdelta = datetime.timedelta(days=7)
print(today + tdelta)  ##One week later from today
print(today - tdelta)  ##One week before from today

# 'date2 = date1 + timedelta'
# 'timedelta = date1 + date2'

birthday = datetime.date(2024, 5, 18)
till_bday = birthday - today
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())
# -------------------------------------------------------------------------------------
# will be using hours, minutes, seconds and microseconds when working with 'time'
import datetime

t = datetime.time(8, 24, 12, 10004)
print(t)
print(t.hour)
# -------------------------------------------------------------------------------------
#'datetime.datetime()' combines the info 'date' and 'time' gives hence its usefulness
import datetime

d_t = datetime.datetime(1524, 4, 21, 9, 15, 54, 100011)
print(d_t)
print(d_t.year)
print(d_t.time())
tdelta = datetime.timedelta(days=7)
print(d_t + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)  ##returns current local date time with a timezone of 'None'
print(
    dt_now
)  # users have the option to pass in a timezone but if not returns same as above
print(dt_utcnow)  ##returns the current UTC time but the TZ info is still set to 'None'
# -------------------------------------------------------------------------------------
# So nothing we did so far has given us time zone 'aware' date times; we have to explicitly set those
# Using 'pytz'
# from our terminal we just need to type in 'pip install pytz'
#'pytz' has been recommended in Python's official documentation at the timezone section
# timezone aware
import datetime
import pytz

dt = datetime.datetime(1524, 5, 5, 6, 20, 56, 110011, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
# -------------------------------------------------------------------------------------
# We can add in any desired timezone through:
import datetime
import pytz

dt_colorado = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
print(dt_colorado)
dt_sydney = dt_utcnow.astimezone(pytz.timezone("Australia/Sydney"))
print(dt_sydney)
# Printing out all of the timezones in 'pytz':
for tz in pytz.all_timezones:
    print(tz)
# -------------------------------------------------------------------------------------
# converting our 'naive' date time to a timezone 'aware' one:
import datetime
import pytz

dt_fethiye = datetime.datetime.now()
fethiye_tz = pytz.timezone("Europe/Istanbul")

dt_fethiye = fethiye_tz.localize(dt_fethiye)  # 'naive' date time ---> 'aware' date time
print(dt_fethiye)

# after we converted our date time into an aware one we can change the TZ as we like:
dt_us_eastern = dt_fethiye.astimezone(pytz.timezone("US/Eastern"))
print(dt_us_eastern)
# -------------------------------------------------------------------------------------
# Couple of simple ways to display 'datetime':
import datetime
import pytz

dt_fethiye = datetime.datetime.now(tz=pytz.timezone("Europe/Istanbul"))
# ISO format is useful when we want to save these dates or pass them around for internal use
print(dt_fethiye.isoformat())

# 'strftime' - Datetime to String
# 'strptime' - String to Datetime
# Desired format: 'Month XX, XXXX'
print(dt_fethiye.strftime("%B %d, %Y"))
# Converting a string into date time
dt_string = "July 2, 2023"
dt = datetime.datetime.strptime(dt_string, "%B %d, %Y")
print(dt)
