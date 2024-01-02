weight = float(input("Introduce your weight: "))
height = float(input("Introduce your height: "))
bmi = weight / (height ** 2)
print("Your BMI is " + str(round(bmi, 2)))