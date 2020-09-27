def getGCD(num1, num2):
    while num1 % num2 != 0:
        reminder = num1 % num2
        num1 = num2
        num2 = reminder

    return num2


num1 = int(input())
num2 = int(input())

gcd = getGCD(num1, num2)
lcm = int((num1 * num2) / gcd)

print("gcd:", gcd)
print("lcm:", lcm)
