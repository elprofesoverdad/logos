# Personalización opencart

> **Nota: la carpeta admin se renombra...**

## Footer de admin

Aquí tienes la solución definitiva con año dinámico (2025 será variable), tu dominio correcto y texto exacto:

### 1. Controlador Modificado (`admin/controller/common/footer.php`)
```php
// Buscar esta línea (~línea 20):
$data['text_footer'] = sprintf($this->language->get('text_footer'), $this->config->get('config_name'), date('Y'));

// Reemplazar con:
$data['custom_footer'] = sprintf(
    '© 2009-%s DotEcommerce Todos los derechos reservados Mundo mejor UK | Versión %s',
    date('Y'),  // Año dinámico
    VERSION     // Versión automática de OpenCart
);
```

### 2. Vista Actualizada (`admin/view/template/common/footer.twig`)
```twig
<footer id="footer">
  <a href="https://mundomejor.uk" target="_blank" rel="noopener">{{ custom_footer }}</a>
  {% if debug %}
  <br />{{ text_debug }} {{ debug }}
  {% endif %}
</footer>
```

### Versión OCMOD (recomendada):

```xml
<modification>
    <name>MundoMejor Custom Footer</name>
    <code>mm_custom_footer</code>
    <file path="admin/controller/common/footer.php">
        <operation>
            <search><![CDATA[$data['text_footer'] = sprintf($this->language->get('text_footer'), $this->config->get('config_name'), date('Y'));]]></search>
            <add position="replace"><![CDATA[
            $data['custom_footer'] = sprintf(
                '© 2009-%s DotEcommerce Todos los derechos reservados Mundo mejor UK | Versión %s',
                date('Y'),
                VERSION
            );
            ]]></add>
        </operation>
    </file>
    <file path="admin/view/template/common/footer.twig">
        <operation>
            <search><![CDATA[<footer id="footer">{{ text_footer }}</footer>]]></search>
            <add position="replace"><![CDATA[
            <footer id="footer">
              <a href="https://mundomejor.uk" target="_blank" rel="noopener">{{ custom_footer }}</a>
              {% if debug %}
              <br />{{ text_debug }} {{ debug }}
              {% endif %}
            </footer>
            ]]></add>
        </operation>
    </file>
</modification>
```

### Pasos de instalación:
1. Guarda el código XML como `mm_custom_footer.ocmod.xml`
2. En tu admin de OpenCart:
   - Extensions > Installer > Subir archivo
   - Extensions > Modifications > Actualizar (icono refresh)
3. Limpia la caché de Twig (Dashboard > Developer Settings > Clear cache)


## logo página ppal:

Se cambia normalmente en el backend

## logo admin:  

> /admin ó el nombre que le pusiste:

* /var/www/html/tienda/empresas-henao/tienda-henao/jefe/view/image/logo.png

* es una imagen de 180x35 px


## Modificar el footer del frontend



### ✅ Confirmación forense

1. **El HTML real del footer (`<p>Powered by...`) no está hardcodeado en `footer.twig`**, sino que se inyecta vía la variable `{{ text_powered }}`.

2. `{{ text_powered }}` **viene del archivo de idioma**:

   ```
   /var/www/html/tienda/extension/language_spanish_es/catalog/language/es/common/footer.php
   ```

   Línea 18:

   ```php
   $_['text_powered'] = 'Powered by <a href="https://www.opencart.com">OpenCart</a><br/> %s &copy; %s';
   ```

3. El archivo Twig simplemente hace esto en alguna línea posterior:

   ```twig
   <p>{{ text_powered }}</p>
   ```

---

### 🎯 ¿Entonces dónde modificar de forma **directa y efectiva**?

#### Opción 1: Modificar el archivo de idioma

Archivo:

```bash
/var/www/html/tienda/extension/language_spanish_es/catalog/language/es/common/footer.php
```

Modificar:

```php
$_['text_powered'] = 'DotEcommerce Mundo Mejor UK &copy; ' . date('Y');
```

❗️Pero los archivos de idioma **no admiten código PHP dinámico**. Así que debes escribirlo **ya evaluado**:

```php
$_['text_powered'] = 'DotEcommerce Mundo Mejor UK © 2025';
```

Puedes automatizar que se actualice el año con un cron que reescriba el archivo cada enero si lo deseas.

---

#### Opción 2: Modificar `footer.twig` directamente

Busca en:

```bash
/var/www/html/tienda/catalog/view/template/common/footer.twig
```

Localiza esta línea:

```twig
<p>{{ text_powered }}</p>
```

Y reemplázala por:

```twig
<p>DotEcommerce Mundo Mejor UK © {{ "now"|date("Y") }}</p>
```

## Versión OCMOD (recomendada):




### 🎯 Objetivo del OCMOD:

Modificar directamente `catalog/view/template/common/footer.twig`
Reemplazando esta línea:

```twig
<p>{{ text_powered }}</p>
```

Por esta:

```twig
<p><a href="https://mundomejor.uk" target="_blank" rel="noopener">DotEcommerce Mundo Mejor UK</a> © {{ "now"|date("Y") }}</p>
```

---

## 📦 `custom_footer_twig.ocmod.xml` — contenido completo:

Guarda esto como `custom_footer_twig.ocmod.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<modification>
  <name>Custom Footer Twig - DotEcommerce Mundo Mejor</name>
  <code>custom_footer_twig</code>
  <version>1.0</version>
  <author>Daniel Díaz</author>
  <link>https://mundomejor.uk</link>

  <file path="catalog/view/template/common/footer.twig">
    <operation>
      <search><![CDATA[<p>{{ text_powered }}</p>]]></search>
      <replace><![CDATA[
<p><a href="https://mundomejor.uk" target="_blank" rel="noopener">DotEcommerce Mundo Mejor UK</a> © {{ "now"|date("Y") }}</p>
      ]]></replace>
    </operation>
  </file>
</modification>
```

---

## 📂 ¿Dónde lo subes y activas?

1. Ve a **Admin → Extensiones → Instalador de extensiones**

   * Sube `custom_footer_twig.ocmod.xml`
2. Luego ve a **Admin → Extensiones → Modificaciones**

   * Activa (ícono +) si es necesario
   * Pulsa el botón **Refrescar (⟳)** arriba a la derecha
3. Limpia caché (Admin → Configuración → Rendimiento → “Limpiar tema” y “Limpiar modificación”)

---

## 📌 Resultado

* Tu footer cambiará **sin tocar el archivo original `footer.twig`**.
* El texto es **dinámico con el año actual** gracias a Twig: `{{ "now"|date("Y") }}`.
* Puedes **desactivarlo en cualquier momento** desde el panel.

---

