# Manual de Referencia para el Uso de la API de TMDb

Este manual proporciona una guía concisa sobre cómo utilizar la API de The Movie Database (TMDb) para buscar información sobre películas y series. A continuación, se detalla el endpoint de búsqueda y los campos devueltos.

## 1. Endpoint de Búsqueda MIXTO Series y Películas

**Descripción**: Este endpoint permite buscar tanto películas como series utilizando una consulta de texto. 

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/search/multi?query={query}&include_adult=false&language=en-US&page=1
```

**Parámetros**:

- **query**: La cadena de búsqueda (por ejemplo, "the avengers").
- **include_adult**: (opcional) Si se establece en `false`, excluye contenido para adultos.
- **language**: (opcional) Define el idioma de los resultados (por defecto es inglés).
- **page**: (opcional) Número de página para paginación de resultados.

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/search/multi?query=the%20avengers&include_adult=false&language=en-US&page=1' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una búsqueda, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "page": 1,
  "results": [
    {
      "backdrop_path": "/path/to/backdrop.jpg",
      "id": 12345,
      "title": "The Avengers",
      "original_title": "The Avengers",
      "overview": "Descripción de la película.",
      "poster_path": "/path/to/poster.jpg",
      "media_type": "movie", // o "tv" para series
      "release_date": "2012-04-25",
      "first_air_date": "1961-01-07", // solo para series
      "vote_average": 7.5,
      "vote_count": 1000
    }
    // ... más resultados
  ],
  "total_results": 100,
  "total_pages": 10
}
```

**Campos Clave**:

- **id**: Identificador único de la película o serie.
- **title / original_title**: Título en inglés y título original.
- **overview**: Sinopsis o descripción breve.
- **poster_path**: Ruta del cartel que se puede usar para construir la URL completa del cartel.
- **backdrop_path**: Ruta del fondo que se puede usar para construir la URL completa del fondo.
- **media_type**: Indica si el resultado es una película (`movie`) o una serie (`tv`).
- **release_date / first_air_date**: Fecha de lanzamiento o primera emisión.
- **vote_average / vote_count**: Promedio y conteo de votos, útil para evaluar la popularidad.

---

Esta sección del manual se centra en cómo obtener información detallada sobre una película específica utilizando su ID, que se relaciona directamente con la búsqueda inicial. **Es crucial destacar que el ID obtenido en la búsqueda (por ejemplo, `24428` para "The Avengers") se utiliza para acceder a datos más específicos sobre esa película.**

## 2. Endpoint para Obtener Detalles de una Película

**Descripción**: Este endpoint permite obtener información detallada sobre una película utilizando su ID.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/movie/{movie_id}?language=en-US
```

**Parámetros**:

- **movie_id**: El identificador único de la película (por ejemplo, `24428`).
- **language**: (opcional) Define el idioma de los resultados (por defecto es inglés).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/movie/24428?language=en-US' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "adult": false,
  "backdrop_path": "/9BBTo63ANSmhC4e6r62OJFuK2GL.jpg",
  "belongs_to_collection": {
    "id": 86311,
    "name": "The Avengers Collection",
    "poster_path": "/yFSIUVTCvgYrpalUktulvk3Gi5Y.jpg",
    "backdrop_path": "/zuW6fOiusv4X9nnW3paHGfXcSll.jpg"
  },
  "budget": 220000000,
  "genres": [
    {
      "id": 878,
      "name": "Science Fiction"
    },
    {
      "id": 28,
      "name": "Action"
    },
    {
      "id": 12,
      "name": "Adventure"
    }
  ],
  "homepage": "https://www.marvel.com/movies/the-avengers",
  "id": 24428,
  "imdb_id": "tt0848228",
  "origin_country": [
    "US"
  ],
  "original_language": "en",
  "original_title": "The Avengers",
  "overview": "When an unexpected enemy emerges and threatens global safety and security, Nick Fury, director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in need of a team to pull the world back from the brink of disaster. Spanning the globe, a daring recruitment effort begins!",
  "popularity": 148.519,
  "poster_path": "/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
  "production_companies": [
    {
      "id": 420,
      "logo_path": "/hUzeosd33nzE5MCNsZxCGEKTXaQ.png",
      "name": "Marvel Studios",
      "origin_country": "US"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "release_date": "2012-04-25",
  "revenue": 1518815515,
  "runtime": 143,
  "spoken_languages": [
    {
      "english_name": "English",
      "iso_639_1": "en",
      "name": "English"
    },
    {
      "english_name": "Hindi",
      "iso_639_1": "hi",
      "name": "हिन्दी"
    },
    {
      "english_name": "Russian",
      "iso_639_1": "ru",
      "name": "Pусский"
    }
  ],
  "status": "Released",
  "tagline": "Some assembly required.",
  "title": "The Avengers",
  "video": false,
  "vote_average": 7.72,
  "vote_count": 30703
}
```

