## **PROMPT GENERADOR SEO  OG PARA IA MkDocs  GitHub Pages**

---

**🎯 Objetivo:**
Automatizar la creación de bloques `extra_head` en formato YAML para archivos `.md` (Markdown) utilizados en MkDocs Material, publicados como GitHub Pages, incluyendo:

* Metadatos SEO multilingües (español, inglés, chino simplificado)
* Etiquetas Open Graph y Twitter Cards
* JSON-LD estructurado con entidades Schema.org
* Imagen destacada en formato MkDocs
* Canonical URL y estructura de breadcrumbs

Este prompt debe permitir que **una IA reciba como entrada un archivo Markdown (ej: `/home/usuario/.../documento.md`)**, determine automáticamente la URL final en GitHub Pages, y genere toda la estructura `extra_head` correcta con base en la ruta, el contenido y la imagen principal.

---

**📥 ENTRADAS REQUERIDAS PARA LA IA:**

1. `ruta_local`: Ruta absoluta del archivo `.md` en el sistema local Linux, por ejemplo:

   ```
   /home/daniel/tron/1-LEGOS/NEGOCIO/MMA/PRODUCTOS/DotEcomerce/Sistema DotEcomerce.md
   ```

2. `repositorio_github`: Nombre del repositorio donde se publica en GitHub Pages (ej. `logos`)

3. `usuario_github`: Nombre de usuario/organización en GitHub (ej. `elprofesoverdad`)

4. `imagen_destacada`: Ruta relativa a `/assets/` donde está la imagen destacada (ej. `/assets/dot-ecommerce-tienda-virtual.jpg`)

5. `titulo_documento`: Título optimizado del documento SEO (ej. `Sistema DotEcomerce – Tienda Virtual Barquisimeto`)

6. `descripcion_seo`: Descripción concisa del documento para Google, OG y Twitter

7. `precio_desde`: Precio base del producto/servicio ofrecido (ej. `300`)

8. `precio_completo`: Precio con consultoría incluida (ej. `500`)

9. `autor_nombre`: Nombre del autor (ej. `Daniel Hung`)

10. `autor_url`: URL oficial del autor (siempre: `https://mundomejor.uk/danielhung`)

---

**🔄 CONVERSIÓN AUTOMÁTICA DE URL FINAL (LOGICA IMPLEMENTAR EN LA IA):**

Dado:

```
/home/daniel/tron/1-LEGOS/NEGOCIO/MMA/PRODUCTOS/DotEcomerce/Sistema DotEcomerce.md
```

Se convierte en:

```
https://{usuario_github}.github.io/{repositorio_github}/1-LEGOS/NEGOCIO/MMA/PRODUCTOS/DotEcomerce/Sistema%20DotEcomerce/
```

> 👇 Reglas:

* Se omite `/home/daniel/tron/`
* Se aplica `encodeURIComponent` a carpetas con espacios (`Sistema DotEcomerce` → `Sistema%20DotEcomerce`)
* Se antepone: `https://{usuario_github}.github.io/{repositorio_github}/`

---

**📤 SALIDA ESPERADA: BLOQUE COMPLETO YAML (`extra_head`)**

```yaml
classes: landing-page
extra_head: |
  <link rel="canonical" href="{{URL_FINAL}}" />
  <link rel="alternate" hreflang="es" href="{{URL_FINAL}}" />
  <link rel="alternate" hreflang="en" href="{{URL_FINAL}}?lang=en" />
  <link rel="alternate" hreflang="zh-Hans" href="{{URL_FINAL}}?lang=zh-Hans" />
  <link rel="alternate" hreflang="x-default" href="{{URL_FINAL}}" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{{titulo_documento}}" />
  <meta property="og:description" content="{{descripcion_seo}}" />
  <meta property="og:url" content="{{URL_FINAL}}" />
  <meta property="og:image" content="https://{{usuario_github}}.github.io/{{repositorio_github}}{{imagen_destacada}}" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{{titulo_documento}}" />
  <meta name="twitter:description" content="{{descripcion_seo}}" />
  <meta name="twitter:image" content="https://{{usuario_github}}.github.io/{{repositorio_github}}{{imagen_destacada}}" />

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "@id": "{{URL_FINAL}}#webpage",
    "url": "{{URL_FINAL}}",
    "name": "{{titulo_documento}}",
    "description": "{{descripcion_seo}}",
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [ ... construir con cada carpeta como nivel ... ]
    },
    "author": {
      "@type": "Person",
      "@id": "{{autor_url}}#person",
      "name": "{{autor_nombre}}",
      "url": "{{autor_url}}"
    },
    "publisher": {
      "@type": "Organization",
      "@id": "https://{{usuario_github}}.github.io/{{repositorio_github}}/#organization",
      "name": "Mundo Mejor",
      "url": "https://mundomejor.uk",
      "logo": {
        "@type": "ImageObject",
        "url": "https://{{usuario_github}}.github.io/{{repositorio_github}}/assets/logo-mundomejor.png"
      }
    },
    "image": {
      "@type": "ImageObject",
      "url": "https://{{usuario_github}}.github.io/{{repositorio_github}}{{imagen_destacada}}",
      "width": 1200,
      "height": 630
    }
  }
  </script>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "{{titulo_documento}}",
    "image": "https://{{usuario_github}}.github.io/{{repositorio_github}}{{imagen_destacada}}",
    "description": "{{descripcion_seo}}",
    "brand": {
      "@type": "Brand",
      "name": "DotEcomerce"
    },
    "offers": {
      "@type": "AggregateOffer",
      "priceCurrency": "USD",
      "lowPrice": "{{precio_desde}}",
      "highPrice": "{{precio_completo}}",
      "offerCount": 2,
      "offers": [
        {
          "@type": "Offer",
          "price": "{{precio_desde}}",
          "itemOffered": { "@type": "Service", "name": "Tienda básica DotEcomerce" },
          "priceCurrency": "USD",
          "url": "{{URL_FINAL}}"
        },
        {
          "@type": "Offer",
          "price": "{{precio_completo}}",
          "itemOffered": { "@type": "Service", "name": "Sistema DotEcomerce completo (con SEO + Consultoría)" },
          "priceCurrency": "USD",
          "url": "{{URL_FINAL}}"
        }
      ]
    }
  }
  </script>
```

---

**🧠 Contexto de esta plantilla:**
Este prompt fue diseñado en colaboración con un consultor SEO que publica artículos en MkDocs, alojados en GitHub Pages con estructura de carpetas activa. Cada documento tiene una imagen destacada proporcionada manualmente, y se desea posicionar los contenidos para mercados de:

* Venezuela (especialmente Barquisimeto, Lara)
* Latinoamérica
* China continental (con traducciones al chino simplificado)
* Público global (en inglés)

Además, se desea reforzar la autoridad del autor con perfil en `https://mundomejor.uk/danielhung`, sin alterar que el canonical siempre apunte al dominio de GitHub Pages (`https://elprofesoverdad.github.io/...`).

Este prompt es lo suficientemente completo para que cualquier IA estructure automáticamente el SEO y OG necesario, deduciendo la URL final, generando el bloque YAML completo y listando todos los datos estructurados correctamente, con práctica validación y soporte multilingüe internacional.
