# Sqlite Inserción y búsqueda, consultas.



## Notas sobre JOIN e uniones union en tablas. chuletas en consultas chuleta consulta

* **Dadas las siguientes tablas relacionadas:**

 ![ejemplodeconsultas](imagenes/join.png)

Si deseamos una lista de los marcadores y sus categorías:

# Análisis Join relaciones muchos a muchos tablas intermedias o tablas de asociación ( association table).

* Dada la  **tablaA** marcadores y **tablaB** categorias Con una relación muchos a muchos y **tablaI** una tabla intermedia:

``` sql title="Algoritmo"
SELECT tablaA.campo, tablaB.campo FROM tablaA INNER JOIN tablaI ON
 tablaA.clave_primaria = tablaI.clave_foránea_para_tablaA  
INNER JOIN tablaB ON tablaB.clave_primaria = tablaI.clave_foránea_para_tablaB  
```

``` sql title="Ejemplo en la Db legos.db"
SELECT marcadores.nombre, categorias.nombre_categoria FROM marcadores INNER JOIN marc_cat ON  marcadores.id  = marc_cat.id_marcador 
INNER JOIN categorias ON categorias.id = marc_cat.id_categoria

```

!!! info "**Para unir mas de dos tablas:**"
    ``` sql
    SELECT *
    FROM table1
    INNER JOIN table2
    ON table1.id = table2.id
    INNER JOIN table3
    ON table2.id = table3.id;
    ```



## LEFT JOIN

* **Ejemplo para saber que categorías no tienen marcadores.**

* Para comprender esto se toman ahora las tablas **categorias** como **tablaA**, **marc_cat como** como **tablaI**.

* LEFT JOIN arroja una matriz o cuadrícula como resultado, que incluye los **elementos de tablaA completos** emparejados con los de la tablaI **si** elemento de la tablaI, no tiene un elemento coincidente en la tablaA **entonces** en la matriz resultante de parejas, se rellena la casilla correspondiente del elemento de tablaI faltante con NULL.

* Por último se utiliza ORDER BY o IS NULL para Ordenar o Mostrar solo los elementos NUll (no tienen marcadores).

* Tanto tablaA, como tabla B, ***en el ejemplo anterior***; tienen una relación uno a muchos con tablaI, entonces: podemos aplicar una consulta LEFT JOIN uno a muchos de **uno:** tablaA ( categorias) **a muchos:** tablaI (marc_cat).

``` sql title="LEFT JOIN con ORDER BY"
SELECT
   tablaA.campo_a_ver, 
   tablaI.campo_a_ver
FROM
   tablaA
LEFT JOIN tablaI ON
   tablaI.clave_foránea_para_tablaA = tablaA.clave_primaria
ORDER BY
   tablaI.campo_a_ver;
```
``` sql title="LEFT JOIN con ORDER BY"
SELECT
   categorias.nombre_categoria, 
   marc_cat.id_categoria
FROM
   categorias
LEFT JOIN marc_cat ON
   marc_cat.id_categoria = categorias.id
ORDER BY
   marc_cat.id_categoria;
```
* **Con IS NULL**

``` sql title="LEFT JOIN con IS NULL"
SELECT
   categorias.nombre_categoria, 
   marc_cat.id_categoria
FROM
   categorias
LEFT JOIN marc_cat ON
   marc_cat.id_categoria = categorias.id
WHERE
   marc_cat.id_categoria IS NULL;
```

## INTERSECT Intersección.



* **Hallar las categorias que si tienen marcadores.** á las ocurrencias en A y B;  ó la intersección entre la tabla primaria y la secundaria.

*  

```sql
SELECT clave_primaria
FROM tabla_primaria
INTERSECT
SELECT clave_foránea_para_tabla_primaria
FROM tabla_Secundaria
ORDER BY id;
```

```sql
SELECT id
FROM categorias
INTERSECT
SELECT id_categoria
FROM marc_cat
ORDER BY id;
```

## Unión UNION

