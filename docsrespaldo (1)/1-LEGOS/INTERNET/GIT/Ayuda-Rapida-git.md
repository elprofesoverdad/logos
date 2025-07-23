# Chuleta de Git
 [IMPORTANTE MANUAL OFICIAL GIT CLI](https://cli.github.com/manual)
#Crear nuevo repo

## Como dice Elias Hung
``` bash
Instalar la Git Cli
gh auth login
gh repo create
cd tron
git config --global user.email "elprofesorverdad@gmail.com"
git config --global user.name "EliasHung"

git add -v /home/daniel/tron/1-LEGOS/0-A-PROYECTOS /home/daniel/tron/1-LEGOS/0-ORGANIZACION /home/daniel/tron/1-LEGOS/BASES-DE-DATOS-Y-ESTRUCTURAS /home/daniel/tron/1-LEGOS/Bash /home/daniel/tron/1-LEGOS/CONFIGURACION-ESCRITORIO /home/daniel/tron/1-LEGOS/CONTROL-REMOTO /home/daniel/tron/1-LEGOS/ESTUDIO /home/daniel/tron/1-LEGOS/GIT /home/daniel/tron/1-LEGOS/INTERNET /home/daniel/tron/1-LEGOS/MULTIMEDIA /home/daniel/tron/1-LEGOS/SERVIDORES-WEB /home/daniel/tron/1-LEGOS/WEKAN /home/daniel/tron/biblioteca /home/daniel/tron/config /home/daniel/tron/data /home/daniel/tron/programas /home/daniel/tron/Scripts /home/daniel/tron/tron /home/daniel/tron/zboveda /home/daniel/tron/README.md /home/daniel/tron/plugins/bash /home/daniel/tron/config

git commit -am "primer commit desastre"
git push -u origin main
git config --global --add safe.directory /home/daniel/tron

```

> Contenido del .gitignore

``` bash
# Carpetas Ignoradas
1-LEGOS/CURSOS/
plugins/AppImage
plugins/broot
plugins/ComprimidosO.deb
plugins/FileZilla3
plugins/kaban
plugins/micro
plugins/mpv
plugins/navegadores
plugins/node
plugins/nodeStreaming
plugins/NOip
plugins/python
plugins/radio
plugins/rclone
plugins/shdoc
plugins/snap
plugins/sqlite
plugins/system
plugins/Tv
plugins/yq
```

crear un .gitignore manual:

### Algunos comandos Git CLI (gh)
[referencia de comandos](https://cli.github.com/manual/gh_help_reference)

``` bash
* Listar repo: gh repo list
* Eliminar repositorio gh:        gh repo delete [<repository>] [flags] ---> Opciones --yes eliminar sin preguntar
* [Gestionar llaves repo] (https://cli.github.com/manual/gh_repo_deploy-key)
* Editar repositorio:             gh repo edit
* Cambio de nombre:               gh repo rename [<new-name>] [flags]
* Repo establecido por defecto:   gh repo set-default [<repository>] [flags]
* Sincronización de repositorio   gh repo sync [<destination-repository>] [flags]
* Buscar en repos (toto git)      gh search repos [<query>] [flags]
* Vel estado 					  gh status [flags]


```

### Ignorar Archivos
**Fuente:** [LIBRO DE GIT ESPAÑOL](https://git-scm.com/book/es/v2)
**Fuente:** [https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring)

``` bash
$ cat .gitignore
*.[oa]
*~
```
La primera línea le dice a Git que ignore cualquier archivo que termine en ".o" o ".a": archivos de objetos y archivos que pueden ser el producto de la construcción de su código. La segunda línea le dice a Git que ignore todos los archivos cuyos nombres terminen con una tilde ( ~)
Las reglas para los patrones que puede poner en el .gitignorearchivo son las siguientes:

* Las líneas en blanco o las líneas que comienzan con #se ignoran.
* Los patrones globales estándar funcionan y se aplicarán recursivamente a lo largo de todo el árbol de trabajo.
* Puede comenzar los patrones con una barra diagonal ( /) para evitar la recursividad.
* Puede finalizar los patrones con una barra diagonal ( /) para especificar un directorio.
* Puede negar un patrón comenzando con un signo de exclamación ( !).

Los patrones globales son como expresiones regulares simplificadas que usan los shells. Un asterisco ( *) coincide con cero o más caracteres; [abc]coincide con cualquier carácter dentro de los corchetes (en este caso, a, b o c); un signo de interrogación ( ?) coincide con un solo carácter; y los corchetes que encierran caracteres separados por un guión ( [0-9]) coinciden con cualquier carácter entre ellos (en este caso, del 0 al 9). También puede usar dos asteriscos para hacer coincidir directorios anidados; a/**/zcoincidiría con a/z, a/b/z, a/b/c/z, y así sucesivamente.

Aquí hay otro .gitignorearchivo de ejemplo:
``` bash
# ignore all .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf
```

## Como dice Alex 
[https://gist.github.com/alexpchin/dc91e723d4db5018fef8](https://gist.github.com/alexpchin/dc91e723d4db5018fef8)

``` bash
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:alexpchin/<reponame>.git
git push -u origin master
añadir
git add
```
## Como dice Sarah sin la cli

``` bash
git init
git add .
git commit -m "add my files"
git remote add origin <url>
git push -u origin main
```

## Como dice Sarah con la CLI de github
[https://www.techielass.com/create-a-new-github-repository-from-the-command-line/](https://www.techielass.com/create-a-new-github-repository-from-the-command-line/)

``` bash
gh auth login
git init
git add .
git commit -m "initial commit"
gh auth login
gh repo create my-newrepo --public --source=. --remote=upstream --push
```



# Notas del curso de Harvard

``` bash

instantanea con mensaje
git commit -m "mensaje"

instantarnea agregando los ultimos cambios y mensaje

git commit -am "mensaje"

ver mi llave ssh
eval $(ssh-agent -s)

crear la llave ssh para git
ssh-keygen -t ed25519 -C elias1hung@gmail.com

agregar la llave al servicio de llaves
ssh-add ~/.ssh/id_ed25519

la llave esta guardada en  
~/.ssh/

para ver la llave 
cat ~/.ssh/id_ed25519.pub

esa llave es la que se coloca en el sitio web de git

ver el log
git log

volver al commit anterior
git reset

regresar al ultimo commit
git reset --hard hash_de_commit

regresar a lo que sea que este en github
git reset --hard origin/master

cuantas ramas tengo y donde esta la cabeza
git branch
(el asterisco de la salida dice donde esta la cabeza)

crear una nueva rama de desarrollo
git checkout rombre_rama

fusionar rama cualquiera a actual
primero me ubico en la rama que va a ser afectada
git checkout actual
git merge cualquiera 

NOTA: despues de resolver los conflixtos solo hacer git commit -am "resolucion de conflictox"

bifurcar tener una copia local

GitHub Pages : GitHub Pages es una forma sencilla de publicar un sitio estático en la web. (Aprenderemos más adelante sobre sitios estáticos y dinámicos). Para hacer esto:
Cree un nuevo repositorio de GitHub.
Clone el repositorio y realice cambios localmente, asegurándose de incluir un index.htmlarchivo que será la página de destino de su sitio web.
Empuje esos cambios a GitHub.
Navegue a la página Configuración de su repositorio, desplácese hacia abajo hasta Páginas de GitHub y elija la rama maestra en el menú desplegable.
Desplácese hacia abajo hasta la parte Páginas de GitHub de la página de configuración, y después de unos minutos, debería ver una notificación que dice "Su sitio está publicado en: ..." ¡incluyendo una URL donde puede encontrar su sitio!
``` 



