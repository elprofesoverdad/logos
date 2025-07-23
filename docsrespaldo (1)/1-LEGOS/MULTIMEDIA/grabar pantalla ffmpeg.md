# Para grabar la pantalla de tu laptop en Linux

¡Hola! Para grabar la pantalla de tu laptop en Linux de manera nativa desde la consola, puedes utilizar la herramienta "ffmpeg". Aquí te dejo los pasos para grabar la pantalla y el audio:

1. Instalar ffmpeg: Si no lo tienes instalado, puedes hacerlo en la mayoría de las distribuciones Linux ejecutando el siguiente comando en la terminal:
   
   ```bash
   sudo apt install ffmpeg
   ```

2. Grabar la pantalla con audio: Para grabar la pantalla con audio, puedes usar el siguiente comando en la terminal:
   
   ```bash
   ffmpeg -f x11grab -s $(xdpyinfo | grep dimensions | awk '{print $2}') -i :0.0 -f alsa -i default -c:v libx264 -preset ultrafast -c:a aac output.mp4
   ```
   
   Este comando grabará la pantalla y el audio en un archivo de video llamado "output.mp4". Puedes detener la grabación presionando Ctrl + C en la terminal.