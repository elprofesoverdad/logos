# Kitty manualito

## Control remoto por scripts kitty script

* Recordar activar control remoto en la configuración o al inici de el script, también proporcionar clave y contraseña de ser necesario.

* Desde una sesión de bash en terminal se puede correr un script bash que contenga lo siguiente, los pasos están comentados en el código.

``` Bash
# Se inicia una instancia de kitty, en una ventana llamada "VENTANA"
setsid kitty --listen-on unix:/tmp/kitty.sock2 --title "VENTANA"

# Se crean dos pestañas una llamada PrimeraTab y otra llamada SegundaTab

kitty @ --to=unix:/tmp/kitty2.sock launch --type=tab --tab-title "PrimeraTab" --keep-focus bash 
kitty @ --to=unix:/tmp/kitty2.sock launch --type=tab --tab-title "SegundaTab" --keep-focus bash 

# Se cambia a la primera pestaña
kitty @ --to=unix:/tmp/kitty2.sock  focus-tab --match 'title:^PrimeraTab'

# Se escribe y \n es "enter"  entonces se ejecutan los comandos y funciones en la pestaña activa
# sirve para ejecutar scripts
kitty @ --to=unix:/tmp/kitty2.sock send-text "actz \n"
kitty @ --to=unix:/tmp/kitty2.sock send-text "AltoNivel \n"
kitty @ --to=unix:/tmp/kitty2.sock send-text "ls \n"

# Se obtiene el texto de la pestaña activa
kitty @ --to=unix:/tmp/kitty2.sock get-text

# Se abre un programa arbitrario por medio de la pestaña activa 
kitty @ --to=unix:/tmp/kitty2.sock  launch mousepad


```
## Clonar en ventana o pestañas

```bash
kitty @ --to=unix:/tmp/kitty2.sock send-text "clone-in-kitty --title "I am a clone" \n"

```
!!! note "clonar kitty"
    ``` bash
    También se puede clonar con:
    clone-in-kitty
    clone-in-kitty --type=tab
    clone-in-kitty --title "I am a clone"
    ```

## Reproducir video dentro de kitty

``` bash title="Video in kitty"

hay que saber el id de la ventana, si se dió un nombre a la
ventana como "VENTANA" se utilizará este nombre, 
en caso contrario buscar kitty como nombre de ventana:

xwininfo -name VENTANA
SALIDA:
xwininfo: Window id: 0x440000e "VENTANA"

con el id reproducir mpv:

mpv --wid=0x440000e "rutavideo.mp4"

```

