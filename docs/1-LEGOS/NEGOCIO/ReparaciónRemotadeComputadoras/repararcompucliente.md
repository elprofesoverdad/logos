Para conectarte a la computadora de tu cliente a través de ngrok y repararla sin que tu cliente tenga que interactuar de alguna forma, puedes seguir los siguientes pasos:

Descarga ngrok en la computadora de tu cliente y extrae el archivo.

Crea una cuenta en ngrok y obtén tu authtoken.

Crea un archivo de script en la carpeta de inicio del usuario de tu cliente. Por ejemplo, si el usuario de tu cliente se llama "cliente_n", crea el archivo en la siguiente ruta: /home/cliente_n/start_reparacion.sh

Abre el archivo de script en un editor de texto y agrega el siguiente contenido:

#!/bin/bash
ngrok authtoken <tu_authtoken_de_ngrok>
ngrok tcp 22 --region <tu_region_de_ngrok> > /dev/null &
sleep 5
ssh -o "StrictHostKeyChecking no" -o "UserKnownHostsFile=/dev/null" -p $(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' | awk -F ":" '{print $2}') usuario_remoto@localhost
Reemplaza <tu_authtoken_de_ngrok> con tu authtoken de ngrok y <tu_region_de_ngrok> con la región de ngrok que deseas utilizar.

Guarda el archivo y ciérralo.

Ejecuta el siguiente comando para darle permisos de ejecución al archivo de script:

chmod +x /home/cliente_n/start_reparacion.sh
Para que el script se ejecute automáticamente todos los días, puedes agregar una entrada en el archivo crontab del usuario de tu cliente. Para hacer esto, ejecuta el siguiente comando en la terminal:
crontab -e
Esto abrirá el archivo crontab en el editor de texto predeterminado. Agrega la siguiente línea al final del archivo:

@reboot /home/cliente_n/start_reparacion.sh
Guarda y cierra el archivo.

Con estos pasos, el script se ejecutará automáticamente cada vez que se inicie la computadora de tu cliente y se conectará a través de ngrok para que puedas reparar la computadora de tu cliente sin que tu cliente tenga que interactuar de alguna forma. El script también establecerá una conexión SSH con la computadora de tu cliente para que puedas acceder a ella y realizar las reparaciones necesarias.