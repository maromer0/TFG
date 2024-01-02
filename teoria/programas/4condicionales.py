'''CONDICIONALES'''
'''define una función'''
def evaluacion(nota):
	valoracion="aprobado"
	if nota < 5:
		valoracion="suspenso"
	return valoracion

'''con input todos los valores son interpretados como string'''
nota_alumno=input("introduce la nota del alumno: ")
'''usamos int(valor) para convertir a variable tipo int'''
print(evaluacion(int(nota_alumno)))
print("\n")


edad=int(input("introduce tu edad: "))
if edad < 18:
    print("eres menor de edad")
elif edad > 18:
    print("eres mayor de edad")
else:
	print("ahora puedes ir a la carcel")
print("\n")


salario_presidente=int(input("introduce el salario del presidente: "))
print("salario presidente: " + str(salario_presidente))
salario_director=int(input("introduce el salario del director: "))
print("salario director: " + str(salario_director))
salario_administrativo=int(input("introduce el salario del administrativo: "))
print("salario administrativo: " + str(salario_administrativo))
if salario_presidente > salario_director > salario_administrativo:
	print("no hay ningun error")
else:
	print("hay algo raro")


opcion=input("Elige una: Informática - Matematicas - Fisica\n")
'''transformamos todo a minusculas'''
asignatura=opcion.lower()
'''compara el valor de asignatura con las opciones disponibles'''
if asignatura in ("informática - matematicas - fisica"):
    print(asignatura + " es correcta")
else:
    print(asignatura + " es incorrecta")
