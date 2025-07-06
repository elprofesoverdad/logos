## 🧩 1. Estructura general de pasos

* Origen: `/var/www/html/dotecomerce` + `/var/www/storage` (túnel Cloudflared → `https://tienda.mundomejor.uk/`)
* Pruebas: `http://localhost/dotecomerce-dev`
* Cliente: réplica local con dominio final SSL (Cloudflared)

---

## 📦 2. Backup completo (entorno actual)

```bash
# Crear carpeta en Escritorio
mkdir -p $HOME/Escritorio/backupOc

# Backup de tienda
sudo tar czvpf $HOME/Escritorio/backupOc/files.tar.gz -C /var/www/html/dotecomerce . --same-owner

# Backup de storage
sudo tar czvpf $HOME/Escritorio/backupOc/storage.tar.gz -C /var/www/storage . --same-owner

# Backup de base de datos
mysqldump -u root -p opencart > $HOME/Escritorio/backupOc/db.sql
```

---

## 📇 3. Preparar Apache + VirtualHost (`dotecomerce-dev`)

```bash
sudo micro /etc/apache2/sites-available/dotecomerce-dev.conf
```

Pegar:

```apache
<VirtualHost *:80>
  ServerName localhost/dotecomerce-dev
  DocumentRoot /var/www/html/dotecomerce-dev
  <Directory /var/www/html/dotecomerce-dev>
    AllowOverride All
    Require all granted
  </Directory>
  ErrorLog ${APACHE_LOG_DIR}/dotecomerce_error.log
  CustomLog ${APACHE_LOG_DIR}/dotecomerce_access.log combined
</VirtualHost>
```

Activar:

```bash
sudo a2enmod rewrite ssl
sudo a2ensite dotecomerce-dev.conf
sudo systemctl reload apache2
```

---

## 🔍 3.a Verificación inicial con curl

Crear entorno de prueba y archivo de respuesta:

```bash
sudo mkdir -p /var/www/html/dotecomerce-dev /var/www/storage-dev \
  && sudo chown -vR www-data:www-data /var/www/html/dotecomerce-dev /var/www/storage-dev \
  && sudo chmod -vR 755 /var/www/html/dotecomerce-dev /var/www/storage-dev \
  && echo "OK" | sudo tee /var/www/html/dotecomerce-dev/index.html
```

Verificar:

```bash
curl -L -I http://localhost/dotecomerce-dev
```

---

## 📂 4. Restaurar archivos y base de datos

```bash
# Restaurar archivos
sudo tar xzvpf $HOME/Escritorio/backupOc/files.tar.gz -C /var/www/html/dotecomerce-dev
sudo tar xzvpf $HOME/Escritorio/backupOc/storage.tar.gz -C /var/www/storage-dev

# Asignar permisos correctos
sudo chown -vR www-data:www-data /var/www/html/dotecomerce-dev /var/www/storage-dev
sudo chmod -vR 755 /var/www/html/dotecomerce-dev /var/www/storage-dev

# Crear nueva base de datos y usuario
mysql -u root -p -e "
  CREATE DATABASE opencart2 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
  CREATE USER 'opencart1'@'localhost' IDENTIFIED BY 'Copa007copa.';
  GRANT ALL PRIVILEGES ON opencart2.* TO 'opencart1'@'localhost';
  FLUSH PRIVILEGES;"

# Importar base de datos
mysql -u root -p opencart2 < $HOME/Escritorio/backupOc/db.sql
```

---

## 🔧 5. Configurar `config.php` y `admin/config.php`

```bash
sudo micro /var/www/html/dotecomerce-dev/config.php
```

Contenido:

```php
<?php
// APPLICATION
define('APPLICATION', 'Catalog');

// HTTP
define('HTTP_SERVER', 'http://localhost/dotecomerce-dev/');

// DIR
define('DIR_OPENCART', '/var/www/html/dotecomerce-dev/');
define('DIR_APPLICATION', DIR_OPENCART . 'catalog/');
define('DIR_EXTENSION', DIR_OPENCART . 'extension/');
define('DIR_IMAGE', DIR_OPENCART . 'image/');
define('DIR_SYSTEM', DIR_OPENCART . 'system/');
define('DIR_STORAGE', '/var/www/storage-dev/');
define('DIR_LANGUAGE', DIR_APPLICATION . 'language/');
define('DIR_TEMPLATE', DIR_APPLICATION . 'view/template/');
define('DIR_CONFIG', DIR_SYSTEM . 'config/');
define('DIR_CACHE', DIR_STORAGE . 'cache/');
define('DIR_DOWNLOAD', DIR_STORAGE . 'download/');
define('DIR_LOGS', DIR_STORAGE . 'logs/');
define('DIR_SESSION', DIR_STORAGE . 'session/');
define('DIR_UPLOAD', DIR_STORAGE . 'upload/');

// DB
define('DB_DRIVER', 'mysqli');
define('DB_HOSTNAME', 'localhost');
define('DB_USERNAME', 'opencart1');
define('DB_PASSWORD', 'Copa007copa.');
define('DB_DATABASE', 'opencart2');
define('DB_PORT', '3306');
define('DB_PREFIX', 'oc_');
define('DB_SSL_KEY', '');
define('DB_SSL_CERT', '');
define('DB_SSL_CA', '');
```

