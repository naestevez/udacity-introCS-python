def factorial(n):
    i = 0
    a = n
    while i < n:
        a = n - i
        i = i + 1
        a = a * n
        return a

#n * n-1 * n-2 * n-3



print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