**Campos Clave**:

- **id**: Identificador único de la película (debe coincidir con el ID utilizado en la búsqueda).
- **original_title**: Título original de la película.
- **overview**: Sinopsis o descripción detallada.
- **poster_path**: Ruta del cartel que se puede usar para construir la URL completa del cartel.
- **backdrop_path**: Ruta del fondo que se puede usar para construir la URL completa del fondo.
- **genres**: Lista de géneros asociados a la película, cada uno con su propio ID y nombre.
- **production_companies**: Información sobre las compañías productoras, incluyendo su ID y nombre.
- **homepage**: URL oficial de la película.

---

 Continuación del Manual de Referencia para el Uso de la API de TMDb

En esta sección, abordaremos cómo obtener los videos relacionados con una película específica utilizando su ID. **Es importante resaltar que el ID utilizado aquí debe ser el mismo que se obtuvo anteriormente (por ejemplo, `24428` para "The Avengers"), lo que permite acceder a los trailers y otros videos asociados a esa película.**

## 3. Endpoint para Obtener Videos de una Película

**Descripción**: Este endpoint permite obtener una lista de videos relacionados con una película específica, incluyendo trailers y clips.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US
```

**Parámetros**:

- **movie_id**: El identificador único de la película (por ejemplo, `24428`).
- **language**: (opcional) Define el idioma de los resultados (por defecto es inglés).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/movie/24428/videos?language=en-US' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "id": 24428,
  "results": [
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Assembling the Lakota",
      "key": "r_pPfp7lnIM",
      "site": "YouTube",
      "size": 1080,
      "type": "Featurette",
      "official": true,
      "published_at": "2024-07-05T19:00:33.000Z",
      "id": "668b87a2047a30c74898ccd2"
    },
    {
      "iso_639_1": "en",
      "name": "Official Trailer 2",
      "key": "hIR8Ar-Z4hw",
      "site": "YouTube",
      "type": "Trailer",
      ...
    }
    // ... más resultados
  ]
}
```

**Campos Clave**:

- **id**: Identificador único de la película (debe coincidir con el ID utilizado en la búsqueda).
- **results**: Lista de videos relacionados, donde cada video tiene:
  - **name**: Título del video.
  - **key**: Clave del video que se utiliza para construir la URL del video en YouTube (por ejemplo, `https://www.youtube.com/watch?v={key}`).
  - **site**: El sitio donde está alojado el video (generalmente YouTube).
  - **type**: Tipo de video (por ejemplo, `Trailer`, `Featurette`, `Clip`).
  - **official**: Indica si el video es oficial.

### Consideraciones Importantes

- **Relación entre Endpoints**: Es esencial recordar que el ID utilizado en este endpoint debe ser el mismo que se obtuvo del endpoint de búsqueda y del endpoint de detalles de la película. Esto permite acceder a información específica sobre los trailers y otros videos relacionados.

- **Construcción de URLs para Videos**: Utiliza la clave (`key`) devuelta en los resultados para construir la URL completa del video. Por ejemplo, para un trailer:
  
  ```plaintext
  https://www.youtube.com/watch?v={key}
  ```

---

Continuación del Manual de Referencia para el Uso de la API de TMDb

