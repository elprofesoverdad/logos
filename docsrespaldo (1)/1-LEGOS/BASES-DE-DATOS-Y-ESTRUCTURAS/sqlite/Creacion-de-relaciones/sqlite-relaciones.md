# Sqlite crear tablas con relaciones y consultas con relaciones:

!!! warning "Tablas Intermedias"
  En la creación de tablas intermedias, muchos a muchos, los campos de las claves foráneas no son únicos, puesto que se repiten.

# Aplicación Marcadores Video:

## Este es el diagrama de entidad relación de db Marcadores de Video:

![entidad relacion marcadores video](imagenes/erMarcadoresVideo.png)

## Al terminar la depuración quedó asi:

![entidad relacion mejorado](imagenes/ermejorado.png)

# ¿Cuándo usar NoT NULL, ON UPDATE CASCADE, ON DELETE ?

## Análisis:


* A los registros de la tabla cat-video  los llamaremos asociación categoría video, y así para cada tabla de asociación que rompe relaciones muchos a muchos (a esta tabla de asociación la llamaremos tabla intermedia).

* ¿Se puede agregar una asociación (registro) en cat_video, sin que halla un registro correspondiente en la tabla video?, la respuesta es no, entonces en la tabla cat_video el campo id_video debe ser NOT NULL, y así se analizan todos los campos de las tablas intermedias.

* Para DELETE y UPDATE ON CASCADE, se analiza de la tabla n a la tabla 1: ¿Puede haber una asociación en la tabla cat_video sin que haya un video correspondiente en la tabla video? la respuesta es nó; y como también, si cambia el id de video en 1 (tabla videos), también debe cambiar el correspondiente id en la asociación (en la tabla cat_videos), entonces las claves foráneas en la tabla cat_videos, deben ser las dos ON DELETE y ON UPDATE; de esta manera si se borra o se actualiza una categoría (tabla 1), se borrará o se actualizará una asociación en la tabla cat-videos (tabla n). De esta manera se analizan las demás tablas.

## Sintaxis para las relaciones:

``` sql
/*Para las tablas Intermedias:*/

CREATE TABLE cat-videos(
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  id_video NOT NULL INTEGER REFERENCES videos(id) ON UPDATE CASCADE ON DELETE CASCADE, 
  id_categoria NOT NULL INTEGER REFERENCES categorias(id) ON UPDATE CASCADE ON DELETE CASCADE
);

```
# Código Completo para Db Videos Marcadores:

``` sql

--
-- Archivo generado con SQLiteStudio v3.4.3 el lun. abr. 3 19:39:31 2023
--
-- Codificación de texto usada: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabla: cat_videos
CREATE TABLE cat_videos(
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  id_videos  INTEGER NOT NULL REFERENCES videos(id) ON UPDATE CASCADE ON DELETE CASCADE, 
  id_cat  INTEGER NOT NULL REFERENCES categorias(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Tabla: categorias
CREATE TABLE categorias (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_categoria VARCHAR (20) NOT NULL);

-- Tabla: cla_cat
CREATE TABLE cla_cat(
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  id_clase  INTEGER NOT NULL REFERENCES clase(id) ON UPDATE CASCADE ON DELETE CASCADE, 
  id_cat  INTEGER NOT NULL REFERENCES categorias(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Tabla: clase
CREATE TABLE [clase] ( 
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  [nombre_clase] VARCHAR(20),
  [id_curso] INTEGER INTEGER NOT NULL REFERENCES curso(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Tabla: curso
CREATE TABLE [curso] ( 
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  [nombre_curso] VARCHAR(20)
);

-- Tabla: marc_cat
CREATE TABLE marc_cat (id INTEGER PRIMARY KEY AUTOINCREMENT, id_marcador INTEGER REFERENCES marcadores (id) ON DELETE CASCADE ON UPDATE CASCADE UNIQUE NOT NULL, id_categoria INTEGER REFERENCES categorias (id) ON DELETE CASCADE ON UPDATE CASCADE UNIQUE NOT NULL);

-- Tabla: marcadores
CREATE TABLE [marcadores] ( 
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  [nombre] VARCHAR(250) NOT NULL,
  [tiempo] VARCHAR(250) NOT NULL,
  [id_video] INT NOT NULL,
  CONSTRAINT [Fk_marcador_video] FOREIGN KEY ([id_video]) REFERENCES [videos] ([id]) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tabla: video_clase
CREATE TABLE video_clase(
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  id_video  INTEGER NOT NULL REFERENCES videos(id) ON UPDATE CASCADE ON DELETE CASCADE, 
  id_clase  INTEGER NOT NULL REFERENCES clase(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Tabla: videos
CREATE TABLE [videos] ( 
  [id] INTEGER PRIMARY KEY AUTOINCREMENT,
  [video_ruta] VARCHAR(20),
  [nombre_video] VARCHAR(20)
);

-- Índice: cateindex
CREATE INDEX cateindex ON marc_cat (id_categoria);

-- Índice: indexcat
CREATE INDEX indexcat 
ON video_clase (id_clase);

-- Índice: indexcccla_cat
CREATE INDEX indexcccla_cat 
ON cla_cat (id_cat);

-- Índice: indexccclase
CREATE INDEX indexccclase
ON cla_cat (id_clase);

-- Índice: indexcurso
CREATE INDEX indexcurso 
ON clase (id_curso);

-- Índice: indexcvcat
CREATE INDEX indexcvcat 
ON cat_videos (id_cat);

-- Índice: indexcvvideos
CREATE INDEX indexcvvideos 
ON cat_videos (id_videos);

-- Índice: indexvcvideos
CREATE INDEX indexvcvideos 
ON video_clase (id_video);

-- Índice: marcaindex
CREATE INDEX marcaindex ON marc_cat (id_marcador);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

```

