# Strategy
# select a pivot(assume it p) from the input list
# split the input list into three lists
# list S: smaller than p, list E: equal to p, list G: greater than p

from randomlist import make_list

def quick_sort(arr):
    n = len(arr)        # length of input list
    pivot = arr[n // 2]   # choose any value for pivot

    S, E, G = [], [], []    # empty list to append the values satisfying our strategy

    for i in arr:       # split all elements from our strategy
        if i < pivot:
            S.append(i)
        elif i == pivot:
            E.append(i)
        elif i > pivot:
            G.append(i)
        else:
            print("Something be wrong")

    if not S or not G:  # recursion init
        if not S and G:
            return E + quick_sort(G) 
        if S and not G:
            return quick_sort(S) + E
        if not S and not G:
            return E

    return quick_sort(S) + E + quick_sort(G)    # recursion

arr = make_list(10)
print(f'original list: {arr}')
print(f'sorted using quicksort: {quick_sort(arr)}')