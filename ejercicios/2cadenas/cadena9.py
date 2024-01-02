birthday = input("introduce your birthday (dd/mm/yyyy): ")
print("Day: " + birthday[:2])
print("Month: " + birthday[3:5])
print("Year: " + birthday[6:])

day = birthday[:birthday.find('/')]
monthyear = birthday[birthday.find('/') + 1:]
month = monthyear[:monthyear.find('/')]
year = monthyear[monthyear.find('/') + 1:]
print("Day: " + day)
print("Month: " + month)
print("Year: " + year)