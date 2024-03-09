# A company that produces wallet wants to decide their wallet size
# There is some cards and their size is given
# For example, the card sizes are [[60, 50], [30, 70], [60, 30], [80, 40]]
# Then the wallet size become 80 * 50 = 4000
# Because we rotate the card [30,70], then [[60, 50], [70, 30], [60, 30], [80, 40]]
# Thus, width is 80 and height is 50. Finally we return the size of wallet 4000

def solution(sizes):
    m_w, m_h = 0,  0
    for size in sizes:
        if size[0] < size[1]:
            tem = size[0]
            size[0] = size[1]
            size[1] = tem
        if m_w < size[0]:
            m_w = size[0]
        if m_h < size[1]:
            m_h = size[1]
    return m_w * m_h

#    answer = 0
#    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))