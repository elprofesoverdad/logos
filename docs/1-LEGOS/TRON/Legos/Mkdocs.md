# Manual Mkdocs

## Instalación

!!! note "Nota Importante"
    Cuando lo pida el entorno es Mkdocs con la primera mayúscula.
    ojo deactivate entorno viejo y borrar.

!!! success
    antes de hacer build copiar el .yaml

```bash
crearentorno
activarentorno
pip install mkdocs-material
cd ~/tron/biblioteca
rm -vr Mkdocs
mkdir Mkdocs
cd Mk*
mkdocs new .
mkdocs build
```

## Resaltado Lineas de codigo:

```
    ``` python  title="Calculadora.py" linenums="1" hl_lines="164 65 66 67"
```

## Tablas:

* Las tablas de datos se pueden usar en cualquier posición en la documentación de su proyecto y pueden contener Markdown arbitrario, incluidos bloques de código en línea, así como íconos y emojis :

Data table

| Method   | Description                          |
| -------- | ------------------------------------ |
| `GET`    | :material-check:     Fetch resource  |
| `PUT`    | :material-check-all: Update resource |
| `DELETE` | :material-close:     Delete resource |

## Listas de definiciones:

```
`Lorem ipsum dolor sit amet`

:   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
    tellus non sem sollicitudin, quis rutrum leo facilisis.

`Cras arcu libero`

:   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
    ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

    Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
    Nam vulputate tincidunt fringilla.
    Nullam dignissim ultrices urna non auctor.
```

## Lista Ordenada:

```
1.  Vivamus id mi enim. Integer id turpis sapien. Ut condimentum lobortis
    sagittis. Aliquam purus tellus, faucibus eget urna at, iaculis venenatis
    nulla. Vivamus a pharetra leo.

    1.  Vivamus venenatis porttitor tortor sit amet rutrum. Pellentesque aliquet
        quam enim, eu volutpat urna rutrum a. Nam vehicula nunc mauris, a
        ultricies libero efficitur sed.

    2.  Morbi eget dapibus felis. Vivamus venenatis porttitor tortor sit amet
        rutrum. Pellentesque aliquet quam enim, eu volutpat urna rutrum a.

        1.  Mauris dictum mi lacus
        2.  Ut sit amet placerat ante
        3.  Suspendisse ac eros arcu
```

## Sincronizar Construir y lanzar servidor

legos

ver [/home/daniel/tron/programas/sincronizar/libsincronizar.sh](/home/daniel/tron/programas/sincronizar/libsincronizar.sh)

# Manualito Markdown Mkdocs Material

# Tipos de Advertencias:

```yaml
Hay que colocar tres !!! la palabra clave y el título entre comillas y el texto que sigue
a tabulación de cuatro espacios.

    admonition:
      note: octicons/tag-16
      abstract: octicons/checklist-16
      info: octicons/info-16
      tip: octicons/squirrel-16
      success: octicons/check-16
      question: octicons/question-16
      warning: octicons/alert-16
      failure: octicons/x-circle-16
      danger: octicons/zap-16
      bug: octicons/bug-16
      example: octicons/beaker-16
      quote: octicons/quote-16
```

!!! info inline "Alinear a la Izquierda"

    Colocamos:
    \!\!\! info inline
    arriba del contenido al cual se desea colocar al lado.

!!! note ""
    para este cuadrito cuadrito solo !!! note ""

```

```

!!! info inline end "Alinear a la derecha"

    Colocamos:
    \!\!\! info inline end
    arriba del contenido al cual se desea colocar al lado.

??? warning "Nota Plegable"
    ??? en lugar de !!!
    Agregar un +después del ???token hace que el bloque se expanda

## Resaltar líneas específicas, numerar, título¶

!!! info "Importante"
    Las líneas específicas se pueden resaltar pasando los números de línea al hl_lines argumento
    colocado justo después del código abreviado del idioma. Tenga en cuenta que el recuento de
    líneas comienza en 1, independientemente del número de línea inicial especificado
    como parte de linenums. para título: title="burbuja.py", numerar líneas: linenums="1", pueden comenzar en otro número que no sea 1.

!!! example "Ejemplo"

    **\`\`\` hl_lines="2 3" py linenums="1" title="burbuja.py"**
    codigo
    \`\`\` 

```python
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

# Resaltar código en línea

!!!  info "Resaltar bloques de código en línea"
    El resaltado de sintaxis se puede aplicar a los bloques de código en línea prefijándolos con un shebang, es decir , seguido directamente por el código abreviado del idioma#! correspondiente .

!!! example "Ejemplo"
    The \`#!python range()\` function is used to generate a sequence of numbers.   

 The `#!python range()` function is used to generate a sequence of numbers.   

# Enlazando a una parte de otro documento:

```
Please see the \[project license](about.md#license) for further details. 
```

# Otros

## botones

```
++ctrl+alt+delete++
```

++ctrl+alt+delete++

## pestañas

```
=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
```

=== "C"

    ``` c
    #include <stdio.h>
    
    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>
    
    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

## [Link a Diagramas pueden ser para MLM ER, de flujo entre otros](https://squidfunk.github.io/mkdocs-material/reference/diagrams/)

## Resaltado

!!! info "Importante"
    los "\" no van, no se colocan, para resaltar

```
Texto puede ser {\--borrado--} y  text {\++añadido++}. Combinado {\~~en~>una simple~~} operación.
{\==Resaltado==} También es posible  {\>>añadir comentarios en línea<<}.

{\==

El Formato puede ser aplicado a bloques

\==}

\- \==mas fácil resaltado==
```

Texto puede ser {--borrado--} y  text {++añadido++}. Combinado {~~en~>una simple~~} operación.
{==Resaltado==} También es posible  {>>añadir comentarios en línea<<}.

{==

El Formato puede ser aplicado a bloques

==}

==mas fácil resaltado==

## Texto con sub y superíndices

H~2~O
A^T^A

## [link como IMAGENES](https://squidfunk.github.io/mkdocs-material/reference/images/)

## [lINK LISTAS importante las de definiciones](https://squidfunk.github.io/mkdocs-material/reference/lists/)

Cambiar el icono de Favicon
De forma predeterminada, MkDocs utiliza el icono de favorito de MkDocs . Para usar un icono diferente, cree un img subdirectorio en el docs directorio y copie su favicon.ico archivo personalizado en ese directorio. MkDocs detectará y usará automáticamente ese archivo como su ícono de favoritos.