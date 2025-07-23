# Manual Detallado: Instalación y Despliegue de Ubuntu Server con Ventoy, LAMP, OpenCart y Cloudflare Tunnel

Este documento unifica todos los pasos necesarios para:

- Preparar un pendrive de instalación con Ventoy  
- Instalar y configurar un servidor Ubuntu con LAMP  
- Asegurar MySQL y gestionar contraseñas  
- Crear un túnel Cloudflare para exponer el sitio  
- Configurar Apache y VirtualHosts  
- Migrar una instancia local de OpenCart al servidor  

Cada sección incluye explicaciones, validaciones y buenas prácticas para evitar errores comunes.

---

## Variables de entorno

Define al principio valores personalizables para facilitar la automatización:

```bash
# Ruta de la ISO descargada
ISO_PATH="$HOME/Descargas/ubuntu-22.04.5-live-server-amd64.iso"

# Dispositivo USB (ajusta al resultado de `lsblk -f`)
USB_DEV="/dev/sdb"

# Nombre del túnel y dominio
TUNNEL_NAME="tienda-tunnel"
DOMAIN="tienda.mettgorras.uk"
```

---

## 📁 Requisitos Previos

* PC con GNU/Linux (Ubuntu, Debian, Kubuntu, etc.)  
* Pendrive USB ≥ 8 GB (se formateará)  
* Conexión a Internet para descargas  
* Cuenta en Cloudflare con dominio apuntado  

Valida que tengas las herramientas básicas:

```bash
which wget curl git lsblk ip systemctl cloudflared
```

---

## 🔧 Paso 1: Preparar Pendrive con Ventoy

1. Localiza tu pendrive con `lsblk -f` y confirma que `USB_DEV` corresponde al dispositivo correcto.

2. Descarga Ventoy y extrae:

   ```bash
   cd ~/Descargas
   wget -q https://github.com/ventoy/Ventoy/releases/download/v1.1.05/ventoy-1.1.05-linux.tar.gz
   tar -xzvf ventoy-1.1.05-linux.tar.gz
   cd ventoy-1.1.05
   ```

3. Instala Ventoy en el USB:

   ```bash
   sudo sh Ventoy2Disk.sh -i "$USB_DEV"
   ```

   Confirma con `y` cuando se solicite. Ventoy creará dos particiones: gestor de arranque y exFAT para ISOs.

4. Monta la partición Ventoy y copia la ISO:

   ```bash
   udisksctl mount -b /dev/disk/by-label/Ventoy
   cp "$ISO_PATH" /media/$USER/Ventoy/
   sync
   udisksctl unmount -b /dev/disk/by-label/Ventoy
   ```

5. Arranca desde el USB en la máquina de destino y elige la ISO en el menú Ventoy.

---

## 🛠️ Paso 2: Instalar micro y Midnight Commander

### Instalar micro

```bash
curl https://getmic.ro | bash
sudo mv micro /usr/local/bin/
micro --version
```

### Instalar Midnight Commander

```bash
sudo apt update
sudo apt install -y mc
```

### Configurar micro como editor por defecto

```bash
sudo update-alternatives --install /usr/bin/editor editor /usr/local/bin/micro 40
sudo update-alternatives --config editor
```

### Ajustes automáticos para micro

```bash
install -d ~/.config/micro
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

---

## 🚀 Paso 3: Instalación Rápida de LAMP

1. Instala Apache, MariaDB y PHP con un solo comando:

   ```bash
   sudo apt update
   sudo apt install -y lamp-server^
   ```

2. Asegura MySQL:

   ```bash
   sudo mysql_secure_installation
   ```

3. Habilita `mod_rewrite` en Apache:

   ```bash
   sudo a2enmod rewrite
   sudo systemctl restart apache2
   ```

---

## 🛡️ Paso 4: Configurar seguridad de MySQL

Responde en `mysql_secure_installation`:

- `y` → Activar VALIDATE PASSWORD COMPONENT  
- `1` → Política MEDIUM  
- Enter → Saltar cambio de contraseña si usas auth_socket  
- `y` → Eliminar usuarios anónimos  
- `y` → Deshabilitar login remoto de root  
- `y` → Eliminar base de datos test  
- `y` → Recargar privilegios  

---

## 🔐 Paso 5: Restablecer contraseña root de MySQL (recuperación)

Si `skip-grant-tables` falla:

1. Detén MySQL y elimina procesos sobrantes:

   ```bash
   sudo systemctl stop mysql
   sudo pkill -f mysqld_safe
   ```

2. Crea directorio y ajusta permisos:

   ```bash
   sudo mkdir -p /var/run/mysqld
   sudo chown mysql:mysql /var/run/mysqld
   ```

3. Inicia modo seguro:

   ```bash
   sudo mysqld_safe --skip-grant-tables --skip-networking &
   ```

4. Conéctate y cambia contraseña:

   ```bash
   mysql -u root
   FLUSH PRIVILEGES;
   ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'TuNuevaContraseña';
   FLUSH PRIVILEGES;
   EXIT;
   ```

5. Reinicia MySQL:

   ```bash
   sudo pkill -f mysqld_safe
   sudo systemctl start mysql
   ```

---

## 🌐 Paso 6: Configurar Cloudflare Tunnel

1. Instala cloudflared:

   ```bash
   wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
   sudo dpkg -i cloudflared-linux-amd64.deb
   ```

2. Autentica tu cuenta:

   ```bash
   cloudflared tunnel login
   ```

3. Crea el túnel:

   ```bash
   cloudflared tunnel create "$TUNNEL_NAME"
   ```

4. Asigna DNS al túnel:

   ```bash
   cloudflared tunnel route dns "$TUNNEL_NAME" "$DOMAIN"
   ```

5. Prepara `~/.cloudflared/config.yml`:

   ```yaml
   tunnel: <ID_DEL_TUNNEL>
   credentials-file: ~/.cloudflared/<ID_DEL_TUNNEL>.json

   ingress:
     - hostname: $DOMAIN
       service: http://localhost:80
     - service: http_status:404
   ```

6. Crea servicio systemd:

   ```bash
   sudo tee /etc/systemd/system/cloudflared.service > /dev/null <<EOF
   [Unit]
   Description=Cloudflared Tunnel
   After=network.target

   [Service]
   Type=simple
   ExecStart=/usr/bin/cloudflared tunnel run $TUNNEL_NAME
   Restart=always
   RestartSec=5
   User=$USER

   [Install]
   WantedBy=multi-user.target
   EOF

   sudo systemctl daemon-reload
   sudo systemctl enable --now cloudflared
   ```

---

## ⚙️ Paso 7: Configuración de Apache y VirtualHosts

1. Crea directorios base:

   ```bash
   sudo mkdir -p /var/www/html/tienda /var/www/html/default-root
   echo "<h1>No disponible</h1>" | sudo tee /var/www/html/default-root/index.html
   ```

2. VirtualHost para la tienda:

   ```bash
   sudo tee /etc/apache2/sites-available/tienda.conf > /dev/null <<EOF
   <VirtualHost *:80>
     ServerName $DOMAIN
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

