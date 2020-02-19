def fibonacci_generator(n):
    a = 0
    b = 1
    while n > 0:
        a, b = b, a + b
        yield a
        n -= 1


def fibonacci(n):
    fib_g = fibonacci_generator(n)
    for i in fib_g:
        print(i)

