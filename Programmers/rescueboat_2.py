# There is rescue boat which can only hold two people
# There are some people in uninhabited island, and we have to rescue them using this boat
# Given variable: people, limit
# people is array of integer that represent weight of people
# limit is integer that the limitation weight of rescue boat
# Return the minimum value of the num of rescue boat that we need


# strategy
# only two people => sort
# first, hold the heaviest person in the boat
# then check if the lighest person can ride the boat
def solution(people, limit):
    answer = 0
    # only two people => sort
    people.sort(reverse=True)
    # using two pointer
    i = 0
    j = len(people) - 1

    while i < j:
        # first, hold the heaviest person in the boat
        boat = people[i]
        i += 1
        # then check if the lighest person can ride the boat
        if boat + people[j] <= limit:
            boat += people[j]
            j -= 1
        answer += 1

    if i == j:
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([70, 80, 50, 50], 150))