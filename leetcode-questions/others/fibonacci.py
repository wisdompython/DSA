def fibonacci(n):
    
    a = 0
    b = 1

    fib = [a, b]
    for i in range(n):

        c = a + b

        fib.append(c)

        a = b

        b = c    


    return fib


print(fibonacci(10))