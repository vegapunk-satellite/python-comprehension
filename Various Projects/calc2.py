def max_of_arrays1(list_of_lists):
    list_of_lens = [len(list) for list in list_of_lists]
    max_len = max(list_of_lens)
    max_list = []
    for i in range(max_len):
        list_at_i = []
        for list in list_of_lists:
            if i < len(list):
                list_at_i.append(list[i])
        max_at_i = max(list_at_i)
        max_list.append(max_at_i)
    return max_list


# def max_of_arrays2(list_of_lists):
#     list_of_lens = [len(list) for list in list_of_lists]
#     max_len = max(list_of_lens)
#     max_list = []
#     for i in range(max_len):
#         max_at_i = -100None if list[i]max_at_i is None or  > max_at_i:)
#         max_at_i =
#         max_at_i = list[i]max(list_at_iax_at_i)
#     return max_list

list1 = [16, 25, 253, 14, 524, 45]
list2 = [38, 246, 33, 47]
list3 = [40, 59, 28, 65, 371]
list4 = max_of_arrays1([list1, list2, list3])
print(list4)
