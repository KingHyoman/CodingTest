# There is a game which uses the natural nums
# Rules
# See the below example
# assume three people(a, b, and c)are playing the game
# a: 0 -> b: 1 -> c: 2 -> ... -> a: 9 -> b: 1 -> c: 0 -> a: 1 -> b: 1 -> c: 1 -> a: 2 -> ...
# If the length of num is one, then just say it
# If the length of num is greater than one, then split it and say only one digits as same as ex)
# We can apply this game for other base N
# If the game is played in base 2 with 3 people
# then, a: 0 -> b: 1 -> c: 1 -> ...
# In this situation, the given variable is n, t, m and p
# n => base, t => the order of we have to figure out
# m => the num of people who play the game, p => the order of me
# 2 <= n <= 16, 0 < t <= 1000, 2 <= m <= 100, 1 <= p <= m
# 
# strategy
# make a function that convert dec num into any base n num
# figure out all num until t * m(all cases)
# using modular m and remain p => find the answer 

def dectoN(n, num):
    result = ''
    if num == 0:
        return '0'
    while num > 0:
        r = num % n
        if r < 10:
            result += str(r)
        else:
            if r == 10:
                result += 'A'
            elif r == 11:
                result += 'B'
            elif r == 12:
                result += 'C'
            elif r == 13:
                result += 'D'
            elif r == 14:
                result += 'E'
            elif r == 15:
                result += 'F'
        num //= n
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    idx = 0
    while len(answer) < t * m:
        answer += dectoN(n, idx)
        idx += 1
    answer = answer[:t * m]
    real_answer = ''
    for i in range(len(answer)):
        if (i + 1) % m == p:
            real_answer += answer[i]
        if m == p:
            if (i + 1) % m == 0:
                real_answer += answer[i]


    return real_answer


for i in range(100):
    print(dectoN(13, i))