# A certain dictionary contains all words that consist only of vowels
# The first letter in the dictionary is "A", which is followed by "AA"
# The last word will be "UUUUU".
# given variable: word
# returns the rank of that "word" in the dictionary given above.
# ex) "AAAAE"
# The first word in the dictionary is "A", followed by "AA", "AAA", "AAAA", "AAAAA", "AAAAE"
# The answer is 6

def solution(word):
    cnt = 0
    tem = []
    alpha = {0: 'A', 1: 'E', 2: 'I', 3: 'O', 4: 'U'}
    for i in alpha:
        cnt += 1
        if len(tem) < 1:
            tem.append(alpha[i])
        elif len(tem) > 1:
            while len(tem) > 1:
                tem.pop()
            tem[-1] = alpha[i]
        if word == ''.join(tem):
            return cnt
        for j in alpha:
            cnt += 1
            if len(tem) < 2:
                tem.append(alpha[j])
            elif len(tem) > 2:
                while len(tem) > 2:
                    tem.pop()
                tem[-1] = alpha[j]
            if word == ''.join(tem):
                return cnt
            for k in alpha:
                cnt += 1
                if len(tem) < 3:
                    tem.append(alpha[k])
                elif len(tem) > 3:
                    while len(tem) > 3:
                        tem.pop()
                    tem[-1] = alpha[k]
                if word == ''.join(tem):
                    return cnt
                for l in alpha:
                    cnt += 1
                    if len(tem) < 4:
                        tem.append(alpha[l])
                    elif len(tem) > 4:
                        while len(tem) > 4:
                            tem.pop()
                        tem[-1] = alpha[l]
                    if word == ''.join(tem):
                        return cnt
                    for m in alpha:
                        cnt += 1
                        if len(tem) < 5:
                            tem.append(alpha[m])
                        else:
                            tem[-1] = alpha[m]
                        if word == ''.join(tem):
                            return cnt
                        


    return cnt

print(solution('AAAAE'))