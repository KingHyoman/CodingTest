# Prerequisite skill: a skill that is required to be learned prior to learning a certain skill
# ex) Spark → Lightning bolt → Thunder // the Lightning bolt should be learned prior to learning Thunder
# Other skills not listed in the above order (such as Healing) can be learned regardless of order
# ex) Spark → Healing → Lightning bolt → Thunder // is possible
# Given variable: skill, skill_trees
# skill: a string consists of upper-alphabet
# skill_trees: containing skill trees created by users 
# return the number of available skill trees
# ex) skill: "CBD", skill_trees: ["BACDE", "CBADF", "AECB", "BDA"]
# "CBADF" and "AECB" are possible skill trees from the skill "CBD"

def solution(skill, skill_trees):
    answer = 0
    skill_sets = set([s for s in skill])    # For checking if it is in skill
    for skill_tree in skill_trees:
        bit = 1
        idx = 0
        for s in skill_tree:
            if s not in skill_sets:
                continue
            else:
                if idx < len(skill) and skill[idx] == s:
                    # If the order is correct
                    idx += 1
                    continue
                else:
                    # If not, break the loop
                    bit = 0
                    break
        if bit == 1:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))