def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = mergeSort(lst[:mid])
    right_half = mergeSort(lst[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i <len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    result.extend(left[i:])
    result.extend(right[j:])
    return result