# Mkdocs IA consultas a la IA.

## git mkdocs como con ia

```
* Crea un token de Git en GitHub siguiendo estos pasos:

* Haz clic en tu foto de perfil en la esquina superior derecha de la página de GitHub y selecciona "Settings".
* Haz clic en "Developer settings" en el menú de la izquierda.
*  Haz clic en "Personal access tokens".
* Haz clic en "Generate new token".
* Asigna un nombre a tu token y selecciona los permisos necesarios para que pueda acceder a tu repositorio.
* Haz clic en "Generate token" y copia el token generado.
* Agrega el token de Git como variable de entorno en tu computadora ejecutando el siguiente comando en la terminal:

``` bash
export GITHUB_TOKEN=<tu token de Git>
```

* Crear el sitio mkdocs y dentro de la carpeta site: ejecuta el siguiente comando para agregar los archivos generados por MkDocs al repositorio y hacer un commit en la carpeta site de mkdocs:

```bash
2021  git add .
2022  git commit -m "Inicio Sitio Henao Hung"
2023  git remote add origin git@github.com:EliasHung/HenaoHungAsociation.git
2025  git checkout master
2026  git branch -D gh-pages
2027  git reset --hard HEAD~1
2032  git branch
2033  git remote -V
2035  git status
2036  git checkout -b gh-pages
2037  ls
2038  git add index.html
2039  git commit -m "Agregada página principal"
2040  git push origin gh-pages
2041  history
```

* Ejecuta el siguiente comando para enviar los cambios al repositorio en GitHub:

```bash
git push origin main
```

* Finalmente, ve a la configuración de tu repositorio en GitHub y busca la sección "GitHub Pages". En el menú desplegable "Source", selecciona la rama gh-pages. Si todo está configurado correctamente, tu sitio web debería estar disponible en la dirección https://tuusuario.github.io/turepositorio.

## Una rama para cada ciente

* Para crear una rama en Git, puedes usar el comando "git branch nombre_de_la_rama". Por ejemplo, si deseas crear una rama para el cliente "Juan", puedes ejecutar el comando "git branch juan". Luego, puedes cambiar a la rama recién creada usando el comando "git checkout nombre_de_la_rama".

* Una vez que hayas creado las ramas para cada cliente y hayas trabajado en el sitio web de cada cliente en su propia rama, puedes hacer push de cada rama a GitHub. Cada cliente podrá ver su propio trabajo accediendo a la URL correspondiente a su rama en GitHub Pages.

* Por ejemplo, si la URL de tu sitio web es "https://tunombredeusuario.github.io/tunombrederepositorio", entonces la URL para el trabajo del cliente "Juan" sería "https://tunombredeusuario.github.io/tunombrederepositorio/juan". De esta manera, cada cliente podrá ver su propio trabajo y no tendrá acceso a la rama de otros clientes.