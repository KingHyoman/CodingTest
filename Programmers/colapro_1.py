# Coke problem
# If we give store a empty bottle, then the store give us b coke
# If we have total n bottles of coke, then how many coke can we drink?

def solution(a, b, n):
    answer = 0

    while n >= a:
        r = n % a
        n = (n // a) * b
        answer += n
        n += r


    return answer

print(solution(2, 1, 20))