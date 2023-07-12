# Previously on string formatting, we have accessed necessary values within lists and dictionaries.
# We can also access attributes in a similar way.
# We will be using a small test class here called person which has 'name' and 'age' attributes.
# After, we need to create an instance of that specific class. Which later will be used as an argument when formating.
# Users can grab the desired value with '.attribute'
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_one = Person("Shanks", "39")
person_two = Person("Luffy", "19")

sentence_one = "My name is {0.name} and I am {0.age} years old.".format(person_one)
sentence_two = "My name is {0.name} and I am {0.age} years old.".format(person_two)
print(sentence_one)
print(sentence_two)

# Passing keyword arguments to format:
sentence_3 = "My name is {name} and I am {age} years old.".format(name="Shanks", age=39)
print(sentence_3)
# When users unpack a dictionary, it will fill in those keyword arguments.
# Most readable and convenient way to print out dictionary values
person = {"name": "Nami", "age": 20}
sentence_4 = "My name is {name} and I am {age} years old.".format(**person)
print(sentence_4)

# Format and print out numbers:
# While looping through 1 to 10 and print numbers of the output double digit(zero padded).
for i in range(1, 11):
    counter = "The value is {:02}".format(
        i
    )  #':03' within placeholder would have triple digitted the output
    print(counter)

# Formating decimal places:
pi = 3.14159265

sentence_pi = "Pi is equal to {:.2f}".format(pi)  #':.2f' for two decimals
print(sentence_pi)

# Putting in comma seperators for larger numbers:
sentence_cs = "1 MB is equal to {:,} bytes".format(
    1000**2
)  #':,' for comma seperating output
print(sentence_cs)
# We can even chain these formatting functionalities and use them together.
