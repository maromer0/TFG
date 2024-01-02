rent = int(input("anual income: "))
if rent < 10000:
    tax = 5/100
elif rent < 20000:
    tax = 15/100
elif rent < 35000:
    tax = 20/100
elif rent < 60000:
    tax = 30/100
else:
	tax = 45/100
print("Total: {rent:11.2f} €".format(rent = rent * tax))