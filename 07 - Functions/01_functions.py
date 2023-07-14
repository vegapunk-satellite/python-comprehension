# Functions are basicly some instructions packaged together that perform a specific task.
# Users can create functions with 'def' keyword, which stands for definition.
def user_func():  # In cases functions have parameters, they all go inside the parenthesis.
    pass  # 'pass' keyword allows users to have blank functions, which they can populate at a different time.


# Running the created function:
# Putting parenthesis is crucial for the execution of the function.
print(
    user_func
)  # Won't be running the user function. Instead returns the location of the function within the memory.
user_func()  # Returns 'None' in cases where users 'pass' the definition.


# Testing out the real time usefulness of defining a greeting function:
# Assume that users was given a task of creating a script that;
# prints out multiple recent discounts whenever it is executed.
# The manual approach is really tedious... And can lead users to have simple mistakes.
print("NOVEMBER FEVER IS HERE!")
print(
    "Pick and choose among four different discounted bundles, made in collab with Soul King!"
)
print("Discounts up to %58 for electronic soundbars!")
print("Lumix lenses discounted up to %38!")
print("Panasonic Web Store")


# In some instances these four lines above might need to be on hundreds of locations in multiple different files...
# Functions come in handy in such cases. Allows users put code with a specific purpose into a single location.
# Described concept is known; 'keeping the code DRY(don't repeat yourself)' among the CompSci community.
def discount_msg():
    print("NOVEMBER FEVER IS HERE!")
    print(
        "Pick and choose among four different discounted bundles, made in collab with Soul King!"
    )
    print("Discounts up to %58 for electronic soundbars!")
    print("Lumix lenses discounted up to %38!")
    print("Panasonic Web Store")


discount_msg()


# Up above at the beginning of the script we used 'pass' and it returned 'None';
# But that is not the case whenever the function is defined.
def greeting_msg():
    return "Hello friend!"


print(
    greeting_msg()
)  # When function is executed; the 'return' value will be equal to the data type, in current case it is a string; 'str'.

# Users can treat the 'return' value just like the data type which it is.
# Understanding this concept will allow users to chain together some functionality...
# Let us grab that returned string value and try to execute it with some methods which we learned a while ago.

# Uppercasing the returned value:
print(greeting_msg().upper())
