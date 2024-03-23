# Using cizer encrpy
# ex) "A B C", 2 -> "C D E"
# ASCII code A: 65 ~ Z: 90, a: 97 ~ Z: 122 // " ": 32

def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) == 32:
            answer += " "
            continue
        elif ord(i) >= 65 and ord(i) <= 90:
            x = ord(i) - 65
            tem = chr((x + n) % 26 + 65)
        else:
            x = ord(i) - 97
            tem = chr((x + n) % 26 + 97)
        answer += tem
    return answer