## Lógica de las relaciones:

Observando el siguiente código:

``` sql

CREATE TABLE categoria( 
    categoria_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    categoria VARCHAR(25) NOT NULL, 
    activa BOOL 
) ENGINE=InnoDB; 

CREATE TABLE producto( 
    producto_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    categoria_id INT(11) NOT NULL,
    producto VARCHAR(255) NOT NULL,
    precio DECIMAL(7, 2) NOT NULL,
    descripcion BLOB,
    FOREIGN KEY (categoria_id)
    REFERENCES categoria(categoria_id)
) ENGINE=InnoDB;

```

No siempre una categoría está en una tabla hija, o es padre de una tabla intermedia, en el ejemplo anterior de marcadores de video, las categorías son una relación muchos a muchos con los videos, en este ejemplo, una categoría tiene muchos productos, pero muchos productos no tienen muchas categorías, cada prosucto tienen solo una categoría, entonces la relación de la tabla categoría a producto es 1-n o uno a muchos.




# TEORÍA:



## Definiciones:



* **Tabla Principal:** Aquella que es referenciada en la secundaria, en ella no se
encuantran claves foráneas, la clave foranea de la tabla secundaria se asocia comunmente
a la clave principal de la tabla principal.

* **Tabla secundaria:** En ella se hace la restricción o se escribe la clave foránea hay que **indexar la clave foránea** y definir las funciones on delete y on update en esta
tabla. 

```sql
- Crear base de datos:
sqlite3 disco.db

> Dentro del shell de sqlite:

- abrir una base de datos
.open disco.db

-Mostrar las tablas:
.tables disco.db

```


## Activar soporte de claves foráneas:

``` sql

sqlite> PRAGMA foreign_keys;
0
sqlite> PRAGMA foreign_keys = ON;
sqlite> PRAGMA foreign_keys;
1
sqlite> PRAGMA foreign_keys = OFF;
sqlite> PRAGMA foreign_keys;
0
```

# Creación de la tabla principal y de  secundaria, con sus claves foráneas y on update, on delete con un ejemplo de disco - artistas y tracks opistas (canciones):



## Creando la tabla artistas:

``` sql

CREATE TABLE artist(
  artistid    INTEGER PRIMARY KEY, 
  artistname  TEXT
);

```

## Creando la tabla pistas:

``` sql
# "REFERENCES artist" enlaza automaticamente a la clave principal en artistas.

CREATE TABLE track(
  trackid     INTEGER,
  trackname   TEXT, 
  trackartist INTEGER REFERENCES artist ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE INDEX trackindex ON track(trackartist)  ; 


------------------------------------------------
* Otra forma de crear pistas:

CREATE TABLE track(
  trackid     INTEGER, 
  trackname   TEXT, 
  trackartist INTEGER,
  FOREIGN KEY(trackartist) REFERENCES artist(artistid) ON UPDATE CASCADE ON DELETE CASCADE
  CREATE INDEX trackindex ON track(trackartist);
);

```




## Insertando artistas y pistas, cada uno a su tabla: 

