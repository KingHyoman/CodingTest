# Test case
# "abcde" -> "c"
# "qwer" -> "we"

def solution(s):
    n = len(s) // 2
    if len(s) % 2 != 0:
        return s[n]
    else:
        return s[n-1:n+1]