En esta sección, abordaremos cómo obtener imágenes y posters relacionados con una película específica utilizando su ID. **Es fundamental destacar que el ID utilizado aquí debe ser el mismo que se obtuvo anteriormente (por ejemplo, `24428` para "The Avengers"), lo que permite acceder a los posters y otras imágenes asociadas a esa película.**

## 4. Endpoint para Obtener Imágenes de una Película

**Descripción**: Este endpoint permite obtener una lista de imágenes, incluyendo posters y fondos, relacionados con una película específica.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/movie/{movie_id}/images
```

**Parámetros**:

- **movie_id**: El identificador único de la película (por ejemplo, `24428`).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/movie/24428/images' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "backdrops": [
    {
      "aspect_ratio": 1.778,
      "height": 2160,
      "file_path": "/9BBTo63ANSmhC4e6r62OJFuK2GL.jpg",
      "vote_average": 5.39,
      "vote_count": 6,
      ...
    },
    ...
  ],
  "posters": [
    {
      "aspect_ratio": 0.67,
      "height": 3000,
      "file_path": "/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
      "vote_average": 7.72,
      "vote_count": 30704,
      ...
    },
    ...
  ]
}
```

**Campos Clave**:

- **backdrops**: Lista de imágenes de fondo asociadas a la película.
- **posters**: Lista de posters asociados a la película.
- **file_path**: Ruta de cada imagen que se puede usar para construir la URL completa.
- **vote_average**: Promedio de votos para cada imagen, útil para determinar la calidad o popularidad.
- **vote_count**: Conteo de votos para cada imagen.

### Obtención de Posters Principales

Para obtener los posters principales y aquellos con mayor promedio de votos, puedes filtrar los resultados en tu aplicación. Por ejemplo, puedes seleccionar las tres imágenes con el mayor `vote_average` de la lista `posters`.

### Consideraciones Importantes

- **Relación entre Endpoints**: Es esencial recordar que el ID utilizado en este endpoint debe ser el mismo que se obtuvo del endpoint de búsqueda y del endpoint de detalles de la película. Esto permite acceder a información específica sobre los posters y otros elementos visuales relacionados.

- **Construcción de URLs para Imágenes**: Utiliza el `file_path` devuelto en los resultados para construir la URL completa de las imágenes. Por ejemplo:
  
  ```plaintext
  https://image.tmdb.org/t/p/w500{file_path}
  ```

---

Continuación del Manual de Referencia para el Uso de la API de TMDb

En esta sección, abordaremos cómo obtener posters e imágenes relacionadas con una película específica utilizando su ID. **Es crucial resaltar que el ID utilizado aquí debe ser el mismo que se obtuvo anteriormente (por ejemplo, `24428` para "The Avengers"), lo que permite acceder a los posters y otras imágenes asociadas a esa película.**

## 5. Endpoint para Obtener Posters e Imágenes de una Película

**Descripción**: Este endpoint permite obtener una lista de imágenes, incluyendo posters y fondos, relacionados con una película específica.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/movie/{movie_id}/images
```

**Parámetros**:

- **movie_id**: El identificador único de la película (por ejemplo, `24428`).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/movie/24428/images' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "backdrops": [
    {
      "aspect_ratio": 1.778,
      "height": 2160,
      "file_path": "/9BBTo63ANSmhC4e6r62OJFuK2GL.jpg",
      "vote_average": 5.39,
      "vote_count": 6
    },
    ...
  ],
  "posters": [
    {
      "aspect_ratio": 0.67,
      "height": 3000,
      "file_path": "/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg",
      "vote_average": 7.72,
      "vote_count": 30704
    },
    ...
  ]
}
```

**Campos Clave**:

- **backdrops**: Lista de imágenes de fondo asociadas a la película.
- **posters**: Lista de posters asociados a la película.
- **file_path**: Ruta de cada imagen que se puede usar para construir la URL completa.
- **vote_average**: Promedio de votos para cada imagen, útil para determinar la calidad o popularidad.
- **vote_count**: Conteo de votos para cada imagen.

### Obtención de Posters Principales

Para obtener los posters principales y aquellos con mayor promedio de votos, puedes filtrar los resultados en tu aplicación. Por ejemplo, puedes seleccionar las tres imágenes con el mayor `vote_average` de la lista `posters`.

