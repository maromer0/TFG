email = input("introduce email: ")
count = 0
for i in email:
    if i == '@' or i == '.':
        count += 1
if count == 2:
    print(email[:email.find('@')] + '@ceu.es')
else:
    print("wrong email format")