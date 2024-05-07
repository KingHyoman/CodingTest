# The data consists of ["code", "date", "maximum", "remain"]
# You have to sort it by given condition
# For example, given the following data
# data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
# If the given data needs to be sorted in 
# "ascending order of the current quantity, for items manufactured before 20300501", 
# the processed data that meets the condition would be as follows.
# data = [[3,20300401,10,8],[1,20300104,100,80]]
# There are 4 variables: data, ext, val_ext, sort_by
# Extract data from data where the value of ext is less than val_ext
# sort the extracted data in ascending order based on the value of sort_by

def solution(data, ext, val_ext, sort_by):
    answer = []
    mapping = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    for d in data:
        if d[mapping[ext]] < val_ext:
            answer.append(d)
    answer.sort(key = lambda x:x[mapping[sort_by]])
    return answer