### Ejemplo de Filtrado para Obtener los Mejores Posters

Al recibir la respuesta, puedes implementar un código que filtre los posters por `vote_average` y seleccione los tres mejores:

```python
# Suponiendo que 'response' es el JSON devuelto por la API
top_posters = sorted(response['posters'], key=lambda x: x['vote_average'], reverse=True)[:3]
```

### Consideraciones Importantes

- **Relación entre Endpoints**: Es esencial recordar que el ID utilizado en este endpoint debe ser el mismo que se obtuvo del endpoint de búsqueda y del endpoint de detalles de la película. Esto permite acceder a información específica sobre los posters y otros elementos visuales relacionados.

- **Construcción de URLs para Imágenes**: Utiliza el `file_path` devuelto en los resultados para construir la URL completa de las imágenes. Por ejemplo:
  
  ```plaintext
  https://image.tmdb.org/t/p/w500{file_path}
  ```

---


En esta sección, abordaremos cómo obtener información sobre las personas (actores, directores, etc.) populares utilizando la API de TMDb. **Es importante destacar que el campo `popularity` es un indicador clave que se utiliza para evaluar la popularidad de los actores y sus trabajos.**

## 6. Endpoint para Obtener Personas Populares

**Descripción**: Este endpoint permite obtener una lista de personas populares en la industria del cine y la televisión.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/person/popular?language=en-US&page=1
```

**Parámetros**:

- **language**: (opcional) Define el idioma de los resultados (por defecto es inglés).
- **page**: (opcional) Número de página para paginación de resultados.

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/person/popular?language=en-US&page=1' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "page": 1,
  "results": [
    {
      "adult": false,
      "gender": 1,
      "id": 129700,
      "known_for_department": "Acting",
      "name": "Nozomi Sasaki",
      "original_name": "佐々木希",
      "popularity": 336.058,
      "profile_path": "/k5WCvK8Zrakp6uPizXYxPoPrxIq.jpg",
      ...
    },
    ...
  ]
}
```

**Campos Clave**:

- **id**: Identificador único de la persona.
- **name**: Nombre de la persona.
- **original_name**: Nombre original de la persona.
- **popularity**: Índice de popularidad, que indica cuán conocido es el individuo en la industria. Este valor puede ser utilizado para destacar a los actores más populares en tu aplicación o sitio web.
- **profile_path**: Ruta de la imagen del perfil que se puede usar para construir la URL completa.

### Uso del Campo `popularity`

El campo `popularity` es crucial para determinar qué actores o actrices son más relevantes en un momento dado. Puedes utilizar este dato para:

- **Filtrar Actores Populares**: Mostrar solo los actores con un alto índice de popularidad en tu aplicación.
- **Ordenar Resultados**: Presentar a los actores más populares primero en listas o galerías.
- **Análisis de Tendencias**: Utilizar el índice de popularidad para analizar qué actores están ganando notoriedad o perdiendo interés con el tiempo.

### Ejemplo de Filtrado por Popularidad

Al recibir la respuesta, puedes implementar un código que filtre las personas por `popularity` y seleccione las tres más populares:

```python
# Suponiendo que 'response' es el JSON devuelto por la API
top_people = sorted(response['results'], key=lambda x: x['popularity'], reverse=True)[:3]
```

---

Continuación del Manual de Referencia para el Uso de la API de TMDb

En esta sección, abordaremos cómo obtener los créditos combinados de una persona específica utilizando su ID. **Es importante resaltar que el ID utilizado aquí debe ser el mismo que se obtuvo anteriormente (por ejemplo, `129700` para Nozomi Sasaki), lo que permite acceder a todos los trabajos en los que ha participado, tanto en películas como en series.**

## 7. Endpoint para Obtener Créditos Combinados de una Persona

