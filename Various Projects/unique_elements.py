def find_unique_elements(input_list):
    numbers = {}
    for x in input_list:
        if x in numbers:
            numbers[x] += 1
        else:
            numbers[x] = 1

    return [number for number, count in numbers.items() if count == 1]





test_case = [1, 2, 2, 5, 4, 3, 2, 1]
print(find_unique_elements(test_case)) # [3, 4, 5]