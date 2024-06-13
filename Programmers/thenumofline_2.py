# There are n people in queue
# Thus, there are n! cases to make all orders of line
# Find the k-th case
# Given variable: n, k
# ex) n = 3, k = 5
# (1 ,2, 3) -> (1, 3, 2) -> ... -> (3, 1, 2) -> ...
# The answer is (3, 1, 2)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# First approach
def solution_(n, k):
    answer = []
    nums = {num: 1 for num in range(1, n + 1)}  # To check if it is used
    
    # if n = 3, there are 3! = 6 cases to make a line
    # (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
    # The first position of line is changed: (3 - 1)! = 2!
    # The second position of line is changed: (2 - 1)! = 1!
    # If k = 5, then 5 <= k < 7 thus 3 is in the first position
    # Then k becomes 1(5 - (2 * 2))
    # Thus, 1 <= k < 2, 1 is in the second position
    # Finally, 2 goes the last position of the line
    for i in range(n - 1, 0, -1):  
        idx = 1
        minus = 0
        for j in range(1, factorial(i + 1) + 1, factorial(i)):
            if j <= k and k < j + factorial(i):
                if nums[idx] == 1:
                    answer.append(idx)
                else:
                    while nums[idx] == 0:
                        idx += 1
                    answer.append(idx)
                nums[idx] = 0
                break
            else:
                while nums[idx] == 0:
                    idx += 1
                idx += 1
                minus += factorial(i)

        k -= minus
    
    for idx in nums:
        if nums[idx] == 1:
            answer.append(idx)      # the remain number in nums

    return answer

# Second approach
def solution(n, k):
    answer = []
    arr = [i for i in range(1, n + 1)]

    # From the first approach
    # We can use q and r for this problem
    # Divide by the range in the first approach
    # q would be the num of line
    # r would be the next number
    while arr:
        index = (k - 1) // factorial(n - 1)
        answer.append(arr.pop((index)))

        k = k % factorial(n - 1)
        n -= 1

    return answer 



print(solution(3, 4))