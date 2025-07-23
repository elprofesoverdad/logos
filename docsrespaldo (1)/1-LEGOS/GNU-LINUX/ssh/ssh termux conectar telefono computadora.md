# SSH en tu laptop y en Termux en tu teléfono para conectarte desde el teléfono a la laptop, sigue estos pasos:

En tu laptop:

1. Verifica si ya tienes instalado OpenSSH Server. Puedes hacerlo ejecutando el siguiente comando en la terminal:
   
   ```
   sudo apt-get install openssh-server
   ```

2. Si no tienes instalado OpenSSH Server, instálalo utilizando el comando anterior.

3. Una vez instalado, abre el archivo de configuración de SSH en tu laptop. Puedes hacerlo con el siguiente comando:
   
   ```
   sudo nano /etc/ssh/sshd_config
   ```

4. Dentro del archivo de configuración, asegúrate de que la línea `Port` esté descomentada y establece el número de puerto que deseas utilizar para la conexión SSH. Por ejemplo, puedes usar el puerto 22:
   
   ```
   Port 22
   ```

5. También puedes configurar otras opciones según tus necesidades, como la autenticación de clave pública o restricciones de acceso.

6. Guarda los cambios y cierra el archivo de configuración.

7. Reinicia el servicio SSH para aplicar los cambios:
   
   ```
   sudo service ssh restart
   ```

8. Asegúrate de que el firewall de tu laptop permita las conexiones SSH. Puedes hacerlo permitiendo el tráfico en el puerto que especificaste en el paso 4. La forma exacta de hacer esto depende de la herramienta de firewall que estés utilizando en tu laptop.

En Termux en tu teléfono:

1. Instala la aplicación Termux desde la tienda de aplicaciones de Android.

2. Abre Termux en tu teléfono.

3. Instala OpenSSH en Termux ejecutando el siguiente comando:
   
   ```
   pkg install openssh
   ```

4. Una vez instalado, puedes conectarte a tu laptop utilizando el siguiente comando:
   
   ```
   ssh [usuario]@[dirección_ip_laptop] -p [puerto]
   ```
   
   Reemplaza `[usuario]` con tu nombre de usuario en la laptop, `[dirección_ip_laptop]` con la dirección IP de tu laptop y `[puerto]` con el número de puerto que configuraste en el paso 4 de la sección anterior.

5. Si es la primera vez que te conectas desde Termux a tu laptop, se te pedirá que confirmes la autenticidad de la conexión. Acepta la confirmación y proporciona la contraseña de tu usuario en la laptop cuando se te solicite.

Con estos pasos, deberías poder conectarte desde Termux en tu teléfono a tu laptop a través de SSH. Recuerda que es importante configurar adecuadamente la seguridad y el acceso en tu laptop, así como proteger tus claves privadas y contraseñas.

Ten en cuenta que la configuración exacta puede variar según la distribución de Linux que estés utilizando en tu laptop y la versión de Termux en tu teléfono. Asegúrate de consultar la documentación oficial correspondiente para obtener instrucciones más detalladas y actualizadas.

## SSH Verificación del host ha cambiado desde la última vez que te conectaste

Si estás recibiendo un mensaje de "verificación del host ha cambiado" en Termux, significa que la clave de host del servidor SSH ha cambiado desde la última vez que te conectaste. Esto puede ocurrir si has reinstalado el servidor SSH o si estás intentando conectarte a un servidor diferente.

Para solucionar este problema en Termux, puedes seguir estos pasos:

1. Asegúrate de que estás intentando conectarte al servidor SSH correcto y que no hayas realizado cambios en la configuración del servidor.

2. Si estás seguro de que el servidor es el correcto, puedes eliminar la clave de host antigua almacenada en Termux ejecutando el siguiente comando:
   
   ```
   ssh-keygen -R <dirección IP o nombre de host>
   ```
   
   Reemplaza `<dirección IP o nombre de host>` con la dirección IP o el nombre de host del servidor SSH al que estás intentando conectarte.

3. Después de ejecutar el comando anterior, intenta conectarte nuevamente al servidor SSH. Termux debería mostrar un mensaje solicitando que confirmes la nueva clave de host. Verifica que la clave de host coincida con la esperada y responde "yes" para confirmar.

4. Si sigues teniendo problemas de verificación del host, es posible que haya un problema de seguridad en la conexión. En este caso, es recomendable contactar al administrador del servidor SSH para obtener asistencia adicional.

Recuerda que es importante asegurarte de que estás conectándote al servidor correcto y de confiar en la nueva clave de host antes de confirmarla.
