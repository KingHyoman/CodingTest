# The compression of string
# To compress the given string, use the pattern of string and number
# ex) "aabbaccc" -> "2a2ba3c", thus 8 -> 7
# If "ababcdcdababcdcd" -> "2ab2cd2ab2cd" or "2ababcdcd"
# Find the shortest compression for given string using this method

def solution(s):
    answer = ''     

    # Check all cases
    for r in range(1, len(s) + 1):
        lenofS = len(s)
        idx = 0
        stack = []      # To check can be compressed using number
        count = 1       # number for compressing
        tem_answer = ''

        # Check each cases
        while idx < lenofS:
            tem = s[idx:idx + r]
            if stack:
                if tem == stack[-1]:
                    # If can be compressed
                    count += 1
                else:
                    # cannot be compressed
                    if count > 1:
                        # compress the formal string using number
                        tem_answer += (str(count) + stack[-1])
                    else:
                        # just add when cannot be compressed
                        tem_answer += stack[-1]
                    count = 1

                    stack.append(tem)
            else:
                stack.append(tem)
            idx += r

        # The last string is not considered
        if count > 1:
            tem_answer += (str(count) + stack[-1])
        else:
            tem_answer += stack[-1]  

        # Find the answer(the shortest string)
        if answer:
            if len(answer) > len(tem_answer):
                answer = tem_answer
        else:
            answer = tem_answer
    return len(answer)

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))