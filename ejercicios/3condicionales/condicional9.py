age = int(input("Age: "))
if age < 4:
    ticket = 0
elif age <= 18:
    ticket = 5
else:
    ticket = 10
print("Ticket price: %d€" % ticket)