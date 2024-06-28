# There is a system that provides the title melody of music
# Find the title of music if the part of melody of music is given
# The melody always do not same as provided information
# ex) "ABC"
# ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# ["(start time),(end time),(title),(melody)"]
# Then "ABC" is not in "HELLO", thus the answer is "WORLD"
# If there are 2 or more songs that meet the conditions, 
# First, return the song which has the longest broadcastin time
# Second, if also have 2 or more songs, than return by the origin order

# C#, D#, ... A# should be deal with 1 letters
# change X# into x(lower letter)
def delSharp(str):
    # using stack
    stack = []
    for letter in str:
        if letter == '#':
            tem = stack.pop()
            stack.append(tem.lower())
        else:
            stack.append(letter)
    return ''.join(stack)

# Figure out the time difference
# format: "HH:MM"
def timeDiff(a, b):
    # a: early, b: later
    b_hour = int(b[0:2])
    '''
    if b == "00:00":
        b_hour = 24
    '''
    hour_diff = b_hour - int(a[0:2])
    min_diff = hour_diff * 60 + int(b[3:5]) - int(a[3:5])
    return min_diff

# If the song's time and broadcasting time did not same
# We have to cut or extend the song for same time with broadcasting
def originalMelody(time, melody):
    # melody -> time
    sum_melody = delSharp(melody)
    new_melody = delSharp(melody)
    # If the time of song is shorter
    while len(new_melody) < time:
        new_melody += sum_melody
    
    return new_melody[:time]

def solution(m, musicinfos):
    m = delSharp(m)     # For X# characters
    n = len(m)

    # store only title and melody
    new_musicinfos = []
    for musicinfo in musicinfos:
        tem = musicinfo.split(',')
        new_musicinfos.append([tem[2], originalMelody(timeDiff(tem[0], tem[1]), tem[3])])

    # Find the songs which meet the condition
    answer_lists = []
    cnt = 0     # For the origin order
    for new_musicinfo in new_musicinfos:
        for i in range(len(new_musicinfo[1])):
            if new_musicinfo[1][i:i+n] == m:
                answer_lists.append((len(new_musicinfo[1]), cnt, new_musicinfo[0]))
                break
        cnt += 1

    # For find the song which has best condition
    if len(answer_lists) >= 1:
        max_length = -1     # length of broadcasting
        for answer in answer_lists:
            if answer[0] > max_length:
                max_length = answer[0]
        min_order = 101     # length of origin order
        for i in range(len(answer_lists)):
            if answer_lists[i][0] == max_length and answer_lists[i][1] < min_order:
                min_order = answer_lists[i][1] 
        for answer in answer_lists:
            if answer[0] == max_length and answer[1] == min_order:
                return answer[2]
    
    return "(None)"     # If there is no song meets the condition

#print(delSharp("CC#BCC#BCC#BCC#B"))  
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))