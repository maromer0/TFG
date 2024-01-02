for i in range(1,101,2):
    print(i, end=" ")


contraseña=input("\nintroduce contraseña: ")

for i in range(len(contraseña)):
    elif contraseña[i] == " ":
        print("Contraseña erronea.")
    else:
        print("contraseña OK.")

longitud=len(contraseña)
if longitud < 8:
    print("contraseña erronea.")