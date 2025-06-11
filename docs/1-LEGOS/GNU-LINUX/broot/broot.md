no cambies mi solicitud no te pedi que involucraras alias... porque con rutad ()
{
    echo $(br --sort-by-count -t --conf ~/.config/broot/select_folder.toml $1)
} y la configuración ya funciona

Mis disculpas por la confusión anterior. Vamos a centrarnos en tu solicitud original y proporcionar un manual claro para usar **Broot** en Linux, utilizando las funciones `rutad` y `rutaf` sin involucrar alias. Aquí tienes la información completa.

### Manual para Usar Broot en Linux

#### Paso 1: Crear Archivos de Configuración

1. **Archivo de Configuración para Archivos**:
   Crea un archivo en `~/.config/broot/select.toml` con el siguiente contenido:

   ```toml
   verbs: [
       {
           invocation: "ok"
           key: "enter"
           leave_broot: true
           execution: ":print_path"
           apply_to: "file"
       }
   ]
   ```

2. **Archivo de Configuración para Directorios**:
   Crea otro archivo en `~/.config/broot/select_folder.toml` con este contenido:

   ```toml
   verbs: [
       {
           invocation: "ok"
           key: "enter"
           leave_broot: true
           execution: ":print_path"
           apply_to: "directory"
       }
   ]
   ```

#### Paso 2: Crear Funciones en Bash

Puedes definir las siguientes funciones en tu archivo de configuración de shell (por ejemplo, `~/.bashrc` o `~/.bash_profile`):

```bash
# Función para obtener la ruta de un directorio
rutad() {
    echo $(br --sort-by-count -t --conf ~/.config/broot/select_folder.toml "$1")
}

# Función para obtener la ruta de un archivo
rutaf() {
    echo $(br --sort-by-count -t --conf ~/.config/broot/select.toml "$1")
}
```

### Cómo Usar las Funciones

1. **Para Obtener la Ruta de un Directorio**:
   Llama a la función `rutad`. Por ejemplo:

   ```bash
   ruta_de_directorio=$(rutad)
   echo "Ruta del directorio seleccionado: $ruta_de_directorio"
   ```

2. **Para Obtener la Ruta de un Archivo**:
   Llama a la función `rutaf`. Por ejemplo:

   ```bash
   ruta_de_archivo=$(rutaf)
   echo "Ruta del archivo seleccionado: $ruta_de_archivo"
   ```

### Ejemplo Completo

Aquí tienes un ejemplo completo que puedes agregar a tu archivo de configuración de shell:

```bash
# Definición de funciones
rutad() {
    echo $(br --sort-by-count -t --conf ~/.config/broot/select_folder.toml "$1")
}

rutaf() {
    echo $(br --sort-by-count -t --conf ~/.config/broot/select.toml "$1")
}

# Uso de las funciones
echo "Selecciona un directorio:"
ruta_de_directorio=$(rutad)
echo "Ruta del directorio seleccionado: $ruta_de_directorio"

echo "Selecciona un archivo:"
ruta_de_archivo=$(rutaf)
echo "Ruta del archivo seleccionado: $ruta_de_archivo"
```

### Conclusión

Con esta configuración, puedes utilizar Broot como un selector interactivo para obtener rutas de archivos y directorios en tu terminal Linux. Simplemente ejecuta las funciones `rutad` y `rutaf` según sea necesario, y obtendrás la ruta correspondiente al elemento seleccionado.

