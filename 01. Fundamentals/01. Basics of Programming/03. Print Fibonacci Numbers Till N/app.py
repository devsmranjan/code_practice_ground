def getFibonacciNumbers(n):
    f = 0
    s = 1

    count = 2

    fibonacciNumbers = [f, s]

    while count < n:

        a = f + s
        fibonacciNumbers.append(a)

        f = s
        s = a

        count += 1

    return fibonacciNumbers


n = int(input())
allFibonacciNumbers = getFibonacciNumbers(n)
print(*allFibonacciNumbers, sep="\n")
