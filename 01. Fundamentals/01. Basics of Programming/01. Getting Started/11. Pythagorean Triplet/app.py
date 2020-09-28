def largestNumber(a, b, c):
    if a > b and a > c:
        return a, b, c
    elif b > a and b > c:
        return b, a, c

    return c, a, b


def isPythagoreanTriplet(a, b, c):
    h, p, b = largestNumber(a, b, c)

    return pow(h, 2) == pow(p, 2) + pow(b, 2)


inp = input()

a, b, c = map(int, inp.split())

if isPythagoreanTriplet(a, b, c):
    print("true")
else:
    print("false")
