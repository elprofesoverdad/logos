# La base de datos puede ser

Para crear un archivo YAML que contenga información detallada sobre películas y series, aquí tienes la estructura actualizada con los 15 campos, eliminando el campo de "popularidad del actor" que se duplicaba y ajustando la descripción del campo de popularidad de la película o serie.

### Campos para el YAML

1. **ID**: 
   
   - El identificador único de la película o serie.

2. **Tipo**: 
   
   - Indica si es una película o una serie (por ejemplo, `movie` o `tv`).

3. **Título Original**: 
   
   - El título original de la película o serie.

4. **Descripción/Sinopsis**: 
   
   - Breve descripción del contenido.

5. **Fecha de Estreno**: 
   
   - La fecha en la que se estrenó la película o serie (para películas) o la fecha de la primera emisión (para series).

6. **Fecha del Último Episodio**: 
   
   - La fecha en la que se emitió el último episodio (solo si es una serie y está en emisión).

7. **Número de Episodios en la Temporada Actual**: 
   
   - Total de episodios que tiene la temporada actual (solo para series).

8. **Número Total de Temporadas**: 
   
   - Total de temporadas que tiene la serie.

9. **Géneros**: 
   
   - Lista de géneros a los que pertenece la película o serie.

10. **Compañías Productoras**: 
    
    - Lista de las compañías que produjeron la película o serie.

11. **Actores Principales**: 
    
    - Información sobre los actores principales, incluyendo:
      - Nombre
      - Personaje
      - Ruta a su foto (profile_path)
      - Popularidad del actor

12. **Popularidad**: 
    
    - Un valor numérico que indica cuán popular es el contenido, basado en su promedio de votos y otros factores relevantes.

13. **Estado**: 
    
    - Estado actual de la película o serie (por ejemplo, "En emisión", "Finalizado").

14. **URL del Tráiler**: 
    
    - Enlace al tráiler oficial en YouTube.

15. **URL del Poster**: 
    
    - URL del cartel más popular o votado.

### Ejemplo de Estructura YAML

Aquí tienes un ejemplo de cómo podría verse el archivo YAML con los campos mencionados:

```yaml
id: 24428
type: movie
title_original: "The Avengers"
description: "Cuando un enemigo inesperado surge y amenaza la seguridad global..."
release_date: "2012-04-25"
last_episode_date: null  # Solo para series
episodes_in_current_season: null  # Solo para series
total_seasons: null  # Solo para series
genres:
  - Action
  - Adventure
  - Science Fiction
production_companies:
  - name: "Marvel Studios"
    origin_country: "US"
actors:
  - name: "Robert Downey Jr."
    character: "Tony Stark / Iron Man"
    profile_path: "/path/to/profile.jpg"
    popularity: 95.0  # Popularidad del actor
  - name: "Chris Evans"
    character: "Steve Rogers / Captain America"
    profile_path: "/path/to/profile.jpg"
    popularity: 90.0  # Popularidad del actor
popularity: 148.519  # Popularidad basada en votos y otros factores
status: "Released"
trailer_url: "https://www.youtube.com/watch?v=hIR8Ar-Z4hw"
poster_url: "http://image.tmdb.org/t/p/w500/RYMX2wcKCBAr24UyPD7xwmjaTn.jpg"  # Poster más votado
```