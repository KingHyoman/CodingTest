# There are two n * n maps
# To find the treasure, use two maps and have to calculate them
# Two maps are given by arr of integers
# test case
# n = 5, arr1 = [9, 20, 28, 18, 11], arr2 = [30, 1, 21, 17, 28]
# arr1 in arr of bin nums => [01001, 10100, 11100, 10010, 01011]
# arr2 in arr of bin nums => [11110, 00001, 10101, 10001, 11100]
# in the arr nums, 1 means wall and 0 means empty space
# if arr1 ele and arr2 ele are both 0 then empty space, other cases are wall

# strategy
# first convert decimal to bin
# second compare each bits
# third draw a map

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1_ = bin(arr1[i])[2:]
        if len(arr1_) < n:
            arr1_ = "0" * (n - len(arr1_)) + arr1_
        arr2_ = bin(arr2[i])[2:]
        if len(arr2_) < n:
            arr2_ = "0" * (n - len(arr2_)) + arr2_       
        tem = ""
        for j in range(n):
            if arr1_[j] == "0" and arr2_[j] == "0":
                tem += " "
            else:
                tem += "#"
        answer.append(tem)
    
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

