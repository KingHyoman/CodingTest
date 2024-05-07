# Given variable: name, yearning, photo
# name: the array of strings that store people name
# yearning: the array of integer that store the score of each people in name(same order)
# photo: the array of array of strings that each array means the people in photos
# Figure out the score of each photos
# Ex) name: ["may", "kein", "kain", "radi"]
# yearning: [5, 10, 1, 3]
# photo: [["may", "kein", "kain", "radi"],
# ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
# The first photo is 19, the second one is 15 and the last one is 6

def solution(name, yearning, photo):
    answer = []
    grade = {}
    for i in range(len(name)):
        grade[name[i]] = yearning[i]
    for image in photo:
        score = 0
        for human in image:
            if human in grade:
                score += grade[human]
        answer.append(score)

    return answer