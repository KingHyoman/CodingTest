# implementation of sqrt
# do not use any built in function
# ex) x ** 0.5 (x)

## for getting input
def get_input():
    n = input('Enter a positive integer: ')
    return int(n)

# two strategies
# using linear search: O(N)
def lin_sqrt(n):
    if n == 1:
        return 1
    for i in range(n):
        if (i + 1) * (i + 1) > n:
            break
        
    return i

# using binary search O(log N)
def bin_sqrt(n):
    if n == 1:
        return n
    idx = n // 2
    i = 1
    j = n
    while True:
        if idx * idx > n:
            j = idx
        elif idx * idx < n:
            i = idx
        idx = (i + j) // 2 

        if idx * idx == n:
            return idx
        elif j - i == 1:
            return i



print(bin_sqrt(get_input()))