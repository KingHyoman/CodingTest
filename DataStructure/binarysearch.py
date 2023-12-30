# Strategy
# searching method that remove half of unsatisfied elements
# input list must be sorted

from randomlist import make_list

## recursion version
def binary_search_re(arr, target, i, j):
    if i > j:   # not in list
        return

    mid = (i + j) // 2
    if arr[mid] < target:
        return binary_search_re(arr, target, mid + 1, j)    # right-half
    elif arr[mid] > target:
        return binary_search_re(arr, target, i, mid - 1)    # left-half
    else:
        return mid + 1      # target

## iteration version
def binary_search_it(arr, target):
    n = len(arr)
    i = 0       # front pointer 
    j = n       # back pointer
    idx = n // 2    # index pointer

    while arr[idx] != target:
        if arr[idx] < target:
            i = idx
        elif arr[idx] > target:
            j = idx
        idx = (i + j) // 2

    return idx + 1

arr = make_list(10, True)
print(f'original list: {arr}')
tar = input('enter target number: ')
print(f'{tar} is in {binary_search_re(arr, int(tar), 0, len(arr))}')