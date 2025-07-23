Para modificar tu snippet en Visual Studio Code de manera que puedas aplicar el formato de párrafos a un texto seleccionado sin borrarlo, puedes utilizar la variable `TM_SELECTED_TEXT`, que permite que el texto seleccionado se incluya dentro del snippet. Esto te permitirá envolver el texto seleccionado con la estructura de párrafos que has definido.

Aquí está cómo podrías modificar tu snippet:

```json
"Insertar Párrafos": {
    "prefix": "parr",
    "body": [
        "{% assign parrafos = '${TM_SELECTED_TEXT}' %}",
        "",
        "{% assign parrafos_array = parrafos | split: '/n' %}",
        "{% include componentes/parrafo.html parrafos=parrafos_array %}"
    ],
    "description": "Insertar la estructura de párrafos en Jekyll"
}
```

### Pasos para implementar el cambio:

1. **Abre el archivo de snippets**: Ve a la paleta de comandos (Ctrl+Shift+P) y busca "Preferences: Configure User Snippets". Selecciona el archivo donde tienes definido tu snippet.

2. **Modifica el snippet**: Reemplaza el cuerpo del snippet existente con el código proporcionado arriba.

3. **Usa el snippet con un atajo**: Para aplicar este snippet a un texto seleccionado, simplemente selecciona el texto en tu editor, luego escribe `parr` y presiona `Tab` o `Enter`. El texto seleccionado se insertará en la estructura de párrafos definida.

### Asignar un atajo de teclado

Si deseas asignar un atajo específico para insertar este snippet sin tener que escribir el prefijo, puedes hacerlo editando el archivo `keybindings.json`. Aquí te muestro cómo hacerlo:

1. **Abre keybindings.json**: Ve a la paleta de comandos y busca "Preferences: Open Keyboard Shortcuts (JSON)".

2. **Agrega la siguiente entrada**:

```json
{
    "key": "ctrl+p", // Cambia esto por la combinación de teclas que prefieras
    "command": "editor.action.insertSnippet",
    "args": {
        "snippet": "{% assign parrafos = '${TM_SELECTED_TEXT}' %}\n\n{% assign parrafos_array = parrafos | split: '/n' %}\n{% include componentes/parrafo.html parrafos=parrafos_array %}"
    },
    "when": "editorTextFocus"
}
```

### Consideraciones

- **TM_SELECTED_TEXT**: Esta variable se reemplazará automáticamente con el texto que hayas seleccionado cuando uses el snippet.
  
- **Atajos de teclado**: Asegúrate de que la combinación de teclas que eliges no esté ya en uso por otra función en VS Code.

Con estos cambios, podrás aplicar tu snippet fácilmente al texto seleccionado sin necesidad de borrarlo, optimizando así tu flujo de trabajo en Jekyll.

Citations:
[1] https://simplanova.com/blog/vs-code-snippets-user-personalization/
[2] https://github.com/microsoft/vscode/issues/62907
[3] https://pieces.app/blog/vs-code-snippets-guide
[4] https://stackoverflow.com/questions/39333639/visual-studio-code-snippet-as-keyboard-shortcut-key/68975512
[5] https://code.visualstudio.com/docs/editor/userdefinedsnippets
