# ex) "try hello world" -> "TrY HeLlO WoRlD"
# ASCII code A: 65 ~ Z: 90, a: 97 ~ z: 122 // " ": 32

def solution(s):
    cnt = 0
    ans = ""
    for i in s:
        if i == " ":
            ans += " "      # return space
            if cnt != 0:
                cnt = 0     # do not count the space
            continue
        if cnt % 2 == 0 and ord(i) >= 97:       # if the order is even and there is a lower char
            ans += chr(ord(i) - 32)
        elif cnt % 2 != 0 and ord(i) <= 90:     # if the order is odd and there is a upper char
            ans += chr(ord(i) + 32)
        else:       # remain things
            ans += i
        cnt += 1
    return ans

print(solution("try hello world"))