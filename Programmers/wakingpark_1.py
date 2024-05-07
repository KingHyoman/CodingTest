# There is a park and a robot is walking in this park
# This robot walks by program
# The robot cannot walk if there is a border
# Ex) park: ["SOO","OXX","OOO"]
# O means it is available walking here
# X means cannot walk here, S means the start points
# routes(programmed): ["E 2","S 2","W 1"]
# There is four way(E, W, S, N) and the distance of the route
# If the command lead the robot out of the park, then ignore
# You have to figure out the final spot of the robot
# In this case, "S 2" has the border, thus ignore it
# The final spot: [0, 0] -> [0, 2] -> [0, 1]

def solution(park, routes):
    border = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            # starting point
            if park[i][j] == 'S':
                start_x = i
                start_y = j
            # the border
            if park[i][j] == 'X':
                border.append((i, j))


    for route in routes:
        bit = 0
        # Divide by the way of command(N, S, E, w)
        if route[0] == 'S':
            if start_x + int(route[2]) >= len(park):
                bit = 1
                continue
            for x in range(int(route[2])):
                if (start_x + x + 1, start_y) in border:
                    bit = 1
                    break
            if not bit:
                start_x += int(route[2])
            print(f'{route[0]}, ({start_x}, {start_y})')
        if route[0] == 'N':
            if start_x - int(route[2]) < 0:
                bit = 1
                continue
            for x in range(int(route[2])):
                if (start_x - x - 1, start_y) in border:
                    bit = 1
                    break
            if not bit:
                start_x -= int(route[2])
            print(f'{route[0]}, ({start_x}, {start_y})')
        if route[0] == 'E':
            if start_y + int(route[2]) >= len(park[0]):
                bit = 1
                print('fuck')
                continue
            for y in range(int(route[2])):
                if (start_x, start_y + y + 1) in border:
                    bit = 1
                    break
            if not bit:
                start_y += int(route[2])
            print(f'{route[0]}, ({start_x}, {start_y})')
        if route[0] == 'W':
            if start_y - int(route[2]) < 0:
                bit = 1
                continue
            for y in range(int(route[2])):
                if (start_x, start_y - y - 1) in border:
                    bit = 1
                    break
            if not bit:
                start_y -= int(route[2])
            print(f'{route[0]}, ({start_x}, {start_y})')
      

    
    return [start_x, start_y]

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))