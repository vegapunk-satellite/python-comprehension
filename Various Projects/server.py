# Write a function named apply_operation that takes a dictionary as input of the following form:
# Each key is a string: either “+”, or “*”. Each value is a list of integers.
# Your function should return a list of integers where the operation in the key is applied on the
# integers in the value.
# For example if the input is: [ (“+”, [1, 2, 3, 4]), (“*”, [2, 3, 4]), (“+”, [-2, -1, 5]), (“*”, [-2, 4, 6]) ],
# the return value should be [10, 24, 2, -48]. Write a test for your function.


from functools import reduce

def apply_op(op, values):
    match op:
        case "+":
            return reduce(lambda a, b: a + b, values)
        case "*":
            return reduce(lambda a, b: a * b, values)


def apply_operation(operation_values_list):
    return [apply_op(t[0], t[1]) for t in operation_values_list]

# def apply_operation(operation_values_list):
#     output = []
#     for t in operation_values_list:
#         op = t[0]
#         values = t[1]
#         result = apply_op(op, values)
#         output.append(result)
#     return output


inputs = [("+", [1, 2, 3, 4]), ("*", [2, 3, 4]), ("+", [-2, -1, 5]), ("*", [-2, 4, 6])]
print(apply_operation(inputs))