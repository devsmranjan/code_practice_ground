def checkPrime(n):
    # run upto square root of n
    d = 2

    while d * d <= n:
        if n % d == 0:
            return "not prime"

        d += 1

    return "prime"


t = int(input())

for i in range(t):
    n = int(input())
    print(checkPrime(n))