``` sql
INSERT INTO artist (artistid, artistname) VALUES (1, 'Dean Martin  ');
INSERT INTO artist (artistid, artistname) VALUES (2, 'Frank Sinatra ');

INSERT INTO track (trackid, trackname, trackartist) VALUES (11, 'That''s Amore ', 1);
INSERT INTO track (trackid, trackname, trackartist) VALUES (12, 'Christmas Blues ', 1);
INSERT INTO track (trackid, trackname, trackartist) VALUES (13, 'My Way ', 2);

```

## Prueba de referencias:

``` sql
Este comando produce error:

INSERT INTO track VALUES(14, 'Mr. Bojangles', 3);

porque no existe artista con id=3

Este no produce error a menos que se configure NOT NULL la clave foránea
en la tabla hija o secundaria.

INSERT INTO track VALUES(14, 'Mr. Bojangles', NULL);
```



# Explicaciones:



## Crear Referencias directamente a la clave principal de la tabla padre (principal).
## Crear índice para la clave foránea.

``` sql

CREATE TABLE track(
  trackid     INTEGER,
  trackname   TEXT, 
  trackartist INTEGER REFERENCES artist
);
CREATE INDEX trackindex ON track(trackartist); 
```



## On update, on delete:


Permite actualizar la tabla principal y que los cambios se realicen automáticamente
en la tabla secundaria.


``` sql
-- Esquema de la base de datos 
CREATE TABLE artista( 
  artistid INTEGER PRIMARY KEY, 
  artistname TEXT 
); 
CREATE TABLE track( 
  trackid INTEGER, 
  trackname TEXT, 
  trackartist INTEGER REFERENCES artista(artistid) ON UPDATE CASCADE 
); 

```

La acción **ON DELETE y ON UPDATE**  asociada con cada clave externa en una base de datos SQLite es una de "NO ACTION", "RESTRICT", "SET NULL", "SET DEFAULT" o "CASCADE". Si una acción no se especifica explícitamente, el valor predeterminado es "SIN ACCIÓN".

* **SIN ACCIÓN NO ACTION** : configurar "SIN ACCIÓN" significa simplemente eso: cuando se modifica o elimina una clave principal de la base de datos, no se realiza ninguna acción especial.

* **RESTRINGIR RESTRICT:** La acción "RESTRINGIR" significa que la aplicación tiene prohibido eliminar (para  ON DELETE RESTRICT) o modificar (para ON UPDATE RESTRICT) una clave principal cuando existen una o más claves secundarias asignadas a ella. La diferencia entre el efecto de una acción RESTRINGIR y la aplicación normal de una restricción de clave externa es que el procesamiento de la acción RESTRINGIR ocurre tan pronto como se actualiza el campo, no al final de la declaración actual como lo haría con una restricción inmediata, o al final de la transacción actual como lo haría con una restricción diferida. Incluso si la restricción de clave externa a la que está asociada se difiere, la configuración de una acción RESTRICT hace que SQLite devuelva un error inmediatamente si se elimina o modifica una clave principal con claves secundarias dependientes.

* **SET NULL:** si la acción configurada es "SET NULL", entonces cuando se elimina una clave principal (para ON DELETE SET NULL) o se modifica (para ON UPDATE SET NULL), las columnas de clave secundaria de todas las filas en la tabla secundaria que se asignó a la clave principal se configuran para contener valores SQL NULL.

* **SET DEFAULT:** Las acciones "SET DEFAULT" son similares a "SET NULL", excepto que cada una de las columnas clave secundarias está configurada para contener el valor predeterminado de la columna en lugar de NULL. Consulte la documentación CREATE TABLE para obtener detalles sobre cómo se asignan los valores predeterminados a las columnas de la tabla.

* **CASCADA CASCADE** : una acción "CASCADA" propaga la operación de eliminación o actualización en la clave principal a cada clave secundaria dependiente. Para una acción "ON DELETE CASCADE", esto significa que también se elimina cada fila de la tabla secundaria que estaba asociada con la fila principal eliminada. Para una acción "ON UPDATE CASCADE", significa que los valores almacenados en cada clave secundaria dependiente se modifican para que coincidan con los nuevos valores de clave principal.


## Claves foráneas para campos compuestos:

``` sql
CREATE TABLE album(
  albumartist TEXT,
  albumname TEXT,
  albumcover BINARY,
  PRIMARY KEY(albumartist, albumname)
);

CREATE TABLE song(
  songid     INTEGER,
  songartist TEXT,
  songalbum TEXT,
  songname   TEXT,
  FOREIGN KEY(songartist, songalbum) REFERENCES album(albumartist, albumname)
);

```

