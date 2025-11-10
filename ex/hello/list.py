def find_common1(li1, li2):
    common_list = []
    for i in li1:
        if i in li2:
            common_list.append(i)
    return common_list

print(find_common1([1, 2, 3, 4], [3, 4, 5, 6]))           # [3, 4]
print(find_common1(['a', 'b', 'c', 'd'], ['d', 'e', 'f'])) # ['d']