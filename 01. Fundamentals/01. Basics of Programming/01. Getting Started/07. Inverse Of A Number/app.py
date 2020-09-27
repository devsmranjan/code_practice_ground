def getInverseNumber(n):
    inverse = 0
    current_position = 1

    while n != 0:
        current_digit = int(n % 10)

        inverse_digit = current_position
        inverse_position = current_digit

        # make changes to inverse
        inverse += inverse_digit * pow(10, (inverse_position - 1))

        n = int(n / 10)
        current_position += 1

    return inverse


n = int(input())

print(getInverseNumber(n))
