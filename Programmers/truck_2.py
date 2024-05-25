# given variables: bridge_length, weight, truck_weights
# There are some trucks in "truck_weights" waiting to pass the bridge
# Bridge has the length of "bridge_length"
# Bridge can withstand total "weight"
# Figure out the minimum time to pass the bridge for all trucks
# ex) (2, 10, [7, 4, 5, 6])
# [0, 0] -> [7, 0] -> [0, 7] -> [4, 0] -> [5, 4] -> [0, 5]
# -> [6, 0] -> [0, 6] -> [0, 0]
# 8 seconds

def solution(bridge_length, weight, truck_weights):
    # initial setting
    answer = 1
    tot_weight = truck_weights[0]
    tot_num = 1
    truck_locate = [0]
    in_bridge = [truck_weights.pop(0)]

    # until all trucks are gone
    while in_bridge or truck_weights:
        # move
        for i in range(len(truck_locate)):
            truck_locate[i] += 1 
        # if weight issue is okay, than append one truck
        if truck_weights and (tot_weight + truck_weights[0]) <= weight and (tot_num + 1) <= bridge_length:
            tot_weight += truck_weights[0]
            tot_num += 1
            truck_locate.append(0)
            in_bridge.append(truck_weights.pop(0))    
        answer += 1
        # remove the passed truck
        if (truck_locate[0] + 1) == bridge_length:
            truck_locate.pop(0)
            tot_weight -= in_bridge.pop(0)
            tot_num -= 1
        

    # The last 1 second is not added
    return answer + 1

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))