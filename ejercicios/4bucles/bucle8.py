num = int(input("Insert an integrer: "))
for i in range(1,num+1,2):
    print("")
    for num in range(i, 0, -1):
        if num % 2 != 0:
        	print(num, end=" ")