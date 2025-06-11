# cambiar el logo de inicio de sesión en Ubuntu con XFCE, puedes seguir los siguientes pasos:

* Descarga la imagen que deseas utilizar como nuevo logo de inicio de sesión. Asegúrate de que tenga un tamaño adecuado para la resolución de tu pantalla.

* Abre el terminal y escribe el siguiente comando para copiar la imagen a la carpeta de temas de inicio de sesión de XFCE:

sudo cp /ruta/de/la/imagen /usr/share/xfce4/backdrops/
Reemplaza "/ruta/de/la/imagen" con la ruta de la imagen que descargaste.

* Ahora, necesitas editar el archivo de configuración de inicio de sesión de XFCE para indicar que deseas utilizar la nueva imagen. Para ello, escribe el siguiente comando en el terminal:

sudo mousepad /etc/lightdm/lightdm-gtk-greeter.conf
Esto abrirá el archivo de configuración en el editor de texto Mousepad.

* Busca la línea que comienza con "background=". Debería verse así:

background=/usr/share/backgrounds/warty-final-ubuntu.png
Reemplaza la ruta de la imagen con la ruta de la imagen que copiaste anteriormente. Debería verse así:

background=/usr/share/xfce4/backdrops/nombre_de_la_imagen.jpg
Reemplaza "nombre_de_la_imagen.jpg" con el nombre de la imagen que copiaste anteriormente.

* Guarda el archivo y cierra Mousepad.

* Reinicia tu computadora y deberías ver la nueva imagen de inicio de sesión.