**Descripción**: Este endpoint permite obtener una lista de todos los trabajos (películas y series) en los que ha participado una persona específica.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/person/{person_id}/combined_credits?language=en-US
```

**Parámetros**:

- **person_id**: El identificador único de la persona (por ejemplo, `129700`).
- **language**: (opcional) Define el idioma de los resultados (por defecto es inglés).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/person/129700/combined_credits?language=en-US' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "cast": [
    {
      "adult": false,
      "backdrop_path": null,
      "genre_ids": [28, 35],
      "id": 1100753,
      "original_language": "ja",
      "original_title": "バトルキャッツ！",
      "overview": "Follows the adventures (and cool fights!) of a girl with psychic powers and her anthropomorphic cat best friend.",
      "popularity": 2.566,
      "poster_path": "/5Wm893AGS8jXxOq6EHncl5h4skt.jpg",
      ...
    },
    ...
  ]
}
```

**Campos Clave**:

- **cast**: Lista de trabajos en los que ha participado la persona, donde cada trabajo tiene:
  - **id**: Identificador único del trabajo.
  - **title / original_title**: Título de la película o serie.
  - **overview**: Descripción breve del trabajo.
  - **poster_path**: Ruta del poster que se puede usar para construir la URL completa.
  - **popularity**: Índice de popularidad del trabajo, útil para determinar cuáles son más relevantes.

### ¿Para qué sirve este Endpoint?

El endpoint de créditos combinados es útil para obtener un resumen completo de la carrera de un actor o miembro del equipo. Permite ver todos los proyectos en los que han trabajado, lo que es valioso para:

- **Mostrar Filmografía**: Puedes utilizar esta información para crear una sección en tu aplicación o sitio web que muestre la filmografía completa de un actor o director.
- **Evaluar Popularidad**: Al incluir el índice de popularidad, puedes resaltar las obras más conocidas o exitosas de esa persona.
- **Conectar Proyectos Relacionados**: Facilita la creación de enlaces entre diferentes proyectos y actores, mejorando la experiencia del usuario al explorar contenido relacionado.

---

Continuación del Manual de Referencia para el Uso de la API de TMDb

En esta sección, abordaremos cómo obtener imágenes de una persona específica utilizando su ID. **Es fundamental destacar que el ID utilizado aquí debe ser el mismo que se obtuvo anteriormente (por ejemplo, `129700` para Nozomi Sasaki), lo que permite acceder a las imágenes asociadas a esa persona. Estas imágenes son especialmente importantes para mostrar el cast principal de una película, ya que permiten incluir fotos de los actores en tu aplicación o sitio web.**

## 8. Endpoint para Obtener Imágenes de una Persona

**Descripción**: Este endpoint permite obtener una lista de imágenes asociadas a una persona específica, incluyendo fotos de perfil y otros tipos de imágenes.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/person/{person_id}/images
```

**Parámetros**:

- **person_id**: El identificador único de la persona (por ejemplo, `129700`).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/person/129700/images' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "id": 129700,
  "profiles": [
    {
      "aspect_ratio": 0.667,
      "height": 900,
      "iso_639_1": null,
      "file_path": "/k5WCvK8Zrakp6uPizXYxPoPrxIq.jpg",
      "vote_average": 5.392,
      "vote_count": 8
    },
    ...
  ]
}
```

**Campos Clave**:

- **id**: Identificador único de la persona (debe coincidir con el ID utilizado en la búsqueda).
- **profiles**: Lista de imágenes asociadas a la persona, donde cada imagen tiene:
  - **file_path**: Ruta de la imagen que se puede usar para construir la URL completa.
  - **vote_average**: Promedio de votos para cada imagen, útil para determinar cuáles son más relevantes.
  - **vote_count**: Conteo de votos para cada imagen.

### Importancia del Campo `vote_average`

El campo `vote_average` es crucial para determinar qué imágenes son más populares o bien recibidas. Puedes utilizar este dato para:

- **Filtrar Imágenes Populares**: Mostrar solo las imágenes con un alto índice de votación en tu aplicación.
- **Ordenar Resultados**: Presentar las imágenes más populares primero en listas o galerías.

### Ejemplo de Filtrado por Votación

Al recibir la respuesta, puedes implementar un código que filtre las imágenes por `vote_average` y seleccione las tres más votadas:

