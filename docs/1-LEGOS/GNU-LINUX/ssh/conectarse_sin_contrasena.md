# Conectarse a ssh sin contraseña

Sí, existe un modo para conectarte usando SSH sin tener que ingresar la contraseña cada vez. Se llama autenticación por clave pública. Funciona generando un par de claves (pública y privada) en tu máquina y configurando el servidor remoto para que autorice conexiones con tu clave pública.

Los pasos serían:

Genera una pareja de claves en tu máquina local con el comando:
ssh-keygen

Copia tu clave pública al servidor remoto con:
ssh-copy-id tron@172.16.141

Esto agregará tu clave pública al archivo ~/.ssh/authorized_keys en el servidor remoto.

Luego cuando te conectes usando SSH, ya no tendrás que ingresar la contraseña. Por ejemplo:

kitty ssh tron@172.16.141

Nota: Para una conexión realmente sin contraseña, necesitarás poner una contraseña en blanco cuando generes tus claves SSH. De lo contrario, aún tendrás que ingresar la contraseña de tu clave privada local cada vez que te conectes.