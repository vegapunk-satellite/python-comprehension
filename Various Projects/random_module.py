import random

x = []
i = 0
while i < 10:
    i += 1
    x.append(random.randint(0, 100))

print(x)

number = int(input("Give me a number: "))

print(min(x))
print(max(x))

for num in x:
    if num == number:
        print("You found the number")
        break

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print("9 ", end="")
    print("\n")

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print("9 ", end="")
        k += 1

    k = 0
    print("\n")


def find_max_zeroes(num):
    if not num:
        return 1
    bin_num = bin(num)[2:]
    print(bin_num)
    return len(max(bin_num.replace("1", " ").split(), key=len))


if __name__ == "__main__":
    num = int(input("Enter integer number:"))
    max_zeroes = find_max_zeroes(num)
    print("max 0's count is", max_zeroes)

# key for mix and matches with the text
