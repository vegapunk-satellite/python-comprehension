# Python allows users to loop through various types of data.
# Looping through a whole list of numbers:
nums = [1, 2, 3, 4, 5]


for num in nums:
    print(
        nums
    )  # Returns all the values in the list from beginning up until the end on every next iteration.


# 'break' quits the loop, while 'continue' moves on with the next iteration.
# breaking out of a loop:
nums = [1, 2, 3, 4, 5]


for num in nums:
    if num == 5:
        print("Number found!")
        break  # Will break out from the loop and stop iterating; at the moment '5' is found.
    print(nums)  # Will prompt each element of the list; up until the conditional.


# Ignoring a value, while iterating through:
# Continue statement will skip to the next iteration of the list.
for num in nums:
    if num == 4:
        print("Hidden!")
        continue  # Prompts out the user message while skipping the conditional value.
    print(nums)  # Will continue prompting out the remainder of the list.


# Users can a loop within a loop, with 'nested loops':
# Iterating through the letters 'abc' with each number in our list.
for num in nums:
    for (
        letter
    ) in (
        "abc"
    ):  # Users have the ability to replace the conditional, with an inner loop.
        print(num, letter)


# Looping through within a range of values:
# Let us try looping from 1 up until 10
# range(starting_number, up_to_but_not_included_number)
for i in range(
    1, 11
):  # In cases where the starting number is not passed in, by default starts from '0'.
    print(i)
