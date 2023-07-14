if False:
    print("Conditional was false.")  # Does simply nothing.

if True:
    print("Conditional was true.")  # Returns the print statement.

# Unlike the code above; putting some code that evaluates to either True or False will be more convenient for users.
# For example; let us execute a print statement only if the language is 'Python'.
"""
Comparison Signs:

Equal:            ==
Not Equal:        !=
Greater Than:     >
Less Than:        <
Greater or Equal: >=
Less or Equal:    <=
Object Identity:  is
"""

# 'if' statements:
language = "Python"

if language == "Python":
    print("You are currently using Python v3.11")


# 'else' statements:
language_2 = "Python"

if language_2 == "Python":
    print("You are currently using Python v3.11")
else:
    print("No match!")


# Checking for multiple conditionals:
# 'elif(else if)' statements:
# Unlike 'if' and 'else'; users are able to create many 'elif' statements for the sake of their specific purpose.
# Users whom are coming from another programming languages; at this point might be expecting to use a term called 'switch case',
# but Python does not have switch case feature simply because ' if - elif - else ' statements are plenty clean enough...

language_3 = "Java"

if language_3 == "Python":
    print("Conditional was True")
elif language_3 == "Java":
    print("Language is Java")
elif language_3 == "JavaScript":
    print("Language is JavaScript")
else:
    print("No match")
