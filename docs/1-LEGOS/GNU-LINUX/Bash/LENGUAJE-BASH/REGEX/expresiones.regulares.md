# Expresiones regulares regex reg-exp

## expresiones comunes:

### Para validar valores separados por comas:

^[0-9a-zA-Z]+(,[0-9a-zA-Z]+)*$

### Otros:

ver [https://atareao.es/tutorial/terminal/comodines-y-expresiones-regulares/](https://atareao.es/tutorial/terminal/comodines-y-expresiones-regulares/) 

> En marcadores de chrome carpeta cursos y on-line hay informacion y herramientas valiosas.

## Validaciones regexp expresiones regulares

## Ejemplo de uso en script:

``` bash

var="123abc457def"

if [[ $var =~ ^[a-z]*[0-9] ]]; then
    echo "Matched"
else
    echo "Not matched"
fi
```

##### Validar dso nombres con espacio en blanco validar nombre validar palabras con espacios.

Prueba esto:
``` bash
^[A-Za-z]+[\ \t][A-Za-z]+$
Si desea validar nombres y apellidos en mayúsculas, puede usar:

^[A-Z][a-z]+[\ \t][A-Z][a-z]+$
```

##### Este código bash devuelve un número entero para números enteros como 123, flotante para números de punto flotante como 123.4 y una cadena para cualquier otro valor de entrada como "123", One23 123. o 123.4.5.
``` bash
#!/bin/bash
read -p "Type a number or a string: " input
if [[ $input =~ ^[+-]?[0-9]+$ ]]; then
echo "Input is an integer."

elif [[ $input =~ ^[+-]?[0-9]+\.$ ]]; then
echo "Input is a string."

elif [[ $input =~ ^[+-]?[0-9]+\.?[0-9]*$ ]]; then
echo "Input is a float."

else
echo "Input is a string."
fi

```


##### Validar un dominio url:



``` bash
read -p "Enter a domain name: " domain

# Validate domain name
validate="^([a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]\.)+[a-zA-Z]{2,}$"

# If user doesn't enter anything
if [[ -z "$domain" ]]; then
    echo "You must enter a domain"
fi

if [[ "$domain" =~ $validate ]]; then
    echo "Valid $domain name."
else
    echo "Not valid $domain name."
fi
```

# ALGUNAS EXPRESIONES REGULARES ÚTILES

Indicarte antes de comentarte sobre estos ejemplos de expresiones regulares que, normalmente van delimitados por //. Es decir, la expresión regular viene a ser /expresión-regular/.

* **Caracteres alfabéticos.** /^[a-zA-Z]*$/. Estos patrones son los mas sencllos de utilizar, sin embargo es un buen comienzo.
* **Caracteres en minúsculas.** /^([a-z]*$ Igual que en el caso anterior, pero esta vez en minúculas.
* Números. /^[0-9]*$/. La tercera opción pero solo para dígitos. Sin embargo, a partir de ahora, la cosa se va a ir complicando.
* **Nombre de usuario.** /^[a-z0-9_-]{3,16}$/. En este caso, el nombre de usuario debe tener una longitud mínima de tres * caracteres y máxima de 16. Solo puede estar compuesto por letras minúsculas, números, además de _ y -. Podrías incluir también las mayúsculas de la siguiente forma, /^[a-zA-Z0-9_-]{3,16}$/.
* **Contraseña.** Esto es muy similar al anterior, pero, por un lado podemos considerar cambiar la longitud mínima y máxima de la contraseña, y por otro lado incluir algunos otros caracteres. Así podría ser algo como [a-zA-Z0-9_-$!¡@?¿=;:]{8,20}$/. Hemos aumentado la longitud mínima a 8 y la máxima a 20 y además hemos incorporado algunos caracteres mas o menos extraños como pueden ser$!¡@?¿=;:.
* **Correo electrónico.** Este patrón ya tiene un poco mas d e dificultad. /^([a-z0-9_\.-]+)@([a-z0-9_\.-])\.([a-z\.]{2,6})$/. Se divide en tres grupos diferenciados, tipo antes@despues.fin. Los dos primeros admiten letras, números, además de _, - y .. Mientras que el último solo admite letras y el ., pero además con una longitud mínima de 2 y máxima de 6.
* **Dirección web.** Otro patrón realmente interesante, /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/
* **Código postal.** [0-9]{5}(\-?[0-9]{4})?$
* **Para direcciones IP.** Prepárate, que este es un buen chorizo /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$. Con esto nos aseguramos que cada uno de los grupos es número comprendido entre 0 y 255.
* **Etiquetas html.** Esta es muy interesante y seguro que la utilizarás en mas de una ocasión. Se trata de un patrón para etiquetas html. /^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$/
* **Tarjetas de crédito.** Como ves las cosas se van complicando, pero las posibilidades son realmente espectaculares. Puedes hacer casi cualquier cosa que te puedas imaginar, tan solo es cuestión de estudiarlo con el suficiente detalle. /^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6011[0-9]{12}|622((12[6-9]|1[3-9][0-9])|([2-8][0-9][0-9])|(9(([0-1][0-9])|(2[0-5]))))[0-9]{10}|64[4-9][0-9]{13}|65[0-9]{14}|3(?:0[0-5]|[68][0-9])[0-9]{11}|3[47][0-9]{13})*$/.
* **Fechas.** Al fin y al cabo, se pueden establecer expresiones regulares que nos ayuden en todas nuestras taresm y simjplifiquen el trabajo. '#^((19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01]))*$#
Imágenes. /[^\s]+(?=\.(jpg|gif|png))\.\2)
