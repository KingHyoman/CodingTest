# There are some menu in the restaurant
# We will make a set menu choosing two or more than each menu
# There are some condition making a set menu
# 1. more than 2 people called
# 2. the most called combination of menu
# Then return the all set menu we can make
# Given variableL: orders, course
# orders: the list of strings which means the each customers ordered
# course: the list of integer which represent the num of menu in setmenu

import itertools

def solution(orders, course):
    answer = []
    # Check all cases
    # Because the size of orders and course are small
    for num in course:
        results = {}    # To store the num of menu which called by customers
        for order in orders:
            tem = list(itertools.combinations(order, num))      # All cases of set menus that the num is num
            menus = [''.join(sorted(menu)) for menu in tem]
            for menu in menus:
                # init the dict
                if menu not in results:
                    results[menu] = 1
                else:
                    results[menu] += 1
        max = 0     # To find the maximum value that called
        new_menus = []
        for result in results:
            if results[result] >= 2 and results[result] > max:
                max = results[result]
        for result in results:
            if results[result] == max:
                new_menus.append(result)
        if new_menus:
            for new in new_menus:
                answer.append(new)

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))