```python
# Suponiendo que 'response' es el JSON devuelto por la API
top_images = sorted(response['profiles'], key=lambda x: x['vote_average'], reverse=True)[:3]
```

---

Continuación del Manual de Referencia para el Uso de la API de TMDb

En esta sección, abordaremos cómo obtener información detallada sobre una serie específica utilizando su ID. **El ID de la serie se obtiene del endpoint de búsqueda mixto, que permite localizar tanto películas como series. En este caso, el ID de la serie es `124364`, que corresponde a la serie "FROM".**

## 9. Endpoint para Obtener Detalles de una Serie

**Descripción**: Este endpoint permite obtener información detallada sobre una serie utilizando su ID.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/tv/{tv_id}?language=en-US
```

**Parámetros**:

- **tv_id**: El identificador único de la serie (por ejemplo, `124364`).
- **language**: (opcional) Define el idioma de los resultados (por defecto es inglés).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/tv/124364?language=en-US' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "adult": false,
  "backdrop_path": "/q3UGWifvIpdey1T2efX4dSmbZpU.jpg",
  "created_by": [
    {
      "id": 2347147,
      "credit_id": "6088c7ca2da8460057c88d59",
      "name": "John Griffin",
      "original_name": "John Griffin",
      "gender": 2,
      "profile_path": "/lAIA3ECbx2ZtMUiOyqTbWNvKTdO.jpg"
    }
  ],
  "episode_run_time": [
    50
  ],
  "first_air_date": "2022-02-20",
  "genres": [
    {
      "id": 9648,
      "name": "Mystery"
    },
    {
      "id": 18,
      "name": "Drama"
    },
    {
      "id": 10765,
      "name": "Sci-Fi & Fantasy"
    }
  ],
  "homepage": "https://www.mgmplus.com/series/from",
  "id": 124364,
  "in_production": true,
  "languages": [
    "en",
    "ka",
    "de"
  ],
  "last_air_date": "2024-11-17",
  "last_episode_to_air": {
    "id": 5560983,
    "name": "Revelations: Chapter One",
    "overview": "Tensions are at an all time high as the residents of town learn that one of their own has gone missing.",
    "vote_average": 0,
    "vote_count": 0,
    "air_date": "2024-11-17",
    "episode_number": 9,
    "episode_type": "standard",
    "production_code": "",
    "runtime": 58,
    "season_number": 3,
    "show_id": 124364,
    "still_path": "/g5OzMqOZRNiCsAtGYPrC57NpYkT.jpg"
  },
  "name": "FROM",
  "next_episode_to_air": {
    "id": 5560984,
    "name": "Revelations: Chapter Two",
    "overview": "",
    "vote_average": 0,
    "vote_count": 0,
    "air_date": "2024-11-24",
    "episode_number": 10,
    "episode_type": "finale",
    "production_code": "",
    "runtime": null,
    "season_number": 3,
    "show_id": 124364,
    "still_path": null
  },
  "networks": [
    {
      "id": 922,
      "logo_path": "/9aH86hGHVQfvhAqrDRv1EINoxua.png",
      "name": "Epix",
      "origin_country": "US"
    },
    {
      "id": 6219,
      "logo_path": "/89TXvQzvoKvyqD9EEogohzMJ8D6.png",
      "name": "MGM+",
      "origin_country": "US"
    }
  ],
  "number_of_episodes": 30,
  "number_of_seasons": 3,
  "origin_country": [
    "US"
  ],
  "original_language": "en",
  "original_name": "FROM",
  "overview": "Unravel the mystery of a nightmarish town in middle America that traps all those who enter. As the unwilling residents fight to keep a sense of normalcy and search for a way out, they must also survive the threats of the surrounding forest – including the terrifying creatures that come out when the sun goes down.",
  "popularity": 2012.101,
  "poster_path": "/cjXLrg4R7FRPFafvuQ3SSznQOd9.jpg",
  "production_companies": [
    {
      "id": 106544,
      "logo_path": "/psd84iF7PTGrKf4yFOStKj8JbAh.png",
      "name": "AGBO",
      "origin_country": "US"
    },
    {
      "id": 51593,
      "logo_path": "/qkmCZvtCAbNmRto9RdOd2mRm1IB.png",
      "name": "Midnight Radio",
      "origin_country": "US"
    },
    {
      "id": 6805,
      "logo_path": "/4774MDXAu1vsapNyTv1LK3S5Ww1.png",
      "name": "Epix",
      "origin_country": "US"
    },
    {
      "id": 2230,
      "logo_path": "/igOjospzsKQIbpuFCGhoN5F9icS.png",
      "name": "MGM Television",
      "origin_country": "US"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "seasons": [
    {
      "air_date": "2022-02-20",
      "episode_count": 10,
      "id": 192632,
      "name": "Season 1",
      "overview": "",
      "poster_path": "/ps46NdLlH70ptDD8ailTL8TCZU3.jpg",
      "season_number": 1,
      "vote_average": 7.6
    },
    {
      "air_date": "2023-04-23",
      "episode_count": 10,
      "id": 323757,
      "name": "Season 2",
      "overview": "Hidden truths about the nature and terrifying origins of the town begin to emerge, even as life for its residents is plunged into chaos by the arrival of mysterious newcomers.",
      "poster_path": "/A9opOOAgp9u2BEl5AteNkA5nrZW.jpg",
      "season_number": 2,
      "vote_average": 6.8
    },
    {
      "air_date": "2024-09-22",
      "episode_count": 10,
      "id": 391491,
      "name": "Season 3",
      "overview": "",
      "poster_path": "/sj64QEEb6JM1CdCfXHaIbA3WPx8.jpg",
      "season_number": 3,
      "vote_average": 7.1
    }
  ],
  "spoken_languages": [
    {
      "english_name": "English",
      "iso_639_1": "en",
      "name": "English"
    },
    {
      "english_name": "Georgian",
      "iso_639_1": "ka",
      "name": "ქართული"
    },
    {
      "english_name": "German",
      "iso_639_1": "de",
      "name": "Deutsch"
    }
  ],
  "status": "Returning Series",
  "tagline": "",
  "type": "Scripted",
  "vote_average": 8.2,
  "vote_count": 1429
}
```

