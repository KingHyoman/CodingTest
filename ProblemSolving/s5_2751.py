# Test 2


def asc_order():
    arr = getting_input()
    arr = sorted(arr)
    for i in arr:
        print(i)
    return

def getting_input():
    n = input()
    arr = [int(input()) for _ in range(int(n))]
    return arr

asc_order()
