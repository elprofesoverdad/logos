Para crear un script bash que permita enviar el curso 1 de tu carpeta cursos a un cliente solo cuando haya pagado por él, necesitarás seguir los siguientes pasos:

Crear una carpeta dentro de la carpeta "CURSOS" de tu máquina con el nombre del cliente que haya pagado por el curso 1.
Agregar la carpeta compartida "CURSOS" en Syncthing en la computadora del cliente y agregar la "compartición selectiva" para la carpeta del curso que deseas compartir con el cliente. La carpeta del curso debe aparecer dentro de la ruta /home/nombre_cliente/tron/CURSOS en la computadora del cliente.
Crear un archivo bash que se encargue de enviar el curso 1 a la carpeta "CURSOS" del cliente que haya pagado por él. Este archivo debe contener los siguientes comandos:
#!/bin/bash
# Definir la ruta de la carpeta "CURSOS" en tu máquina
ruta_cursos="/home/tu_usuario/tron/CURSOS"

# Definir la ruta de la carpeta "CURSOS" en la máquina del cliente
ruta_cliente="/home/nombre_cliente/tron/CURSOS"

# Definir el ID del dispositivo del cliente en Syncthing
id_cliente="ID_del_cliente_en_Syncthing"

# Verificar si el cliente ha pagado por el curso 1
if [ cliente_ha_pagado_por_curso_1 ]; then
  # Copiar el curso 1 a la carpeta del cliente en Syncthing
  cp $ruta_cursos/curso_1 $ruta_cliente/curso_1
  # Agregar la carpeta del curso 1 a la compartición selectiva del cliente en Syncthing
  curl -X POST -H "X-API-Key: API_KEY_de_Syncthing" "http://localhost:8384/rest/db/completion?folder=$ruta_cliente/curso_1&device=$id_cliente"
fi




Sí, es cierto que el script que te propuse anteriormente no incluye una salida de progreso que permita saber cuándo finaliza la transferencia de Syncthing. Para solucionar esto, puedes agregar un bucle que verifique el estado de la transferencia cada cierto tiempo y muestre una salida de progreso numérica.

Aquí te dejo una versión modificada del script que incluye esta funcionalidad:

#!/bin/bash

# Ruta de la carpeta CURSOS en tu computadora
fuente="/home/tu_usuario/CURSOS/curso_1"

# ID del cliente
id_cliente="1234"

# Ruta de la carpeta CURSOS en la computadora del cliente
ruta_cliente="/home/nombre_cliente/tron/CURSOS/curso_1"

# Inicio de la transferencia
echo "Iniciando transferencia de $fuente a $ruta_cliente en el dispositivo $id_cliente"

# Comando de transferencia
comando="curl -X POST -H \"X-API-Key: API_KEY_de_Syncthing\" \"http://localhost:8384/rest/db/completion?folder=$ruta_cliente&device=$id_cliente\" --data-binary @-"

# Transferencia de archivos
rsync -r --progress --exclude='.DS_Store' "$fuente/" -e "$comando" "nombre_de_tu_dispositivo:/tmp/" > /dev/null

# Verificación de estado de la transferencia
while true; do
    estado=$(curl -s -X GET -H "X-API-Key: API_KEY_de_Syncthing" "http://localhost:8384/rest/system/status" | jq -r '.connections[].state' | grep -o 'syncing\|idle')
    if [ "$estado" == "idle" ]; then
        echo "Transferencia finalizada"
        break
    else
        progreso=$(curl -s -X GET -H "X-API-Key: API_KEY_de_Syncthing" "http://localhost:8384/rest/system/status" | jq -r '.connections[].progress' | awk '{s+=$1} END {print int(s/NR)}')
        echo "Progreso: $progreso%"
    fi
    sleep 5
done




#!/bin/bash

# Definir las variables necesarias
HOME_SYNC_ID="id_sync_de_home"
CLIENT_1_SYNC_ID="id_sync_cliente_1"
COURSE_NAME="curso 1"

# Sincronizar la carpeta del curso 1 de home con la carpeta CURSOS del cliente 1
syncthing-cli -apikey="tu_api_key" -endpoint="http://localhost:8384" \
    --folder "$COURSE_NAME" \
    --device "$CLIENT_1_SYNC_ID" \
    --send-only \
    --ignore-permissions \
    --path "/home/elias/CURSOS/$COURSE_NAME" \
    --remote-path "/home/cliente1/CURSOS/$COURSE_NAME"

# Asegurarse de que la sincronización se haya completado correctamente
if [ $? -eq 0 ]; then
    echo "La sincronización del curso $COURSE_NAME con el cliente 1 se ha completado correctamente."
else
    echo "Se ha producido un error al sincronizar el curso $COURSE_NAME con el cliente 1."
fi



Sí, para enviar tanto los cursos como la actualización de la aplicación, Elías debería configurar la carpeta "tron" en lugar de la carpeta "CURSOS" en los clientes.

Para enviar un curso a un cliente determinado, Elías podría utilizar el siguiente script en bash:

#!/bin/bash
# Configuración
API_KEY="tu_api_key"
ENDPOINT="http://localhost:8384"
CLIENT_SYNC_ID="id_del_cliente"
COURSE_NAME="nombre_del_curso"

# Enviar curso
syncthing-cli -apikey="$API_KEY" -endpoint="$ENDPOINT" -folder="nombre_de_la_carpeta_en_tron" -device-id="$CLIENT_SYNC_ID" -send-only "$COURSE_NAME"
En este script, se utiliza la herramienta syncthing-cli para enviar el curso a un cliente determinado. El script requiere que se configuren la API_KEY y el ENDPOINT de Syncthing, así como el CLIENT_SYNC_ID y el COURSE_NAME correspondientes al cliente y al curso que se desea enviar.

Para sincronizar la aplicación, Elías podría utilizar el siguiente script en bash:

#!/bin/bash
# Configuración
API_KEY="tu_api_key"
ENDPOINT="http://localhost:8384"
CLIENT_SYNC_ID="id_del_cliente"

# Sincronizar carpeta tron
syncthing-cli -apikey="$API_KEY" -endpoint="$ENDPOINT" -folder="nombre_de_la_carpeta_en_tron" -device-id="$CLIENT_SYNC_ID" -force-rescan
En este script, se utiliza la herramienta syncthing-cli para sincronizar la carpeta "tron" en el cliente. El script requiere que se configuren la API_KEY y el ENDPOINT de Syncthing, así como el CLIENT_SYNC_ID correspondiente al cliente al que se desea sincronizar la carpeta "tron". El parámetro -force-rescan fuerza a Syncthing a escanear y sincronizar la carpeta "tron" en el cliente.


En cuanto al script para borrar una carpeta enviada por error, aquí te proporciono un ejemplo:

#!/bin/bash
# Configuración
API_KEY="tu_api_key"
ENDPOINT="http://localhost:8384"
CLIENT_1_SYNC_ID="id_del_cliente_1"
COURSE_NAME="nombre_del_curso"

# Eliminar carpeta del cliente
curl -X DELETE -H "X-API-Key: $API_KEY" "$ENDPOINT/rest/db/$CLIENT_1_SYNC_ID/$COURSE_NAME"