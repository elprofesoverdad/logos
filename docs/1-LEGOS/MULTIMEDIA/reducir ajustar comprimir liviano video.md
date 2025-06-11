# Comprimir ajustar reducir video.

Para ajustar el comando de `ffmpeg` y asegurarte de que el tamaño del video resultante sea menor a 32 MB, puedes probar con una tasa de bits más baja. Aquí tienes un ejemplo de comando con una tasa de bits objetivo más baja:

```bash
ffmpeg -i video.mp4 -b:v 1.5M -minrate 1M -maxrate 2M -bufsize 2M video_reducido.mp4
```

En este comando, he reducido la tasa de bits a 1.5 Mbps como objetivo, con una tasa de bits mínima de 1 Mbps y máxima de 2 Mbps. Esto debería ayudarte a obtener un archivo de video con un tamaño más cercano a los 32 MB sin sacrificar demasiada calidad.

Por favor, prueba este comando y verifica el tamaño del archivo resultante para asegurarte de que cumple con tus requisitos de tamaño. ¡Espero que esta modificación te ayude a lograr el tamaño deseado sin comprometer la calidad de tu video!