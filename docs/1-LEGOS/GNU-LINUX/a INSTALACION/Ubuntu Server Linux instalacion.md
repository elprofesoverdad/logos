# Instalar una ISO  pendrive Ventoy Ubuntu Server Linux instalacion 

# Manual detallado para instalar una ISO mediante un pendrive usando Ventoy (Ubuntu Server como ejemplo)

Este manual explica paso a paso y con justificaciones técnicas, cómo preparar un pendrive con Ventoy para instalar una distribución Linux (usando como ejemplo `ubuntu-22.04.5-live-server-amd64.iso`) en cualquier computadora. Funciona en sistemas GNU/Linux como Ubuntu o Kubuntu.

---

## 📁 Requisitos previos

* Una PC con Linux (Ubuntu, Kubuntu, Debian, etc.)
* Un pendrive USB de al menos 8 GB (se borrará por completo)
* ISO de Ubuntu descargada en tu carpeta de Descargas
* Ventoy (descargado desde [https://www.ventoy.net/en/download.html](https://www.ventoy.net/en/download.html))

---

## ✅ Paso 1: Descargar y extraer Ventoy

1. Abre una terminal y ubícate en la carpeta de Descargas:

```bash
cd ~/Descargas
```

2. Descarga Ventoy (si no lo tienes):

```bash
wget https://github.com/ventoy/Ventoy/releases/download/v1.1.05/ventoy-1.1.05-linux.tar.gz
```

3. Extrae el archivo:

```bash
tar -xzvf ventoy-1.1.05-linux.tar.gz
cd ventoy-1.1.05
```

---

## 🔧 Paso 2: Instalar Ventoy en el pendrive

> **Advertencia:** Todos los datos del USB se borrarán. Asegúrate de hacer copia de seguridad.

1. Conecta el pendrive USB a tu PC.
2. Identifica el nombre del dispositivo USB:

```bash
lsblk
```

Busca el nombre del dispositivo según su tamaño (por ejemplo `/dev/sda`).

3. Instala Ventoy:

```bash
sudo sh Ventoy2Disk.sh -i /dev/sda
```

Confirma dos veces escribiendo `y` cuando te lo solicite.

Ventoy creará dos particiones:

* Una pequeña para el gestor de arranque
* Otra grande con formato exFAT donde colocarás las ISOs

---

## 📂 Paso 3: Montar la partición Ventoy y copiar la ISO

1. Monta la partición con etiqueta "Ventoy":

```bash
udisksctl mount -b /dev/disk/by-label/Ventoy
```

2. Copia la ISO directamente a la raíz del USB:

```bash
cp ~/Descargas/ubuntu-22.04.5-live-server-amd64.iso /media/daniel/Ventoy/
```

Verás un mensaje como:

```
'/home/daniel/Descargas/ubuntu-22.04.5-live-server-amd64.iso' -> '/media/daniel/Ventoy/ubuntu-22.04.5-live-server-amd64.iso'
```

3. Asegura que los datos se escriban correctamente:

```bash
sync
```

4. Desmonta el USB:

```bash
udisksctl unmount -b /dev/disk/by-label/Ventoy
```

---

## 🚀 Paso 4: Usar el pendrive en otra PC para instalar Ubuntu

1. Inserta el pendrive en la computadora de destino.
2. Enciende la PC y entra al menú de arranque (F12, ESC, F10, etc.).
3. Selecciona el dispositivo USB.
4. Verás el menú de Ventoy mostrando la ISO copiada.
5. Selecciona la ISO `ubuntu-22.04.5-live-server-amd64.iso` y presiona Enter.

Se iniciará el proceso de instalación de Ubuntu Server.

---

## 🧪 Paso 5: Verificar red y acceder al servidor por SSH

1. En el servidor (recién instalado), abre la terminal y obtén su IP con:

```bash
ifconfig
```

Busca la IP local asignada, por ejemplo `172.16.0.191`

2. Desde tu laptop, instala `nmap` si no lo tienes:

```bash
sudo apt install nmap
```

3. Verifica si el puerto SSH está abierto:

```bash
nmap -p 22 172.16.0.191
```

Ejemplo de resultado:

```
PORT   STATE SERVICE
22/tcp open  ssh
```

4. Conéctate por SSH:

```bash
ssh daniel@172.16.0.191
```

Se mostrará algo como:

```
The authenticity of host '172.16.0.191 (172.16.0.191)' can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '172.16.0.191' to the list of known hosts.
daniel@172.16.0.191's password:
```

Introduce la contraseña del servidor y accederás a la consola remota.

---

## ✅ Justificación técnica de por qué funciona

* **Ventoy crea un gestor de arranque personalizado** compatible con UEFI/BIOS.
* **La ISO no se quema**, sino que se monta directamente desde el USB.
* **Copia simple = mantenimiento fácil**: solo agregas/quitas archivos ISO en el pendrive.
* **Compatibilidad total** con sistemas Linux y otros (Windows, utilitarios, etc.).

---

## Instalación de Programas

Perfecto, aquí va una versión más concisa y pulida para el manual, que incluye instalación y configuración automática de **micro** con tus preferencias, además de **Midnight Commander (`mc`)**:

---

## 🛠️ Instalación Rápida – micro + mc

### 1. Instalar micro (versión más reciente y sin dependencias pesadas)

```bash
curl https://getmic.ro | bash        # Descarga el instalador
sudo mv micro /usr/local/bin/       # Lo mueve al PATH del sistema
micro --version                     # Verifica instalación
```

Este método instala una **versión actualizada estática** de micro, más reciente que la del repositorio APT ([GeeksforGeeks][1], [GitHub][2]).

---

### 2. Instalar Midnight Commander (`mc`)

```bash
sudo apt update
sudo apt install -y mc
```

`mc` es el manejador de archivos en consola por excelencia: doble panel, atajos, conversiones, edición, FTP, etc.&#x20;

---

### 3. Configurar micro como editor por defecto

```bash
sudo update-alternatives --install /usr/bin/editor editor /usr/local/bin/micro 40
sudo update-alternatives --config editor    # Elegir micro como opción predeterminada
```

Así `editor`, `VISUAL` y scripts que llamen `$EDITOR` usarán micro .

---

### 4. Establecer configuración personalizada automáticamente

Tu configuración preferida para micro:

```json
{
  "mkparents": true,
  "paste": true,
  "savecursor": true,
  "saveundo": true,
  "scrollbar": true,
  "softwrap": true,
  "tabstospaces": true,
  "wordwrap": true
}
```

Para aplicarla automáticamente, usa este comando:

```bash
install -d ~/.config/micro && \
cat > ~/.config/micro/settings.json << 'EOF'
{
    "mkparents": true,
    "paste": true,
    "savecursor": true,
    "saveundo": true,
    "scrollbar": true,
    "softwrap": true,
    "tabstospaces": true,
    "wordwrap": true
}
EOF
```

Esto crea de una sola vez la carpeta y el archivo de configuración, igualando tu setup local.

---

### ✅ Resumen final de comandos

```bash
# 1. Instalar micro
curl https://getmic.ro | bash && sudo mv micro /usr/local/bin/ && micro --version

# 2. Instalar mc
sudo apt update && sudo apt install -y mc

# 3. Registrar micro como editor por defecto
sudo update-alternatives --install /usr/bin/editor editor /usr/local/bin/micro 40
sudo update-alternatives --config editor

# 4. Configurar micro con tus preferencias
install -d ~/.config/micro
cat > ~/.config/micro/settings.json << 'EOF'
{ "mkparents": true, "paste": true, "savecursor": true, "saveundo": true, "scrollbar": true, "softwrap": true, "tabstospaces": true, "wordwrap": true }
EOF
```

---

Con esto tendrás un **editor moderno** (`micro`) perfectamente configurado, y un **explorador eficiente** (`mc`) por consola, listos para desarrollar scripts, editar configuraciones y documentar tu instalación automática de LAMP y OpenCart.

¿Te preparo un script completo con todo esto, y luego pasamos a la instalación LAMP+OpenCart+Cloudflared?

[1]: https://www.geeksforgeeks.org/linux-unix/micro-lightweight-terminal-based-text-editor/?utm_source=chatgpt.com "Micro - Lightweight terminal based text editor - GeeksforGeeks"
[2]: https://github.com/zyedidia/micro?utm_source=chatgpt.com "zyedidia/micro: A modern and intuitive terminal-based text editor"






---

## ✅ Instalación rápida del stack LAMP

Ubuntu incluye un **metapaquete** llamado `lamp-server^` (nota la traílla `^`) que instala:

* Apache (servidor web)
* MariaDB/MySQL (base de datos)
* PHP y extensiones básicas

Con tu comando:

```bash
sudo apt-get update
sudo apt-get install lamp-server^
```

Obtener todo de una vez es más conveniente y seguro, ideal para entornos de desarrollo o VM. ([digitalocean.com][1], [cherryservers.com][2], [askubuntu.com][3])

---

### ⚠️ Recuerda

* `lamp-server^` cubre la instalación, **pero no aplica configuraciones adicionales** como:

  * Asegurar MariaDB (`mysql_secure_installation`)
  * Habilitar `mod_rewrite` en Apache (`a2enmod rewrite`)
  * Crear hosts virtuales
* Por tanto, siempre recomiendo combinar este comando inicial con pasos adicionales específicos para tu tienda.



## Instalacion de dependencias de Opencart

``` bash
sudo apt update && \
sudo apt install -y apache2 libapache2-mod-php \
  php-curl php-zip php-gd php-mbstring php-xml php-mysqli php-intl \
  zlib1g-dev && \
sudo a2enmod rewrite ssl headers && \
sudo systemctl restart apache2


```

---

## 🔄 Ejemplo completo combinado

Aquí tienes el flujo optimizado para el manual automatizado:

```bash
sudo apt-get update
sudo apt-get install lamp-server^ -y

# Seguridad de la base de datos
sudo mysql_secure_installation

# Habilitar Apache rewrite
sudo a2enmod rewrite
sudo systemctl restart apache2
```


---

### 📝 ¿Cómo lo incluyo en tu documento “bola de nieve”?

Añadiré una sección breve justo después del punto “Instalación LAMP”:

* `sudo apt-get install lamp-server^` para preparar todo el stack base en un solo paso.
* Luego sigue con ajustes de seguridad y configuración según tu entorno.

---

¿Te parece bien este enfoque? Si prefieres desglosar los componentes (Apache, PHP, MariaDB) uno a uno para mayor control, también puedo hacerlo.

[1]: https://www.digitalocean.com/community/tutorials/how-to-install-lamp-stack-on-ubuntu?utm_source=chatgpt.com "How To Install LAMP Stack (Apache, MySQL, PHP) on Ubuntu"
[2]: https://www.cherryservers.com/blog/install-lamp-on-ubuntu-22-04?utm_source=chatgpt.com "How to Install LAMP Stack on Ubuntu 22.04 [6 Steps] - Cherry Servers"
[3]: https://askubuntu.com/questions/785440/how-to-install-lamp-server-on-ubuntu?utm_source=chatgpt.com "How to Install LAMP server on Ubuntu [duplicate]"
---

## 🛡️ Detalles y respuestas para `mysql_secure_installation`

### 1. **VALIDATE PASSWORD COMPONENT**

```plaintext
VALIDATE PASSWORD COMPONENT can be used to test passwords...
Press y|Y for Yes, any other key for No:
```

**¿Qué hace?** Activa un plugin que evalúa la fortaleza de las contraseñas nuevas ([DigitalOcean][1]).
**Respuesta recomendada:** `y` — para habilitar control de contraseñas y mantener seguridad básica. Luego elige el nivel.

---

### 2. **Nivel de política de contraseñas**

```plaintext
Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG:
```

* `0 (LOW)`: mínima de 8 caracteres
* `1 (MEDIUM)`: incluye mayúsculas, minúsculas, números y símbolos
* `2 (STRONG)`: además compara con diccionario ([DigitalOcean][1])
  **Recomendación:** `1` si deseas balance entre seguridad y usabilidad (como seleccionaste antes). `2` si quieres máxima seguridad.

---

### 3. **Establecer contraseña para root**

```plaintext
Please set the password for root here.
```

Si estás usando `auth_socket` (autenticación sin contraseña), este paso se salta y no se cambia ([DigitalOcean][1]).
**En tu caso:** Si no configuraste contraseña, puedes ignorarlo (solo presiona Enter). O alternar plugin luego con `ALTER USER` para usarla.

---

### 4. **Confirmar uso de la contraseña**

```plaintext
Do you wish to continue with the password provided? (Press y|Y for Yes, any other key for No):
```

**Tú**: si te salteaste, presiona `Y` para continuar sin cambiar.

---

### 5. **Eliminar usuarios anónimos**

```plaintext
Remove anonymous users? (Press y|Y for Yes, any other key for No):
```

**Qué hace:** elimina accesos que permiten login sin credenciales .
**Respuesta recomendada:** `y` — aumenta la seguridad.

---

### 6. **Deshabilitar login remoto de root**

```plaintext
Disallow root login remotely? (Press y|Y for Yes, any other key for No):
```

Evita conexiones root desde IP externas.
**Recomendado:** `y` — permites solo accesos SSH+sudo.

---

### 7. **Eliminar base de datos de pruebas**

```plaintext
Remove test database and access to it? (Press y|Y for Yes, any other key for No):
```

Elimina base `test` que puede ser explotada.
**Respuesta:** `y` — más seguridad ([phoenixNAP | Global IT Services][2]).

---

### 8. **Recargar privilegios**

```plaintext
Reload privilege tables now? (Press y|Y for Yes, any other key for No):
```

Aplica inmediatamente los cambios.
**Respuesta:** `y`.

---

## 🧾 Resumen de respuestas ideal

| Pregunta                           |     Respuesta     |
| ---------------------------------- | :---------------: |
| Setup VALIDATE PASSWORD COMPONENT? |        `y`        |
| Nivel de política (0/1/2)?         |        `1`        |
| Establecer contraseña root?        | Enter (`saltado`) |
| Continuar con esa contraseña?      |        `y`        |
| Remove anonymous users?            |        `y`        |
| Disallow root login remotely?      |        `y`        |
| Remove test database?              |        `y`        |
| Reload privilege tables now?       |        `y`        |

Esto es lo típico para **entornos productivos/servidores**, balanceando seguridad y usabilidad ([DigitalOcean][1], [phoenixNAP | Global IT Services][2]).

---

## ✅ Incluir en tu manual

Agregaré esta sección en el punto “Seguridad de MariaDB” del manual tipo:

> 🛡️ **mysql\_secure\_installation**
> Responde paso a paso:
>
> * `y` → activar validación
> * `1` → política MEDIUM
> * Enter → saltar cambio de contraseña si usas `auth_socket`
> * `y`, `y`, `y`, `y` → eliminar anónimos, deshabilitar root remoto, borrar DB test y recargar privilegios.
>
> > Esto asegura tu servidor sin bloquear funcionalidades esenciales.

¿Quieres que prepare un script / automatización para realizar esto sin intervención interactiva?

[1]: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04?utm_source=chatgpt.com "How to Install MySQL on Ubuntu – Step-by-Step Guide | DigitalOcean"
[2]: https://phoenixnap.com/kb/mysql-secure-installation?utm_source=chatgpt.com "mysql_secure_installation Script {+Extensive List of Script Options}"


## Abrir una cuenta en Gmail nueva, comprar el dominio y el Hospedaje.

## Configuración de Cloudflare Tunnel para exponer Apache/OpenCart en Ubuntu Server

Este manual documenta paso a paso la instalación, configuración, corrección de errores y puesta en marcha exitosa de un túnel de Cloudflare para exponer un servidor LAMP (Apache + OpenCart) bajo un dominio con subdominio, usando Cloudflare Tunnel.


---

## 1. Instalación de Cloudflared

```bash
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
```

Verificación:

```bash
cloudflared --version
```

---

## 2. Login a Cloudflare y generación de credenciales

```bash
cloudflared tunnel login
```

Esto abrirá una URL en el navegador para autorizar el servidor. Tras la autorización se crea el archivo `cert.pem` en `~/.cloudflared/`.

---

## 3. Crear el túnel

```bash
cloudflared tunnel create tienda-tunnel
```

Esto genera un archivo `.json` con credenciales del túnel en `~/.cloudflared/`.

Ejemplo:

```
/home/daniel/.cloudflared/48f9e81b-830a-4745-a61c-4aaa79ed5acc.json
```

---

## 4. Asignar DNS al túnel en Cloudflare

```bash
cloudflared tunnel route dns tienda-tunnel tienda.mettgorras.uk
```

Esto crea un registro **CNAME** automático en Cloudflare apuntando el subdominio `tienda.mettgorras.uk` al túnel.

---

## 5. Crear el archivo de configuración `config.yml`

Ubicación: `~/.cloudflared/config.yml`

Contenido corregido:

```yaml
tunnel: 48f9e81b-830a-4745-a61c-4aaa79ed5acc
credentials-file: /home/daniel/.cloudflared/48f9e81b-830a-4745-a61c-4aaa79ed5acc.json

ingress:
  - hostname: tienda.mettgorras.uk
    service: http://localhost:80
  - service: http_status:404
```

> ❌ Nota: **No se permite usar paths como `/dotecomerce/` en el campo `service`.** Cloudflare no admite rutas. Solo hostname y puerto.

---

## 6. Ejecutar el túnel manualmente (diagnóstico)

```bash
cloudflared tunnel --config ~/.cloudflared/config.yml run
```

### Resultado esperado:

```
INF Connection established
INF Route: tienda.mettgorras.uk => http://localhost:80
```

Verificación:

```bash
curl -I https://tienda.mettgorras.uk
```

Debe responder:

```
HTTP/2 200 OK
```

---

## 7. (Opcional) Crear servicio systemd manualmente

```bash
sudo tee /etc/systemd/system/cloudflared.service > /dev/null <<EOF
[Unit]
Description=Cloudflared Tunnel (manual)
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/cloudflared tunnel --config /home/daniel/.cloudflared/config.yml run
Restart=always
RestartSec=5
User=daniel

[Install]
WantedBy=multi-user.target
EOF
```

Activar servicio:

```bash
sudo systemctl daemon-reload
sudo systemctl enable cloudflared
sudo systemctl restart cloudflared
systemctl status cloudflared
```

---

## ✅ Resultado final

Tienda accesible vía:

```
https://tienda.mettgorras.uk
```

Túnel Cloudflare activo permanentemente, iniciando al encender el servidor.


---

# Continuación del Manual: Configuración Apache para tienda OpenCart

## 1. Crear archivo de VirtualHost para tienda.mettgorras.uk

```bash
sudo tee /etc/apache2/sites-available/tienda.conf > /dev/null <<EOF
<VirtualHost *:80>
  ServerName tienda.mettgorras.uk
  DocumentRoot /var/www/html/tienda
  <Directory /var/www/html/tienda>
    Options -Indexes +FollowSymLinks
    AllowOverride All
    Require all granted
  </Directory>
  ErrorLog \${APACHE_LOG_DIR}/tienda_error.log
  CustomLog \${APACHE_LOG_DIR}/tienda_access.log combined
</VirtualHost>
EOF

```

## 2. Crear VirtualHost para proteger la raíz (`/`)

```bash
sudo tee /etc/apache2/sites-available/default-root.conf > /dev/null <<EOF
<VirtualHost *:80>
  ServerName mettgorras.uk
  DocumentRoot /var/www/html/default-root

  <Directory /var/www/html/default-root>
    Options -Indexes
    AllowOverride None
    Require all denied
  </Directory>

  ErrorLog \${APACHE_LOG_DIR}/default_error.log
  CustomLog \${APACHE_LOG_DIR}/default_access.log combined
</VirtualHost>
EOF
```

## 3. Crear carpetas y archivos necesarios

```bash
sudo mkdir -p /var/www/html/{dotecomerce,default-root}
echo "<h1>No disponible</h1>" | sudo tee /var/www/html/default-root/index.html
```

## 4. Activar y aplicar configuración

```bash
sudo a2ensite tienda.conf
sudo a2ensite default-root.conf
sudo a2dissite 000-default.conf
sudo systemctl reload apache2
```

## 5. Verificación local y por tunnel

```bash
curl -I http://localhost/                 # Debe dar 403 o acceso denegado
curl -I http://localhost/tienda           # Si pruebas acceso directo
curl -I http://tienda.mettgorras.uk       # Desde Cloudflare Tunnel
```

---

Esta configuración asegura que solo `tienda.mettgorras.uk` sirve contenido desde OpenCart y protege la raíz de Apache para no exponer nada por accidente.


---

# Continuación del Manual: Configuración Apache para tienda OpenCart

## 1. Crear archivo de VirtualHost para tienda.mettgorras.uk

```bash
sudo tee /etc/apache2/sites-available/tienda.conf > /dev/null <<EOF
<VirtualHost *:80>
  ServerName tienda.mettgorras.uk

  DocumentRoot /var/www/html/tienda

  <Directory /var/www/html/tienda>
    Options -Indexes +FollowSymLinks
    AllowOverride All
    Require all granted
  </Directory>

  ErrorLog \${APACHE_LOG_DIR}/tienda_error.log
  CustomLog \${APACHE_LOG_DIR}/tienda_access.log combined
</VirtualHost>
EOF
```

## 2. Crear VirtualHost para proteger la raíz (`/`)

```bash
sudo tee /etc/apache2/sites-available/default-root.conf > /dev/null <<EOF
<VirtualHost *:80>
  ServerName mettgorras.uk
  DocumentRoot /var/www/html/default-root

  <Directory /var/www/html/default-root>
    Options -Indexes
    AllowOverride None
    Require all denied
  </Directory>

  ErrorLog \${APACHE_LOG_DIR}/default_error.log
  CustomLog \${APACHE_LOG_DIR}/default_access.log combined
</VirtualHost>
EOF
```

## 3. Crear carpetas y archivos necesarios

```bash
sudo mkdir -p /var/www/html/{tienda,default-root}
echo "<h1>Tienda OpenCart activa</h1>" | sudo tee /var/www/html/tienda/index.html
echo "<h1>No disponible</h1>" | sudo tee /var/www/html/default-root/index.html
```

## 4. Activar y aplicar configuración (en una sola línea)

```bash
sudo a2ensite tienda.conf default-root.conf && sudo a2dissite 000-default.conf && sudo systemctl reload apache2
```

## 5. Verificación local y por tunnel

```bash
curl -I http://localhost/                 # Debe dar 403 o acceso denegado
curl -I http://tienda.mettgorras.uk       # Desde Cloudflare Tunnel
```

---

Esta configuración asegura que solo `tienda.mettgorras.uk` sirve contenido desde OpenCart y protege la raíz de Apache para no exponer nada por accidente.

## 6. Revertir configuración en un solo comando

Para deshacer rápidamente todo en la máquina equivocada, ejecuta:

```bash
sudo a2dissite tienda.conf default-root.conf && sudo a2ensite 000-default.conf && \
sudo rm -f /etc/apache2/sites-available/tienda.conf /etc/apache2/sites-available/default-root.conf && \
sudo rm -rf /var/www/html/tienda /var/www/html/default-root && \
sudo systemctl reload apache2
```

Este comando:

* Deshabilita los VirtualHosts `tienda` y `default-root`, y reactiva el host por defecto `000-default`.
* Elimina los archivos de configuración y los directorios creados.
* Recarga Apache para que vuelva a la configuración original.

---

## Si MySQL falla y no tienes la contraseña

Claro, vamos a resolverlo paso a paso agregando la solución probada para que puedas resetear la contraseña de `root` en MySQL correctamente incluso con los errores que salieron. Basado en casos reales que incluyeron la falta de `/var/run/mysqld` o que ya existía otro proceso de mysqld activo, aquí tienes una guía actualizada:

---

## 🔐 Restablecer contraseña `root` de MySQL en Ubuntu (Cuando `skip-grant-tables` falla)

### 🧪 Diagnóstico del problema

Si al intentar conectarte con:

```bash
mysql -u root
```

o al correr el modo seguro:

```bash
sudo mysqld_safe --skip-grant-tables --skip-networking &
```
**importante...  presionar enter para que puedas salir del letargo de la consola...**


obtienes errores como:

* `Directory '/var/run/mysqld' ... doesn't exist`
* `A mysqld process already exists`
* `Access denied`

Esto suele deberse a:

* El servicio MySQL aún no se detuvo totalmente;
* No existe el directorio `/var/run/mysqld`;
* El archivo `.pid` sobrante bloquea el inicio del nuevo proceso.

---

### ✅ Pasos para resolverlo

#### 1. Detener MySQL completamente

```bash
sudo systemctl stop mysql
```

Luego verifica que no haya procesos de mysqld en ejecución:

```bash
ps aux | grep mysqld
```

Si encuentras alguno, termina con:

```bash
sudo kill PID_del_proceso
```

#### 2. Crear el directorio necesario y ajustar permisos

```bash
sudo mkdir -p /var/run/mysqld
sudo chown mysql:mysql /var/run/mysqld
```

Esto evita el error por falta del directorio o permisos insuficientes ([Ask Ubuntu][1], [dev.mysql.com][2]).

#### 3. Iniciar el servidor en modo seguro (skip-grant-tables)

```bash
sudo mysqld_safe --skip-grant-tables --skip-networking &
```

Este modo evita cargar tablas de permisos y deshabilita conexiones externas, útil para recuperación .

#### 4. Conectarse como root sin contraseña

```bash
mysql -u root
```

#### 5. En el prompt de MySQL, recargar privilegios y cambiar la contraseña

```sql
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Copa007copa.';
FLUSH PRIVILEGES;
EXIT;

```

O si el `ALTER USER` falla (error 1290), usa:

```sql
USE mysql;
UPDATE user SET authentication_string = '' WHERE user='root' AND host='localhost';
-- O SET PASSWORD FOR 'root'@'localhost' = PASSWORD('...') según versión
FLUSH PRIVILEGES;
EXIT;
```

([LinuxConfig][3])

#### 6. Cerrar el modo seguro y reiniciar MySQL

```bash
sudo killall mysqld
sudo systemctl start mysql
```

#### 7. Verificar acceso con contraseña

```bash
mysql -u root -p
```

Ingresa la contraseña recién creada.

---

## 📝 Integración en el manual de migración (para producción)

Esta sección debe ubicarse **antes** del paso que crea la base de datos, para asegurar acceso delegado desde root sin fallos por `auth_socket`.

---

## 🔐 Mejoras opcionales de seguridad tras resetear la contraseña

Una vez hayas iniciado sesión como root, puedes:

```sql
DELETE FROM mysql.user WHERE User = '';
DROP DATABASE IF EXISTS test;
FLUSH PRIVILEGES;
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'TuContraseñaFuerte#2025';
```

Y asegurar `root` solo localmente:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'TuContraseñaFuerte#2025';
FLUSH PRIVILEGES;
```

O incluso restablecer el plugin `auth_socket` si prefieres. También considera configurar `bind-address = 127.0.0.1` en `/etc/mysql/mysql.conf.d/mysqld.cnf` y eliminar remote root ([LinuxHostSupport][4], [Server Fault][5]).

---

¿Quieres que ahora actualice el manual con esta sección completa? O prefieres añadirle directamente también la parte de creación de bases y migración posterior?

[1]: https://askubuntu.com/questions/878652/unable-to-reset-mysql-root-password-tried-everthing?utm_source=chatgpt.com "Unable to reset MySQL root password, tried everthing - Ask Ubuntu"
[2]: https://dev.mysql.com/doc/en/resetting-permissions.html?utm_source=chatgpt.com "B.3.3.2 How to Reset the Root Password - MySQL :: Developer Zone"
[3]: https://linuxconfig.org/how-to-reset-mysql-root-password-on-your-linux-server?utm_source=chatgpt.com "How to reset MySQL root password on your Linux server - LinuxConfig"
[4]: https://linuxhostsupport.com/blog/how-to-reset-your-mysql-or-mariadb-root-password-on-ubuntu-22-04/?utm_source=chatgpt.com "How to Reset Your MySQL or MariaDB Root Password on Ubuntu ..."
[5]: https://serverfault.com/questions/933844/stuck-trying-change-mysql-root-password?utm_source=chatgpt.com "Stuck trying change mysql root password - Server Fault"

# Manual de Migración OpenCart: desde entorno dev local a servidor cliente por SSH

Este procedimiento replica la instalación de OpenCart desde tu entorno `localhost/dotecomerce-dev` en tu laptop hacia el servidor Ubuntu conectado por SSH (vía Cloudflared o red local).

---

## 🌟 Opcion recomendada: Cambiar autenticación del root para usar contraseña (modo producción)

Si obtienes este error:

```
ERROR 1698 (28000): Access denied for user 'root'@'localhost'
```

Significa que `root` está usando `auth_socket` para autenticarse. Para permitir acceso con contraseña:

```bash
sudo mysql -u root
```

Dentro del prompt de MySQL:

```sql
UNINSTALL COMPONENT 'file://component_validate_password';
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Copa007copa.';
FLUSH PRIVILEGES;
EXIT;
```

Luego verifica acceso:

```bash
mysql -u root -p
```

---

## Replicar el opencart Modelo, instalado.

* Replicar OpenCart instalado localmente en `/var/www/html/dotecomerce-dev` con storage en `/var/www/storage-dev/`
* Transferirlo a: `/var/www/html/tienda` y `/var/www/storage` en el servidor remoto
* Configurar correctamente los archivos `config.php` para el dominio de producción: `https://tienda.mettgorras.uk/`

---

## 1. Crear backup desde entorno local

```bash
mkdir -p ~/Escritorio/backupTienda && \
tar czvpf ~/Escritorio/backupTienda/tienda.tar.gz -C /var/www/html/dotecomerce-dev . --same-owner && \
tar czvpf ~/Escritorio/backupTienda/storage.tar.gz -C /var/www/storage-dev . --same-owner && \
mysqldump -u root -p opencart2 > ~/Escritorio/backupTienda/db.sql
```

---

## 2. Copiar backups al servidor remoto (vía SSH)

Ejecutar desde la **laptop local**:

```bash
scp ~/Escritorio/backupTienda/* daniel@172.16.0.191:/tmp/
```

---

## 3. Restaurar en el servidor remoto

Conectado por SSH al servidor:

```bash
# Crear directorios definitivos
sudo mkdir -p /var/www/html/tienda /var/www/storage

# Extraer archivos
sudo tar xzvpf /tmp/tienda.tar.gz -C /var/www/html/tienda
sudo tar xzvpf /tmp/storage.tar.gz -C /var/www/storage

# Asignar permisos
sudo chown -R www-data:www-data /var/www/html/tienda /var/www/storage
sudo chmod -R 755 /var/www/html/tienda /var/www/storage

# Crear base de datos
mysql -u root -p -e "
CREATE DATABASE opencart2 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'opencart1'@'localhost' IDENTIFIED BY 'Copa007copa.';
GRANT ALL PRIVILEGES ON opencart2.* TO 'opencart1'@'localhost';
FLUSH PRIVILEGES;"

# Importar base de datos
mysql -u root -p opencart2 < /tmp/db.sql
```

---

## 4. Configurar config.php y admin/config.php

```bash
sudo micro /var/www/html/tienda/config.php
```

```php
<?php
define('APPLICATION', 'Catalog');
define('HTTP_SERVER', 'https://tienda.mettgorras.uk/');
define('HTTPS_SERVER', 'https://tienda.mettgorras.uk/');
define('DIR_OPENCART', '/var/www/html/tienda/');
define('DIR_APPLICATION', DIR_OPENCART . 'catalog/');
define('DIR_EXTENSION', DIR_OPENCART . 'extension/');
define('DIR_IMAGE', DIR_OPENCART . 'image/');
define('DIR_SYSTEM', DIR_OPENCART . 'system/');
define('DIR_STORAGE', '/var/www/storage/');
define('DIR_LANGUAGE', DIR_APPLICATION . 'language/');
define('DIR_TEMPLATE', DIR_APPLICATION . 'view/template/');
define('DIR_CONFIG', DIR_SYSTEM . 'config/');
define('DIR_CACHE', DIR_STORAGE . 'cache/');
define('DIR_DOWNLOAD', DIR_STORAGE . 'download/');
define('DIR_LOGS', DIR_STORAGE . 'logs/');
define('DIR_SESSION', DIR_STORAGE . 'session/');
define('DIR_UPLOAD', DIR_STORAGE . 'upload/');
define('DB_DRIVER', 'mysqli');
define('DB_HOSTNAME', 'localhost');
define('DB_USERNAME', 'opencart1');
define('DB_PASSWORD', 'Copa007copa.');
define('DB_DATABASE', 'opencart2');
define('DB_PORT', '3306');
define('DB_PREFIX', 'oc_');



```

```bash
sudo micro /var/www/html/tienda/admin(copa007copa )/config.php

Importante: el admin es el que se eligió al cambiar el nombre mosca... en este caso
es copa007copa 
```

```php
<?php
define('APPLICATION', 'Admin');
define('OPENCART_SERVER', 'https://www.opencart.com/');
define('HTTP_SERVER', 'https://tienda.mettgorras.uk/copa007copa/');
define('HTTP_CATALOG', 'https://tienda.mettgorras.uk/');
define('DIR_OPENCART', '/var/www/html/tienda/');
define('DIR_APPLICATION', '/var/www/html/tienda/copa007copa/');
define('DIR_EXTENSION', DIR_OPENCART . 'extension/');
define('DIR_IMAGE', DIR_OPENCART . 'image/');
define('DIR_SYSTEM', DIR_OPENCART . 'system/');
define('DIR_CATALOG', DIR_OPENCART . 'catalog/');
define('DIR_STORAGE', '/var/www/storage/');
define('DIR_LANGUAGE', DIR_APPLICATION . 'language/');
define('DIR_TEMPLATE', DIR_APPLICATION . 'view/template/');
define('DIR_CONFIG', DIR_SYSTEM . 'config/');
define('DIR_CACHE', DIR_STORAGE . 'cache/');
define('DIR_DOWNLOAD', DIR_STORAGE . 'download/');
define('DIR_LOGS', DIR_STORAGE . 'logs/');
define('DIR_SESSION', DIR_STORAGE . 'session/');
define('DIR_UPLOAD', DIR_STORAGE . 'upload/');
define('DB_DRIVER', 'mysqli');
define('DB_HOSTNAME', 'localhost');
define('DB_USERNAME', 'opencart1');
define('DB_PASSWORD', 'Copa007copa.');
define('DB_DATABASE', 'opencart2');
define('DB_PORT', '3306');
define('DB_PREFIX', 'oc_');
```

---

## 5. Reemplazar URLs en base de datos (opcional)

```bash
mysql -u root -p -D opencart2 -e \
"UPDATE oc_setting SET value = REPLACE(value, 'http://localhost/dotecomerce-dev', 'https://tienda.mettgorras.uk') WHERE value LIKE '%localhost%';"

mysql -u root -p opencart2 -e "UPDATE oc_modification SET status = 0 WHERE code LIKE '%admin%'"
sudo rm -rf /var/www/storage/cache/* /var/www/storage/modification/*

sudo systemctl reload apache2

```

---

## 6. Limpiar caché y recargar Apache

```bash
sudo rm -vrf /var/www/storage/cache/* /var/www/storage/modification/*
sudo systemctl reload apache2

```
## 7. Borrar archivo de prueba
```bash
sudo rm /var/www/html/index.html
```



Verifica en navegador:

* [https://tienda.mettgorras.uk](https://tienda.mettgorras.uk)
* [https://tienda.mettgorras.uk/admin](https://tienda.mettgorras.uk/admin)

---

## ✅ Checklist final de migración

| Paso                                          | Estado |
| --------------------------------------------- | ------ |
| Archivos comprimidos, copiados y extraídos    | ☑      |
| Directorios `tienda` y `storage` con permisos | ☑      |
| Base de datos creada e importada              | ☑      |
| Archivos `config.php` correctamente editados  | ☑      |
| URL actualizada en base de datos              | ☑      |
| Apache recargado, caché limpia                | ☑      |
| Sitio operativo vía Cloudflare Tunnel         | ☑      |

## Marketplace Opencart
Este mensaje se basa en información actualizada de la comunidad y la documentación oficial. No es hacking, sino configuraciones autorizadas para tu propia tienda.

---

## 🛑 Problema

El error **"Signature hash does not match!"** aparece al intentar instalar extensiones desde el Marketplace, lo que impide su instalación.

---

## 📌 Causas frecuentes

1. **Dominio no registrado correctamente**: OpenCart genera la firma (hash) basada en el dominio registrado. Si no coincide, da error. ([OpenCart Community][1], [webocreation.com][2])
2. **API Key demasiado larga** o no válida en la configuración de OpenCart. ([OpenCart Community][3])
3. **Problemas de caché**, extensiones o permisos.&#x20;

---

## ✅ Pasos para resolver

### 1. Registro correcto del dominio en OpenCart.com

* Ingresa a tu cuenta en [OpenCart.com](https://www.opencart.com/)
* Ve a **Dashboard → Your Stores**, y añade tu tienda con **solo el dominio** (sin `http://` o `https://`, sin slash final).
  Ejemplo: `tienda.mettgorras.uk` ([webocreation.com][2])
* Al guardar, obtendrás el **Username** y **SecretKey** (API Credentials).

### 2. Configurar el Marketplace en tu OpenCart

En el panel admin:
`Extensions → Marketplace → Settings`
Introduce:

* **Marketplace Username**: el nombre que ves en tu cuenta OpenCart.com
* **API Key / SecretKey**: el generado para ese dominio

Guarda y asegúrate de que se muestre como conectado sin errores.

---

### 3. Verificar versión y compatibilidad

* Asegúrate de estar usando una versión **estable**, preferiblemente **OpenCart 3.0.4.0**, ya que las 4.x tienen errores conocidos. ([webocreation.com][4], [OpenCart Community][3])

---

### 4. Limpiar cachés y validar

Después de guardar las credenciales:

```bash
# Limpia caché de OpenCart:
mysql -u root -p opencart2 \
  -e "UPDATE oc_setting SET value = NULL WHERE `key`='config_marketplace_api';"
# o simplemente revisa que estén guardadas.

# En admin_php: Extensions → Modifications → “Refresh”

# Limpia almacenamiento:
sudo rm -rf /var/www/storage/cache/* /var/www/storage/modification/*

# Reinicia Apache:
sudo systemctl reload apache2
```

Luego recarga el Marketplace.

---

### 5. Si el error persiste

* Verifica que la **API Key no exceda los 256 caracteres** ([Fórum OpenCart Brasil][5], [OpenCart Community][3])
* **Re-descarga la extensión manualmente** desde opencart.com y súbela en `Extensions → Installer`. ([webocreation.com][2])

---

## 🔍 En resumen

| Paso                    | Acción                                           |
| ----------------------- | ------------------------------------------------ |
| ✅ Registrar dominio     | En OpenCart.com como `tienda.mettgorras.uk`      |
| ✅ Insertar credenciales | Username + SecretKey en Settings del Marketplace |
| ✅ Borrar cachés         | En modificaciones + storage                      |
| ✅ Verificar key         | No más de 256 caracteres                         |
| ✅ Reiniciar Apache      | `systemctl reload apache2`                       |
| ✅ Probar instalación    | Desde Marketplace o vía Installer manual         |

---

