# Conjunto de herramientas para control de tiempo, intervalos cronometros, temporizadores, calendarios alarmas; en linux bash.

## Sumas de tiempo:

``` bash
* Sumar al tiempo actual date: 

date -d '+1 minute' '+%a%_d %b; %I:%M %p'

* '+1 minute' agrega un minuto a la hora actual.
* '+%a%_d %b; %I:%M %p' es el formato de presentacion de la hora.

- Para la presentación solo de la hora sin la fecha:
date -d '+1 minute' '+%I:%M %p'

* minute se puede cambiar por las medidas de tiempo en ingles:
    second, day, etc.
```


## Comando at:

> Usos frecuentes de at:

Relative time: “now + 1 hour” or “now + 30 minutes”
Absolute time: “2:30 PM” or “15:30”
Date and time: “10:00 AM tomorrow” or “2023-04-01 18:00”

* Si el tiempo se especifica con 4 cifras, 00:00 at entiende horas:minutos.
* Si el tiempo se especifica con 2 cifras, 00 at entiende horas.
* Si se indica AM/PM entiende meridiem, en caso contrario, hora militar.(24 hrs)

* para falsear los segundos:

echo "sleep 5 ; COMMAND" | at now

* Usarlo en un script bash con zenity:

echo "DISPLAY=$DISPLAY zenity --info --text=\"time is up\"" | at now + 35 minutes

``` bash



echo 'notify-send "El día de trabajo ha terminado!"' | at 4:00PM 

echo 'notify-send "Hora del té!"' | at now + 3 minutes 


* Necesita agregar la variable DISPLAY al entorno para trabajar con ato cron. Escribe esto: 

echo 'export DISPLAY=:0; notify-send "Enjoy!"' | at 04:00 PM 

* Un crontab para la notificación diaria a las 4 p. m. se vería así:

0 16 * * * /home/username/notify.sh


```