**Campos Clave**:

- **id**: Identificador único de la serie.
- **name**: Título de la serie.
- **overview**: Sinopsis o descripción breve.
- **backdrop_path**: Ruta del fondo que se puede usar para construir la URL completa del fondo.
- **first_air_date**: Fecha en que se emitió por primera vez la serie.
- **genres**: Lista de géneros asociados a la serie.

### Importancia del Endpoint

Este endpoint es esencial para obtener información detallada sobre una serie específica. Proporciona datos relevantes que pueden ser utilizados para:

- **Mostrar Detalles en Aplicaciones**: Puedes mostrar información como el título, sinopsis y géneros en tu aplicación o sitio web.
- **Construir Secciones Dedicadas a Series**: Utiliza esta información para crear secciones específicas para series en tu plataforma, mejorando la experiencia del usuario al explorar contenido.

---

Continuación del Manual de Referencia para el Uso de la API de TMDb

En esta sección, abordaremos cómo obtener imágenes relacionadas con una serie específica utilizando su ID. **El ID de la serie se obtiene del endpoint de búsqueda mixto, que permite localizar tanto películas como series. En este caso, el ID de la serie es `124364`, que corresponde a la serie "FROM".**

## 10. Endpoint para Obtener Imágenes de una Serie

**Descripción**: Este endpoint permite obtener una lista de imágenes asociadas a una serie específica, incluyendo fondos y posters.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/tv/{tv_id}/images
```

**Parámetros**:

- **tv_id**: El identificador único de la serie (por ejemplo, `124364`).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/tv/124364/images' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "backdrops": [
    {
      "aspect_ratio": 1.778,
      "height": 2160,
      "file_path": "/q3UGWifvIpdey1T2efX4dSmbZpU.jpg",
      "vote_average": 5.458,
      "vote_count": 13
    },
    ...
  ],
  "posters": [
    {
      "aspect_ratio": 0.67,
      "height": 3000,
      "file_path": "/cjXLrg4R7FRPFafvuQ3SSznQOd9.jpg",
      "vote_average": 7.72,
      "vote_count": 30704
    },
    ...
  ]
}
```

