# Sets are basicly unordered collection of values with no duplicates.
cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}

# Will print out in a random order at each execution, due to the given nature of sets.
print(cs_courses)  # Got rid of duplicate "Math"

# More common usages of 'sets':
# 01 - Membership Test('Testing out whether a value is part of the set.'):
print("Math" in cs_courses)  # Returns a boolean value, for the specific case 'True'.
# Could be done with lists and tuples as well; but sets are more optimized for this feature...


# 02 - Determining the values which sets share or don't share within each other:
comp_sci_courses = {"History", "Math", "Physics", "CompSci"}
art_courses = {"History", "Math", "Art", "Design"}

# Spotting same values:
print(
    comp_sci_courses.intersection(art_courses)
)  # returns intersecting values of two sets
# Spotting out the different values:
print(comp_sci_courses.difference(art_courses))  # returns the uncommon CompSci courses
# Combining two sets:
print(comp_sci_courses.union(art_courses))  # returns all available courses

# Creating empty; lists, tuples, sets:
# Empty Lists
empty_list = []
empty_list_2 = list()

# Empty Tuples
empty_tuple = ()
empty_tuple_2 = tuple()

# Empty Sets
empty_set = {}  # Won't be returning an empty set... It's an empty dictionary!
empty_set_2 = set()  # Correct syntax for creating an empty set!
