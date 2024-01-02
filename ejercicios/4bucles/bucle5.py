money = float(input("Amount to invest: "))
annual_interest = float(input("Anual interest: "))
years = int(input("Years: "))
for i in range(years):
    money *= 1 + (annual_interest/100)
    print(f"Year {i+1}: {money:.2f}€")
