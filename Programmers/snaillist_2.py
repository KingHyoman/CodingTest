# Given variable: n(integer)
# Ex) n = 4 => [1,2,9,3,10,8,4,5,6,7]
# Ex) n = 5 => [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# Ex) n = 6 => [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
# Think about the triangle which is the height and the width is n
# Snail

def solution(n):
    # For store the answer
    answer = [0] * ((n+1) * n // 2)
    limit = len(answer)

    # Doing all cases
    idx = 0     # index of list
    value = 1   # the value of given index
    const = 2   # For init the next triangle(after 1 loop)
    ###
    # the range of loop
    # There would be 3 loops
    first_start = 1
    first_end = n
    middle_end = n - 1
    final_start = n
    final_end = 2
    ###
    while value <= limit:
        # First loop: going down
        for di in range(first_start, first_end):
            if value > limit:
                break
            answer[idx] = value
            value += 1
            idx += di

        # Second loop: going side
        for _ in range(middle_end):
            if value > limit:
                break
            answer[idx] = value
            value += 1
            idx += 1

        # Third loop: going up
        for di in range(final_start, final_end, -1):
            if value > limit:
                break
            answer[idx] = value
            value += 1
            idx -= di

        # For the last value of the one loop
        answer[idx] = value
        value += 1
        idx += const

        # update all ranges
        first_start += 2
        first_end -= 1
        middle_end -= 3
        final_start -= 1
        final_end += 2
        const += 2


    return answer

print(solution(4))
print(solution(5))
print(solution(6))