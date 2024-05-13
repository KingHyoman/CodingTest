# Correct Parenthesis: If it is opened with a '(', it must be closed with a ')'
# "()()" or "(())()" is a correct parenthesis.
# ")()(" or "(()(" is an incorrect parenthesis.
# input: string s
# check if it is correct parenthesis or not

def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                continue
            else:
                return False            
    if stack:
        return False
    return True