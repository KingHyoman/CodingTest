# To anticipate the number of gift that receive next month
# There are two conditions
# Assume between two people
# First, if A give more gifts than B, then A receives gift from B next month
# Second, if two people give and take same num of gifts, then using the constant
# gift constant(For per person): (the num of giving) - (the num of receivine)
# Then return the maximum value of gifts receiving among the people
# Ex) 

def solution(friends, gifts):
    answer = 0
    fri_num = {friends[i]: i for i in range(len(friends))}
    gift_way = {friend: [0 for i in range(len(friends))] for friend in friends}
    const_gift = {friend: 0 for friend in friends}
    anticipated = [0  for i in range(len(friends))]
    
    # The first condition: the num of gift
    # The second condition: constant of gift
    for gift in gifts:
        tem = gift.split(' ')
        gift_way[tem[0]][fri_num[tem[1]]] += 1
        const_gift[tem[0]] += 1
        const_gift[tem[1]] -= 1
    
    tem = 0
    for friend in friends:
        for idx in range(len(gift_way[friend])):
            if idx == fri_num[friend]:
                continue
            else:
                if gift_way[friend][idx] > gift_way[friends[idx]][tem]:
                    anticipated[tem] += 1
                    print(f'A: {friend} <- {friends[idx]}')
                elif gift_way[friend][idx] == gift_way[friends[idx]][tem]:
                    if const_gift[friend] > const_gift[friends[idx]]:
                        anticipated[tem] += 1
                        print(f'{friend} <- {friends[idx]}')
                    pass
        tem += 1
    
    print(fri_num)
    print(gift_way)
    print(const_gift)
    print(anticipated)

    return max(anticipated)

print(solution(["muzi", "ryan", "frodo", "neo"], \
               ["muzi frodo", "muzi frodo", "ryan muzi", \
                "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
print(solution(["joy", "brad", "alessandro", "conan", "david"], \
               ["alessandro brad", "alessandro joy", "alessandro conan", \
                "david alessandro", "alessandro david"]))
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))