Para girar un video 90 grados en contra de las agujas del reloj utilizando `ffmpeg`, puedes usar el siguiente comando:

```bash
ffmpeg -i inputVideo.mp4 -vf "transpose=2" outputVideo.mp4
```

### Desglose del Comando

- `-i inputVideo.mp4`: Especifica el archivo de video de entrada.

- `-vf "transpose=2"`: Aplica el filtro de video para girar el video. El número `2` indica que se debe rotar 90 grados en contra de las agujas del reloj.

- `outputVideo.mp4`: Especifica el nombre del archivo de salida, donde se guardará el video girado.

Este comando reencodificará el video y lo guardará con la nueva orientación. Si deseas evitar la pérdida de calidad, asegúrate de que el formato de salida sea compatible con la rotación sin necesidad de reencodificación, aunque esto no siempre es garantizado en todos los reproductores.

Citations:
[1] https://ottverse.com/rotate-a-video-using-ffmpeg-90-180/
[2] https://creatomate.com/blog/how-to-rotate-videos-using-ffmpeg
