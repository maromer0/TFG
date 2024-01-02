grade = float(input("performance evaluation(0.0, 0.4, 0.6...): "))
if grade == 0:
	lvl = "unacceptable"
elif grade == 0.4:
    lvl = "acceptable"
else:
    lvl = "meritorious"
print("Performance: %s" % lvl)
print("Bonus: %.2f€" % (grade * 2400))