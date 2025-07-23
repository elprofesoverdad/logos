# manualito ripgrep

nota ripgrep puede devolver el numero de columna de la coincidencia dentro del archivo.

## Instalación:

```shell
$ curl -LO https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep_13.0.0_amd64.deb

$ sudo apt install -y $PWD/ripgrep_13.0.0_amd64.deb
```

## Para capturar y filtrar la salida de un comando en línea, puedes usar la siguiente sintaxis:

```shell
comando | rg patrón
```

Donde `comando` es el comando que deseas ejecutar y `patrón` es el patrón que deseas buscar en la salida del comando. El operador de tubería `|` redirige la salida del comando a `ripgrep`, que filtra la salida según el patrón especificado.

Por ejemplo, si deseas buscar la cadena “buscado” en la salida del comando `cat archivo.txt`, puedes usar el siguiente comando:

```shell
cat archivo.txt | rg buscado
```

Este comando buscará la cadena “buscado” en la salida del comando `cat archivo.txt`.

## Ejemplos

Para crear los archivos de ejemplo, puedes usar el siguiente comando de Bash:

```shell
for i in {1..5}; do
    echo "Contenido de prueba con perro y perros" > "archivo$i lista.txt"
done

for i in {6..10}; do
    echo "Contenido de prueba con perro y perros" > "archivo$i listas.txt"
done
```

Este comando creará 10 archivos de texto con nombres que contienen la palabra “lista” o “listas” y el número del archivo. Cada archivo contendrá la frase “Contenido de prueba con perro y perros”.

Para buscar los archivos que contienen la palabra “lista” o “listas” en sus nombres, puedes usar el siguiente comando de `ripgrep`:

```shell
rg -g '*lista*' -g '*listas*' .
```

Este comando buscará los archivos que contienen la palabra “lista” o “listas” en sus nombres en la carpeta actual y mostrará sus nombres.

## Tabla ripgrep

comandos de `ripgrep` para cada opción de búsqueda en Linux:

la opción -l devuelve solo el nombre del archivo, la -C el contexto cercano a la coincidencia

| **Opción de búsqueda**                                   | **Comando de ripgrep para Linux**        |
| -------------------------------------------------------- | ---------------------------------------- |
| lista                                                    | `rg -g '*lista*' -l $tron`               |
| listas                                                   | `rg -g '*listas*' -l $tron`              |
| lista y listas                                           | `rg -g '*lista*' -g '*listas*' -l $tron` |
| lista en el contenido                                    | `rg -w 'lista' $tron`                    |
| Nombre del archivo y solo lo regional                    | `rg -g '*lista*' -l $tron`               |
| Párrafo cercano a la coincidencia interna de la búsqueda | `rg -C 1 'lista' $tron`                  |

## uso con exclusión de archivos:

Para buscar solo los nombres de archivo que contienen la palabra “lista” pero no “listas”, puedes usar el siguiente comando de `ripgrep`:

```shell
rg -g '*lista*' -g '!*listas*' -l $tron
```

Este comando buscará los archivos que contienen la palabra “lista” en sus nombres y no contienen la palabra “listas” en sus nombres en la carpeta especificada por la variable $tron y mostrará sus nombres.

En Windows, el signo de interrogación `?` se utiliza como un carácter comodín que representa cualquier carácter individual. Para buscar solo los nombres de archivo que contienen la palabra “lista” pero no “listas” en Linux, puedes usar el siguiente comando de `ripgrep`:

```shell
rg -g '*lista[!s]*' -l $tron
```

Este comando buscará los archivos que contienen la palabra “lista” en sus nombres y no contienen la palabra “listas” en sus nombres en la carpeta especificada por la variable $tron y mostrará sus nombres.

* --exclude-dir no es compatible con ripgrep en todas las plataformas. En su lugar, puedes utilizar la opción --ignore-file para proporcionar un archivo que contenga patrones de exclusión. Para hacer esto, puedes crear un archivo .ignore en la carpeta raíz de tu proyecto y agregar la siguiente línea:

* /home/daniel/tron/programas/sesiones/historial/
  Luego, puedes utilizar el siguiente comando para buscar la palabra "daniel" en archivos con extensión .sh dentro de la carpeta tron y sus subcarpetas, excluyendo la carpeta /home/daniel/tron/programas/sesiones/historial/ y cualquier subdirectorio que contenga la palabra "historial":

```shell
rg -i --no-heading --color=always --ignore-file=.ignore --glob='*.sh' daniel /ruta/a/tron/
```

* Este comando debería excluir cualquier carpeta que contenga la palabra "historial" en su ruta, lo que debería evitar que aparezca el archivo pestanas.sh en la búsqueda.

* recomendable redireccionar la salida para analizarla y quitar la opcion de color.