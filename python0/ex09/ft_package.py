def count_in_list(lst, target):
    """count in list"""
    count = 0
    for x in lst:
        if x == target:
            count += 1
    return count
