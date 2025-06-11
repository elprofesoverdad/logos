



# syncthing reenvvio de puertos

Pasos claros para redirigir Syncthing desde la computadora remota a la computadora local:

1. En la computadora remota (172.16.0.124), asegúrate de tener Syncthing instalado y funcionando correctamente.

2. Abre una terminal en la computadora remota y ejecuta el siguiente comando para iniciar Syncthing:
   
   ```
   syncthing
   ```
   
   Esto iniciará el servidor Syncthing en la computadora remota.

3. En tu computadora local (172.16.0.217), abre una terminal y ejecuta el siguiente comando para establecer un túnel SSH hacia la computadora remota:
   
   ```
   ssh -L 9090:localhost:8384 daniel@172.16.0.124
   ```
   
   Esto creará un túnel SSH que redirige el puerto 8384 de la computadora remota al puerto 9090 de tu computadora local.

4. Ahora, en tu navegador web en la computadora local, ve a la siguiente dirección:
   
   ```
   http://localhost:9090
   ```
   
   Esto te llevará a la interfaz de Syncthing en la computadora remota, pero redirigida a través del túnel SSH hacia tu computadora local.

De esta manera, podrás acceder y controlar Syncthing en la computadora remota desde tu computadora local a través del túnel SSH.

Espero que estos pasos sean más claros y te ayuden a lograr tu objetivo. Si tienes alguna otra pregunta, no dudes en hacerla.
