invest = int(input("Insert invest amount: "))
annual_interest = int(input("Insert annual interest: "))
years = int(input("Insert the number of years: "))
print("Final amount: " + str(round(invest * (annual_interest / 100 + 1) ** years, 2)))