# given variable: numbers
# figure out the biggest num from the combination of numbers
# ex) [6, 10, 2]
# [6102, 6210, 1062, 1026, 2610, 2106]
# Thus the biggest num is 6210

# strategy
# ---1
# using the comparison of string
# in string '4' > '39999999.....'
# but there is a problem
# we have to define '3' > '30' but in strings '30' > '3'
# How we can solve it?

# ---2
# The range of num in numbers is 0 ~ 1000
# Thus if we compare '303030' and '333' rather than '30' and '3'
# Then we can define '3' > '30'
def solution(numbers):
    # ---1
    str_numbers = [str(number) for number in numbers]
    # ---2
    # if we use x: x * 2
    # then like '9' > '990' cannot be defined
    str_numbers.sort(reverse=True, key=lambda x: x * 3)
        
    return str(int(''.join(str_numbers)))


print(solution([3, 30, 34, 5, 9]))
print(solution([399999999999, 4]))
print(solution([990, 9]))