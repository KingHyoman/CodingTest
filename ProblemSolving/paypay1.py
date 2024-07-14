# Given 2 non-negative integers in a binary representation as a string - 
# return sum of them in a binary representation and discard intial zeros (if any)

def bintodec(binnum):
    base = 1
    result = 0
    for digit in binnum[::-1]:
        result += (base * int(digit))
        base *= 2
    return result  

def dectobin(decnum):
    result = ''
    if decnum == 0:
        return '0'
    while decnum > 0:
        result += str(decnum % 2)
        decnum //=2
    return result[::-1]

def solution(bin1, bin2):
    dec1, dec2 = bintodec(bin1), bintodec(bin2)
    result = dec1 + dec2
    return dectobin(result)

print(solution("0", "0"))
print(solution("10", "11"))
print(solution("1001", "1111"))
