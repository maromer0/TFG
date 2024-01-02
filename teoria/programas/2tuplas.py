'''TUPLAS'''
'''convertir lista a tupla es lo mismo al revés'''
mitupla=tuple(milista)
'''cuenta cuantas veces está el valor en la tupla'''
print(mitupla.count("manuel"))
'''longitud tupla'''
print(len(mitupla))
'''creamos variable tupla'''
tupla_desempaquetado=("manuel", 24, 260298)
'''desempaquetamos tupla y asignamos cada valor a una variable'''
nombre, edad, fecha_nacimiento=tupla_desempaquetado