ver file:///home/daniel/tron/1-LEGOS/BASES-DE-DATOS-Y-ESTRUCTURAS/sqlite/ManualitoCompleto/UNION%20de%20SQLite%20con%20ejemplos,%20UNION%20vs.%20UNION%20ALL-www.sqlitetutorial.net.mhtml

## Resumen Inserción 1-n Uno a Muchos:

``` sql
INSERT INTO bar (description, foo_id) VALUES
    ( 'registro uno',     (SELECT id from foo WHERE type='azul') ),
    ( 'otro registro', (SELECT id from foo WHERE type='rojo' ) );
```
## Análisis:


*  bar es hija de la tabla foo, además su campo foo_id es una clave foránea relacionada a la clave principal de la tabla foo./

* foo tiene una relación 1-n con bar, pero no es una **tabla intermedia**.

* Hay un SELECT dentro del Insert, esta consulta se puede remplazar dinámicamente con una variable $loquesea, en bash, de esta manera y de forma intermedia; se puede preguntar al usuario, el **"color que tendrá el registro"**, en otras palabras se le pregunta, que registro de la tabla principal está relacionado con que registro de la clave secundaria.


> Entonces generalizando:

``` sql
 
/* valor="valor_en_la_tabla_primaria" */

INSERT INTO tabla_secundaria (campo_etc_secundaria, clave_foránea) VALUES
    ( 'registro uno',     (SELECT id from tabla_primaria WHERE type='$valor') ),
    ( 'otro registro', (SELECT id from tabla_primaria WHERE type='$valor' ) );

```


## Para Tablas Intermedias:

## En la imagen un ejemplo de una tabla intermedia de la db legos.

![muestra la imagen de dos tablas muchos a muchos y la intermedia que resuelve la relación](imagenes/tabla.intermedia.png)

> **IMPORTANTE:** de antemano debo conocer los nombres de los campos en las tablas principales, para el registro en la tabla intermedia.

**1.** En el caso de la db MarcadoresVideo, las categorías y los nombres de los videos, deben incluirse en la tabla categorías y videos respectivamente, si son varias categorías: 
    
  * Las categorías deben leerse, desde la tabla categorías, y verificar que no están repetidas.

  * Si no están repetidas, se insertan una a una con un ciclo.
  * En este mismo ciclo las categorías se guardan en un vector.

**2.** En este punto se inserta el nombre del video dentro de la tabla video.

  * Debe validarse que el nombre del video sea único.
  * El nombre del video se guarda en una variable.

**3.** Se realiza un insert de dos campos, en la tabla intermedia de esta manera en psudocódigo:

``` sql

/* nombre_video="valor_en_la_Variable" */
/* nombre_categoria="vector_categorias[]" */

for i in vector[i]; do
INSERT INTO cat_videos (id_videos, id_cat)
 VALUES
 ((SELECT id from tabla_primaria WHERE type='$nombre_video'), (SELECT id from tabla_primaria WHERE type='$vector_categorias[i]'));
done

```

## Resumen de Inserción:

* **De videos, cat_video y categorias:**
 
**1.** Introducir la ruta y nombre de video en la tabla videos.

**2.** Introducir la categoría para el video seleccionado, si son varias, guardar un vector.

**3** Introducir en ciclo para cada categoría, el nombre del video en la **tabla intermedia** cat_videos.

## Actualizar la tabla categorías de un video.

**0** Si se actualiza (o borra) un nombre de video o una categoría, en su tabla respectiva que se encuentre registrada en la tabla intermedia cat_videos; se actualizará la tabla intermedia automáticamente. el proceso siguiente es para incluir categorías nuevas o existentes a un video.

**1** Primero se busca si el video existe en la tabla videos. con un like

**2** Luego con el nombre del video, y el nombre de la categoría se busca en la tabla categorias, si la categoría(as) existe: si existe: OK, si no existe, se actualizará la tabla categoría con vector.

