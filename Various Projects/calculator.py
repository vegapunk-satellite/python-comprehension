# "12 + 13 - 5 * (4-2)"
# "9*3 - 12/4 + 4"

# def calculate(operations):
#     pass


def greeting():
    print(
        """
Calculator is operating...
"""
    )


def calculate():
    operation = input(
        """
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
"""
    )

    number_1 = float(input("Please enter the first number: "))
    number_2 = float(input("Please enter the second number: "))

    if operation == "+":
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

        again()

    elif operation == "-":
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

        again()

    elif operation == "*":
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

        again()

    elif operation == "/":
        print("{} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)

        again()

    else:
        print("You have not typed a valid operator, please run the program again.")

        again()


def again():
    calc_again = input(
        """
Do you want to calculate again?
Please type Y for YES or N for NO.
"""
    )

    if calc_again.upper() == "Y":
        calculate()
    elif calc_again.upper() == "N":
        print("See you later.")
    else:
        again()


calculate()
