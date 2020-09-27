def getTotalDigits(n):
    count = 0

    while n != 0:
        count += 1
        n = int(n / 10)

    return count


n = int(input())
print(getTotalDigits(n))
