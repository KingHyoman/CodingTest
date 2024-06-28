# Using LZW algorithm, implement the compression
# LZW algorithm
# 1. using dictionary => initial with string has length 1      {1: A, 2: B, .... 26: Z}
# 2. Find the longest string in dictionary that same as given word
# 3. print out the index of word and pop this word
# 4. If there is a remain word, then append this word in dictionary
# repeat 2 ~ 4
# return the list of index

# the class of LZW
class LZW():
    def __init__(self):
        # initial
        self.idxAlpha = {chr(i + 64): i for i in range(1, 27)}
        self.nextnum = 27

    def printIdx(self):
        return self.idxAlpha

    def isinIdx(self, word):
        # check if it is dict
        return word in self.idxAlpha

    def idxAdd(self, word):
        if self.isinIdx(word):
            # if it is already in dict
            # ignore
            return 1
        else:
            # if it is not in dict
            # add
            self.idxAlpha[word] = self.nextnum
            self.nextnum += 1
            return 0
    
    def returnValue(self, idx):
        return self.idxAlpha[idx]


def solution(msg):
    answer = []
    lzw = LZW()
    cnt = 0
    for i in range(len(msg)):
        if cnt != 0:
            # check if there is a remain word
            cnt -= 1
            continue
        end = i + 1
        while end < len(msg) + 1 and lzw.isinIdx(msg[i:end]):
            # check until it is not in dict
            end += 1
            cnt += 1
        cnt -= 1

        # append the index
        answer.append(lzw.returnValue(msg[i:end - 1]))
        lzw.idxAdd(msg[i:end])

    return answer

a = 'asb'
print(a[0:6])   # [a:b] => b can greater than len of given structure

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))