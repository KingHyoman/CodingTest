# Given variable: str1, str2(all of them are string)
# Using Jaccard Similarity, find the similarity between str1 and str2
# Jaccard Similarity
# If there are two sets A={1, 2, 3} and B = {3, 4, 5}
# First, figure out the union = {1, 2, 3, 4, 5} and intersection = {3}
# Then divide intersection by union => 1/5 is the Jaccard Similarity of str1 and str2
# Apply it for string

def solution(str1, str2):
    # make two clustering sets for str1 and str2
    # The set is consisted of 2 characters of string
    set1, set2 = [], []
    set1_set, set2_set = set(), set()
    tem = ''
    for str in str1:
        if str.isalpha():
            tem += str.lower()
        else:
            tem = ''
        if len(tem) == 2:
            if tem not in set1_set:
                set1_set.add(tem)
            else:
                set1.append(tem)
            tem = str.lower()
        
    tem = ''
    for str in str2:
        if str.isalpha():
            tem += str.lower()
        else:
            tem = ''
        if len(tem) == 2:
            if tem not in set2_set:
                set2_set.add(tem)
            else:
                set2.append(tem)
            tem = str.lower()

    # make unionset and intersection set
    uniset = set1_set.union(set2_set)
    itrset = set1_set.intersection(set2_set)

    # Final format of printing
    if len(uniset) == 0 and len(itrset) == 0:
        return 65536
    
    # sort function
    set1.sort(key=lambda x: (x[0], x[1]))
    set2.sort(key=lambda x: (x[0], x[1]))

    if set1 and set2:
        i, j = 0, 0
        itr, uni = 0, 0
        while i < len(set1) and j < len(set2):
            if set1[i] == set2[j]:
                itr += 1
                uni += 1
                i += 1
                j += 1
            else:
                if set1[i] > set2[j]:
                    j += 1
                    uni += 1
                elif set2[j] > set1[i]:
                    i += 1
                    uni += 1
        print(len(set1), len(set2))
        print(i, j)
        if i == len(set1):
            uni += (len(set2) - j)
        elif j == len(set2):
            uni += (len(set1) - i)

        return int((len(itrset) + itr)*65536/(len(uniset) + uni))
    elif set1:
        return int(len(itrset)*65536/(len(uniset) + len(set1)))
    elif set2:
        return int(len(itrset)*65536/(len(uniset) + len(set2)))


    return int(len(itrset)*65536/len(uniset))


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))

