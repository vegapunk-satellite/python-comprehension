# Passing arguments into a function is simply creating parameters within the parenthesis.
# Customizing the greeting.
def greeting_msg(greeting):
    return "{} friend!".format(greeting)


# Whenever the parameters within the parenthesis are required arguments, like in current case.
# Upon the execution; users have to pass in the argument which they created.
# In cases where it's accidentaly forgotten, users will be prompted out with a TypeError.
# print(greeting_msg())

# Let's pass in our preferential phrase into the function, for the 'greeting' argument.
# Which will set it equal to the string users chose.
print(greeting_msg("Welcome"))


# In cases where there is a default value for the parameters;
# users have the freedom of not passing in an argument, which can be convenient in some cases.
def specific_greeting(greeting, name="friend"):
    return "{} {}!".format(greeting, name)


print(
    specific_greeting("Howdy")
)  # Successfuly executes even without second argument due to the given default value.
print(specific_greeting(greeting="Come on in and make yourself at home"))

# Required positional arguments have to come before keyword arguments.
# print(specific_greeting(name="Makino-san", "Hey there"))  # Returns a SyntaxError.
print(specific_greeting("Hey there", name="Makino-san"))  # Correct syntax.
