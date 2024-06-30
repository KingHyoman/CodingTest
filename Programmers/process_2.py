# The operating system manage the processes with following rules
# 1. There are some processes in waiting queue
# 2. The OS allocates the resource for the process with two steps
# 2-1. has high priority(big num)
# 2-2. the order of queue
# Assume that there is no interrupt(it means, if a process is executed, then it will exit)
# Given variable: priorities(list of priorities of processes), location
# return that the order of given location following those rules

class Priorityqueue():
    def __init__(self, priorities):
        # for store the process and priority
        self.processes = {process: priorities[process] for process in range(len(priorities))}
        # for store all priority without same value
        self.priorities = set([priority for priority in priorities])
        # for store executed processes
        self.executed = set()
    
    def printfunc(self):
        # just check the variables
        print(f'processes: {self.processes}')
        print(f'priorities: {self.priorities}')
        print(f'executed: {self.executed}')

    def highPriority(self):
        # return the priority which should be executed first
        if self.priorities:
            return max(self.priorities)
    
    def delPriority(self):
        # remove the highest priority in the set
        if self.priorities:
            self.priorities.remove(self.highPriority())
    
    def isExcuted(self, process):
        # check the given process is in the executed set
        return process in self.executed

    def addExcuted(self, process):
        # add the given process into the executed set
        self.executed.add(process)

    def lenofExecuted(self):
        # the length of executed set
        return len(self.executed)
    
    def processProirity(self, process):
        # Just return the pririty of given process
        return self.processes[process]
    
    def forcheck(self, cur_process):
        # Check if there is a same priority processes among the unexecuted processes
        curr_priority = self.processes[cur_process]
        cnt = 0
        for process in self.processes:
            if process not in self.executed and self.processes[process] == curr_priority:
                cnt += 1

        return cnt != 0

def solution(priorities, location):
    queue = Priorityqueue(priorities)
    limit = len(priorities)
    process = 0
    answer = 1

    # Until all processes are executed
    while queue.lenofExecuted() < limit:
        if location == process and queue.processProirity(process) == queue.highPriority():
            break
        elif queue.processProirity(process) == queue.highPriority():
            # should be executed
            queue.addExcuted(process)
            answer += 1
            if queue.forcheck(process):
                # check if there is other processes that have same priority
                pass
            else:
                # if not, delete the priority from the set
                queue.delPriority()
        # using modular to re-cycle
        process = (process + 1) % limit
    
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))