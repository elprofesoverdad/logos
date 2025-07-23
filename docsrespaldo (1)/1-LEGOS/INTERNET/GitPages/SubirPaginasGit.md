# Subir paginas github pages

## subir tus páginas a GitHub Pages sin afectar tu dominio privado, puedes seguir los siguientes pasos:

1. Abre la terminal de tu computadora y navega hasta el directorio donde se encuentran los archivos de tu sitio web.

2. Inicializa un repositorio git en este directorio con el siguiente comando:

```bash
git init
Agrega los archivos al repositorio con el siguiente comando:
git add .
Realiza un commit con los archivos agregados:
git commit -m "Primer commit"
Crea un repositorio en GitHub y vincúlalo al repositorio local con el siguiente comando:
git remote add origin https://github.com/tu-usuario/tu-repositorio.git
Reemplaza "tu-usuario" con tu nombre de usuario de GitHub y "tu-repositorio" con el nombre del repositorio que acabas de crear.

Empuja los cambios al repositorio remoto con el siguiente comando:
git push origin master
```

## Si ya tienes tu sitio web en producción en el dominio "dreamuniversity.la" y quieres actualizarlo con las modificaciones que tienes en la rama "gh-pages" de tu repositorio de GitHub, puedes seguir los siguientes pasos:


Asegúrate de tener la última versión de la rama "gh-pages" con el siguiente comando:

```bash
git checkout gh-pages
git pull origin gh-pages
Agrega los archivos modificados al repositorio local con el siguiente comando:
git add .
Realiza un commit con los archivos modificados:
git commit -m "Actualización del sitio web"
Empuja los cambios al repositorio remoto en la rama "gh-pages" con el siguiente comando:
git push origin gh-pages
Espera unos minutos para que los cambios se reflejen en el sitio web. Puedes verificar si los cambios se han aplicado correctamente accediendo al sitio web en tu navegador.

```

## Si deseas encontrar la carpeta en tu computadora donde se encuentra el repositorio de Git, puedes utilizar el siguiente comando en tu terminal:

```bash
git rev-parse --show-toplevel
```
## Para publicar las páginas en Git Pages, asegúrate de que los archivos estén en la rama "gh-pages". Si aún no has creado esa rama, puedes crearla con el siguiente comando:
```bash
git checkout -b gh-pages
```
 ## Para ver la lista de ramas en tu repositorio de Git, puedes utilizar el siguiente comando en tu terminal:
```bash
git branch

git branch -r
```