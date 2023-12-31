def max_meeting_room():
    schedule = input_meeting_schedule()
    schedule = sorted(schedule, key=lambda x : (x[1], x[0]))     # sort by 1. end time, 2. starting time
    #print(schedule)
    result = 1
    pointer = 0

    for i in range(1, len(schedule)):
        if schedule[pointer][1] <= schedule[i][0]:
            pointer = i
            result += 1

        
    return result

    '''
    # O(N)
    # sort by 1. starting time, 2. end time
    for i in range(1, len(schedule)):
        if schedule[pointer][0] <= schedule[i][0] and schedule[pointer][1] >= schedule[i][1] and schedule[pointer][1] != schedule[i][0]:
            pointer = i
        if schedule[pointer][1] <= schedule[i][0]:
            pointer = i
            result += 1

    return result + 1
    '''

    '''
    # O(N^2)
    for i in range(len(schedule)):
        cnt = 0
        idx = i
        for j in range(i + 1, len(schedule)):
            if schedule[idx][1] <= schedule[j][0]:
                cnt += 1
                idx = j
        result.append(cnt + 1)
    print(result)
    return max(result)
    '''



def input_meeting_schedule():   # due to form of input
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    return arr

print(max_meeting_room())