# n people play the word relay
# There are some rules in this game
# 1. Starting from person number 1, each person says a word in turn
# 2. After the last person says a word, person number 1 starts again
# 3. A person should say a word that starts with the last character of the previously said word
# 4. A person cannot say a word that has already been said
# 5. Words with one character are not valid
# Find the person and order who mistaked

def solution(n, words):
    said = {}
    for i in range(len(words)):
        if i != 0 and words[i][0] != words[i - 1][-1]:
            return [(i % n) + 1, (i // n) + 1]
        if words[i] not in said:
            said[words[i]] = True
            continue
        if words[i] in said:
            return [(i % n) + 1, (i // n) + 1]
    return [0, 0]



print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))