# randomly generate a list
# two parameters
# N: number of elements, sorted: sort or not

import random

def make_list(N, sorted=False):
    a = [1] * N
    for i in range(1, N):
        a[i] = a[i-1] + random.randrange(1, 100)
    if not sorted:
        random.shuffle(a)
    return a

#print(make_list(10, True))