# Aware dates and times let users determine the timezones and keep track of daylight savings.
# Even though it is a third party package, 'pytz' has been recommended in Python's official documentation at the timezone section.
# It can be installed within the command prompt via the pip.
# From our terminal we just need to type in 'pip install pytz'.


# Using 'pytz':
import datetime
import pytz


# Creating timezone aware dates and times via 'pytz.UTC'.
dt = datetime.datetime(
    1524, 5, 5, 6, 20, 56, 110011, tzinfo=pytz.UTC
)  # Adding in tzinfo as an argument and creating aware datetime.
print(dt)  # '+00:00' is the UTC offset.


dt_now = datetime.datetime.now(
    tz=pytz.UTC
)  # Adding in tz as an argument and creating aware datetime.
print(dt_now)  # Returns the current UTC time.


dt_utcnow = datetime.datetime.utcnow().replace(
    tzinfo=pytz.UTC
)  # Replacing tzinfo to pytz.UTC, 'utcnow()' becomes an aware datetime.
print(dt_utcnow)  # Returns the current UTC time.


# Accessing all of the timezones within the 'pytz':
for tz in pytz.all_timezones:
    print(tz)


# Converting to a different timezone:
import datetime
import pytz


# Usage of 'astimezone()' method:
dt_colorado = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
print(dt_colorado)
dt_sydney = dt_utcnow.astimezone(pytz.timezone("Australia/Sydney"))
print(dt_sydney)


# Converting our 'naive' datetime to a timezone 'aware' datetime:
import datetime
import pytz


dt_fethiye = (
    datetime.datetime.now()
)  # 'naive' datetime since there is no timezone as an argument.
fethiye_tz = pytz.timezone("Europe/Istanbul")  # Converting to the desired timezone.


# Timezone '.localize()' function converts a naive datetime into an aware one.
dt_fethiye = fethiye_tz.localize(dt_fethiye)  # 'aware' datetime.
print(dt_fethiye)


# After converting the naive datetime into an aware one; users can change the timezone again when desired.
dt_us_eastern = dt_fethiye.astimezone(pytz.timezone("US/Eastern"))
print(dt_us_eastern)


# Couple of simple ways to display datetime:
# Used formats can be found in Python's official documentation at the timezones section.
import datetime
import pytz


dt_fethiye = datetime.datetime.now(tz=pytz.timezone("Europe/Istanbul"))
# ISO format tends to be helpful when users want to save these dates or pass them around for internal use.
print(dt_fethiye.isoformat())


# 'strftime' - Converting datetime into a string.
# 'strptime' - Converting a string into datetime format.
# Let us test with an example where the desired format is: 'Month XX, XXXX'
print(dt_fethiye.strftime("%B %d, %Y"))


# Converting a string into datetime format:
dt_string = "July 2, 2023"
dt = datetime.datetime.strptime(dt_string, "%B %d, %Y")
print(dt)