**3** Entonces, se busca la asociación cat_videos, y se insertan todas las apariciones del video correspondiente (1 solo video) en esa tabla, para la categoría indicada.

**4** *OTRAS PENDIENTES* 
  - Borrar asociaciones de categorías a un video.
  - Leer videos y sus categorías asociadas (Buscar videos por categoría).



## Consulta de selección uno a muchos:

``` sql
SELECT producto.*, categoria.* 
FROM   producto INNER JOIN categoria USING(categoria_id)
```
> Nota Importante:

> Si  el campo de unión en la tabla categorías se llama categoría_id y en la tabla producto la clave foránea se llama FK_categoria, la consulta queda sí:

``` sql

SELECT producto.*, categoria.* 
FROM   producto INNER JOIN categoria 
       ON producto.FK_categoria = categoria.categoria_id

```
## Notas:

* Con *SELECT producto.*, categoria.*  estamos seleccionando todos los campos de la tabla producto y todos los campos de la tabla categoria. Mientras que con FROM producto INNER JOIN categoria USING(categoria_id), estamos diciendo que: desde la tabla producto unida internamente a la tabla categoria (FROM producto INNER JOIN categoria) utilizando el campo categoria_id (USING(categoria_id)).

* En este caso producto es la tabla secundaria y categoría la primaria, así que (FROM producto INNER JOIN categoria), es: FROM tabla_secundaria INNER JOIN tabla_primaria; y (USING(categoria_id)) es (USING(nombre_clave_foranea)).

* Resumiendo el comando queda así:


``` sql
SELECT tabla_secundaria.*, tabla_primaria.* 
FROM tabla_secundaria INNER JOIN tabla_primaria (USING(nombre_clave_foranea))
```



# Inicio, ejemplo con tablas foo y bar:

## Dada la tabla fo y la tabla bar:

``` sql 

/* Creamos la tabla fo y bar; bar es hija de la tabla foo, además su campo foo_id es una clave foránea relacionada a la clave principal de la tabla foo.*/

CREATE TABLE foo
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE bar
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(40) NOT NULL UNIQUE,
    foo_id INTEGER NOT NULL REFERENCES foo ON DELETE RESTRICT
);


/* Se insertan los datos en foo (tabla principal).*/



INSERT INTO foo (type) VALUES
    ( 'rojo' ),
    ( 'verde' ),
    ( 'azul' );


/*De esta manera se insertan los datos en la tabla relacionada*/


INSERT INTO bar (description, foo_id) VALUES
    ( 'registro uno',     (SELECT id from foo WHERE type='azul') ),
    ( 'otro registro', (SELECT id from foo WHERE type='rojo' ) );

```

## Análisis:

* Hay un SELECT dentro del Insert, esta consulta se puede remplazar dinámicamente con una variable $loquesea, en bash, de esta manera y de forma intermedia; se puede preguntar al usuario, el **"color que tendrá el registro"**, en otras palabras se le pregunta, que registro de la tabla principal está relacionado con que registro de la clave secundaria.


## Consultas búsqueda:

## Consulta sencilla.

``` sql
SELECT * FROM libro_transacciones WHERE prestatario_id = 1;
libro_transacciones
```

## recorrer una carpeta y grabar los nombres de archivos o directorios en una tabla:

``` sqlite

/*Primero cd a la ruta de la carpeta...*/

$(for f in *; do echo "INSERT INTO [clase] (nombre_clase, id_curso) VALUES ('$f', 1);" | sqlite $data/sqlite/legos/legos.db; done)

el 1 de id_curso es para mantener la integridad referencial con la tabla cursos.
```

## Consulta conrelaciones. 


## Dada la siguiente base de datos:

``` sql
CREATE TABLE categoria( 
    categoria_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria VARCHAR(25) NOT NULL, 
    activa BOOL 
); 

CREATE TABLE producto( 
    producto_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria_id INTEGER NOT NULL,
    producto TEXT NOT NULL,
    precio TEXT NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (categoria_id)
    REFERENCES categoria(categoria_id)
);

```

