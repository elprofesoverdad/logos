# Syncthing manualito

# Syncthing Instalar en Ubuntu sin interfaz gráfica, debes seguir los siguientes pasos:

1. Agrega la clave GPG y el repositorio de Syncthing a tu sistema:

``` bash
curl -s https://syncthing.net/release-key.txt | sudo apt-key add -
echo "deb https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
```
2. Actualiza la lista de paquetes e instala Syncthing:

``` bash
sudo apt-get update
sudo apt-get install syncthing
```


## Script al inicio de XFCE

* Para ejecutar un script al inicio de sesión de XFCE, puedes agregarlo a la lista de aplicaciones de inicio. Para hacer esto, sigue los siguientes pasos:

1. Abre el menú de aplicaciones y busca "Configuración de sesión y arranque".
2. En la pestaña "Aplicaciones de inicio", haz clic en el botón "Añadir".
3. En el cuadro de diálogo "Añadir aplicación de inicio", ingresa un nombre para el script y la ruta completa del archivo de script que deseas ejecutar.
4. Haz clic en "Añadir" para agregar la aplicación de inicio.


## Script de Inicio y supervision de Servicio

``` bash

#!/bin/bash


# Iniciar el servicio Syncthing
syncthing &

# Esperar a que el servicio se inicie
service_started=false
for i in {1..10}; do
    if curl -s -f http://localhost:8384 > /dev/null; then
        service_started=true
        break
    fi
    sleep 1
done

# Comprobar si el servicio está activo
if $service_started; then
    # Mostrar notificación de sincronización activa
    notify-send "Sincronización activa" -t 30000
else
    # Mostrar alerta de error
    zenity --error --text="No se pudo iniciar el servicio Syncthing"
fi
```




## Compartición selectiva de Syncthing Solucion Final.

* Con la compartición selectiva, puedes compartir solo las carpetas específicas que contienen los cursos a los clientes que han pagado por ellos. De esta manera, no tendrás que crear una carpeta para cada cliente y podrás tener todos los cursos en una sola carpeta en cada destino.

* Para hacer esto, primero debes crear una carpeta principal llamada "CURSOS" en tu dispositivo y agregar todas las subcarpetas de los cursos dentro de ella. Luego, en Syncthing, selecciona la opción de "compartición selectiva" para cada subcarpeta y elige los clientes específicos con los que deseas compartir esa subcarpeta.

* De esta manera, cada cliente solo tendrá acceso a las subcarpetas de los cursos que han pagado y no verán los demás cursos en la carpeta principal "CURSOS". Además, podrás agregar nuevos cursos a la carpeta principal sin tener que crear nuevas carpetas para cada cliente.



## Comparticion sencilla.

Ahora, para configurar la sincronización de archivos entre las computadoras de tus amigos y la tuya, debes seguir los siguientes pasos:

* En la computadora de tus amigos, ejecuta el siguiente comando para iniciar Syncthing:
syncthing
* Accede a la interfaz web de Syncthing desde tu navegador web ingresando la dirección http://localhost:8384.

* En la interfaz web de Syncthing, haz clic en "Agregar dispositivo" y luego ingresa el ID de dispositivo de tu computadora.

* En la sección "Compartir", haz clic en "Agregar carpeta" y luego selecciona la carpeta /home/$usuario/tron en la computadora de tus amigos. Configura la carpeta para recibir archivos únicamente.

* En tu computadora, repite los pasos 1 y 2 para iniciar Syncthing y acceder a la interfaz web.

* En la interfaz web de Syncthing, haz clic en "Agregar dispositivo" y luego ingresa el ID de dispositivo de la computadora de tus amigos.

* En la sección "Compartir", haz clic en "Agregar carpeta" y luego selecciona la carpeta existente con importantes documentos en tu computadora. Configura la carpeta para enviar archivos únicamente.





