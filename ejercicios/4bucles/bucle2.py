



age = int(input('what is your age?'))
if age < 0:
    raise ValueError("'age' cannot be negative.")
for i in range(age):
    print(i+1)