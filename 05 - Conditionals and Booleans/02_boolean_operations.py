# Boolean Operations:
# 'and', 'or', 'not':
user = "Admin"
logged_in = True

# Having two seperate conditions for the specific cause:
# Usage of the 'and' keyword:
if user == "Admin" and logged_in:
    print(
        "Admin Page"
    )  # In this specific case will return the 'if' statement's message, since both conditions are 'True'.
else:
    print(
        "Bad Creds"
    )  # Prompts out whenever a condition or multiple conditions are 'False'.


# In cases where users only cares about one of the conditionals is necessary:
# Usage of the 'or' keyword:
user = "Admin"
logged_in = False

if user == "Admin" or logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# In cases where switching boolean values is convenient;
# meaning changing 'True' to a 'False' or visa versa...
# Usage of the 'not' keyword:
user = "Admin"
logged_in = False

if not logged_in:  # Basicly means 'if not logged in'; prompt this condional's message.
    print("Please Log In")
else:
    print("Welcome")


# The difference among '==' and 'is' operators:
# ' == ' (equal) operator checks for object values, while on the other hand;
# 'is' operator checks for object identity which stands for sharing the same ID inside memory.
# Two objects might have the same exact value, yet still can have seperate locations on system's memory.

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Returns 'True' since both lists have same values.
print(id(a))  # Object identity for 'a'.
print(id(b))  # Object identity for 'b'.
print(a is b)  # Returns 'False' since both lists have seperate object identities.

a = b  # (id(a) == id(b))
print(a is b)
