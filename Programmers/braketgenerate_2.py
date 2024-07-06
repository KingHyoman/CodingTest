# For '(' and ')'
# If the num of '(' and ')' are same => We define it "balanced"
# If "balanced" and can match it => We define it "correct"
# Given variable: p(string which consists of '(' and ')')
# If the given variable is always "balanced", then convert it into "correct"

# The way to convert
# 1. if p is empty => return p
# 2. separate p into u and v => u must be "balanced" and v can be empty string
# 3. if u is "correct"
# -> repeat v from step 1 // return u + new_v
# 4. if u is not "correct"
# -> repeat v from step 1 // remove the first and last bracket from u and reverse all brackets// 
# -> return '(' + new_v + ')' + new_u

def checkBracket(s):
    # For check it is "correct"
    # Using stack
    stack = []
    return_bit = True
    for bracket in s:
        if not stack and bracket == ')':
            return_bit = False
            break
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return_bit = False
                break
    return return_bit

def breakBracket(s):
    # To separate into two string
    # u is the minimum of 'balanced' from s
    left, right = 0, 0
    u, v = '', ''
    for bracket in s:
        if bracket == '(':
            left += 1
        else:
            right += 1
        u += bracket
        if left == right:
            break
    v = s[left + right:]
    return u, v
    

def solution(p):
    # According to converting method

    # step 1
    if not p or checkBracket(p):
        return p
    
    # step 2
    u, v = breakBracket(p)

    # step 3
    if checkBracket(u):
        return u + solution(v)
    
    # step 4
    else:
        var1 = '('
        new_v = solution(v)
        var1 = var1 + new_v + ')'
        new_u = ''
        for bracket in u[1:len(u) - 1]:
            if bracket == '(':
                new_u += ')'
            else:
                new_u += '('

        return var1 + new_u

print(solution(""))
a, b = breakBracket("()))((()")  