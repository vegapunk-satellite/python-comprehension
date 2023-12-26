def fibonacci(n):
    fib = [1, 1]
    for i in range(n - 2):
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib


print(fibonacci(50))
