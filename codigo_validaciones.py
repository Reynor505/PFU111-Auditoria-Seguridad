# codigo_validaciones.py
# Etapa intermedia: incorpora validación de rangos y opciones.
# Todavía no incluye manejo de errores para entradas no numéricas.

print("=== REGISTRO DE USUARIO ===")

nombre = input("Ingrese su nombre: ").strip()
while not (1 <= len(nombre) <= 50):
    print("Error: el nombre debe tener entre 1 y 50 caracteres.")
    nombre = input("Ingrese su nombre: ").strip()

edad = int(input("Ingrese su edad (0-120): "))
while not (0 <= edad <= 120):
    print("Error: la edad debe estar entre 0 y 120.")
    edad = int(input("Ingrese su edad (0-120): "))

nota = float(input("Ingrese su nota (0-100): "))
while not (0 <= nota <= 100):
    print("Error: la nota debe estar entre 0 y 100.")
    nota = float(input("Ingrese su nota (0-100): "))

opcion = int(input("Ingrese una opción (1-3): "))
while opcion not in (1, 2, 3):
    print("Error: la opción debe ser 1, 2 o 3.")
    opcion = int(input("Ingrese una opción (1-3): "))

if edad >= 18:
    print(nombre, "es mayor de edad.")
else:
    print(nombre, "es menor de edad.")

print("Nota registrada:", nota)

if opcion == 1:
    print("Mostrar información")
elif opcion == 2:
    print("Modificar información")
else:
    print("Eliminar información")

print("Proceso finalizado.")
