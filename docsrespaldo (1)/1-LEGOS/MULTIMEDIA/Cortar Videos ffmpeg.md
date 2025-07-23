# Cortar videos con ffmpeg

1. Para cortar el video en 00:01:10 descartando la parte final:

```bash
ffmpeg -i input.mp4 -ss 00:01:10 -c copy output_inicio.mp4
```

2. Para cortar el video en 00:01:10 descartando la parte inicial:

```bash
ffmpeg -i input.mp4 -t 00:01:10 -c copy output_final.mp4
```

3. Para cortar el video entre dos puntos de tiempo específicos, puedes usar el siguiente comando:

```bash
ffmpeg -i input.mp4 -ss 00:01:10 -to 00:02:30 -c copy output_entre_puntos.mp4
```

Este comando cortará el video desde el punto de tiempo 00:01:10 hasta el punto de tiempo 00:02:30, conservando esa sección del video en el archivo de salida "output_entre_puntos.mp4
