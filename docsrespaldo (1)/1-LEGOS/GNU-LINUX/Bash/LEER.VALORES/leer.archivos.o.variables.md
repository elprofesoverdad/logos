# Bash Leer archivo separado por comas cvs  CSV

## Para leer valores separados por coma desde una variable bash:

``` bash

Sin cambiar el IFS, ni programas externos:

variable=abc,def,ghij
for i in ${variable//,/ }
do
    # llamar comandos y procedimientos
    echo "$i"
done

SALIDA:
abc
def
ghij


# Cambiando el IFS:

oldIFS==$IFS
var=a,b,c,d

IFS=, read -a vector <<< "$var"

for i in "${vector[@]}"; do echo "$i"; done

SALIDA:
a
b
c
d


```
## Si es un archivo con valores de columnas separados por comas:

``` bash

#para un archivo llamado foo con este contenido

[IP ADRESS], [ID-Number], [Name]
[IP ADRESS], [ID-Number], [Name]
[IP ADRESS], [ID-Number], [Name]

* Entonces, para imprimir la dirección IP de cada línea, use:
$ awk -F', ' '{print $1}' < foo

* Para imprimir el número de identificación de cada línea, utilice:
$ awk -F', ' '{print $2}' < foo

* Para imprimir el nombre de cada línea, utilice:
$ awk -F', ' '{print $3}' < foo

* También es posible crear una awkdeclaración única que cree una salida que combine los distintos campos de entrada:
$ awk -F', ' '{print "ssh " $1 " /path/to/myscript.sh " $2 " " $3}' < foo

* Una vez que haya revisado el resultado de esa declaración para asegurarse de que sea precisa y efectiva para sus propósitos, puede ejecutarla fácilmente conectándola a un shell:

$ awk -F', ' '{print "ssh " $1 " /path/to/myscript.sh " $2 " " $3}' < foo | bash


```

 
## Verificar si una cadena está presente en una lista de cadenas separadas por comas:

Me gustaría conocer una manera ordenada en la que pueda verificar si hay una cadena en un valor de cadenas separado por comas. por ejemplo: si

``` bash

x="abc,def,ghi"
y="abc"

debería volver verdadero
y si
y="ab"

RESPUESTA:

19


Podrías usar globos:

[[ ",$x," = *",$y,"* ]]

```

## Expresion regular para validar cadena separada por comas:
de [https://stackoverflow.com/questions/6448573/regular-expression-help-comma-delimited-string](https://stackoverflow.com/questions/6448573/regular-expression-help-comma-delimited-string)
^[0-9a-zA-Z]+(,[0-9a-zA-Z]+)*$

## Convierte filas separadas por comas en 1 columna.

bob,john,jane,sam,joyce
``` bash
$ IFS=, read -a names <<< "bob,john,jane,sam,joyce"
$ printf "%s\n" "${names[@]}"
bob
john
jane
sam
joyce

tambien de esta forma:
awk:

$ echo "bob,john,jane,sam,joyce" | awk -F, -v OFS="\n" '{$1=$1; print}'
bob
john
jane
sam
joyce
```
## Analizar filas separadas por comas:
de [https://www.cyberciti.biz/faq/unix-linux-bash-read-comma-separated-cvsfile/](https://www.cyberciti.biz/faq/unix-linux-bash-read-comma-separated-cvsfile/)

La sintaxis es la siguiente frase en un archivo CSV llamado input.csv:

``` bash
while IFS=, read -r field1 field2
do
    echo "$field1 and $field2"
done < input.csv
```
## Cómo analizar un archivo CSV en Bash:
``` bash
#!/bin/bash
# Purpose: Read Comma Separated CSV File
# Author: Vivek Gite under GPL v2.0+
# ------------------------------------------
INPUT=data.csv
OLDIFS=$IFS
IFS=','
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read flname dob ssn tel status
do
	echo "Name : $flname"
	echo "DOB : $dob"
	echo "SSN : $ssn"
	echo "Telephone : $tel"
	echo "Status : $status"
done < $INPUT
IFS=$OLDIFS
```

## Tratar con datos/valores o campos faltantes:

``` bash

#!/bin/bash
missing=false
while IFS=, read -r field1 field2
do
	if [ "$field1" == "" ]
	then
		echo "field1 is empty or no value set"
		missing=true
   	elif [ "$field2" == "" ]
	then
		echo "field2 is empty or no value set"
		missing=true
	else
		echo "$field1 and $field2"
	fi
done < input.csv
if [ $missing ]
then
	echo "WARNING: Missing values in a CSV file. Please use the proper format. Operation failed."
	exit 1
else
	echo "CSV file read successfully."
fi
```

Muchos programas de utilidad de línea de comandos de Linux y Unix, como cortar, pegar, unir, ordenar, uniq, awk, sed, pueden dividir archivos en un delimitador de coma y, por lo tanto, pueden procesar archivos CSV simples. Por ejemplo:

``` bash
awk -F',' '{ print $1 " " $2 }'
```
