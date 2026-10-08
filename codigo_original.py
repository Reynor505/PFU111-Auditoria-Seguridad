# codigo_original.py
# Versión equivalente en Python del programa entregado para la auditoría.
# Esta versión conserva intencionalmente las principales debilidades:
# no valida rangos ni controla errores de conversión.

print("=== REGISTRO DE USUARIO ===")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nota = float(input("Ingrese su nota: "))
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
elif opcion == 3:
    print("Eliminar información")
else:
    print("Opción no válida")

print("Proceso finalizado.")
