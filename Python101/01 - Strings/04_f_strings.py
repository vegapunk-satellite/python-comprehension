# 'f strings' is relatively recent functionality. Works only with python version 3.6 or above...
# Basically the idea behind 'f strings' is to make string formatting as simple as possible.
greeting = "Greetings dear customer"
statement = "Welcome to the world of the future!"


# Proper syntax: f'user_message'
# Instead of using the '.format()' method, users can pass in the variables within the placeholders.
message = f"{greeting}, {statement} Please mark the locations you wished to visit and enjoy the ride."
print(message)


# 'f strings' allow users to actually write code within the placeholder.
# For some reason if users want to tweak the variables with built in functionality;
# like upper casing the store statement part per se...
message_2 = f"{greeting}, {statement.upper()} Please mark the locations you wished to visit and enjoy the ride."
print(message_2)


# There are plenty of methods like '.upper()' which can be cast on strings.
# To see which attributes and methods can be used with that specific variable;
# users can pass that variable inside the 'dir()' function.
print(dir(greeting))


# To see in-depth information about these methods:
# Users can pass in 'str' within the 'help()' method. Reading documentation will help big time.
print(help(str))
# Users can pass in specific methods inside 'help', in cases where they are not sure about the functionality.
print(help(str.lower))
