def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def small(a,b):
    if a < b:
        return a
    else:
        return b

def smallest(a, b, c):
    return small(a, small(b, c))



def median(a, b, c):
    if a == smallest(a,b,c):
        if b == biggest(a,b,c):
            return c
        else:
            return b
    elif a == smallest(a,b,c):
        if c == biggest(a,b,c):
            return b
        else:
            return c
    elif a == biggest(a,b,c):
        if b == smallest(a,b,c):
            return c
        else:
            return b
    elif a == biggest(a,b,c):
        if c == smallest(a,b,c):
            return b
        else:
            return c
    elif b == smallest(a,b,c):
        if c == biggest(a,b,c):
            return a
        else:
            return c
    elif b == smallest(a,b,c):
        if a == biggest(a,b,c):
            return c
        else:
            return a
    elif b == biggest(a,b,c):
        if c == smallest(a,b,c):
            return a
    elif b == biggest(a,b,c):
        if a == smallest(a,b,c):
            return c
    elif c == smallest(a,b,c):
        if a == biggest(a,b,c):
            return b
    elif c == smallest(a,b,c):
        if b == biggest(a,b,c):
            return a
    elif c == biggest(a,b,c):
        if a == smallest(a,b,c):
            return b
    elif c == biggest(a,b,c):
        if b == smallest(a,b,c):
            return a
    #checks for biggest first

    else:
        print("Numbers were not passed in argument")







print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7
