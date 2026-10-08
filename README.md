# PFU111 - Auditoría de Seguridad

## Descripción

Este proyecto corresponde a una auditoría de seguridad realizada sobre un programa desarrollado en Python.

El objetivo principal fue identificar una vulnerabilidad relacionada con el ingreso de datos, realizar las correcciones necesarias y comprobar mediante pruebas que el programa funcione correctamente.

## Objetivos

* Identificar una vulnerabilidad en el código original.
* Analizar el problema encontrado.
* Mejorar la seguridad del programa.
* Implementar validación de datos.
* Implementar manejo de errores.
* Realizar pruebas de validación.
* Documentar el proceso mediante Git y GitHub.

## Tecnologías utilizadas

* Python 3
* Git
* GitHub
* Visual Studio Code

## Archivos del proyecto

| Archivo                                     | Descripción                                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------------- |
| `codigo_original.py`                        | Código original utilizado para identificar la vulnerabilidad.                   |
| `codigo_mejorado.py`                        | Código corregido con validaciones y manejo de errores.                          |
| `codigo_validaciones.py`                    | Código utilizado para realizar las pruebas de validación.                       |
| `informe_auditoria.pdf`                     | Informe de la auditoría de seguridad.                                           |
| `Reporte_Evidencias_Ronald cruz _chino.pdf` | Documento PDF que contiene las evidencias del desarrollo, pruebas y resultados. |
| `README.md`                                 | Documentación del proyecto.                                                     |

## Vulnerabilidad identificada

La vulnerabilidad encontrada estaba relacionada con el ingreso de datos no válidos por parte del usuario.

En el código original, cuando el programa esperaba un número y el usuario ingresaba texto, por ejemplo:

```text
abc
```

se podía producir un error `ValueError`, provocando que el programa terminara incorrectamente.

## Corrección aplicada

Para solucionar el problema se implementó validación de entrada mediante `try/except`.

El programa ahora controla los datos ingresados por el usuario y muestra un mensaje cuando se introduce un valor incorrecto.

Ejemplo:

```python
try:
    valor = float(input(mensaje))

except ValueError:
    print("Error: debe ingresar un número válido. Intente nuevamente.")
```

También se establecieron límites para evitar valores fuera del rango permitido.

## Pruebas realizadas

Se realizaron diferentes pruebas para comprobar la corrección del programa.

### Entrada no numérica

```text
Entrada: abc
Resultado: Se muestra un mensaje de error y el programa permite volver a intentarlo.
```

### Valor fuera del rango

```text
Entrada: Un valor fuera del límite establecido.
Resultado: Se solicita nuevamente un valor válido.
```

### Entrada válida

```text
Entrada: Un número dentro del rango permitido.
Resultado: El programa acepta el dato y continúa correctamente.
```

## Evidencias

Las evidencias de la auditoría se encuentran reunidas en:

`Reporte_Evidencias_Ronald cruz _chino.pdf`

El documento contiene evidencias del código original, vulnerabilidad identificada, código mejorado, pruebas de validación, ejecución correcta y repositorio GitHub.

## Control de versiones

El proyecto fue desarrollado utilizando Git para registrar los cambios realizados durante las diferentes etapas.

Los principales commits realizados son:

* **Commit 1:** código original.
* **Commit 2:** incorporación de validaciones.
* **Commit 3:** incorporación de manejo de errores.
* **Commit 5:** incorporación de documentación y validaciones.
* **Commit final:** reemplazo del informe Word por PDF.
* **Commit 6:** incorporación de evidencias.

El historial de commits permite observar la evolución del proyecto y los cambios realizados durante la auditoría.

## Conclusión

La auditoría permitió identificar y corregir un problema relacionado con la validación de los datos ingresados por el usuario.

Después de implementar el manejo de errores y las validaciones correspondientes, el programa puede controlar entradas incorrectas sin finalizar inesperadamente.

Además, el uso de Git y GitHub permitió mantener un registro de los cambios realizados y organizar la documentación y evidencias del proyecto.



Proyecto académico - PFU111
