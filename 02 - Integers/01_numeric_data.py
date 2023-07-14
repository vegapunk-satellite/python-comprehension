# Passing in variables which contain numeric data to the 'type()' function allows the user to grab data type.
num = 3
num_pi = 3.14


print(type(num))
print(type(num_pi))


"""
Arithmetic Operators:
Addition              +
Subtraction           -
Multiplication        *
Division              /
Floor Division       //
Exponent             **
Modulo                %
"""


# While I'm sure everybody reading the script is pretty familiar with first four operators; ' + - * / '
# If users wish to drop the decimal on division operation, using floor division will suffice. ' // '
# Next operator allows users to work with exponents and powers. ' ** '
# Last operator is called the modulo operator. Returns the remainder after a division. ' % '


flr_div = 14 // 4
print(flr_div)


expo = 5**6
print(expo)


m_op = 157 % 8
print(m_op)


# A common use case for the modulo operator is to tell if a number is even or odd.
# Every time we divide a number by '2' there are only two possible remainders.
# Result is either going to be '0' if the number is even, '1' if the number is odd.


# Printing out the even numbers:
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for num in n_list:
    if num % 2 == 0:
        print(num)


# Just like in real life Math class arithmetic, we can also use parentheses in our code to change the order of operations.
print(3 * 2 + 1)  # returns '7'
print(3 * (2 + 1))  # returns '9'


# Incrementing a variable:
num = 1
num_2 = 29


# num = num + 1
num += 1  # Simpler alternative of the code above, can be applied with other operations as well.
num_2 *= 3


print(num)
print(num_2)
