# Tower of hanoi
# There are three rods and a number of disks of variety diameters
# This game follows two rules
# 1. Only one disk may be moved at a time.
# 3. No disk may be placed on top of a disk that is smaller than it.
# assume that the names of rods are 1, 2 and 3
# If the num of disks (n) is given, 
# return the method that move the disk min

# ex) n = 2
# [[1, 2], [1, 3], [2, 3]]

answer = []

def hanoi(n, start=1, middle=2, destination=3):
    if n == 1:
        answer.append([start, destination])
    else:
        hanoi(n - 1, start, destination, middle)
        answer.append([start, destination])
        hanoi(n - 1, middle, start, destination)

def solution(n):
    hanoi(3)
    return answer

solution(3)