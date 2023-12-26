# Dictionaries allow users to work with key & value pairs.
# Users may have heard this concept from other languages; under names of 'hash maps' or 'associative arrays'.
# Key & value pairs are two linked values; where 'key' is a unique identifier, that lets us find the data. And 'value' is that data.


# Let us try defining a student variable using a dictionary:
student = {
    "name": "Robin",
    "age": 30,
    "courses": ["History", "CompSci"],
}  #'value/s' can be any type of immutable data.
print(student["name"])
print(student["age"])
print(student["courses"])


# If users search an invalid key, python will prompt KeyError:
# print(student['phone'])


# We can overcome the KeyError issue by simply using the '.get()' method.
# Instead of the error message, it will return None.
print(student.get("phone"))  # Returns None
print(student.get("name"))  # Returns the value of the  specific key


# We can also specify a default value for the keys that don't exist;
# by passing that default value as a second argument;
print(student.get("phone", "Not Found"))


# Adding that non-existent key into the dictionary:
# dict['key'] = value
student["phone"] = "556-8787"
# Updating the value of an existed list:
student["name"] = "Nico Robin"
print(student)


# Updating the whole dictionary:
# Update method allows the user to have more configuration over the specific dictionary.
student.update(
    {
        "name": "Tony Chopper",
        "age": 17,
        "phone": "556-0110",
        "courses": ["Medicine", "Chemistry"],
    }
)
print(student)


# Removing values from the dictionary:
# Removing the key directly:
del student["phone"]


# Popping the key to store it inside a variable:
age = student.pop("age")
print(student)
print(age)
