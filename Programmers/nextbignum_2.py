# Find the next num of n with following rules
# 1. the next num of n is greater than n
# 2. the next num of n has same num of 1 in binary form
# 3. the next num of n is the min of rule 1 and 2
# Ex) 78(1001110) -> 83(1010011)

# count the number of 1 in given binary num
def count_1(num_str):
    cnt = 0
    for s in num_str:
        if s == '1':
            cnt += 1
    return cnt

def solution(n):
    answer = 0
    stan = count_1(bin(n)[2:])
    # check
    while True:
        n += 1
        if count_1(bin(n)[2:]) == stan:
            break
    
    return n

print(solution(78))