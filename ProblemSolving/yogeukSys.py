# how can deal with [0, 4], [1, 3], [3, 4]?
# sort by end point -> start point

def pang(targets):
    targets = sorted(targets, key=lambda x : (x[1], x[0]))
    answer = 1
    pointer = 0
    for i in range(1, len(targets)):
        if targets[pointer][1] <= targets[i][0]:
            pointer = i
            answer += 1

    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(pang(targets))

targets = [[4, 5], [1, 4], [5, 7]]
print(pang(targets))

targets = [[5,12], [10,14]]
print(pang(targets))

targets = [[0, 4], [1, 2], [1, 3], [3, 4]]
print(pang(targets))

targets = [[0, 4], [0, 1], [2, 3]]
print(pang(targets))
