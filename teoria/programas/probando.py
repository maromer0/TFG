'''BUCLES'''

'''crear bucle sintaxis'''
for i in ["h","o","l","a"]:
    '''con la variable end se puede añadir un caracter fijo a acada corrida del bucle'''
    print(i, end="	")

for i in range(5):
    print(i, end=" ")

contador = 0
miemail=input("\nIntroduce tu direccion de email: ")
for i in miemail:
    if (i == "@" or i == "."):
        contador += contador

if contador == 2:
    print("correo electronico válido")
else:
    print("correo inválido")
    
'''permite añadir texto en cada ciclo del bucle [0:4]'''
for i in range(5):
    print(f"valor de i: {i}")

for i in range(0,50,5):
	print(i, end=" ")
