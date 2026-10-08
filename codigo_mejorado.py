# codigo_mejorado.py
# Registro de usuario con validación de entradas y manejo de errores.

def pedir_nombre():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if 1 <= len(nombre) <= 50:
            return nombre
        print("Error: el nombre no puede estar vacío ni superar 50 caracteres.")


def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: ingrese un valor entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def pedir_real(mensaje, minimo, maximo):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: ingrese un valor entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: debe ingresar un número válido.")


def mostrar_informacion(nombre, edad, nota):
    print("\n--- INFORMACIÓN DEL USUARIO ---")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Nota: {nota:.2f}")


def main():
    print("=== REGISTRO DE USUARIO SEGURO ===")

    nombre = pedir_nombre()
    edad = pedir_entero("Ingrese su edad (0-120): ", 0, 120)
    nota = pedir_real("Ingrese su nota (0-100): ", 0, 100)
    opcion = pedir_entero(
        "Ingrese una opción (1: Mostrar, 2: Modificar, 3: Eliminar): ",
        1,
        3
    )

    if edad >= 18:
        print(f"{nombre} es mayor de edad.")
    else:
        print(f"{nombre} es menor de edad.")

    print(f"Nota registrada: {nota:.2f}")

    if opcion == 1:
        mostrar_informacion(nombre, edad, nota)
    elif opcion == 2:
        print("Función de modificación seleccionada.")
    elif opcion == 3:
        print("Función de eliminación seleccionada.")

    print("\nProceso finalizado correctamente.")


if __name__ == "__main__":
    main()
