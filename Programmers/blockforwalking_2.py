# There is a infinite list which is initialized by 0
# [0, 0, 0, 0, ... ]
# We will change this array as following rules
###
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, ... ] => First fill 1 in position 1*2, 1*3, 1*4, ...
# [0, 1, 1, 2, 1, 2, 1, 2, 1, 2, ... ] => Second fill 2 in position 2*2, 2*3, 2*4, ...
# [0, 1, 1, 2, 1, 3, 1, 2, 1, 2, ... ] => Third fill 3 in position 3*2, 3*3, 3*4, ...
# ...
###
# If you repeat until 5, then the result would be [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
# Given variable: begin, end
# Return array[begin:end]
# range: 1 <= being <= end <= 1000000000
# block: 1 ~ 10000000


#######################################
## crazy method: figure out all section
def solution_(begin, end):
    answer = [0] * 1000000000
    for i in range(1, 1000000000 // 2):
        n = 2
        while n * i <= 1000000000:
            answer[(n * i) - 1] = i
            n += 1
        
    return answer[begin:end]
## crazy method: figure out all section
#######################################

# This problem have to find the maximum divisor of n(except n)
# Thus this function returns the maximum divisor
def maxd(n):
    max = 0
    if n == 1:  # if n is 1
        return 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if max == 0:    # when n is prime num, 
                max = i
            else:
                if n // i <= 10000000:      # Because of the range of num
                    return n // i
                else:
                    max = i
                    pass
    if max == 1:
        return max
    return max

def solution(begin, end):
    length = (end - begin) + 1
    answer = [0] * length
    for i in range(length):
        answer[i] = maxd(i + begin)     # fill the array
        pass
    return answer

print(maxd(100000014))
print(solution(1, 20))
print(solution(100000014, 100000016))