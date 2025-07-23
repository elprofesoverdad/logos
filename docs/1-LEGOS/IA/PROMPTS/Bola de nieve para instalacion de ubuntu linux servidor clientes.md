# Prompt Bola de Nieve 🌨️ Instalacion en Servidor Ubuntu para clientes.

Este documento es tu **fuente maestra de contexto**. Cada vez que inicies una sesión, pégame aquí este contenido completo y retomaré puntualmente desde el último estado.

---

## 📜 1. CONTEXTO GLOBAL (immutable)

> Define el escenario general y no debe modificarse salvo por ChatGPT con consentimiento expreso.

* **Entorno local:** Laptop Kubuntu con LAMP (Apache, MariaDB/MySQL, PHP).
* **Exposición a Internet:** Túnel Cloudflared configurado en `/etc/cloudflared/config.yml`, dominio público apuntando al servidor.
* **Proyecto principal:** Replicar y versionar instalación de OpenCart en servidor local y en servidor cliente.
* **Versiones clave:** OpenCart 4.x, PHP 8.2, Apache 2.4+, MariaDB 10.5+.
* **Rutas base:**

  * Local: `/var/www/html/tienda-local/`
  * Remoto cliente: `/var/www/html/tienda-cliente/`

---

## 🆕 2. INSTRUCCIONES DINÁMICAS (editable)

> Aquí el usuario añade cambios de requisitos, nuevas directivas, límites o prioridades.

* Ejemplo de entradas:

  * «A partir de hoy, usar siempre Bash v5.2 y Python v3.10 para scripts.»
  * «Automatizar despliegue con Ansible en lugar de scripts aislados.»
  * «Registrar todos los logs en `/opt/logs/deploy.log` con formato JSON.»

> **Regla:** Priorizar estas directrices sobre el resto del documento.

---

## 🛠️ 3. CONFIGURACIÓN Y FLUJOS DE TRABAJO

### 3.1 Entorno local (Laptop Kubuntu)

* Apache configurado en `/etc/apache2/sites-available/tienda-local.conf`.
* Base de datos en MariaDB con usuario `oc_admin`, base `oc_local`.
* Cloudflared: `cloudflared service install`, tunel activo `cloudflared tunnel run`.

### 3.2 Entorno remoto (Servidor Cliente)

* Recursos: VPS Ubuntu 22.04 con LAMP.
* Dominio: `cliente.tu-dominio.com` apunta al túnel Cloudflared.
* Config inicial: SSH acceso por clave pública, firewall UFW abierto solo puertos 80, 443, 22.

---

## 📋 4. TAREAS Y SCRIPTS PENDIENTES

1. **Instalación LAMP automatizada:** script Bash o Ansible.
2. **Duplicación de tienda:** sincronizar archivos y base de datos.
3. **Adaptación de config.php:** reemplazar rutas y credenciales.
4. **Deploy Cloudflared:** registrar nuevo servicio en `/etc/systemd/system/`.
5. **Verificación automática:** health-check HTTP y SSH.

---

## 🔍 5. MÉTRICAS Y VALIDACIONES

* Cada script debe retornar código 0 si todo OK.
* Logs en `/var/log/deploy.log` con timestamp ISO 8601.
* Validar con `curl -I https://cliente.tu-dominio.com/` respuesta 200.

# Método permanente de configuración (infraestructura)

Todas las configuraciones de servicios, red, Apache, etc. se aplicarán de forma controlada y reproducible mediante el siguiente patrón:

### ✅ 6.  structura estándar para crear archivos de configuración desde consola

```bash
sudo tee /ruta/del/archivo.conf > /dev/null <<EOF
<contenido>
EOF
```

Este patrón se aplica para:

* Servicios systemd (`/etc/systemd/system/...`)
* VirtualHost de Apache (`/etc/apache2/sites-available/...`)
* Archivos `config.yml` para Cloudflared
* Archivos `.env` o scripts persistentes

### ✅ Ejemplo aplicado a systemd:

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

Luego se activa con:

```bash
sudo systemctl daemon-reload
sudo systemctl enable cloudflared
sudo systemctl restart cloudflared
```

Este método se aplica **permanentemente** en todos los contextos de instalación, tanto en tu laptop como en servidores remotos de clientes. Facilita la automatización, la auditablez y el versionado manual de la infraestructura.

---

## 📝 7. NOTAS Y ACTUALIZACIONES

> Fecha: 2025-07-11

* Versión inicial del prompt bola de nieve.
* Pendiente: definir formato de logs en JSON.

---

**Uso:** Copia todo este documento en el chat en cada sesión. Modifica únicamente la sección 2 para introducir nuevos requisitos. ¡Yo retomaré el flujo completo automáticamente!
