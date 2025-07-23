# Calcular las ganancias por nivel en una estructura de mercadeo multinivel (MLM)

## Introducción:

Este script es un ejemplo de cómo se puede calcular las ganancias por nivel en una estructura de mercadeo multinivel (MLM). Permíteme explicarte cómo funciona y para qué puede ser utilizado.

En el MLM, los afiliados se organizan en diferentes niveles, donde cada nivel tiene un número determinado de afiliados. El objetivo es calcular las ganancias que se pueden obtener en cada nivel, considerando un margen de ganancia por venta y un monto total destinado a premios y bonificaciones.

El script comienza definiendo algunas variables, como el margen de ganancia por venta, el monto total destinado a premios y bonificaciones, y el número total de afiliados en la red. Estas variables se pueden ajustar según las necesidades de cada caso.

Luego, el script calcula el número de niveles en la estructura MLM. Esto se hace dividiendo el número total de afiliados entre 2 hasta que se llegue a 0. Cada vez que se realiza la división, se incrementa el contador de niveles. Esto nos dará el número total de niveles en la estructura.

Después de calcular el número de niveles, el script procede a calcular las ganancias por nivel. Utiliza un bucle for para recorrer cada nivel, desde el nivel 1 hasta el número total de niveles. En cada iteración, se calcula la ganancia por nivel utilizando la fórmula: monto_premios * margen_ganancia / (2 ^ (nivel-1)). Esto asegura que las ganancias se reduzcan a la mitad en cada nivel descendente.

Finalmente, el script muestra los resultados. Muestra el número total de niveles en la estructura MLM y las ganancias por nivel. Esto proporciona una visión clara de cuánto se puede ganar en cada nivel de la estructura.

Este script puede ser utilizado por ejecutivos y personas involucradas en la administración de una estructura MLM. Les permite calcular y visualizar las ganancias potenciales en cada nivel, lo que puede ser útil para tomar decisiones estratégicas, establecer metas de ventas y motivar a los afiliados.

Aquí tienes un ejemplo de cómo se verían los resultados:

El número de niveles en la estructura MLM es: 5
Las ganancias por nivel son:
Nivel 1: 100.00
Nivel 2: 50.00
Nivel 3: 25.00
Nivel 4: 12.50
Nivel 5: 6.25

## Código del script:

```shell
#!/bin/bash

# Definir variables
margen_ganancia=0.2  # Margen de ganancia por venta
monto_premios=500  # Monto total destinado a premios y bonificaciones
num_afiliados=1000  # Número total de afiliados en la red
ganancias_por_nivel=()  # Vector para almacenar las ganancias por nivel

# Calcular el número de niveles
num_niveles=0
while (( num_afiliados > 0 )); do
  num_niveles=$(( num_niveles + 1 ))
  ganancias_por_nivel[$num_niveles]=0
  num_afiliados=$(( num_afiliados / 2 ))
done

# Calcular las ganancias por nivel
for (( nivel=1; nivel<=num_niveles; nivel++ )); do
  ganancias_por_nivel[$nivel]=$(echo "scale=2; $monto_premios * $margen_ganancia / (2 ^ ($nivel-1))" | bc)
done

# Mostrar resultados
echo "El número de niveles en la estructura MLM es: $num_niveles"
echo "Las ganancias por nivel son:"
for (( nivel=1; nivel<=num_niveles; nivel++ )); do
  echo "Nivel $nivel: ${ganancias_por_nivel[$nivel]}"
done
```

* Respecto de este script hay unas consideraciones importantes:

Entradas:
-----------------------

Número de Afiliados por nivel.
Margen de ganancia por venta.  

Salidas:
-----------------------

Las ganancias por nivel.

Observaciones:
------------------------

* Punto 1: Respecto del margen de ganancia: Que pasa si el margen de ganancia es variable, pues son diversos productos con márgenes de ganancia distintos?

* Punto 2: Respecto del monto total destinado a premios y bonificaciones: para mantener motivada una fuerza de ventas y que el MLM sea sostenible, los premios deben ser numerosos en la base, sencillos premios, variados, numerosos, menos costosos, pero numerosos entonces la base necesita mas presupuesto de premios y sería bueno que una de las salidas del sistema fuese ese valor tanto en porcentaje como en dólares del monto de los premios por nivel. Otra cosa importante es que conforme se escala en la matriz, pues va quedando menos gente, que tiene mas hijos, en otras palabras tu porcentaje de ganancias debería decrecer y aumentar tus ingresos, por otro lado, mientras mas te acercas a la base, tu porcentaje de ganancias debería ser mayor, entonces  las salidas deseadas en esta parte son: porcentaje y monto en dolares de premios por nivel, porcentaje y monto de ganancias por nivel.

* Punto 3 Respecto  del número total de afiliados a la red, la matriz debería ser de niveles limitados 5, 20, 100. tener un límite, y pasado ese límite no se puede seguir ascendiendo, sin embargo debería poder pasarse a un nivel como de socio accionista de la empresa con el tiempo, en el cual ganas un royalty para toda la vida de las ganancias que los vendedores de tu decendencia y solo de la tuya.

* Punto 4 Respecto de "número total de afiliados entre 2" por que el numero de afiliados entre dos, es mas eficaz y eficiente asi? por que
