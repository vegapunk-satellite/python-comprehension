def find_sum_indices1(numbers, target):
    pairs = []
    for index1 in range(len(numbers)):
        number1 = numbers[index1]
        for index2 in range(index1+1, len(numbers)):
            number2 = numbers[index2]
            if (number1 + number2) == target:
                pairs.append((index1, index2))
    return pairs


def find_sum_indices2(numbers, target):
    pairs = []
    complement_to_index_map = {}
    for index1 in range(len(numbers)):
        number1 = numbers[index1]
        number2 = target - number1
        if number2 in complement_to_index_map:
            index2 = complement_to_index_map[number2]
            pairs.append((index1, index2))
        complement_to_index_map[number1] = index1
    return pairs


numbers = [5, 14, 12, 10, 6, 22, 15, 10, 3, 9]
target = 20

# 5->0, 14->1, 12->2, 6->3, 22->4, 15->5

# [(0, 5), (1, 3)]

pairs_of_indices = find_sum_indices2(numbers, target)
print("Pairs of indices that sum to target number are: " + str(pairs_of_indices))

# N elemanli liste icin ((N-1) * N) / 2 kadar islem yapilacak.