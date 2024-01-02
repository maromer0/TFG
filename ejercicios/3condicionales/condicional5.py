age = int(input("How old are you: "))
income = int(input("What is your monthly income: "))
if age > 16 and income >= 1000:
    print("pay taxes")
else:
    print("do not pay taxes")