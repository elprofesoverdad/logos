# Compilar instalar sqlite con FOREIGN_KEYS ON

Busqué esta variable pero jamás la encontré:

SQLITE_DEFAULT_FOREIGN_KEYS= <0 o 1>

no se encuentra por ninguna parte.

## Para agregar clavers foráneas a sqlite:

* Vaya a la página web de SQLite en http://www.sqlite.org/download.html y descargue el archivo sqlite_amalgation.xxxx.tar.gz más reciente, puede llamarse de otra forma, como: sqlite-autoconf-3410200.tar.gz.

> Es importante que tenga la canfiguracion de la imagen, en rojo se pueden ver los archivos install de instalación y en amarillo sqlite3.c que es el archivo que abriremos para cambiar la configuración.





![captura de pantalla de los archivos de configuración e instalación](imagenes/directorio.png)  

* Se incluye: #define SQLITE_DEFAULT_FOREIGN_KEYS 1 al principio del documento como se muestra en la imagen.



> no se debe colocar signo de igual, u otra cosa.




![captura de pantalla el cambio de variable](imagenes/concambio.png)  


* luego se compila como dice el archivo README.txt: estando dentro de la carpeta de instalación.

``` bash
SUMMARY OF HOW TO BUILD
=======================

  Unix:      ./configure; make

```
* Al sqlite se compila y el binario sqlite3 aparece dentro de esta carpeta, cuando se ingresa sqlite3 en el terminal puede que no sea este binario el que se ejecute,
para estar seguros hay que ejecutar:

``` bash

command -V sqlite3

SALIDA:

$ command -V sqlite3
sqlite3 está asociado (/home/linuxbrew/.linuxbrew/bin/sqlite3)

```

En este caso sqlite está asociado a brew, hay que manipular $PATH para usar sqlite.

yo lo que hice fue exportar la ruta a la carpeta del instalador en bash.rc
y para que el sistema no se confunda con sqlite3 renombré el binario a sqlite. 




