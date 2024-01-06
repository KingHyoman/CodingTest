# H - index
# The h-index is an author-level metric 
# that measures both the productivity and citation impact of the publications, 
# initially used for an individual scientist or scholar. 
# from wikipidia

# Strategy
# Sort
# Count

# How can deal [7,7,7,7,7,7]?
def hIndex(citations):
    arr = sorted(citations, reverse=True)
    cnt = 0
    for i in arr:
        cnt += 1
        if cnt > i:
            return cnt - 1

    return cnt

arr = [6, 5, 3, 3, 0]
print(hIndex(arr))

arr = [3, 4]
print(hIndex(arr))