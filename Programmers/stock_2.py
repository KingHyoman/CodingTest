# stock prices
# given variables: prices
# Ex) [1, 2, 3, 2, 3]
# return array of integers that means the time of stock does not decrease
# For example, [4, 3, 1, 1, 0]

def solution_(prices):
    # Simple solution
    # just check all cases

    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)
    return answer

def solution(prices):
    # using stack
    # store all cases except decreasing
    # when the price decreases, use the record in the stack

    stack = [0]
    # set the answers
    answers = [i for i in range(len(prices) - 1, -1, -1)]

    for i in range(1, len(prices)):
        # check if it is decreasing
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answers[idx] = i - idx
        stack.append(i)
    
    return answers
