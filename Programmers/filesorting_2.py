# Sorting files
# assume that there are five files: ["img12.png", "img10.png", "img2.png", "img1.png"]
# Usually the computer sorts this files: ["img1.png", "img10.png", "img12.png", "img2.png"] 
# But we want to sort using different method
# First split the file name into 3 parts: head, num and tail
# head: until not num       ex) img1.png -> 'img'
# num: the part only num    ex) img1.png -> '1'
# tail: the others          ex) img1.png -> '.png'
# Second, sort by head(we do not consider the upperletter and lowerletter -> 'img' and 'IMG' are same)
# Third, sort by num(we do not consider the 0 in front of num -> '1' and '01' are same)
# Fourth, sort by the original order

# ex)
# ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# There are all img(IMG) thus skip the second step
# '01' and '1' are same thus, "img1.png" -> "IMG01.GIF"
# same as above, "img02.png" -> "img2.JPG"
# Thus the final order is ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

def solution(files):
    # to save the head, num and the original order
    # This will use after the standard of sorting
    digits = set([str(i) for i in range(10)])
    order = {}

    for i in range(len(files)):
        tem = []
        head = ''
        num = ''

        idx = 0
        while files[i][idx] not in digits:
            head += files[i][idx].lower()
            idx += 1
        while idx < len(files[i]) and files[i][idx] in digits:
            num += files[i][idx]
            idx += 1

        tem.append(head)
        tem.append(int(num))
        tem.append(i)

        order[files[i]] = tem

    # Apply the step by step
    return sorted(files, key=lambda x: (order[x][0], order[x][1], order[x][2]))