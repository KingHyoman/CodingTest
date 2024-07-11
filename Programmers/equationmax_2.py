# There is an expression which consists of three operators(+, -, *) and num
# We can define the priority of the operators
# Find the best priority which become the maximum value(absolute value) in expression
# Cannot define two or more operators have same priority
# Given variable: string(the expression)
# ex) "100-200*300-500+20"
# when "* > + > -" => the value become |-60420|

# There is only 6 cases of priorities and the len of expression is lower than 100
# Thus we can check all the cases
# Using permutation to check all operators

import itertools

def operation(a, b, ops):
    # For calculation
    if ops == '+':
        return a + b
    elif ops == '*':
        return a * b
    elif ops == '-':
        return a - b

def solution(expression):
    answer = 0

    # splitting the expression into list
    new_exp = []
    for_num = ''
    operators = set()
    for s in expression:
        if s == '*' or s == '-' or s == '+':
            new_exp.append(int(for_num))
            for_num = ''
            new_exp.append(s)
            operators.add(s)
        else:
            for_num += s
    new_exp.append(int(for_num))
    operators = list(operators)
    original_exp = new_exp

    # The priority
    priorities = list(itertools.permutations(operators, len(operators)))
    
    # loop for check all the cases
    results = []
    for priority in priorities:
        new_exp = original_exp
        for oper in priority:
            # Using stack to calculation
            # using a bit to check if it is an target operator
            num_tem = 0
            bit = False
            stack = []
            for target in new_exp:
                if target == oper:
                    num_tem = stack.pop()
                    bit = True
                else:
                    if bit:
                        stack.append(operation(num_tem, target, oper))
                        num_tem = 0
                        bit = False
                    else:
                        stack.append(target)
                print(stack)
            new_exp = stack

        results.append(abs(stack[-1]))

            
    
    return max(results)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("1-1-1-1-1"))

