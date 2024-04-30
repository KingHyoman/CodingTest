# Ex) keymap = ["ABACD", "BCEFD"], target = ["ABCD","AABB"]
# keymap means the keyboard. There is two key "ABACD" and "BCEFD"
# When you press "ABACD" then A -> B -> A -> C -> D 
# Same as "BCEFD"
# Figure out the minimum num of pressing keyboard using that keymap
# In case "ABCD": A is 1(press "ABACD" one time), B is 1(press "BCEFD" one time)
# , C is 2(press "BCEFD" 2 times), D is 5(press any keyboards 5 times)
# So 9
# Same way, press 4 times in "AABB"

def solution(keymap, targets):
    answer = []
    dic = {}
    # Using dic, store the minimun num of pressing
    for key in keymap:
        for idx in range(len(key)):
            if key[idx] not in dic:
                dic[key[idx]] = idx + 1
            else:
                if dic[key[idx]] > idx + 1:
                    dic[key[idx]] = idx + 1
    
    for target in targets:
        cnt = 0
        bit = 0
        for alphabet in target:
            if alphabet not in dic:
                bit = 1
            else:
                cnt += dic[alphabet]
        if not bit:
            answer.append(cnt)
        else:
            answer.append(-1)
        

    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))