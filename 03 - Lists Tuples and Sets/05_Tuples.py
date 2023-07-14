# Tuples too allow users to work with sequential data like lists we have seen previously.
# Both of these data types are very similar to each other, but with one major difference.


# Users can not modify tuples because they are immutable, while lists are mutable and modifiable.
# Consider using 'lists' upon the need of modification.
# Consider using 'tuples' upon the need of looping through and having access.


# Mutable Objects(lists):
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1


print(list_1)
print(list_2)


list_1[
    0
] = "Art"  # By changing list_1's first value, it also changed list_2. Because they are both the same mutable object.
print(list_1)
print(list_2)


# Immutable Objects(tuples):
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1


print(tuple_1)
print(tuple_2)


# tuple_1[
#     0
# ] = "Art"  # Tuple does not support item assignment hence python will prompt out a Type Error
# print(tuple_1)
# print(tuple_2)


# Users can loop through tuples, access values within them; basicly anything except what mutates.
