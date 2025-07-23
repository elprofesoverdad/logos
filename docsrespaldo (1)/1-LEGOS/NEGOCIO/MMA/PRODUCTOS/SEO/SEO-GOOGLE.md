# Guia y Checklist de SEO de Google

## Estrategia para optimizar la visibilidad de eventos y Noticias. [ver](estrategia-optimizar-visibilidad-eventos-noticias-.md )

- [ ] generar sitemap en formato XML [generate sitemap - Buscar con Google](https://www.google.com/search?q=generate+sitemap&hl=es)

- [ ] [Gestionar sitemaps con el informe "Sitemaps" - Ayuda de Search Console](https://support.google.com/webmasters/answer/7451001?hl=es)

- [ ]  [Gestionar sitemaps con el informe "Sitemaps" - Ayuda de Search Console](https://support.google.com/webmasters/answer/7451001?hl=es)

- [ ]  MArcado de datos y sitemaps de eventos con noticias: **¡Excelente!** Estás en el camino correcto. Permíteme proporcionarte una estrategia clara para optimizar la visibilidad de tus eventos y noticias utilizando datos estructurados:
  
  1. **Página HTML para el Evento**:
     
     - Crea una **página HTML dedicada** para cada evento, como tu “Concierto de Jazz en Vivo”.
     
     - En esta página, agrega el **marcado de datos estructurados** para describir el evento. Utiliza el siguiente ejemplo:
       
       JSON
       
       ```json
       <script type="application/ld+json">
       {
        "@context": "http://schema.org",
        "@type": "Event",
        "name": "Concierto de Jazz en Vivo",
        "startDate": "2024-03-25T19:00:00",
        "endDate": "2024-03-25T22:00:00",
        "location": {
          "@type": "Place",
          "name": "Teatro Municipal"
        }
       }
       </script>
       ```
       
       Código generado por IA. Revisar y usar cuidadosamente. [Más información sobre preguntas frecuentes](https://www.bing.com/new#faq).
     
     - Asegúrate de que esta página esté accesible y enlazada desde otras partes de tu sitio.
  
  2. **Sitemaps**:
     
     - **Sitemap Normal**: Incluye la URL de la página del evento en tu **sitemap normal**. Esto ayudará a Google a rastrear y descubrir la página.
     - **Sitemap de Noticias**: También incluye la misma URL en tu **sitemap de noticias**. Google utilizará esta información para mostrar el evento en Google Noticias.
  
  3. **Páginas de Avance de Noticias**:
     
     - Para las noticias relacionadas con el evento (por ejemplo, anuncios previos, actualizaciones, etc.), crea **páginas separadas**.
     - En estas páginas, utiliza el mismo marcado de datos estructurados para describir el evento.
     - Añade **metadatos adicionales** específicos para las noticias, como el título de la noticia, la fecha de publicación, etc.
  
  4. **Ejemplo de Página de Avance de Noticias**:
     
     - Supongamos que tienes una noticia previa sobre el concierto:
       
       JSON
       
       ```json
       <script type="application/ld+json">
       {
        "@context": "http://schema.org",
        "@type": "NewsArticle",
        "headline": "Anuncio del Concierto de Jazz en Vivo",
        "datePublished": "2024-03-10T10:00:00",
        "articleBody": "¡Próximamente, el Teatro Municipal vibrará con el Concierto de Jazz en Vivo!..."
       }
       </script>
       ```
       
       Código generado por IA. Revisar y usar cuidadosamente. [Más información sobre preguntas frecuentes](https://www.bing.com/new#faq).
     
     - Esta página de avance de noticias también debe estar enlazada desde otras partes de tu sitio.
  
  5. **Monitoreo y Actualización**:
     
     - Mantén tus páginas actualizadas con la información más reciente sobre el evento y las noticias.
     - Monitorea el rendimiento utilizando **Google Search Console** y **Google Analytics**.
  
  En resumen, **una página HTML para el evento**, sitemaps para ambas páginas y **páginas de avance de noticias** con datos estructurados te ayudarán a maximizar la visibilidad. ¡Buena suerte con tu concierto de jazz!
  
  

- [ ]  no follow para que google no de mi prestigio a gente que me use o no siga los enlaces que hago o que hacen en foros.

```html
<a href="https://www.example.com" rel="nofollow">Anchor text here</a>
o bien:


<a href="https://www.example.com" rel="ugc">Anchor text here</a>
```

- [ ] #### Añade `nofollow` automáticamente a las columnas de comentarios y a los tablones de mensajes

- [ ] #### Usa los elementos HTML `<img>` o `<picture>`

- [ ] El elemento `<head>` solo debe contener los siguientes elementos válidos (y ningún otro elemento no válido), según el estándar de HTML:
  
  - `title`
  - `meta`
  - `link`
  - `script`
  - `style`
  - `base`
  - `noscript`
  - `template`  

- [ ] Añade el icono:
1. Crea un icono de página que cumpla con las [directrices](https://developers.google.com/search/docs/appearance/favicon-in-search?hl=es#guidelines).

2. Añade al encabezado de tu página principal una etiqueta `<link>` que tenga esta sintaxis:
   
   <link rel="icon" href="/path/to/favicon.ico">
   
   Para extraer la información del icono de página, Google se basa en los siguientes atributos del elemento `link`:
   
   | Atributos |                                                                                                                                                              |
   | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | `rel`     | Incluye en el atributo `rel` una de las siguientes cadenas:<br><br>- `icon`<br>- `apple-touch-icon`<br>- `apple-touch-icon-precomposed`<br>- `shortcut icon` |
   | `href`    | La URL del icono de página. Puede ser una ruta relativa (`/smile.ico`) o absoluta (`https://example.com/smile.ico`).                                         |

3. Google busca y actualiza tu icono de página siempre que rastrea tu página principal. Si haces algún cambio en este icono y quieres notificárselo a Google, puedes [solicitar la indexación](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl?hl=es) de la página principal de tu sitio. Los cambios pueden tardar varios días en verse reflejados en los resultados de búsqueda.
- [ ] Simplificar la estructura de las URLs
- [ ] Permitir el rastreo de enlaces
- [ ] 