3. VirtualHost por defecto protegido:

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

4. Habilitar y recargar:

   ```bash
   sudo a2ensite tienda.conf default-root.conf
   sudo a2dissite 000-default.conf
   sudo systemctl reload apache2
   ```

---

## 💾 Paso 8: Migración de OpenCart del Entorno Local al Servidor

1. Genera backup en local:

   ```bash
   mkdir -p ~/Escritorio/backupTienda
   tar czf ~/Escritorio/backupTienda/tienda.tar.gz -C /var/www/html/dotecomerce-dev .
   tar czf ~/Escritorio/backupTienda/storage.tar.gz -C /var/www/storage-dev .
   mysqldump -u root -p opencart2 > ~/Escritorio/backupTienda/db.sql
   ```

2. Copia al servidor:

   ```bash
   scp ~/Escritorio/backupTienda/* $USER@172.16.0.191:/tmp/
   ```

3. Restaura en servidor:

   ```bash
   sudo mkdir -p /var/www/html/tienda /var/www/storage
   sudo tar xzf /tmp/tienda.tar.gz -C /var/www/html/tienda
   sudo tar xzf /tmp/storage.tar.gz -C /var/www/storage
   sudo chown -R www-data:www-data /var/www/html/tienda /var/www/storage
   sudo chmod -R 755 /var/www/html/tienda /var/www/storage

   mysql -u root -p -e "
     CREATE DATABASE opencart2 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
     CREATE USER 'opencart1'@'localhost' IDENTIFIED BY 'TuContraseña';
     GRANT ALL PRIVILEGES ON opencart2.* TO 'opencart1'@'localhost';
     FLUSH PRIVILEGES;
   "
   mysql -u root -p opencart2 < /tmp/db.sql
   ```

4. Ajusta `config.php` y `admin/config.php` en `/var/www/html/tienda` y `/var/www/html/tienda/admin` con las rutas y credenciales correspondientes.

5. Actualiza URLs en base de datos:

   ```bash
   mysql -u root -p -D opencart2 -e "
     UPDATE oc_setting
     SET value = REPLACE(value, 'http://localhost/dotecomerce-dev', 'https://$DOMAIN')
     WHERE value LIKE '%localhost%';
   "
   ```

6. Limpia caché y recarga Apache:

   ```bash
   sudo rm -rf /var/www/storage/cache/* /var/www/storage/modification/*
   sudo systemctl reload apache2
   ```

---

## ✅ Checklist Final

| Paso                                         | Estado |
|----------------------------------------------|:------:|
| Pendrive con Ventoy y ISO                    | ☑      |
| micro y mc instalados y configurados         | ☑      |
| LAMP instalado y `mod_rewrite` habilitado    | ☑      |
| MySQL seguro y contraseña root configurada   | ☑      |
| Túnel Cloudflare activo y DNS apuntado       | ☑      |
| VirtualHosts Apache configurados             | ☑      |
| Backup y migración de OpenCart completos     | ☑      |
| Configuraciones de `config.php` aplicadas    | ☑      |
| Caché limpiada y Apache recargado            | ☑      |

Con este flujo tendrás un servidor Ubuntu preparado para servir tu tienda OpenCart de manera segura, accesible vía HTTPS por Cloudflare y con un despliegue fácilmente replicable y mantenible.