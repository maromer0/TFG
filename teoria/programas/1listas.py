'''LISTAS'''
'''crea una lista'''
milista=["manuel","antonio"]
'''agregar miguel en la posicion 1'''
milista.insert(1,"miguel") 
'''agrega el elemento al final de la lista'''
milista.append("sandra")
'''agregra elementos a la lista'''
milista.extend(["juan", "carmen", "ana"])
'''indica la posición en el array del valor indicado'''
print(milista.index("antonio"))
'''borra un elemento de la lista'''
milista.remove("antonio")
'''elimina el último elemento de la lista'''
milista.pop()
'''muestra por pantalla toda la lista'''
print(milista[3:4])
'''devuelve un valor booleano para determinar si se encuentra un valor en la lista'''
print("hantonio" in milista)
print("\n")