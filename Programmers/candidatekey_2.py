# About Candidate Key in Database system
'''
# a relational database is any set of columns 
# that have a unique combination of values in each row, 
# with the additional constraint that removing any column 
# could produce duplicate combinations of values.
'''
# It has two conditions
# Uniqueness: the only one tuple must be searched using this key
# Minimality: if any attribute is removed from key, then the uniquness is broken
# given variable: relation(m * n array)
# ex) relation = [["100","ryan","music","2"], ["200","apeach","math","2"], \
#                ["300","tube","computer","3"],["400","con","computer","4"],\
#                ["500","muzi","music","3"],["600","apeach","music","2"]]
# Then the Candidate keys are (0), (1, 2)

# Strategy: figure out all avaliable keys
# and filter it with uniqueness and minimality
# the len of column: 1 ~ 8
# the len of row: 1 ~ 20
# Thus it is okay to check all cases
import itertools

def solution(relation):
    answers = []
    for i in range(1, len(relation[0]) + 1):
        # All cases of key
        idx_lists = list(itertools.combinations([i for i in range(len(relation[0]))], i))


        for idxs in idx_lists:
            # First: Check the uniqueness
            # For checking if there is a same value using given key
            checking_set = set()
            bit = 1     # if there is not a same value, then pass(bit = 1)
            for tup in relation:
                tem = []
                for idx in idxs:
                    tem.append(tup[idx])
                tem_tup = tuple(tem)
                if tem_tup in checking_set:
                    bit = 0 
                    break
                else:
                    checking_set.add(tem_tup)

            # Second: Check the minimality
            if bit == 1:
                if not answers:
                    answers.append(set(idxs))
                else:
                    # Using subset to check if is it minimum key of attributes
                    for answer in answers:
                        answer_bit = 1
                        if answer.issubset(set(idxs)):
                            answer_bit = 0
                            break
                        else:
                            continue
                    if answer_bit == 1:
                        answers.append(set(idxs))

                          
    return len(answers)

# First test case: 2
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],\
                ["300","tube","computer","3"],["400","con","computer","4"],\
                    ["500","muzi","music","3"],["600","apeach","music","2"]]))
# Second test case: 3
print(solution([["100","100","ryan","music","2"], \
                         ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], \
                            ["400","400","con","computer","4"], ["500","500","muzi","music","3"], \
                                ["600","600","apeach","music","2"]]))
# Third test case: 5
print(solution([["a","1","aaa","c","ng"], ["a","1","bbb","e","g"],\
                ["c","1","aaa","d","ng"], ["d","2","bbb","d","ng"]]))