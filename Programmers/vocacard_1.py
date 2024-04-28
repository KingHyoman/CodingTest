# There are two sets of word cards in specific order
# You have to judge that a given sentense can be made by using word cards
# ex) Two sets of cards: ["i", "drink", "water"], ["want", "to"]
# A given sentence: ["i", "want", "to", "drink", "water"]
# You can make the sentence
# First use "i" in first set and use "want", "to" in second set
# Then use "drink", "water" in first set

def solution(cards1, cards2, goal):
    i = 0
    j = 0
    for g in goal:
        if i >= len(cards1):
            if cards2[j] == g:
                j += 1
                continue
            else:
                return "No"
        if j >= len(cards2):
            if cards1[i] == g:
                i += 1
                continue
            else:
                return "No"
        if cards1[i] == g:
            i += 1
        elif cards2[j] == g:
            j += 1
        else:
            return "No"
    return "Yes"

print(solution(["i", "drink", "water"], ["want", "to"], \
               ["i", "want", "to", "drink", "water"]))


print(solution(["i", "water", "drink"], ["want", "to"], \
               ["i", "want", "to", "drink", "water"]))