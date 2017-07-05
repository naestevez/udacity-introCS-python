def factorial(n):
    i = 1
    factorial = 1
    count = n

    while i <= count:
        factorial = n * factorial
        n = n - 1
        i = i + 1
    return factorial

#n * n-1 * n-2 * n-3



print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720
