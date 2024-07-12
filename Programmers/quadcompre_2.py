# There is an 2^n * 2^n array which consists of only 0 and 1
# We want to compress it using 'Quad Compression'
# Quad Compression
# 1. If the target surface consists of same num => then the num will represent the target surface
# 2. If not, we will divide it into four squares and repeat step 1
# Find the num of 0 and 1
# ex) [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
# The target surface: 2^2 * 2^2
# It do not meet condition 1, thus by condition 2 we will divide in four part
# [[1, 1], [1, 0]], [[0, 0], [0, 0]], [[1, 0], [1, 1]], [[0, 1], [1, 1]]
# The second part consists of only 0
# The first, third and fourth will be divided by condition 2
# Thus the num of 0, 1 is 4, 9

# We need a global variable that we will use recursion
# We have to store all value of recursive function
answer = []

def quad(arr):
    # Divide function

    # First separate it upper part and lower part
    upper_arr = arr[:len(arr) // 2]
    lower_arr = arr[len(arr) // 2:]
    u_left, u_right = [], []
    l_left, l_right = [], []

    # For separate the left part of upper and lower
    i, j = 0, 0
    while i < len(upper_arr):
        u_tem, l_tem = [], []
        while j < len(upper_arr[0]) // 2:
            u_tem.append(upper_arr[i][j])
            l_tem.append(lower_arr[i][j])
            j += 1
        u_left.append(u_tem)
        l_left.append(l_tem)
        i += 1
        j = 0

    # For separate the right part of upper and lower
    i, j = 0, len(upper_arr[0]) // 2
    while i < len(upper_arr):
        u_tem, l_tem = [], []
        while j < len(upper_arr[0]):
            u_tem.append(upper_arr[i][j])
            l_tem.append(lower_arr[i][j])
            j += 1
        u_right.append(u_tem)
        l_right.append(l_tem)
        i += 1
        j = len(upper_arr[0]) // 2
        
    return u_left, u_right, l_left, l_right

def check(arr):
    # the condition is recursive thus we use recursion
    if len(arr) == 1:
        # base case
        # The unit surface
        answer.append(arr[0][0])
        return
    
    pivot = arr[0][0]
    u_left, u_right, l_left, l_right = quad(arr)
    for row in arr:
        for ele in row:
            if ele != pivot:
                # If it does not meet condition 1
                # Following condition 2
                check(u_left)
                check(u_right)
                check(l_left)
                check(l_right)
                return

    # If it meets the condition 1
    answer.append(arr[0][0])
    return

def solution(arr):
    check(arr)
    zero = 0 
    one = 0
    for i in answer:
        # Count the num of 0 and 1
        if i == 0:
            zero += 1
        elif i == 1:
            one += 1
    return [zero, one]

c = [[0, 0], [1, 0]]
a = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],\
     [0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
b = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
#print(solution(c))
#print(solution(b))
print(solution(a))