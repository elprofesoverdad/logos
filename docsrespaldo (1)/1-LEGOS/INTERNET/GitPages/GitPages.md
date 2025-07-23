# git pages como


## subir pagina a git pages 


hola cody he descargado una carpeta con un sitio en bootstrap, quiero entrar a la carpeta de la plantilla y crear un repositorio nuevo git y subir a git pages la plantilla la carpeta donde esta la plantilla se llama dream y quiero crear el repositorio en mi cuenta https://github.com/EliasHung. he creado un dominio en namecheat y aun no he configurado los dns yo quiero que la pagina que esta en la carpeta de la plantilla es decir la carpeta base o raiz del sitio tenga el dominio que cree en namecheat son varias cosas: crear el repositorio desde mi computadora linux ubuntu con bash, subir los archivos de la carpeta dream a github pages, a una rama posiblemente, eso no lo sé lo que si se es que el sitio debe ser escalable, luego tendra un blog y otras cosas por favor dame los comandos bash

jun. 06, 2023 10:31 AM
¡Hola! Entiendo que deseas crear un repositorio Git en tu cuenta de GitHub, subir la carpeta "dream" a Git Pages y configurar el dominio que compraste en Namecheap. Aquí están los comandos de Bash que puedes utilizar:

Crea un nuevo repositorio en tu cuenta de GitHub:
$ git init
$ git add .
$ git commit -m "Initial commit"

 aquí hay que crear el repositorio abriendo el navegador : NOMBRE_DEL_REPOSITORIO en github

$ git remote add origin https://github.com/EliasHung/NOMBRE_DEL_REPOSITORIO.git
$ git push -u origin master

Sube los archivos de la carpeta "dream" a Git Pages:
$ git checkout -b gh-pages
$ git add .
$ git commit -m "Add website files"
$ git push origin gh-pages
Configura el dominio que compraste en Namecheap:
Primero, debes agregar un registro CNAME en la configuración de DNS de tu dominio. Este registro debe apuntar a la URL de Git Pages para tu sitio. Luego, sigue estos pasos:

$ git checkout gh-pages
$ echo "www.dominio.com" > CNAME
$ git add CNAME
$ git commit -m "Add CNAME file"
$ git push origin gh-pages
Recuerda reemplazar "NOMBRE_DEL_REPOSITORIO" y "dominio.com" con los valores correctos para tu sitio.

## dominio personalizado

Primero, asegúrate de haber configurado correctamente tu sitio web en GitHub Pages. Para ello, sigue los pasos que se indican en la sección "Configuring a publishing source for your GitHub Pages site" del sitio de GitHub con los pasos siguientes:

Abre la página de configuración de tu repositorio de GitHub y desplázate hacia abajo hasta la sección "GitHub Pages".

En la sección "Source", selecciona la rama de GitHub Pages que deseas usar para tu sitio web. Si aún no has creado una rama de GitHub Pages, sigue las instrucciones en la sección "Configuring a publishing source for your GitHub Pages site" del sitio de GitHub.

En la sección "Custom domain", escribe tu dominio personalizado "dreamuniversity.lat" y haz clic en "Save".

github muestra un mensaje de error pero eso esta bien

hay que ir a namecheat y

En la sección "Advanced DNS", haz clic en "Add New Record" y selecciona "A Record" en el menú desplegable de "Type".


Ahora, debes crear un registro CNAME para asociar el subdominio "www" con el dominio raíz. Para hacerlo, haz clic en "Add New Record" y selecciona "CNAME Record" en el menú desplegable de "Type".

En el campo "Host", escribe "www" (sin comillas).

En el campo "Value", escribe "eliashung.guthub.io" (sin comillas).

En el campo "TTL", escribe "30 min" 

Haz clic en "Save All Changes" para guardar el registro CNAME.

Espera a que los cambios se propaguen en la red (esto puede tardar varias horas) y verifica que tu sitio web esté disponible en la dirección "dreamuniversity.lat" y en "www.dreamuniversity.lat".


luego hay que ir a github y rechequear los dns y listo




