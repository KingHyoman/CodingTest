# example
# The given string is "banana"
# b -> first b in banana -> -1
# a -> first a in banana -> -1
# n -> first n in banana -> -1
# a -> second a -> the distance for the nearest a is 2 -> 2
# n -> second n -> the distance for the nearest n is 2 -> 2
# a -> third a -> the distance for the nearest a is 2 -> 2

def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
            dic[s[i]] = i
        pass
    return answer

print(solution("banana"))
print(solution("foobar"))