#En este ejercicio vamos a calcular la intensidad y la potencia de un circuito eléctrico
#tomando datos por pantalla y realizando algunas comprobaciónes a los datos.

# Pedir al usuario que ingrese el voltaje y la resistencia.
voltaje = float(input("\nIngrese el voltaje del circuito (voltios): "))
resistencia = float(input("Ingrese el valor de la resistencia (ohmios): "))

# Calcular la intensidad usando la Ley de Ohm (I = V/R).
# Calcular la potencia (P = V * I).
intensidad = voltaje / resistencia
potencia = voltaje * intensidad

# Verificar si la intensidad es un número entero
# Determinar el tipo de dato de la potencia.
intensidad_es_entero = intensidad.is_integer()
tipo_variable_potencia = type(potencia)

# Determinar si la potencia es alta o baja.
potencia_alta = potencia > 100
potencia_baja = not potencia_alta

# Imprimir los resultados.
print(f"\nIntensidad en el circuito: {intensidad:.2f} A.")
print(f"Potencia en el circuito: {potencia:.2f} W.")
print(f"La intensidad es un número entero: {intensidad_es_entero}.")
print(f"Tipo de dato de la variable potencia: {tipo_variable_potencia}.")
print(f"La intensidad indica una potencia nominal alta: {potencia_alta}.")
print(f"La intensidad indica una potencia nominal baja: {potencia_baja}.\n")

# Encuesta de grado de satisfacción.
satisfaccion = input("Ingrese el grado se satisfacción de los resultados obtenidos(Bueno/Malo): ")
satisfaccion = satisfaccion.strip()
satisfaccion = satisfaccion.capitalize()
print(f"¡Su grado de satisfacción es: {satisfaccion}!")



