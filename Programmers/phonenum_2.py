# We want to know that any num contains other num in phone num book
# ex) ["119", "97674223", "1195524421"]
# "1195524421" contains "119"
# In this case, return false
# Otherwise, return true

# strategy: use hashing
# If you use a nested for loop, then it is not meet the time complexity

def solution(phone_book):
    # use dictionary to represent hashing
    phone_num = {num[1]: num[0] for num in enumerate(phone_book)}

    for num in phone_num:
        tem = ''
        for digit in num:
            tem += digit
            
            # in this if condition, we can reduce the time
            # we can access the phone num directly
            if tem in phone_num and num != tem:
                return False
            
    return True
                
        

print(solution(["119", "97674223", "1195524421"]))
print(solution(["12","123","1235","567","88"]))