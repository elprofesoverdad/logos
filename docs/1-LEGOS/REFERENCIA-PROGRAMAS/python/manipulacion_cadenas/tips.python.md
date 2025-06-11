# Tips python Separar nombre de extension en python:

Usando el método find() de las cadenas:

nombre_archivo = "pru.py"
posicion_punto = nombre_archivo.find(".")
nombre_sin_extension = nombre_archivo[:posicion_punto]

Usando el método replace() de las cadenas:

nombre_archivo = "pru.py"
nombre_sin_extension = nombre_archivo.replace(".py", "")

Usando el módulo pathlib:

from pathlib import Path
nombre_archivo = "pru.py"
nombre_sin_extension = Path(nombre_archivo).stem

## pausar una ejecución:

Sí, en Python puedes utilizar la función input() para pausar la ejecución de un programa y esperar a que el usuario ingrese alguna entrada por teclado.

Por ejemplo, si queremos pausar la ejecución de un programa hasta que el usuario presione la tecla Enter, podemos utilizar la función input() de la siguiente manera:

input("Presiona Enter para continuar...")
En este caso, la función input() imprimirá el mensaje "Presiona Enter para continuar..." en la consola y esperará a que el usuario presione la tecla Enter para continuar con la ejecución del programa.

También puedes utilizar la función time.sleep() del módulo time para pausar la ejecución de un programa por un tiempo determinado en segundos. Por ejemplo, si queremos pausar la ejecución del programa por 5 segundos, podemos utilizar la función time.sleep(5) de la siguiente manera:

import time

print("Inicio del programa")
time.sleep(5)
print("Fin del programa")

## verificar si al principio de la linea hay espacios o tabulaciones:

linea = "    Esta línea tiene espacios al inicio"
if linea.startswith(" ") or linea.startswith("\t"):
    print("La línea tiene espacios o tabulaciones al inicio")
Utilizando el método lstrip(): Este método devuelve una copia de la cadena con los caracteres en blanco eliminados al inicio. Si la cadena original tenía espacios o tabulaciones al inicio, la cadena resultante no los tendrá. Por lo tanto, se puede comparar la cadena original con la cadena resultante para verificar si había espacios o tabulaciones al inicio. Por ejemplo:
linea = "    Esta línea tiene espacios al inicio"
if linea != linea.lstrip():
    print("La línea tiene espacios o tabulaciones al inicio")
Utilizando expresiones regulares: Las expresiones regulares son una forma poderosa de buscar patrones en una cadena de texto. En este caso, se puede utilizar una expresión regular para buscar espacios o tabulaciones al inicio de la línea. Por ejemplo:
import re
linea = "    Esta línea tiene espacios al inicio"
if re.match(r'^\s+', linea):
    print("La línea tiene espacios o tabulaciones al inicio")
Utilizando el método split(): Este método divide una cadena en una lista de subcadenas separadas por un delimitador especificado. En este caso, se puede utilizar para dividir la línea en una lista de palabras y verificar si la primera palabra es una cadena vacía. Si es así, significa que la línea tenía espacios o tabulaciones al inicio. Por ejemplo:
linea = "    Esta línea tiene espacios al inicio"
if linea.split()[] == "":
    print("La línea tiene espacios o tabulaciones al inicio")
Utilizando el método isspace(): Este método devuelve True si la cadena está compuesta únicamente por caracteres en blanco (espacios, tabulaciones, saltos de línea, etc.). En este caso, se puede utilizar para verificar si la primera letra de la línea es un carácter en blanco. Por ejemplo:
linea = "    Esta línea tiene espacios al inicio"
if linea[].isspace():
    print("La línea tiene espacios o tabulaciones al inicio")
Cada una de estas formas puede ser útil dependiendo del contexto en el que se esté leyendo el documento y de lo que se quiera hacer con las líneas que tienen espacios o tabulaciones al inicio.