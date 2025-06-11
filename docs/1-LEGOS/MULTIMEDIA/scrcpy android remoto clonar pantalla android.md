# scrcpy android remoto clonar pantalla android

* Android cámara remota

* *Telefono como cámara web o webcam*





[GitHub - Genymobile/scrcpy: Display and control your Android device](https://github.com/Genymobile/scrcpy?tab=readme-ov-file)# 



# Atajos

[](https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md#shortcuts)

Se pueden realizar acciones en la ventana scrcpy usando atajos de teclado y mouse.

En la siguiente lista, MODse encuentra el modificador de acceso directo. De forma predeterminada, es (izquierda) Alto (izquierda) Super.

Se puede cambiar usando `--shortcut-mod`. Las claves posibles son `lctrl`, `rctrl`, `lalt`, `ralt`y . Por ejemplo:`lsuper``rsuper`

```shell
# use RCtrl for shortcuts
scrcpy --shortcut-mod=rctrl

# use either LCtrl+LAlt or LSuper for shortcuts
scrcpy --shortcut-mod=lctrl+lalt,lsuper
```

*[Super](https://en.wikipedia.org/wiki/Super_key_(keyboard_button))suele ser la clave Windowso Cmd.*

| Acción                                                          | Atajo                                                                                                                |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Cambiar el modo de pantalla completa                            | MOD+f                                                                                                                |
| Girar la pantalla hacia la izquierda                            | MOD+ ← *(izquierda)*                                                                                                 |
| Girar la pantalla hacia la derecha                              | MOD+ → *(derecha)*                                                                                                   |
| Voltear la pantalla horizontalmente                             | MOD+ Shift+ ← *(izquierda)* \| MOD+ Shift+ → *(derecha)*                                                             |
| Voltear la pantalla verticalmente                               | MOD+ Shift+ ↑ *(arriba)* \| MOD+ Shift+ ↓ *(abajo)*                                                                  |
| Cambiar el tamaño de la ventana a 1:1 (píxel perfecto)          | MOD+g                                                                                                                |
| Cambiar el tamaño de la ventana para eliminar los bordes negros | MOD+ w\| *Doble clic izquierdo¹*                                                                                     |
| Haga clic en`HOME`                                              | MOD+ h\| *Clic central*                                                                                              |
| Haga clic en`BACK`                                              | MOD+ b\| MOD+ Backspace\| *Haga clic derecho²*                                                                       |
| Haga clic en`APP_SWITCH`                                        | MOD+ s\| *Cuarto clic³*                                                                                              |
| Haga clic en `MENU`(desbloquear pantalla)⁴                      | MOD+m                                                                                                                |
| Haga clic en`VOLUME_UP`                                         | MOD+ ↑ *(arriba)*                                                                                                    |
| Haga clic en`VOLUME_DOWN`                                       | MOD+ ↓ *(abajo)*                                                                                                     |
| Haga clic en`POWER`                                             | MOD+p                                                                                                                |
| Encendido                                                       | *Haga clic derecho²*                                                                                                 |
| Apagar la pantalla del dispositivo (seguir reflejando)          | MOD+o                                                                                                                |
| Encender la pantalla del dispositivo                            | MOD+ Shift+o                                                                                                         |
| Girar la pantalla del dispositivo                               | MOD+r                                                                                                                |
| Expandir panel de notificaciones                                | MOD+ n\| *5to clic³*                                                                                                 |
| Expandir el panel de configuración                              | MOD+ n+ n\| *Doble quinto clic³*                                                                                     |
| Contraer paneles                                                | MOD+ Shift+n                                                                                                         |
| Copiar al portapapeles⁵                                         | MOD+c                                                                                                                |
| Cortar al portapapeles⁵                                         | MOD+x                                                                                                                |
| Sincronizar portapapeles y pegar⁵                               | MOD+v                                                                                                                |
| Inyectar texto en el portapapeles de la computadora             | MOD+ Shift+v                                                                                                         |
| Abrir la configuración del teclado (solo teclado HID)           | MOD+k                                                                                                                |
| Activar/desactivar el contador de FPS (en la salida estándar)   | MOD+i                                                                                                                |
| Pellizcar para hacer zoom/rotar                                 | Ctrl+ *hacer clic y mover*                                                                                           |
| Inclinar (deslizar verticalmente con 2 dedos)                   | Shift+ *hacer clic y mover*                                                                                          |
| Arrastrar y soltar el archivo APK                               | Instalar APK desde la computadora                                                                                    |
| Arrastrar y soltar archivos que no sean APK                     | [Enviar archivo al dispositivo](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#push-file-to-device) |

*¹Haga doble clic en los bordes negros para eliminarlos.*  
*²Hacer clic con el botón derecho enciende la pantalla si estaba apagada; en caso contrario, presiona ATRÁS.*  
*³Cuarto y quinto botones del mouse, si su mouse los tiene.*  
*⁴Para aplicaciones nativas de reacción en desarrollo, `MENU`activa el menú de desarrollo.*  
*⁵Solo en Android >= 7.*

Los atajos con teclas repetidas se ejecutan soltando y presionando la tecla por segunda vez. Por ejemplo, para ejecutar "Expandir panel de configuración":

1. Presiona y sigue presionando MOD.
2. Luego presione dos veces n.
3. Finalmente, suelte MOD.

Todos los atajos *de la tecla*Ctrl + se reenvían al dispositivo, por lo que son manejados por la aplicación activa.



# Video

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#video)

## Fuente

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#source)

De forma predeterminada, scrcpy refleja la pantalla del dispositivo.

En su lugar, es posible capturar la cámara del dispositivo.

Consulte la página dedicada [a la cámara](https://github.com/Genymobile/scrcpy/blob/master/doc/camera.md) .

## Tamaño

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#size)

De forma predeterminada, scrcpy intenta reflejar la resolución del dispositivo Android.

Puede resultar útil reflejar con una definición más baja para aumentar el rendimiento. Para limitar tanto el ancho como el alto a un valor máximo (aquí 1024):

```shell
scrcpy --max-size=1024scrcpy -m 1024   # short version
```

La otra dimensión se calcula de modo que se conserve la relación de aspecto del dispositivo Android. De esa manera, un dispositivo en 1920×1080 se reflejará en 1024×576.

Si la codificación falla, scrcpy vuelve a intentarlo automáticamente con una definición más baja (a menos que `--no-downsize-on-error`esté habilitado).

## tasa de bits

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#bit-rate)

La velocidad de bits de vídeo predeterminada es de 8 Mbps. Para cambiarlo:

```shell
scrcpy --video-bit-rate=2Mscrcpy --video-bit-rate=2000000  # equivalent
scrcpy -b 2M                     # short version
```

## Cuadros por segundo

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#frame-rate)

La velocidad de fotogramas de captura se puede limitar:

```shell
scrcpy --max-fps=15
```

La velocidad de fotogramas de captura real se puede imprimir en la consola:

```
scrcpy --print-fps
```

También se puede habilitar o deshabilitar en cualquier momento con MOD+ i (ver [atajos](https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md) ).

La velocidad de fotogramas es intrínsecamente variable: se produce un nuevo fotograma sólo cuando cambia el contenido de la pantalla. Por ejemplo, si reproduce un vídeo en pantalla completa a 24 fps en su dispositivo, no debería obtener más de 24 fotogramas por segundo en scrcpy.

## Códec

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#codec)

Se puede seleccionar el códec de vídeo. Los valores posibles son `h264`(predeterminado) `h265`y `av1`:

```shell
scrcpy --video-codec=h264  # default
scrcpy --video-codec=h265scrcpy --video-codec=av1
```

H265 puede proporcionar una mejor calidad, pero H264 debería proporcionar una latencia más baja. Los codificadores AV1 no son comunes en los dispositivos Android actuales.

Para uso avanzado, para pasar parámetros arbitrarios a [`MediaFormat`](https://developer.android.com/reference/android/media/MediaFormat), consulte `--video-codec-options`la página de manual o en `scrcpy --help`.

## Codificador

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#encoder)

Es posible que haya varios codificadores disponibles en el dispositivo. Se pueden enumerar por:

```shell
scrcpy --list-encoders
```

A veces, el codificador predeterminado puede tener problemas o incluso fallar, por lo que es útil probar con otro:

```shell
scrcpy --video-codec=h264 --video-encoder='OMX.qcom.video.encoder.avc'
```

## Orientación

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#orientation)

La orientación se puede aplicar en 3 niveles diferentes:

- El [acceso directo](https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md) MOD + rsolicita al dispositivo que cambie entre vertical y horizontal (la aplicación que se está ejecutando actualmente puede negarse, si no admite la orientación solicitada).
- `--lock-video-orientation`cambia la orientación de la duplicación (la orientación del vídeo enviado desde el dispositivo a la computadora). Esto afecta la grabación.
- `--orientation`se aplica en el lado del cliente y afecta la visualización y la grabación. Para la visualización, se puede cambiar dinámicamente usando [atajos](https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md) .

Para bloquear la orientación de la duplicación (en el lado de captura):

```shell
scrcpy --lock-video-orientation      # initial (current) orientation
scrcpy --lock-video-orientation=0    # natural orientation
scrcpy --lock-video-orientation=90   # 90° clockwise
scrcpy --lock-video-orientation=180  # 180°
scrcpy --lock-video-orientation=270  # 270° clockwise
```

Para orientar el vídeo (en el lado de renderizado):

```shell
scrcpy --orientation=0scrcpy --orientation=90       # 90° clockwise
scrcpy --orientation=180      # 180°
scrcpy --orientation=270      # 270° clockwise
scrcpy --orientation=flip0    # hflip
scrcpy --orientation=flip90   # hflip + 90° clockwise
scrcpy --orientation=flip180  # vflip (hflip + 180°)
scrcpy --orientation=flip270  # hflip + 270° clockwise
```

La orientación se puede configurar por separado para visualización y registro si es necesario, mediante `--display-orientation`y `--record-orientation`.

La rotación se aplica a un archivo grabado escribiendo una transformación de visualización en el archivo de destino MP4 o MKV. No se admite la inversión, por lo que solo se permiten los 4 primeros valores al grabar.

## Recortar pantalla

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#crop)

Es posible que la pantalla del dispositivo se recorte para reflejar solo una parte de la pantalla.

Esto es útil, por ejemplo, para reflejar solo un ojo de Oculus Go:

```shell
scrcpy --crop=1224:1440:0:0   # 1224x1440 at offset (0,0)
```

Los valores se expresan en la orientación natural del dispositivo (vertical para un teléfono, horizontal para una tableta).

Si `--max-size`también se especifica, el cambio de tamaño se aplica después del recorte.

Copiar pegar

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#copy-paste)

Cada vez que cambia el portapapeles de Android, se sincroniza automáticamente con el portapapeles de la computadora.

Cualquier Ctrlacceso directo se reenvía al dispositivo. En particular:

- Ctrl+ cnormalmente copias
- Ctrl+ xnormalmente corta
- Ctrl+ vnormalmente pega (después de la sincronización del portapapeles de la computadora al dispositivo)

Normalmente, esto funciona como se esperaba.

Sin embargo, el comportamiento real depende de la aplicación activa. Por ejemplo, *Termux* envía SIGINT en Ctrl+ cen su lugar y *K-9 Mail* redacta un nuevo mensaje.

Para copiar, cortar y pegar en tales casos (pero solo es compatible con Android >= 7):

- MOD+ cinyecta`COPY`
- MOD+ xinyecta`CUT`
- MOD+ vinyecta `PASTE`(después de la sincronización del portapapeles de computadora a dispositivo)

Además, MOD+ Shift+ vinyecta el texto del portapapeles de la computadora como una secuencia de eventos clave. Esto es útil cuando el componente no acepta pegar texto (por ejemplo en *Termux* ), pero puede romper contenido que no sea ASCII.

**ADVERTENCIA:** Al pegar el portapapeles de la computadora en el dispositivo (ya sea mediante Ctrl+ vo MOD+ v), se copia el contenido en el portapapeles de Android. Como consecuencia, cualquier aplicación de Android podría leer su contenido. Debes evitar pegar contenido confidencial (como contraseñas) de esa manera.

Algunos dispositivos Android no se comportan como se esperaba al configurar el portapapeles del dispositivo mediante programación. Se proporciona una opción `--legacy-paste`para cambiar el comportamiento de Ctrl+ vy MOD+ vpara que también inserten el texto del portapapeles de la computadora como una secuencia de eventos clave (de la misma manera que MOD+ Shift+ v).

Para desactivar la sincronización automática del portapapeles, utilice `--no-clipboard-autosync`.



### Instalar APK

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#install-apk)

Para instalar un APK, arrastre y suelte un archivo APK (que termine en `.apk`) en la ventana *scrcpy .*

No hay respuesta visual, se imprime un registro en la consola.

### Enviar archivo al dispositivo

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#push-file-to-device)

Para enviar un archivo `/sdcard/Download/`al dispositivo, arrastre y suelte un archivo (que no sea APK) en la ventana *scrcpy .*

No hay respuesta visual, se imprime un registro en la consola.

El directorio de destino se puede cambiar al inicio:

```shell
scrcpy --push-target=/sdcard/Movies/
```

## Mostrar

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#display)

Si hay varias pantallas disponibles en el dispositivo Android, es posible seleccionar la pantalla a reflejar:

```shell
scrcpy --display-id=1
```

La lista de ID de visualización se puede recuperar mediante:

```shell
scrcpy --list-displays
```

Solo se puede controlar una pantalla secundaria si el dispositivo ejecuta al menos Android 10 (de lo contrario, se refleja como de solo lectura).

## Almacenamiento en búfer

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#buffering)

De forma predeterminada, no hay almacenamiento en búfer de vídeo para obtener la latencia más baja posible.

Se puede agregar almacenamiento en búfer para retrasar la transmisión de video y compensar la fluctuación para obtener una reproducción más fluida (consulte [el n.° 2464](https://github.com/Genymobile/scrcpy/issues/2464) ).

La configuración está disponible de forma independiente para la pantalla, [los disipadores v4l2](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#video4linux) y la reproducción [de audio](https://github.com/Genymobile/scrcpy/blob/master/doc/audio.md#buffering) .

```shell
scrcpy --display-buffer=50   # add 50ms buffering for display
scrcpy --v4l2-buffer=300     # add 300ms buffering for v4l2 sink
scrcpy --audio-buffer=200    # set 200ms buffering for audio playback
```

Se pueden aplicar simultáneamente:

```shell
scrcpy --display-buffer=50 --v4l2-buffer=300
```

## Sin reproducción

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#no-playback)

Es posible capturar un dispositivo Android sin reproducir video o audio en la computadora. Esta opción es útil cuando [se graba](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md) o cuando [v4l2](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#video4linux) está habilitado:

```shell
scrcpy --v4l2-sink=/dev/video2 --no-playbackscrcpy --record=file.mkv --no-playback
# interrupt with Ctrl+C
```

También es posible desactivar la reproducción de vídeo y audio por separado:

```shell
# Send video to V4L2 sink without playing it, but keep audio playback
scrcpy --v4l2-sink=/dev/video2 --no-video-playback

# Record both video and audio, but only play video
scrcpy --record=file.mkv --no-audio-playback
```

## No hay video

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#no-video)

Para deshabilitar completamente el reenvío de video, de modo que solo se reenvíe el audio:

```
scrcpy --no-video
```

## Video4Linux

[](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#video4linux)

Consulte la página dedicada [a Video4Linux](https://github.com/Genymobile/scrcpy/blob/master/doc/v4l2.md) . 





# Grabación

[](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md#recording)

Para grabar transmisiones de video y audio durante la duplicación:

```shell
scrcpy --record=file.mp4scrcpy -r file.mkv
```

Para grabar sólo el vídeo:

```shell
scrcpy --no-audio --record=file.mp4
```

Para grabar sólo el audio:

```shell
scrcpy --no-video --record=file.opusscrcpy --no-video --audio-codec=aac --record=file.aacscrcpy --no-video --audio-codec=flac --record=file.flacscrcpy --no-video --audio-codec=raw --record=file.wav
# .m4a/.mp4 and .mka/.mkv are also supported for opus, aac and flac
```

Las marcas de tiempo se capturan en el dispositivo, por lo que [la variación del retraso de los paquetes](https://en.wikipedia.org/wiki/Packet_delay_variation) no afecta el archivo grabado, que siempre está limpio (solo si lo usa `--record`, por supuesto, no si captura su ventana scrcpy y la salida de audio en la computadora).

## Formato

[](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md#format)

Las transmisiones de video y audio están codificadas en el dispositivo, pero se mezclan en el lado del cliente. Se admiten varios formatos (contenedores):

- MP4 ( `.mp4`, `.m4a`, `.aac`)
- Matroska ( `.mkv`, `.mka`)
- OPUS ( `.opus`)
- FLAC ( `.flac`)
- WAV ( `.wav`)

El contenedor se selecciona automáticamente según el nombre del archivo.

También es posible seleccionar explícitamente un contenedor (en ese caso, no es necesario que el nombre del archivo termine con una extensión conocida):

```
scrcpy --record=file --record-format=mkv
```

## Rotación

[](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md#rotation)

El vídeo se puede grabar girado. Ver [vídeo de orientación](https://github.com/Genymobile/scrcpy/blob/master/doc/video.md#orientation) .

## Sin reproducción

[](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md#no-playback)

Para desactivar la reproducción durante la grabación:

```shell
scrcpy --no-playback --record=file.mp4scrcpy -Nr file.mkv
# interrupt recording with Ctrl+C
```

También es posible desactivar la reproducción de vídeo y audio por separado:

```shell
# Record both video and audio, but only play video
scrcpy --record=file.mkv --no-audio-playback
```

## Límite de tiempo

[](https://github.com/Genymobile/scrcpy/blob/master/doc/recording.md#time-limit)

Para limitar el tiempo de grabación:

```shell
scrcpy --record=file.mkv --time-limit=20  # in seconds
```

La `--time-limit`opción no se limita a la grabación, también afecta a la duplicación simple:

```
scrcpy --time-limit=20 
```



# OTG

[](https://github.com/Genymobile/scrcpy/blob/master/doc/otg.md#otg)

De forma predeterminada, *scrcpy* inyecta eventos de entrada en el nivel de API de Android. Como alternativa, cuando se conecta a través de USB, es posible enviar eventos HID, de modo que scrcpy se comporte como si fuera un teclado y/o mouse físico conectado al dispositivo Android.

Un modo especial permite controlar el dispositivo sin duplicación, utilizando [el teclado](https://github.com/Genymobile/scrcpy/blob/master/doc/keyboard.md#aoa) y [el mouse](https://github.com/Genymobile/scrcpy/blob/master/doc/mouse.md#aoa) AOA . Por lo tanto, es posible ejecutar *scrcpy* solo con simulación física de teclado y mouse (HID), como si el teclado y el mouse de la computadora estuvieran conectados directamente al dispositivo mediante un cable OTG.

En este modo, `adb`(depuración USB) no es necesaria y la duplicación está desactivada.

Esto es similar a `--keyboard=aoa --mouse=aoa`, pero sin duplicación.

Para habilitar el modo OTG:

```shell
scrcpy --otg
# Pass the serial if several USB devices are available
scrcpy --otg -s 0123456789abcdef
```

Es posible desactivar el teclado HID o el mouse HID:

```shell
scrcpy --otg --keyboard=disabledscrcpy --otg --mouse=disabled
```

Solo funciona si el dispositivo está conectado a través de USB.



# Dispositivo

[](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md#device)

Algunos argumentos de la línea de comando realizan acciones en el propio dispositivo mientras se ejecuta scrcpy.

## Mantente despierto

[](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md#stay-awake)

Para evitar que el dispositivo entre en suspensión después de un retraso **cuando el dispositivo está enchufado** :

```shell
scrcpy --stay-awakescrcpy -w
```

El estado inicial se restaura cuando se cierra *scrcpy .*

Si el dispositivo no está enchufado (es decir, sólo conectado a través de TCP/IP), `--stay-awake`no tiene ningún efecto (este es el comportamiento de Android).

## Apagar la pantalla

[](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md#turn-screen-off)

Es posible apagar la pantalla del dispositivo mientras se realiza la duplicación al iniciar con una opción de línea de comandos:

```shell
scrcpy --turn-screen-offscrcpy -S   # short version
```

O presionando MOD+ oen cualquier momento (ver [atajos](https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md) ).

Para volver a encenderlo, presione MOD+ Shift+ o.

En Android, el `POWER`botón siempre enciende la pantalla. Para mayor comodidad, si `POWER`se envía a través de *scrcpy* (haciendo clic con el botón derecho o MOD+ p), obligará a apagar la pantalla después de un pequeño retraso (en el mejor de los casos). El botón físico `POWER`seguirá haciendo que la pantalla se encienda.

También puede resultar útil evitar que el dispositivo entre en suspensión:

```shell
scrcpy --turn-screen-off --stay-awakescrcpy -Sw   # short version
```

## Mostrar toques

[](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md#show-touches)

Para presentaciones, puede resultar útil mostrar toques físicos (en el dispositivo físico). Android expone esta característica en *las opciones de Desarrolladores* .

*Scrcpy* proporciona una opción para habilitar esta función al inicio y restaurar el valor inicial al salir:

```shell
scrcpy --show-touchesscrcpy -t   # short version
```

Tenga en cuenta que solo muestra toques *físicos* (con un dedo en el dispositivo).

## Apagar al cerrar

[](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md#power-off-on-close)

Para apagar la pantalla del dispositivo al cerrar *scrcpy* :

```shell
scrcpy --power-off-on-close
```

## Encendido al inicio

[](https://github.com/Genymobile/scrcpy/blob/master/doc/device.md#power-on-on-start)

De forma predeterminada, al iniciar, el dispositivo está encendido. Para evitar este comportamiento:

```shell
scrcpy --no-power-on
```

# Ventana

[](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md#window)

## Título

[](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md#title)

De forma predeterminada, el título de la ventana es el modelo del dispositivo. Se puede cambiar:

```shell
scrcpy --window-title='My device'
```

## Posición y tamaño

[](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md#position-and-size)

La posición y el tamaño inicial de la ventana se pueden especificar:

```shell
scrcpy --window-x=100 --window-y=100 --window-width=800 --window-height=600
```

## Sin fronteras

[](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md#borderless)

Para desactivar las decoraciones de ventanas:

```shell
scrcpy --window-borderless
```

## Siempre en la cima

[](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md#always-on-top)

Para mantener la ventana siempre arriba:

```shell
scrcpy --always-on-top
```

## Pantalla completa

[](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md#fullscreen)

La aplicación se puede iniciar directamente en pantalla completa:

```shell
scrcpy --fullscreenscrcpy -f   # short version
```

Luego, el modo de pantalla completa se puede alternar dinámicamente con MOD+ f (consulte [los accesos directos](https://github.com/Genymobile/scrcpy/blob/master/doc/shortcuts.md) ).

## Desactivar salvapantallas

[](https://github.com/Genymobile/scrcpy/blob/master/doc/window.md#disable-screensaver)

De forma predeterminada, *scrcpy* no impide que el protector de pantalla se ejecute en la computadora. Para desactivarlo:

```shell
scrcpy --disable-screensaver
```



# Control

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#control)

## Solo lectura

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#read-only)

Para desactivar los controles (todo lo que puede interactuar con el dispositivo: teclas de entrada, eventos del mouse, arrastrar y soltar archivos):

```shell
scrcpy --no-controlscrcpy -n   # short version
```

## Teclado y ratón

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#keyboard-and-mouse)

Leer [teclado](https://github.com/Genymobile/scrcpy/blob/master/doc/keyboard.md) y [mouse](https://github.com/Genymobile/scrcpy/blob/master/doc/mouse.md) .

## 

## Simulación de pellizcar para hacer zoom, rotar e inclinar

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#pinch-to-zoom-rotate-and-tilt-simulation)

Para simular "pellizcar para hacer zoom": Ctrl+ *hacer clic y mover* .

Más precisamente, mantenga presionado Ctrlmientras presiona el botón de clic izquierdo. Hasta que se suelta el botón izquierdo, todos los movimientos del mouse escalan y rotan el contenido (si la aplicación lo admite) en relación con el centro de la pantalla.

 Ctrl.mp4 

Para simular un gesto de inclinación: Shift+ *hacer clic y mover hacia arriba o hacia abajo* .

 cambio.mp4 

Técnicamente, *scrcpy* genera eventos táctiles adicionales desde un "dedo virtual" en una ubicación invertida en el centro de la pantalla. Al presionar se invierten Ctrllas coordenadas *x* e *y* . Usando Shift solo se invierte *x* .

Esto sólo funciona para el modo de mouse predeterminado ( `--mouse=sdk`).

## Haga clic derecho y haga clic con el botón central

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#right-click-and-middle-click)

De forma predeterminada, al hacer clic con el botón derecho se activa ATRÁS (o encender) y al hacer clic con el botón central se activa INICIO. Para desactivar estos atajos y reenviar los clics al dispositivo:

```shell
scrcpy --forward-all-clicks
```

## Soltar archivos

[](https://github.com/Genymobile/scrcpy/blob/master/doc/control.md#file-drop)

# Conexión

[](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#connection)

## Selección

[](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#selection)

Si hay exactamente un dispositivo conectado (es decir, enumerado por `adb devices`), se selecciona automáticamente.

Sin embargo, si hay varios dispositivos conectados, debes especificar cuál usar de una de estas 4 maneras:

- por su serie:
  
  ```shell
  scrcpy --serial=0123456789abcdefscrcpy -s 0123456789abcdef   # short version
  
  # the serial is the ip:port if connected over TCP/IP (same behavior as adb)
  scrcpy --serial=192.168.1.1:5555
  ```

- el que está conectado por USB (si hay exactamente uno):
  
  ```shell
  scrcpy --select-usbscrcpy -d   # short version
  ```

- el que está conectado a través de TCP/IP (si hay exactamente uno):
  
  ```shell
  scrcpy --select-tcpipscrcpy -e   # short version
  ```

- un dispositivo que ya escucha en TCP/IP (ver [más abajo](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#tcpip-wireless) ):
  
  ```shell
  scrcpy --tcpip=192.168.1.1:5555scrcpy --tcpip=192.168.1.1        # default port is 5555
  ```

El número de serie también se puede proporcionar a través de la variable de entorno `ANDROID_SERIAL` (también utilizada por `adb`):

```shell
# in bash
export ANDROID_SERIAL=0123456789abcdefscrcpy
```

```batchfile
:: in cmd
set ANDROID_SERIAL=0123456789abcdefscrcpy
```

```powershell
# in PowerShell
$env:ANDROID_SERIAL = '0123456789abcdef'
scrcpy
```

## TCP/IP (inalámbrico)

[](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#tcpip-wireless)

*Scrcpy* utiliza `adb`para comunicarse con el dispositivo y `adb`puede [conectarse](https://developer.android.com/studio/command-line/adb.html#wireless) a un dispositivo a través de TCP/IP. El dispositivo debe estar conectado a la misma red que la computadora.

### Automático

[](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#automatic)

Una opción `--tcpip`permite configurar la conexión automáticamente. Hay dos variantes.

Si el modo *adb* TCP/IP está deshabilitado en el dispositivo (o si no conoce la dirección IP), conecte el dispositivo a través de USB y luego ejecute:

```shell
scrcpy --tcpip   # without arguments
```

Automáticamente encontrará la dirección IP del dispositivo y el puerto adb, habilitará el modo TCP/IP si es necesario y luego se conectará al dispositivo antes de comenzar.

Si el dispositivo (accesible en 192.168.1.1 en este ejemplo) ya escucha en un puerto (normalmente 5555) las conexiones *adb* entrantes , ejecute:

```shell
scrcpy --tcpip=192.168.1.1       # default port is 5555
scrcpy --tcpip=192.168.1.1:5555
```

### Manual

[](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#manual)

Alternativamente, es posible habilitar la conexión TCP/IP manualmente usando `adb`:

1. Conecte el dispositivo a un puerto USB de su computadora.

2. Conecte el dispositivo a la misma red Wi-Fi que su computadora.

3. Obtenga la dirección IP de su dispositivo, en Configuración → Acerca del teléfono → Estado, o ejecutando este comando:
   
   ```shell
   adb shell ip route | awk '{print $9}'
   ```

4. Habilite `adb`sobre TCP/IP en su dispositivo: `adb tcpip 5555`.

5. Desenchufe su dispositivo.

6. Conéctese a su dispositivo: `adb connect DEVICE_IP:5555` *(reemplace `DEVICE_IP` con la dirección IP del dispositivo que encontró)* .

7. Corre `scrcpy`como de costumbre.

8. Corre `adb disconnect`una vez que hayas terminado.

Desde Android 11, una [opción de depuración inalámbrica](https://developer.android.com/studio/command-line/adb#wireless-android11-command-line) permite evitar tener que conectar físicamente su dispositivo directamente a su computadora.

## Autoencendido

[](https://github.com/Genymobile/scrcpy/blob/master/doc/connection.md#autostart)

Una pequeña herramienta (del autor de scrcpy) permite ejecutar comandos arbitrarios cada vez que se conecta un nuevo dispositivo Android: [AutoAdb](https://github.com/rom1v/autoadb) . Se puede utilizar para iniciar scrcpy:

```shell
autoadb scrcpy -s '{}'
```