**Campos Clave**:

- **backdrops**: Lista de imágenes de fondo asociadas a la serie.
- **posters**: Lista de posters asociados a la serie.
- **file_path**: Ruta de cada imagen que se puede usar para construir la URL completa.
- **vote_average**: Promedio de votos para cada imagen, útil para determinar la calidad o popularidad.
- **vote_count**: Conteo de votos para cada imagen.

### Importancia del Campo `vote_average`

El campo `vote_average` es crucial para determinar qué imágenes son más populares o bien recibidas. Puedes utilizar este dato para:

- **Filtrar Imágenes Populares**: Mostrar solo las imágenes con un alto índice de votación en tu aplicación.
- **Ordenar Resultados**: Presentar las imágenes más populares primero en listas o galerías.

### Ejemplo de Filtrado por Votación

Al recibir la respuesta, puedes implementar un código que filtre las imágenes por `vote_average` y seleccione las tres más votadas:

```python
# Suponiendo que 'response' es el JSON devuelto por la API
top_images = sorted(response['backdrops'], key=lambda x: x['vote_average'], reverse=True)[:3]
```

---

Continuación del Manual de Referencia para el Uso de la API de TMDb

En esta sección, abordaremos cómo obtener videos relacionados con una serie específica utilizando su ID. **El ID de la serie se obtiene del endpoint de búsqueda mixto, que permite localizar tanto películas como series. En este caso, el ID de la serie es `124364`, que corresponde a la serie "FROM".**

### Endpoint para Obtener Videos de una Serie

**Descripción**: Este endpoint permite obtener una lista de videos relacionados con una serie específica, incluyendo trailers, clips y detrás de cámaras.

**URL del Endpoint**:

```
GET https://api.themoviedb.org/3/tv/{tv_id}/videos?language=en-US
```

**Parámetros**:

- **tv_id**: El identificador único de la serie (por ejemplo, `124364`).
- **language**: (opcional) Define el idioma de los resultados (por defecto es inglés).

**Ejemplo de Solicitud**:

```bash
curl --request GET \
  --url 'https://api.themoviedb.org/3/tv/124364/videos?language=en-US' \
  --header 'Authorization: Bearer {YOUR_API_TOKEN}' \
  --header 'accept: application/json'
```

### Campos Devueltos

Al realizar una solicitud a este endpoint, la respuesta incluirá un objeto JSON con la siguiente estructura:

```json
{
  "id": 124364,
  "results": [
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Season 1 - Overview",
      "key": "qHItJdOsslw",
      "site": "YouTube",
      "size": 1080,
      "type": "Featurette",
      "official": true,
      "published_at": "2022-02-17T20:08:28.000Z",
      ...
    },
    ...
  ]
}
```

**Campos Clave**:

- **id**: Identificador único de la serie (debe coincidir con el ID utilizado en la búsqueda).
- **results**: Lista de videos relacionados, donde cada video tiene:
  - **name**: Título del video.
  - **key**: Clave del video que se utiliza para construir la URL del video en YouTube (por ejemplo, `https://www.youtube.com/watch?v={key}`).
  - **site**: El sitio donde está alojado el video (generalmente YouTube).
  - **type**: Tipo de video (por ejemplo, `Trailer`, `Featurette`, `Clip`).
  - **official**: Indica si el video es oficial.

### Importancia del Endpoint

Este endpoint es esencial para obtener contenido multimedia relacionado con una serie. Proporciona datos relevantes que pueden ser utilizados para:

- **Mostrar Trailers y Clips**: Puedes mostrar trailers y otros videos promocionales en tu aplicación o sitio web.
- **Mejorar la Experiencia del Usuario**: Al incluir videos, puedes aumentar el interés y la interacción del usuario con el contenido.

### Ejemplo de Construcción de URL para Videos

Utiliza la clave (`key`) devuelta en los resultados para construir la URL completa del video. Por ejemplo, para un trailer:

```plaintext
https://www.youtube.com/watch?v={key}
```

---
