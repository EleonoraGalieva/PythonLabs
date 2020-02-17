def fibonacci_main(n):
    if n in (1, 2):
        return 1
    if n == 0:
        return 0
    return fibonacci_main(n - 1) + fibonacci_main(n - 2)


def fibonacci(n):
    i = 0
    while i < n:
        print(fibonacci_main(i))
        i += 1

