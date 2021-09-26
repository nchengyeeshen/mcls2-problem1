def binary_search(lst, target):
    """Search a sorted list for an occurrence of target. Return the index of
    target if it is present, else -1."""
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < target:
            low = mid
        elif lst[mid] > target:
            high = mid
        else:
            return mid
    return -1
