# Manual Mysql

## Cambio de contraseña de root:
``` sql
mysql -u root -p
mysql> use mysql;



## GEstion de db
``` sql
* crear base de datos:
    CREATE DATABASE MYDATABASE;

* Selecciona la base de datos
    SHOW DATABASES;
    USE MYDATABASE;

* Crea las tablas y sus campos

CREATE TABLE `EVENTS`(

    `ID` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,

    `NAME` VARCHAR(50),

    `STARTDATE` DATETIME,

    `ENDDATE` DATETIME

);

* Genera las relaciones entre tablas:

Ahora generamos una tabla que esté relacionada con la tabla creada anteriormente. 
Para eso usamos la línea para crear tablas agregando una columna/campo que hace referencia
a la columna de identificador de la anterior.

CREATE TABLE `TICKETS` (

  `ID` INT(11),

  `PRICE` DECIMAL(5,2),

  `EVENTID` INT

);

* Inserta los datos: 

INSERT INTO `EVENTS` (`ID`, `NAME`, `STARTDATE`, `ENDDATE`) VALUES

INSERT INTO `TICKETS` (`ID`, `PRICE`, `EVENTID`) VALUES

(20, 250.00, 1);

(1, 'EVENTO PRUEBA', '2022-05-16 10:07:24', '2022-12-31 19:45:58');

```
