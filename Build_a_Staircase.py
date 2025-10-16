n = int(input("Enter the number of steps: "))
for i in range(1, n + 1):
    for k in range(i):
        print("# ", end="")
    print()