# return sum of numbers in [a, b]
# ex) a = 3, b = 6 => 3 + 4 + 5 + 6 

def solution(a, b):
    n = abs(a - b)
    if n == 0:
        return a
    elif n % 2 != 0:
        return (a + b) * (n // 2 + 1)
    else:
        return (a + b) * (n // 2) + ((a + b) // 2)