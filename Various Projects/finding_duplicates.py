def find_duplicates(list_with_duplicates):
    result = []
    for i in range(len(list_with_duplicates)):
        for j in range(len(list_with_duplicates)):
            if i != j and list_with_duplicates[i] == list_with_duplicates[j] and result.count(list_with_duplicates[i]) == 0:
                result.append(list_with_duplicates[i])
    return result


x = [1, 2, 3, 5, 2, 6, 2, 3, 1, 1, 1]
y = find_duplicates(x)
print(y)

