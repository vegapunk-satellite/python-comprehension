# Factorial program
def factorial(x):
    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


num = int(input("Enter a number: "))

result = factorial(num)
print("The factorial of", num, "is", result)

# # Python program to find the largest number among the three input numbers
#
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
#
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3
#
# print("The largest number is", largest)

# Division table program
# number = int(input("Insert a number for a division table: "))
# for i in range(1, 11):
#     print(number, "x", i, "=", number*i)

# # Program to check if a number is prime or not
#
#
# # To take input from the user
# num = int(input("Enter a number: "))
#
# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")


# # Program to display the Fibonacci sequence up to n-th term
#
# nterms = int(input("Insert desired terms of Fibonacci Sequence: "))
#
# # first two terms
# n1, n2 = 0, term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence up to",nterms,": ")
#    print(n1)
# # generate fibonacci sequence
# else:1
# count = 0
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer.")
# # if there is only one
#    print("Fibonacci Sequence: ")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1