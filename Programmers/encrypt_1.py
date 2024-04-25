# ASCII Code: "a" ~ "z" - 97 ~ 122
# The application of Caesar cipher
# we have to decrypt the s
# The rule is add the index in each letter of s
# But we must not count the letter in skip
# ex) s = "aukks", skip = "wbqd", index = 5
# then "a" -> [b, c, d, e, f], thus "a" becomes "f"
# but b, d are in skip, thus "a" -> [c, e, f, g, h] becomes "h"
# as same rule, "aukks" becomes "happy"


def solution(s, skip, index):
    answer = ''
    for letter in s:
        cnt = 0
        tem = letter
        while cnt < index:
            tem = chr(ord(tem) + 1)
            if ord(tem) == 123:
                tem = 'a'
            if tem in skip:
                continue
            else:
                cnt += 1
        if ord(tem) == 123:
            answer += 'a'     
        else:   
            answer += tem
        
    return answer


print(chr(ord("a")))
print(solution("aukks", "wbqd", 5))
print(solution("z", "abcdefghij", 20))