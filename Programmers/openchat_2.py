# There is a chatting system and the manager wants to see all logs
# Logs: when someone enters or leaves, then the log occurs
# ex) A enters this room, A leaves this room
# There is a special rules: if someone's nickname is changed -> the logs are changed too
# ex) If A -> B then A enters this room -> B enters this room
# given variable: record
# record is a list of strings
# structure of string -> "(function) (userID) (nickname)"
# function: enter, leave, change
# userID: do not change
# nickname is nickname
# Then return all logs

# Using dict: the UserID do not change, thus key is UserID
# the nickname is changeable thing, thus value is nickname
# Using two loops

def solution(record):
    answer = []
    IDandName = {}      # To record the User's nickname(overwrite)
    for r in record:
        tem = r.split(' ')
        if tem[0] == 'Enter' or tem[0] == 'Change':
            IDandName[tem[1]] = tem[2]
    for r in record:
        tem = r.split(' ')
        # we need not to return the output when 'change
        if tem[0] == 'Enter':
            answer.append(f'{IDandName[tem[1]]}님이 들어왔습니다.')
        elif tem[0] == 'Leave':
            answer.append(f'{IDandName[tem[1]]}님이 나갔습니다.')

    return answer