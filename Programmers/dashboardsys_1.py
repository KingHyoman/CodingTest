# There is an community site
# A developer want to make a system that processing reported user
# Users can report anytimes, but many reporting for one users is treated one
# The given inputs are the list of ID, the reporting and the k.
# If user is reported over k, then that user gonna be stopped
# The system send an email user 
# Return the num of emails that users get 

def solution_(id_list, report, k):
    count_get = {i: [] for i in id_list}
    count_give = {i: [] for i in id_list}
    answer = []
    real_answer = []

    for r in report:
        if r.split(' ')[0] not in count_get[r.split(' ')[1]]:
            count_get[r.split(' ')[1]].append(r.split(' ')[0])

        if r.split(' ')[1] not in count_give[r.split(' ')[0]]:
            count_give[r.split(' ')[0]].append(r.split(' ')[1])

    for c in count_get:
        if len(count_get[c]) >= k:
            answer.append(c)

    for c in count_give:
        tem = 0
        for i in answer:
            if i in count_give[c]:
                tem += 1
        real_answer.append(tem)

    return real_answer


def solution(id_list, report, k):
    count_get = {i: 0 for i in id_list}
    tem = []

    for r in set(report):
        count_get[r.split(' ')[1]] += 1

    for i in count_get:
        if count_get[i] >= k:
            tem.append(i)
        count_get[i] = 0

    for r in set(report):
        if r.split(' ')[1] in tem:
            count_get[r.split(' ')[0]] += 1


    return [count_get[i] for i in count_get]

print(solution(["muzi", "frodo", "apeach", "neo"], \
               ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))