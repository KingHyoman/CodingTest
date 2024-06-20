# LCM(Least Common Multiple)
# Return the lcm for given arr
# ex)
# [2, 6, 8, 14] => 168

# strategy
# using Euclidean algorithm
# First find out gcd, then find lcm
def gcd(a, b):
    if b == 0 or a == b:
        return a
    tem = a % b
    a = b
    b = tem
    return gcd(a, b)

def solution(arr):
    answer = 1
    while len(arr) > 1:
        divide = gcd(arr[1], arr[0])
        result = (arr[1] // divide) * (arr[0] // divide) * divide
        arr.pop(0)
        arr.pop(0)
        arr.append(result)
    return arr[0]

print(solution([2,6,8,14]))


# [2,6,8,14]
# [1, 2, 3]