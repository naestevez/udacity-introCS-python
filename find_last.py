def find_last(search, target):
#    if target is equal to the last characters in search
#       if search[-1 * len(target):] == target:
#    find out position of target in search
#        return search.find(search[-1 * len(target):], -1 * len(target))
#    elif target == "":
#        search = search + ""
#        return len(search)
#    else:
#        return -1


#    i = 1
#    while i <= len(search):
#        #find target in search
#        if target == search[search[i * (-1)].find(target) : len(target) + search[i * (-1)].find(target)]
#            return search[i * -1].find(target)
#        i = i + 1

    return search.rfind(target)




print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0

print find_last("abbaabbabbbaaaabbba", "ab")
