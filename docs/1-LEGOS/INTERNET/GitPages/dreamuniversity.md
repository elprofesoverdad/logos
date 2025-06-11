# dreamuniversity

## github git pages

## Configurar tu repositorio en tu computadora de manera automática

1. Verifica si ya tienes una clave SSH en tu computadora. Abre una terminal y ejecuta el siguiente comando:
   
   ```
   ls -al ~/.ssh
   ```
   
   Si ves archivos con nombres como `id_rsa` y `id_rsa.pub`, significa que ya tienes una clave SSH. En ese caso, puedes saltar al paso 3. Si no ves esos archivos, continúa con el paso 2.

2. Genera una nueva clave SSH. En la misma terminal, ejecuta el siguiente comando y presiona Enter en todas las opciones por defecto:
   
   ```
   ssh-keygen -t rsa -b 4096 -C "tu_email@example.com"
   ```
   
   Esto generará una nueva clave SSH en tu directorio `~/.ssh`.

3. Copia tu clave pública al portapapeles. Ejecuta el siguiente comando para copiar tu clave pública:
   
   ```
   cat ~/.ssh/id_rsa.pub | xclip -selection clipboard
   ```
   
   Esto copiará tu clave pública al portapapeles.

4. Abre tu navegador web y ve a tu cuenta de GitHub. Haz clic en tu foto de perfil en la esquina superior derecha y selecciona "Settings".

5. En la barra lateral izquierda, haz clic en "SSH and GPG keys".

6. Haz clic en "New SSH key" o "Add SSH key".

7. En el campo "Title", puedes darle un nombre descriptivo a tu clave SSH (por ejemplo, "Xubuntu SSH Key").

8. En el campo "Key", pega la clave pública que copiaste en el paso 3.

9. Haz clic en "Add SSH key" o "Add key" para guardar la clave SSH en tu cuenta de GitHub.

Ahora que has configurado la autenticación SSH, puedes clonar tu repositorio sin tener que ingresar contraseñas. Abre una terminal y ejecuta el siguiente comando para clonar tu repositorio:

```
git clone git@github.com:EliasHung/dreamuniversity.git
```

Esto clonará tu repositorio en tu computadora y podrás administrarlo desde allí sin ingresar contraseñas.

Recuerda reemplazar `EliasHung/dreamuniversity.git` con la URL de tu repositorio.

## Modificar la rama `gh-pages` en el repositorio

## pages github

 `https://github.com/EliasHung/dreamuniversity`. Para hacerlo, necesitarás seguir los siguientes pasos:

1. Clona el repositorio en tu computadora. Abre una terminal y ejecuta el siguiente comando:
   
   ```
   git clone https://github.com/EliasHung/dreamuniversity.git
   ```
   
   Esto creará una copia local del repositorio en tu directorio actual.

2. Cambia al directorio del repositorio clonado:
   
   ```
   cd dreamuniversity
   ```

3. Verifica en qué rama te encuentras actualmente:
   
   ```
   git branch
   ```
   
   Asegúrate de estar en la rama `gh-pages`. Si no estás en esa rama, puedes cambiar a ella ejecutando el siguiente comando:
   
   ```
   git checkout gh-pages
   ```

4. Realiza las modificaciones que deseas hacer en los archivos de la rama `gh-pages`.

5. Una vez que hayas realizado los cambios, guarda los archivos y ejecuta los siguientes comandos para agregar los cambios, hacer un commit y enviarlos al repositorio remoto:
   
   ```
   git add .
   git commit -m "Descripción de los cambios realizados"
   git push origin gh-pages
   ```
   
   Esto agregará los cambios al repositorio remoto en la rama `gh-pages`.

Recuerda que necesitarás tener los permisos adecuados para poder hacer cambios en el repositorio. Si no tienes los permisos necesarios, deberás solicitarlos al propietario del repositorio.
