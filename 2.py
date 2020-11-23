def f():
    n = int(input('n='))
    factorial = 1
    for i in range(2,n+1):
        factorial *= i
    return factorial

print(f())
