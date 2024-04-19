# A hamburger shop
# 1 - bread, 2 - green trash, 3 - protein
# A hamburger is packed if its order is 1 -> 2 -> 3-> 1
# If there is an given list that means order of ingredients
# then figure out how many hamburgers are maked

# EX) [2, (1, (1, 2, 3, 1), 2, 3, 1)] -> 2
# strategy: use stack and pop

def solution(ingredient):
    answer = 0
    if len(ingredient) < 4:
        return answer
    stack = []
    i = 0
    for num in ingredient:
        stack.append(num)
        if len(stack) > 3:
            if stack[i:i+4] == [1, 2, 3, 1]:
                # stack = stack[:i] => time over
                for _ in range(4):
                    stack.pop()
                answer += 1
                if len(stack) > 3:
                    i = len(stack) - 3
                else:
                    i = 0

            else:
                i += 1

    return answer


#print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
#print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
print(solution([1, 2, 3, 1, 2, 3, 1, 1]))
print(solution([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]))
print(solution([2, 1, 2, 3, 1, 2, 3, 1, 1] ))
print(solution([1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1]))