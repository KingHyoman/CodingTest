# given variables => array of strings, n
# sort the array by index n
# ex) ["sun", "bed", "car"], n = 1
# using "u", "e", "a" then ["car", "bed", "sun"]
# If there is same alphabet, then dic order

def solution(strings, n):
    return sorted(strings, key = lambda x : (x[n], x))