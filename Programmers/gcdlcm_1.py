# given variables => two int
# return [gcd, lcm]

def solution(n, m):
    num = min(n, m)
    gcd, lcm = 0, 0
    for i in range(1, num + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
        pass
    lcm = (n // gcd) * (m // gcd) * gcd
    return (gcd, lcm)

print(solution(3, 12))
print(solution(2, 5))