# Suppose that OO lab develops and sells an iron suit with special functions
# Jump & Teleport
# Jump: jump k spaces but use k battteries
# Teleport: move (current place) * 2
# ex) current position: 4 -> (teleport) -> 8
# given variable: N(purchasers want to go)
# return the minimum required power level to use

# ex) N = 5
# 0 -> jump -> 1 -> teleport -> 2 -> teleport -> 4 -> jump -> 5
# Thus the answer is 2

# strategy: using power of 2
def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans