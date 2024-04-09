# decimal -> ternary scale -> reverse -> decimal
# Test case
# 45(decimal) -> 1200(ternary) -> 0021(reverse) -> 7 (decimal)

# time over
'''
def tentothree(n):
    ans = ""
    while n != 1:
        tem = n % 3
        n //= 3
        n, tem = divmod(n, 3)
        ans += str(tem)
    ans += str(n)
    return int(ans)

print(tentothree(45))

def threetoten(n):
    i = 1
    ans = 0
    while n != 0:
        tem = n % 10
        ans += (i * tem)
        i *= 3
        n //= 10
    return ans

def solution(n):
    answer = 0
    n = tentothree(n)
    answer = threetoten(n)
    return answer
'''

# using function "divmod" and "int(n, 3)"
def solution(n):
    tem = ""
    while n > 0:
        n, q = divmod(n, 3)
        tem += str(q)
    return int(tem, 3)

print(solution(45))