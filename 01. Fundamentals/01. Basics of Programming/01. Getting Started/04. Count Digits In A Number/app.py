def getTotalDigits(n):

    current_number = n
    count = 1

    while current_number > 9:
        count += 1
        current_number = current_number / 10

    return count


n = int(input())
print(getTotalDigits(n))
