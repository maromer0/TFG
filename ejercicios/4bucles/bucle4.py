num = int(input("Positive integrer: "))
for i in range(num, -1, -1):
    if i % 2 != 0:
        print(i, end=",")