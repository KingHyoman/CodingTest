# A dirty human who did not clean its laptop's screen
# That human clean the screen when that human feels dirty from its screen
# That human wants to clean the screen the shortest length of using mouse
# (It means that all icons are contained in one drag as using the shortest path)
# The screen is n*n and there is one icon in 1*1
# Ex) screen: ["..........", ".....#....", "......##..", "...##.....", "....#....."]
# '#' means icon, '.' means empty
# The result: [1, 3, 5, 8]

def solution(wallpaper):
    x_min, y_min = len(wallpaper), len(wallpaper[0])
    x_max, y_max = 0, 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            # the shortest path of mouse(starting point and end point)
            if wallpaper[i][j] == '#':
                if x_min > i:
                    x_min = i
                if y_min > j:
                    y_min = j
                if x_max < i:
                    x_max = i
                if y_max < j:
                    y_max = j
            pass
    return [x_min, y_min, x_max + 1, y_max + 1]