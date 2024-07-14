import math
from decimal import Decimal

def solution(pp, cash):
    answer = []
    bills = {100: "Hundred", 50: "Fifty", 20: "Twenty", 10: "Ten", 5: "Five",\
            2: "Two", 1: "One", 0.5: ".5", 0.25: ".25", 0.1: ".1", 0.05: ".05", 0.01: ".01"}
    billindex = [100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01]
    change = Decimal(str(cash - pp))
    idx = 0

    if change < 0:
        return 'Error'

    while change > 0 and idx < len(billindex):
        if change >= billindex[idx]:
            change -= Decimal(billindex[idx])
            answer.append(bills[billindex[idx]])
        else:
            idx += 1

    return answer

print(solution(230.0, 500.0))
print(solution(17, 16))
print(solution(35, 35))
print(solution(45, 50))
print(solution(15.94, 16.00))