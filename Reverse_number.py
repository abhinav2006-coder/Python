n = int(input())
for i in range(n):
    rev1 = rev2 = rev3 = 0
    sum = 0
    num, num1 = int(input()), int(input())
    while num > 0:
        digit = num % 10
        rev1 = rev1 * 10 + digit
        num //= 10
    while num1 > 0:
        digit = num1 % 10
        rev2 = rev2 * 10 + digit
        num1 //= 10
    sum = rev1 + rev2
    while sum > 0:
        digit = sum % 10
        rev3 = rev3 * 10 + digit
        sum //= 10
    print(rev3)