'''DICCIONARIOS'''
'''crear la variable diccionario'''
midiccionario={"Alemania":"Berlín","Manuel":24,12:"par"}
'''para imprimir se introduce la clave(Berlín) y devuelve el valor (Alemania)'''
print(midiccionario[12])
'''para añadir un nuevo valor al dicecionario'''
midiccionario["Yo"]="Jugando"
'''para corregir es de la misma forma que para añadir'''
midiccionario["Yo"]="Estudiando"
'''para borrar un valor del diccionario'''
del midiccionario[12]
print(midiccionario)
'''se puede usar una tupla como valor del diccionario usando mitupla[i]:"lo que sea"'''
'''tambien se puede asignar varios valores a una clave'''
midiccionario["refrescos"]=["coca-cola","fanta","siete arriba"]
print(midiccionario["refrescos"])
'''muestra todas las claves del diccionario'''
print(midiccionario.keys())
'''muestra todos los valores del diccionario'''
print(midiccionario.values())