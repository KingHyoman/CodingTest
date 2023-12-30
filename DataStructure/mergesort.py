# Strategy
# split it until the number of element in list become 1: merge_sort(arr)
# after merge it with sorting: merge(a, b)

import randomlist

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2    # pivot to split the list in half
    list_1 = arr[:mid]  # 0 to mid
    list_2 = arr[mid:]  # mid to end

    return merge(merge_sort(list_1), merge_sort(list_2))    # split it and merge it

def merge(a, b):
    a_idx = 0
    b_idx = 0
    result = []     

    # merge it
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] > b[b_idx]:
            result.append(b[b_idx])
            b_idx+=1
        elif a[a_idx] <= b[b_idx]:
            result.append(a[a_idx])
            a_idx+=1

    # handle that remain elements in list
    # only one of them is empty
    result = result + a[a_idx:]
    result = result + b[b_idx:]
    
    return result
    
arr = randomlist.make_list(10)
print(f'original list: {arr}')
print(f'sorted using mergesort: {merge_sort(arr)}')
