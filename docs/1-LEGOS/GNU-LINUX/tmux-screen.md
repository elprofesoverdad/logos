# screen linux bash manualito

Aquí tienes un manualito resumido para utilizar los comandos más utilizados de screen:

## Chuletario

* Ver todas las sesiones

```shell
echo $(screen -ls | grep -oP '\d+\.\w+')
```

* Cerrar todas las sesiones abiertas

```shell
screen -ls | grep -oP '\d+\.\w+' | xargs -I {} screen -X -S {} quit
```

## Caso practico

1. Primero, debes conectarte al servidor remoto utilizando SSH. Puedes hacerlo ejecutando el siguiente comando en tu segunda pestaña:
   
   ```
   ssh usuario@servidor_remoto
   ```
   
   Asegúrate de reemplazar "usuario" con tu nombre de usuario y "servidor_remoto" con la dirección IP o nombre de dominio del servidor remoto.

2. Una vez que estés conectado al servidor remoto, puedes verificar las sesiones de screen disponibles utilizando el siguiente comando:
   
   ```
   screen -ls
   ```
   
   Esto mostrará una lista de todas las sesiones de screen disponibles en el servidor remoto.

3. Busca la sesión de screen que ejecuta ngrok. En tu caso, parece que la sesión tiene el ID "3560.pts-0.dreamserver". Para unirte a esta sesión, ejecuta el siguiente comando:
   
   ```
   screen -r 3560.pts-0.dreamserver
   ```
   
   Esto te permitirá acceder a la primera pestaña que ejecuta ngrok.

4. Si la sesión de screen está adjunta y en uso, pero no puedes unirte a ella, es posible que esté siendo utilizada por otra conexión SSH. En ese caso, puedes forzar la desconexión de la sesión utilizando el siguiente comando:
   
   ```
   screen -r -d 3560.pts-0.dreamserver
   ```
   
   Esto desconectará la sesión de screen y te permitirá unirte a ella desde tu segunda pestaña.

## Manualito de Cero

1. Crear una sesión de screen con un nombre específico:
   
   ```
   screen -S nombre_sesion
   ```
   
   Este comando crea una nueva sesión de screen con el nombre especificado.

2. Ver una lista de sesiones disponibles:
   
   ```
   screen -ls
   ```
   
   Este comando muestra una lista de todas las sesiones de screen disponibles.

3. Conectarse a una sesión de screen:
   
   ```
   screen -r ID_sesion
   ```
   
   Utiliza este comando para unirte a una sesión de screen específica utilizando su ID.

4. Crear ventanas adicionales dentro de una sesión de screen:
   
   ```
   Ctrl + A, C
   ```
   
   Esta combinación de teclas crea una nueva ventana dentro de la sesión de screen actual.

5. Cambiar entre ventanas dentro de una sesión de screen:
   
   ```
   Ctrl + A, N
   ```
   
   Utiliza esta combinación de teclas para cambiar a la siguiente ventana dentro de la sesión de screen.

6. Cerrar una ventana dentro de una sesión de screen:
   
   ```
   Ctrl + A, X
   ```
   
   Esta combinación de teclas cierra la ventana actual dentro de la sesión de screen.

7. Salir de una sesión de screen sin cerrarla:
   
   ```
   Ctrl + A, D
   ```
   
   Utiliza esta combinación de teclas para salir de la sesión de screen actual sin cerrarla.

8. Crear sesiones de screen permanentes:
   
   ```
   screen -dmS nombre_sesion
   ```
   
   Este comando crea una nueva sesión de screen en segundo plano que persistirá incluso si el servidor se apaga o reinicia.

En cuanto al caso práctico que mencionaste, intentaste conectarte a la primera pestaña abierta en el servidor remoto que ejecuta un proceso ngrok. Sin embargo, parece que no hay otra sesión de screen disponible para ser retomada. Para poder unirte a la primera pestaña, debes desconectarla de la sesión actual utilizando el comando "screen -d ID_sesion". Luego, podrás unirte a ella utilizando el comando "screen -r ID_sesion".