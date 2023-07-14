# Extremely useful method when printing out DateTime information, like logs or reports.
import datetime


my_date = datetime.datetime(1513, 5, 5, 10, 20, 56)
print(my_date)


# Formatting the according to example: 'Month XX, XXXX'
reformatted = "{:%B %d, %Y}".format(my_date)
print(reformatted)


# Formatting the according to example: 'Month XX, XXXX fell on a Day and was the number XXX day of that year.'
sentence = (
    "{0:%B %d, %Y} fell on a {0:%A} and was the number {0:%j} day of that year.".format(
        my_date
    )
)
print(sentence)


# All functional formatting values are accessible to users within the datetime documentation.
# Reading documentation will benefit the users greatly.
