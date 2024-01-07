# First approach: using combination
# Calculating all cases
# Too high timecomplexity(over than O(n!...))

# Second approach: using binomial theorem
# (x + a)(x + b)(x + c) = x^3 + (a + b + c)x^2 + (ab + bc + ca)x + abc
# thus using upper formula and subtract 1

def uesang(input):
    new_dic = {}
    for element in input:
        if element[1] not in new_dic:
            new_dic[element[1]] = 1
        else:
            new_dic[element[1]] += 1

    result = 1
    for elem in new_dic:
        result *= (1 + new_dic[elem])
    return result - 1


input = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(uesang(input))

input = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(uesang(input))