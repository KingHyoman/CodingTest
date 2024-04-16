# The baby can say only four words and it's combination(below)
# "aya", "ye", "woo", "ma"
# But the baby cannot say the consecutive word (ex -> "yeye")
# given variables => list of strings
# return how many babbling that baby can say

def solution_(babbling):
    answer = 0
    bit = {'aya': 0, 'ye': 0, 'woo': 0, 'ma': 0}
    for bab in babbling:
        stack = ''
        for i in bit.keys():
            bit[i] = 0
        for i in bab:
            stack += i
            if stack == 'aya' or stack == 'ye' or stack == 'woo' or stack == 'ma':
                if bit[stack] == 1:
                    continue
                else:
                    for i in bit.keys():
                        bit[i] = 0
                    bit[stack] = 1
                    stack = ''
        if not stack:
            answer += 1

    return answer

def solution(babbling):
    answer = 0
    for bab in babbling:
        stack = ''
        past = ''
        for i in bab:
            stack += i
            if stack == 'aya' or stack == 'ye' or stack == 'woo' or stack == 'ma':
                if past == stack:
                    pass
                else:
                    past = stack
                    stack = ''

        if not stack:
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
print(solution(["wooyemawooye", "mayaa", "ymaeaya"]))
print(solution(["yeye"]))