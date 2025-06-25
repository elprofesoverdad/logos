# Worker Cloudflare + MkDocs + GitHub Pages

Este manual documenta cómo desplegar un **Cloudflare Worker** para servir de manera dinámica y óptima cualquier contenido desde un sitio generado con **MkDocs** y publicado en **GitHub Pages**, utilizando un subdominio personalizado como `logos.mundomejor.uk`.

---

## 🌟 Objetivo

- Servir correctamente rutas terminadas en `/`, respetando `use_directory_urls: true` de MkDocs.

- Evitar errores `206 Partial Content` que impiden previews en redes sociales como WhatsApp o Facebook.

- Permitir previsualizaciones Open Graph (OG) correctamente con `status: 200 OK`.

- Usar solo un Worker para todas las rutas posibles bajo `/logos/`.

---

## ✅ Requisitos previos

### 🧰 Node.js >= 20

Instalar con `nvm` si es necesario:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.nvm/nvm.sh
export NVM_DIR="$HOME/.nvm"
source "$NVM_DIR/nvm.sh"

nvm install 20
nvm use 20
node -v
```

Cuando pregunte por el nombre del proyecto, colocar:

```bash
logos-worker
```

### ⚙️ Wrangler (CLI oficial de Cloudflare)

Instalación global (usa `sudo` si es necesario):

```bash
npm install -g wrangler
```

---

## 🏗️ Inicialización del Worker

Creamos la carpeta del proyecto e inicializamos con Wrangler:

```bash
mkdir logos-worker
cd logos-worker
wrangler init --yes
```

Esto genera la estructura del Worker:

```
logos-worker/
├── src/index.ts
├── wrangler.jsonc
├── public/
```

---

## ⚒️ Código del Worker (src/index.ts)

Este Worker intercepta cualquier solicitud y la redirige a la versión publicada en GitHub Pages con `index.html` cuando corresponda.

```ts
export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    let path = url.pathname;

    // Si es la raíz sin archivo, agrega index.html
    if (path.endsWith("/")) {
      path += "index.html";
    }

    const target = `https://elprofesoverdad.github.io/logos${path}`;
    const response = await fetch(target, {
      headers: { "User-Agent": "Mozilla/5.0" },
      redirect: "follow"
    });

    const headers = new Headers(response.headers);
    headers.delete("accept-ranges");
    headers.delete("transfer-encoding");
    headers.set("Cache-Control", "public, max-age=300");

    const contentType = response.headers.get("content-type");
    if (contentType) {
      headers.set("Content-Type", contentType);
    }

    const status = response.status === 206 ? 200 : response.status;

    return new Response(response.body, { status, headers });
  }
};
```

---

## 📞 Configuración del Worker (wrangler.jsonc)

```jsonc
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "logos-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-06-20",
  "compatibility_flags": [
    "global_fetch_strictly_public"
  ],
  "assets": {
    "directory": "./public"
  },
  "observability": {
    "enabled": true
  },
  // 👇 Aquí viene la sección importante
  "routes": [
    {
      "pattern": "logos.mundomejor.uk/*",
      "zone_name": "mundomejor.uk"
    }
  ]
}
```

---

## 📍 Configuración DNS en Cloudflare

### Paso 1 — DNS Manual

- Ir a Cloudflare DNS

- Zona: `mundomejor.uk`

- Agregar un nuevo registro:
  
  - Tipo: `A`
  
  - Nombre: `logos`
  
  - IP: `192.0.2.1` (dummy IP)
  
  - Proxy (nube naranja): Activado

> Cloudflare ignorará la IP porque el tráfico será manejado por el Worker.

### Paso 2 — Asignar dominio al Worker

```bash
wrangler deploy
```

---

## 🚀 Despliegue

```bash
wrangler deploy
```

Verifica en:  

[Sistema DotEcomerce - Mundo Mejor Uk: LOGOS](https://logos.mundomejor.uk/1-LEGOS/NEGOCIO/MMA/PRODUCTOS/DotEcomerce/Sistema-DotEcomerce/)

### ### 🧾 Verifica si todo está bien

Puedes confirmar que el dominio está activo y vinculado con:

```bash
wrangler whoami
wrangler dev
```

Y también verificando desde el panel de [Cloudflare → Workers → Triggers](https://dash.cloudflare.com/) que el Worker tiene una ruta `logos.mundomejor.uk/*`.

---

## 🧐 Tips importantes

- MkDocs con `use_directory_urls: true` sirve páginas desde `/ruta/`, pero internamente usa `/ruta/index.html`. El Worker se encarga de resolver esto.

- GitHub Pages responde con `206 Partial Content` a bots. El Worker transforma eso en `200 OK` para asegurar previews.

- La etiqueta `og:image` debe tener:
  
  - Un solo `<meta property="og:image">`
  
  - Dimensiones recomendadas: `1200x630`
  
  - Formato `.jpg` o `.png`
  
  - ⚠️ Evitar caracteres no latinos (como chino) en `og:description`

---

## ✅ Estado final validado

- Subdominio: `logos.mundomejor.uk`

- Worker funcionando: ✅

- Preview en WhatsApp y Facebook: ✅

- Assets CSS y JS: ✅

- Imagen OG visible: ✅

- Error 206 eliminado: ✅

---

## 📛 Referencias

- [Cloudflare Workers](https://developers.cloudflare.com/workers/)

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)

- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
