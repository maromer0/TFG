name = input("User name: ")
num = 0
for i in name:
    num += 1
print(f"{name.upper()} have {num} characters")

print(name.upper() + " have " + str(len(name)) + " characters")