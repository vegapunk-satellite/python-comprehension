# Spotting the values that evaluate to False tends to be convenient:
"""
Various values which evaluate to 'False':

False
None
0(Zero) of any numeric type
Any empty sequence. For example; '' () []
Any empty mapping. For example; {}
"""

condition = 0

if condition:
    print("Evaluated to True")
else:
    print(
        "Evaluated to False"
    )  # Returns 'False', since '0' will naturally be evaluated false.

# Now that we know the values that evaluate to 'False';
condition = "This is the way!"  # any other value by default will evaluate to True...

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
