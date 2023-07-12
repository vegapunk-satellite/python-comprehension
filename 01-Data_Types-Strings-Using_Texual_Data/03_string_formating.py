# String Formating:
# Accessing values within dictionaries:
person_dict = {"name": "Jenn", "age": 23}
# We could have used 'string concatenation'; but it is not so readable.
# If user has an integer; it needs to be cast into a string before being used.
# Plus it leaves room for a lot of small mistakes.

# So, formating is a nice option. A lot easier to read...
# The braces('{}') are placeholders and after our string closes we run the '.format()' method.
# And then we pass in the values which we want to replace our placeholders with.
sentence_1 = "My name is {} and I am {} years old.".format(
    person_dict["name"], person_dict["age"]
)
print(sentence_1)

# Users can explicitly number each placeholder, in cases where the values need to repeat:
tag = "hl"
text = "This is a headline"

sentence_2 = "<{0}> {1} <{0}>".format(tag, text)
print(sentence_2)

# On previous examples we passed in a dictionary into 'format' function;
# we were accessing the necessary of that dictionary within 'format'.
# Alternative way to access these fields from directly within placeholders:

# sentence_3 = "My name is {0[name]} and I am {1[age]} years old.".format(person_dict, person_dict)

# Since we pass in same dictionary twice, let's go ahead and polish our code for the sake of efficiency.
sentence_4 = "My name is {0[name]} and I am {0[age]} years old.".format(person_dict)
print(sentence_4)

# We can access values within 'list/s' using same logic above.
person_list = ["Jenn", 23]
# Instead of key, value pairs; we fill in the desired indexes of the given list inside our placeholders.
sentence_5 = "My name is {0[0]} and I am {0[1]} years old.".format(person_list)
print(sentence_5)
