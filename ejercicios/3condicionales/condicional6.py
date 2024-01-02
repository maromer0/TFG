name = input("Name: ")
gender = input("Gender: ")
if gender.lower() == "women":
    if name.title()[0] < "M":
        print("group A")
    else:
        print("group B")
else:
    if name.title()[0] > "N":
        print("group A")
    else:
        print("group B")