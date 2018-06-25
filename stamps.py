
#Counts number of 5p, 2p, 1p stamps needed to fulfil num
def stamps(num):
    stamp_5 = 5
    stamp_2 = 2
    stamp_1 = 1
    count_5 = 0
    count_2 = 0
    count_1 = 0
    while num > 4:
        num = num - stamp_5
        count_5 = count_5 + 1
    while num < 5 and num > 1:
        num = num - stamp_2
        count_2 = count_2 + 1
    while num < 2 and num > 0:
        num = num - stamp_1
        count_1 = count_1 + 1
    return count_5, count_2, count_1

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
