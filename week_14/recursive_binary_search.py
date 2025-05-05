def binarySearch(lst, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return binarySearch(lst, mid + 1, high, target)
        else:
            return binarySearch(lst, low, mid - 1, target)
    return -1