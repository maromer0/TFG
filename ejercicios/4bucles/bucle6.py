num = int(input("introduce an integrer: "))
for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print("")
