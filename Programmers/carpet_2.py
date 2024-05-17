# There is a carpet consist of yellow and brown
# The center of carpet is yellow and this yellow is surrounded by brown
# If the area of yellow and brown is given, figure out the width and height of carpet
# width >= height
# For example
# brown 10, yellow 2
# Then width is 4, height is 3

def solution(brown, yellow):
    answer = []
    for i in range(int(yellow ** 0.5), 0, -1):
        if yellow % i == 0 and (i + yellow // i) * 2 + 4 == brown:
            answer.append(i + 2)
            answer.append(yellow // i + 2)
            break

    return answer[::-1]