# Para agregar una pista de audio en otro idioma a un vídeo que ya tiene una pista de audio

Por ejemplo ya esta  en español,  y se agregará inglés

```bash
ffmpeg -i input.mp4 -i audio_ingles.mp3 -map 0:v -map 0:a:0 -map 1:a:0 -c:v copy -c:a copy -metadata:s:a:1 language=eng output_con_audio_ingles.mp4
```

En este comando:

- `-i input.mp4` es el archivo de video original en español.
- `-i audio_ingles.mp3` es el archivo de audio en inglés que deseas agregar.
- `-map 0:v -map 0:a:0 -map 1:a:0` se encarga de mapear el video y las pistas de audio del video original y del audio en inglés.
- `-c:v copy -c:a copy` copia los códecs de video y audio sin realizar ninguna conversión.
- `-metadata:s:a:1 language=eng` establece el idioma de la segunda pista de audio como inglés.
