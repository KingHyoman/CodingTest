# This problem is related with "Tuple" which is an datastructure in python
# If there are n elements not duplicated -> we can represent it using set form
# ex) (2, 1, 3, 4)
# {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
# {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
# ... 
# Then return the tuple if the set form of tuple is given
# Given variable: string
# '{', '}', ',' and the num is the only elements of the given string

def splitting(string):
    # We have to split the given string into the list of list form
    string = string[1:len(string) - 1]  # cut the first '{' and last '}'
    tem = ''
    new_list = []
    for idx in range(len(string)): 
        # Split it at '},{'
        if string[idx] == ',' and string[idx - 1] == '}' and string[idx + 1] == '{':
            new_list.append(list(tem.split(',')))
            tem = ''
        # If ',' or num in set
        # Then append it
        else:
            if string[idx] == '{' or string[idx] == '}':
                continue
            else:
                tem += string[idx]

    # The last elements
    new_list.append(list(tem.split(',')))
    # Sort it by the len of element
    new_list.sort(key=lambda x: len(x))
    return new_list

def solution(s):
    answer = []
    new_lists = splitting(s)
    visited = set()
    # Check it
    for new_set in new_lists:
        for ele in new_set:
            # If this element is not in visited
            # Then it would be the next element in the tuple
            if ele not in visited:
                visited.add(ele)
                answer.append(int(ele))
            else:
                continue

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))