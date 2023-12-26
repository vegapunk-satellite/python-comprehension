# Introduction:
# The data types that we'll be going over all have certain methods available to the users which gives access to a lot of useful functionality.
# Functions and methods are basically the same thing, a method is just a function that belongs to an object.


# String methods:
# Lowercasing or upper casing a string:
message = "Good times."
print(message.lower())  # all lowercase
print(message.upper())  # all uppercase


# Counting certain number of characters in our string:
#'count()' method takes a string as an argument
pun = "Hide a tree in a forest, Hide a ship in ships."
print(pun.count("s"))


# Locating certain characters:
print(
    message.find("times")
)  # the argument 'times' start at fifth index of our variable, hence the result
print(message.find("bad"))  # if our argument is not valid find method will return -1


# Replacing certain characters:
#'replace()' method takes two arguments; first the data we would like to replace, followed by its substitute.
#'replace()' method will return a new string with those values replaced, and won't change our original variable.
parallel_universe_message = pun.replace("ships", "docks")
print(parallel_universe_message)


# Concatenating strings:
hail = "Greetings"
proper_way_to_address = "dear customer"


# Using the plus('+') operator is a way to concatenate strings.
# But creates possibility for mistakes and gets tedious after some point.
# automated_store_message = hail + ' ' + proper_way_to_address + '! Would you like to have Senbei or Okaki?'
# print(automated_store_message)


# Formating tends to be more practical in these kind of situations:
automated_store_message = "{} {}! Would you like to have Senbei or Okaki?".format(
    hail, proper_way_to_address
)
print(automated_store_message)
