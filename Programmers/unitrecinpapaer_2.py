# There is a Wcm x Hcm paper grid. Each grid is 1cm x 1cm. 
# Someone cut the paper diagonally so you now have two right-triangle paper pieces
# Decide to use the two triangle paper pieces.
# Write a solution function that returns the number of 1 x 1 squares that you can use
# Given variable: W, H
# ex) W = 8, H = 12
# The answer is 80
# Total: 96, cannot use 16

# strategy: using the unit rectangle of given square
# Unit rectangle: Consist of two disjoint w, h which has same ratio of W:H 
# First -> figure out the nums of 1 * 1 in original rectangle
# Second -> figure out the gcd of W, H and find the rectangle
# Third -> figure out all y values which meet the line -> sum it and figure out the answer
# The worst time complexity: O(W)

def gcd_(a, b):
    # assume that a > b
    if b == 0:
        return a
    tem = a % b
    a = b
    b = tem
    return gcd(a, b)

def gcd(a, b):
    # assume that a > b
    for i in range(b, 0, -1):
        if a % i == 0  and b % i == 0:
            break
    return i

def linear_value(a, b, val):
    # b => y intercept
    # a => x intercept
    # thus -(b/a) is the slope of the line
    return int(-(b/a) * val + b)

def solution(w,h):
    if w == 1 or h == 1:
        return 0
    # The unit squares
    answer = w * h

    # Find the gcd for finding unit rectangle
    # Target 1
    if w >= h:
        GCD = gcd(w, h)
    else:
        GCD = gcd(h, w)

    # Find the unit w and unit h
    unit_w = w // GCD
    unit_h = h // GCD

    unit_sqr = 0
    for x in range(1, unit_w):
        unit_sqr += linear_value(unit_w, unit_h, x)
    nounit_sqrs = ((unit_h * unit_w) - (unit_sqr * 2)) * GCD

    return answer - nounit_sqrs

print(solution(8, 12))

# There is a better way
# Just using the intersection point between the line and the grid of unit square
# Then (the num of intersection point) + 1 will be the unusable square
# Thus, the total num is
# w * h - gcd * (((w/gcd) - 1) + ((h/gcd) - 1) + 1)
# = w * h - w - h + gcd
# This will be much better than upper solution