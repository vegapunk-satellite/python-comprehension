# While loops will keep running until the condition is met or hits a 'break'.
x = 0

while x < 10:  # Loop will run until the condition on this line evaluates to 'False'.
    print(x)
    x += 1  # Incrementing value within while loops is crucial, or else users might experiance an infinite loop.

# Breaking out of a while loop:
while x < 10:
    if x == 5:
        break  # Will break out of the loop before printing '5'.
    print(x)
    x += 1

"""In cases where users accidentally stuck on an infinite loop;
' crtl + c ' shortcut will help breaking out of it on most of the operating systems."""
