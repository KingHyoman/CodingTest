# 'Binary transformation' for string x
# 1. remove all 0 in x
# 2. transfer the len of x into binary form(removed form)
# 3. repeat it until x become '1'
# Then return the num of removed 0 and the num of transfered
# ex) "01110" -> "111" -> "3" -> "11" -> "2" -> "10" -> "1"
# Thus the num of removed 0 is 3 and the num of transfered is also 3

def solution(s):
    zero = 0
    count = 0
    while s != '1':
        lenofs = len(s)
        lenofzero = 0
        for num in s:
            if num == '0':
                lenofzero += 1
        lenofs -= lenofzero
        zero += lenofzero
        count += 1
        lenofzero = 0
        s = str(bin(lenofs)[2:])
        
    return [count, zero]
