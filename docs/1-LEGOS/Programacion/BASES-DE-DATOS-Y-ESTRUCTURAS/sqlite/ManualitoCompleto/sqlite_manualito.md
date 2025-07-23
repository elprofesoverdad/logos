# Manualito sqlite

## convertir segundos a hh\:mm\:ss

``` sql
sqlite> SELECT time(10, 'unixepoch');

SALIDA:
00:00:10

- donde esta el 10 se coloca el nombre del campo que tiene los segundos,
- el nombre del campo debe ser del tipo real. 
.

sqlite> SELECT time(campo_tiempo, 'unixepoch');

* NOTA: para una año de datos en segundos:; 24*30*12*3600=31104000
 segundos tiene el año 8 cifras, más 6 decimales 
 (los decimales de playerctl position), entonces el tipo real 
 es de 8,6 (Ver tipos de datos y afinidad.)
```
## Tipos de datos y afinidad

[https://www.sqlite.org/datatype3.html](https://www.sqlite.org/datatype3.html)

## SQLite ordenar por order by

``` sql
SELECT
   select_list
FROM
   table
ORDER BY
    column_1 ASC,
    column_2 DESC;
``` 



