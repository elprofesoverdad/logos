# Diseñar un post con jeckil y bootstrap

## 

## Estructura básica

```textile
my-jekyll-site/
├── _config.yml
├── _posts/
├── _layouts/
├── _includes/
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
├── index.html
└── other files...
```

## Crear la Plantilla layout Padre del post sin perder el bootstrap

1. Para poder Migrar de Bootstrap a Jeckyll y que los y que bootstrap funcione:

a. pasamos bootstrap si lo hemos descargado a la carpeta assets, también las imágenes que necesitamos y el css y el javascript. Copiamos con blog-css para dejar por el momento la carpeta css original y que no se pierda el bootstrap de la página principal del blog

b. Abre `nombrepost.html` colócale el YAML Front Matter y asegúrate de enlazar correctamente los archivos CSS y JS. Aquí tienes un ejemplo de cómo hacerlo:

```html
---
---

código...

<head>
    <!-- Enlace al CSS de Bootstrap -->
    <link rel="stylesheet" href="{{ '/assets/css/bootstrap.min.css' | relative_url }}">
    <!-- Tu CSS personalizado -->
    <link rel="stylesheet" href="{{ '/assets/css/styles.css' | relative_url }}">
</head>
```

## Notas

### Enlaces

> - Usa `relative_url` para enlazar a archivos estáticos como CSS, JS e imágenes.
> 
> - **Usa `| url`**: Para generar URLs que respeten la configuración de `baseurl` en Jekyll, asegurando que los enlaces funcionen correctamente en diferentes entornos.
> 
> - **Sin `| url`**: Puede ser útil en situaciones donde estás seguro de que siempre estarás en la raíz del dominio, pero es menos flexible.
> 
> - **URLs Absolutas**: Úsalas para enlaces externos o cuando necesites especificar un dominio completo.
>   
>   Dentro de la carpeta `blog`, usa `relative_url` para enlazar a archivos estáticos, pero no para enlazar a otros posts o páginas de Jekyll.



### Procesamiento:

Si deseas que Jekyll procese un archivo que está fuera de las carpetas predeterminadas (_layouts, _includes, _posts... ), asegúrate de incluir el YAML Front Matter :

```html
---
---
```

 al inicio del archivo para que Jekyll pueda interpretar las configuraciones y variables específicas. 



### Ejemplos de Slugs

En el contexto de Jekyll y SEO, un "slug" se refiere a la parte de la URL que identifica de manera única una página o un post en un sitio web. El slug generalmente consiste en palabras clave descriptivas que representan el contenido de la página y que son amigables para los motores de búsqueda y los usuarios. Por ejemplo, en la URL "https://ejemplo.com/articulo-ejemplo", el slug sería "articulo-ejemplo".



Claro, aquí te dejo 15 ejemplos de slugs exitosos que podrían utilizarse en artículos que aborden temas relacionados con las TIC, logística, QR, marketing web, ecommerce y e-learning:

1. **tics-mejores-practicas-seguridad-datos
2. **logistica-eficiente-cadena-suministro
3. **qr-codigos-usos-innovadores
4. **marketing-web-tendencias-2024
5. **ecommerce-experiencia-usuario
6. **elearning-plataformas-interactivas
7. **tics-transformacion-digital-empresas
8. **logistica-optimizacion-rutas-transporte
9. **qr-marketing-campanas-creativas
10. **marketing-web-seo-estrategias-efectivas
11. **ecommerce-pagos-seguros-online
12. **elearning-contenidos-adaptativos
13. **tics-inteligencia-artificial-innovacion
14. **logistica-almacenamiento-inteligente
15. **qr-usabilidad-aplicaciones-moviles
