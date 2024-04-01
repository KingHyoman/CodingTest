# Darts game
# Calculate the final score of darts game
# there are 3 games
# 0~10 (score) is given each games
# with score, there is also S, D, T which S is (score)^1, D is (score)^2 and T is (score)^3
# There are two options of "*" and "#" (It is easy to find a rule about "*" and "#" in test cases)

# Test cases
# 1S2D*3T -> 37 -> 1^1 * 2 + 2^2 * 2 + 3^3
# 1D2S#10S -> 9 -> 1^2 + 2^1 * (-1) + 10^1
# 1D2S0T -> 3 -> 1^2 + 2^1 + 0^3
# 1S*2T*3S -> 23 -> 1^1 * 2 * 2 + 2^3 * 2 + 3^1
# 1D#2S*3S -> 5 -> 1^2 * (-1) * 2 + 2^1 * 2 + 3^1
# 1T2D3D# -> -4	-> 1^3 + 2^2 + 3^2 * (-1)
# 1D2S3T* -> 59	-> 1^2 + 2^1 * 2 + 3^3 * 2

def solution(dartResult):
    answer = 0
    tem = 0
    star = []
    for i in range(len(dartResult)):
        if dartResult[i] == "S":
            star.append(tem)
        elif dartResult[i] == "D":
            star.append(tem ** 2)
        elif dartResult[i] == "T":
            star.append(tem ** 3)
        elif dartResult[i] == "*":
            star[len(star) - 1] = 2 * star[len(star) - 1]
            if len(star) > 1:
                star[len(star) - 2] = 2 * star[len(star) - 2]
        elif dartResult[i] == "#":
            star[len(star) - 1] = -star[len(star) - 1]
        else:
            if tem == -1:
                tem = 10
            elif dartResult[i + 1] == "0":
                tem = -1
            else:
                tem = int(dartResult[i])

    return sum(star)

print(solution("1D#2S*3S"))