Mismo procedimiento para `admin/config.php`.
```bash
sudo micro /var/www/html/dotecomerce-dev/admin/config.php

en mi caso
sudo micro /var/www/html/dotecomerce-dev/copa007copa/config.php


---

y debe quedar asi:

``` php

<?php
// APPLICATION
define('APPLICATION', 'Admin');

// HTTP
define('HTTP_SERVER', 'http://localhost/dotecomerce-dev/copa007copa/');
define('HTTP_CATALOG', 'http://localhost/dotecomerce-dev/');

// DIR
define('DIR_OPENCART', '/var/www/html/dotecomerce-dev/');
define('DIR_APPLICATION', DIR_OPENCART . 'copa007copa/');
define('DIR_EXTENSION', DIR_OPENCART . 'extension/');
define('DIR_IMAGE', DIR_OPENCART . 'image/');
define('DIR_SYSTEM', DIR_OPENCART . 'system/');
define('DIR_CATALOG', DIR_OPENCART . 'catalog/');
define('DIR_STORAGE', '/var/www/storage-dev/');
define('DIR_LANGUAGE', DIR_APPLICATION . 'language/');
define('DIR_TEMPLATE', DIR_APPLICATION . 'view/template/');
define('DIR_CONFIG', DIR_SYSTEM . 'config/');
define('DIR_CACHE', DIR_STORAGE . 'cache/');
define('DIR_DOWNLOAD', DIR_STORAGE . 'download/');
define('DIR_LOGS', DIR_STORAGE . 'logs/');
define('DIR_SESSION', DIR_STORAGE . 'session/');
define('DIR_UPLOAD', DIR_STORAGE . 'upload/');

// DB
define('DB_DRIVER', 'mysqli');
define('DB_HOSTNAME', 'localhost');
define('DB_USERNAME', 'opencart1');
define('DB_PASSWORD', 'Copa007copa.');
define('DB_DATABASE', 'opencart2');
define('DB_PORT', '3306');
define('DB_PREFIX', 'oc_');

define('DB_SSL_KEY', '');
define('DB_SSL_CERT', '');
define('DB_SSL_CA', '');

// OpenCart API
define('OPENCART_SERVER', 'https://www.opencart.com/');


```

## ⚙️ 6. Reemplazar URLs en base de datos

```bash
mysql -u root -pCopa007copa. -D opencart2 -e "
  UPDATE oc_setting
  SET value = REPLACE(value, 'https://tienda.mundomejor.uk', 'http://localhost/dotecomerce-dev')
  WHERE value LIKE '%tienda.mundomejor.uk%';"
```

---

## 🧹 7. Limpiar caché y recargar Apache

```bash
sudo rm -vrf /var/www/storage-dev/cache/* /var/www/storage-dev/modification/*
sudo systemctl reload apache2
```

Verifica en navegador:

* [http://localhost/dotecomerce-dev/](http://localhost/dotecomerce-dev/)
* [http://localhost/dotecomerce-dev/admin/](http://localhost/dotecomerce-dev/admin/)

---

## 🔐 8. Producción cliente (Cloudflared SSL)

* En `config.php`:

  ```php
  define('HTTP_SERVER','https://tienda.cliente.com/');
  define('HTTPS_SERVER','https://tienda.cliente.com/');
  ```
* Cloudflared ya hace el proxy SSL.
* Si se desea Apache con SSL local, usar `<VirtualHost *:443>` + certs.

---

## ✅ Checklist final

| Paso                                          | Estado |
| --------------------------------------------- | ------ |
| Backups completos con permisos preservados    | ☑      |
| VirtualHost creado y activado                 | ☑      |
| `index.html` responde 200 OK con `curl -L -I` | ☑      |
| Archivos restaurados con dueño www-data       | ☑      |
| BD opencart2 + usuario opencart1 creados      | ☑      |
| config.php y admin/config.php actualizados    | ☑      |
| URLs reemplazadas en base de datos            | ☑      |
| Cache vaciada y Apache reiniciado             | ☑      |
| Navegador muestra tienda y admin              | ☑      |

---
