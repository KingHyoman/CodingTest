# There is a cell phone with keypad
# You can press the button only using the right and left thumb
# First, start from "#" for the right thumb and "*" for the left thumb
# 1, 4, 7 must press using the right thumb
# 3, 6, 9 must press using the left thumb
# 2, 5, 8, 0 are pressed by the close one(the distance is calculated by only up down left right ways)
# if both have same distance, then using the "hand" thumb
# Return the string that order of pressing
# Test case
# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], hand = "right"
# "LRLLLRLLRRL"

# definite the distance
def solution_(numbers, hand):
    dis = {(1, 2): 1, (1, 5) : 2, (1, 8): 3, (1, 0): 4,\
            (4, 2): 2, (4, 5): 1, (4, 8): 2, (4, 0): 3, \
            (7, 2): 3, (7, 5): 2, (7, 8): 1, (7, 0): 2, \
            ("*", 2): 4, ("*", 5): 3, ("*", 8): 2, ("*", 0): 1, \
            (2, 2): 0 , (2, 5): 1, (2, 8): 2, (2, 0): 3, \
            (5, 2): 1, (5, 5): 0, (5, 8): 1, (5, 0): 2, \
            (8, 2): 2, (8, 5): 1, (8, 8): 0, (8, 0): 1,\
            (0, 2): 3, (0, 5): 2, (0, 8): 1, (0, 0): 0, \
            (3, 2): 1, (3, 5) : 2, (3, 8): 3, (3, 0): 4,\
            (6, 2): 2, (6, 5): 1, (6, 8): 2, (6, 0): 3, \
            (9, 2): 3, (9, 5): 2, (9, 8): 1, (9, 0): 2, \
            ("#", 2): 4, ("#", 5): 3, ("#", 8): 2, ("#", 0): 1
        }
    answer = ''
    l, r = "*", "#"
    d_l, d_r = 0, 0
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += "L"
            l = number
        elif number == 3 or number == 6 or number == 9:
            answer += "R"
            r = number
        else:
            d_l, d_r = dis[(l, number)], dis[(r, number)]
            if d_l == d_r:
                if hand == "right":
                    answer += "R"
                    r = number
                else:
                    answer += "L"
                    l = number
            else:
                if d_l < d_r:
                    answer += "L"
                    l = number
                else:
                    answer += "R"
                    r = number
    return answer

# definite the cartesian
def solution(numbers, hand):
    pass

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))