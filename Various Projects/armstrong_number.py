# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
# 370 = 3*3*3 + 7*7*7 + 0*0*0
#
#
# 153 % 10   --> 3 !!!
# 153 // 10 --> 15
# 15 % 10  --> 5 !!!
# 15 // 10 --> 1
# 1 % 10 --> 1 !!!
# 1 // 10 --> 0 (END)


def is_armstrong_number(number, power):
    number_as_string = str(number)
    sum = 0
    for char in number_as_string:
        digit = int(char)
        sum += digit**power
    if number == sum:
        return True
    else:
        return False


def is_armstrong_number(number, power):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit**power
        temp = temp // 10
    if number == sum:
        return True
    else:
        return False


for i in range(0, 1000000):
    if is_armstrong_number(i, 3):
        print(f"{i} is an armstrong number with power 3")
