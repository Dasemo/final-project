def combine(list1, list2):
    combined = list1 + list2
    return(list(set(combined)))
print(combine([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9]))
