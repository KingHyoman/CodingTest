# There are 3 variables in this problem
# 1. today => string of today date    ex) "2024.04.25"
# 2. terms => arr of strings => 
# each string represents the name of contract and period  
# ex) "A 6", contract A is valid after 6 months
# 3. privacies => arr of strings =>
# each string represents the date and the name of contract  
# ex) "2021.05.02 A", the contract A is started from 2021.05.02
# To figure out that find the expired contract in the privacies
# assume that the day is until 28

# Test case
# today: "2022.05.19", terms: ["A 6", "B 12", "C 3"]
# privacies: ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# first contract is valid until 2021.11.01 thus it is expired
# second contract is valid until 2022.06.28 thus it is not expired
# third contract is valid until 2022.05.18 thus it is expired
# fourth contract is valid until 2022.05.19 thus it is not expired
# The answer is [1, 3]

def is_date_early(a, b):
    # is date a is earlier than b?
    # yyyy.mm.dd
    # first check the year
    if int(a[0:4]) < int(b[0:4]):
        return True
    elif int(a[0:4]) > int(b[0:4]):
        return False
    else:
        # second check the month
        if int(a[5:7]) < int(b[5:7]):
            return True
        elif int(a[5:7]) > int(b[5:7]):
            return False
        else:
            # last check the day
            if int(a[8:10]) < int(b[8:10]):
                return True
            else:
                return False

def plus_month(date, m):
    # add the month from old date
    new_month = int(date[5:7]) + (m % 12)
    new_year = int(date[0:4]) + (m // 12)
    new_day = int(date[8:10]) - 1
    
    if new_month > 12:
        new_year += 1
        new_month -= 12
    if new_day == 0:
        if new_month == 1:
            new_year -= 1
            new_month = 12
            new_day = 28
        else:
            new_month -= 1
            new_day = 28
    if new_month < 10:
        return f'{new_year}.0{new_month}.{new_day}'
    if new_day < 10:
        return f'{new_year}.{new_month}.0{new_day}'
    
    return f'{new_year}.{new_month}.{new_day}'


def solution(today, terms, privacies):
    answer = []
    dic = {}
    for term in terms:
        dic[term[0]] = int(term[2:])

    i = 1
    for privacy in privacies:
        valid = plus_month(privacy[0:10], dic[privacy[11]])
        if is_date_early(valid, today):
            answer.append(i)
        i += 1


    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], \
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], \
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

