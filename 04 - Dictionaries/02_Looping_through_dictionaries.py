student = {"name": "Sanji", "age": 21, "courses": ["Gastronomy", "Art"]}

print(len(student))  # Returns the number of keys inside that dictionary.
print(student.keys())  # Returns all the specific key names.
print(student.values())  # Returns all the values.
print(student.items())  # Returns key and value pairs.

# Looping through key and values:
for x in student:
    print(x)  # Standard looping will only print keys, but not the values.

# '.items()' method we previously saw let's users loop through key & value pairs.
for key, value in student.items():
    print(key, value)  # Proper syntax for printing out both keys and values.