* Introducimos la siguientes valores:

``` sql
-- Las categorías:


INSERT INTO [categoria] ([categoria_id], [categoria], [activa]) VALUES (1, 'auto', 1);
INSERT INTO [categoria] ([categoria_id], [categoria], [activa]) VALUES (2, 'bicicleta', 1);
INSERT INTO [categoria] ([categoria_id], [categoria], [activa]) VALUES (3, 'avion', 1);

-- Los productos

INSERT INTO [producto] ([producto_id], [categoria_id], [producto], [precio], [descripcion]) VALUES (1, 1, 'ford', '12546', 'fdsfd');
INSERT INTO [producto] ([producto_id], [categoria_id], [producto], [precio], [descripcion]) VALUES (2, 1, 'jeep', '87945', 'asdfds');
INSERT INTO [producto] ([producto_id], [categoria_id], [producto], [precio], [descripcion]) VALUES (3, 1, 'spark', '47444', 'asdfds');
INSERT INTO [producto] ([producto_id], [categoria_id], [producto], [precio], [descripcion]) VALUES (4, 2, 'Una rueda', '451', 'asdfd');
INSERT INTO [producto] ([producto_id], [categoria_id], [producto], [precio], [descripcion]) VALUES (5, 2, 'Dos Ruedas', '4512', 'asdfsd');
INSERT INTO [producto] ([producto_id], [categoria_id], [producto], [precio], [descripcion]) VALUES (6, 3, 'de combate', '41511', 'asdfds');
INSERT INTO [producto] ([producto_id], [categoria_id], [producto], [precio], [descripcion]) VALUES (7, 3, 'comercial', '5454', 'asdfsd');


La consulta:


``` sql


SELECT producto.*, categoria.* 
FROM   producto INNER JOIN categoria USING(categoria_id)

-- Da como resultado:

producto_id  categoria_id  producto    precio  descripcion  categoria_id  categoria  activa
-----------  ------------  ----------  ------  -----------  ------------  ---------  ------
1            1             ford        12546   fdsfd        1             auto       1     
2            1             jeep        87945   asdfds       1             auto       1     
3            1             spark       47444   asdfds       1             auto       1     
4            2             Una rueda   451     asdfd        2             bicicleta  1     
5            2             Dos Ruedas  4512    asdfsd       2             bicicleta  1     
6            3             de combate  41511   asdfds       3             avion      1     
7            3             comercial   5454    asdfsd       3             avion      1    

```

## Análisis 2: 

* Con **SELECT producto.*, categoria.\*  estamos seleccionando todos los campos de la tabla producto y todos los campos de la tabla categoria. Mientras que con FROM producto INNER JOIN categoria USING(categoria_id), estamos diciendo que: desde la tabla producto unida internamente a la tabla categoria (FROM producto INNER JOIN categoria) utilizando el campo categoria_id (USING(categoria_id)).



-

# Tabla de tarea:

```sql
--Tengo dos tablas relacionadas a través de otra (muchos a muchos)

--Este es un extracto del esquema:

CREATE TABLE user (
    user_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    email    TEXT    NOT NULL UNIQUE
);

CREATE TABLE alias (
    alias_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    address  TEXT    NOT NULL UNIQUE
);

CREATE TABLE alias_member (
    alias_id INTEGER NOT NULL,
    user_id  INTEGER NOT NULL,
    PRIMARY KEY(alias_id, user_id),
    FOREIGN KEY(alias_id) REFERENCES alias(alias_id) ON DELETE CASCADE,
    FOREIGN KEY(user_id)  REFERENCES user(user_id)   ON DELETE CASCADE
);

-- ¿Qué hace esto y por qué?

SELECT
    email
FROM
    alias_member 
INNER JOIN
    user
  ON alias_member.user_id = user.user_id
INNER JOIN
    alias 
  ON alias_member.alias_id = alias.alias_id
WHERE address='foo@domain.tld';

```