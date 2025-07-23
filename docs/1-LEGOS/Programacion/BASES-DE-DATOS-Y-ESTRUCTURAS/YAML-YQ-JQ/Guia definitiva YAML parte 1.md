## Manual Definitivo de YAML: Guía Práctica de Referencia

Este manual está diseñado para ser una referencia rápida y práctica para construir archivos YAML de manera efectiva. Abarca todos los casos discutidos, situaciones comunes de duda y buenas prácticas para evitar errores.

### 1. Estructura Básica de YAML

- **Indentación:** Usa **dos espacios** para cada nivel de indentación. No uses tabulaciones.
- **Claves y Valores:** Se definen con la sintaxis `clave: valor`.
- **Listas:** Se definen con un guion (-) seguido de un espacio.

### 2. Tipos de Estructuras

#### 2.1 Diccionarios Simples

```yaml
producto:
  nombre: "SmartPage"
  descripcion: "Una herramienta para crear páginas web."
```

- **Descripción:** Aquí `producto` es un diccionario con dos pares clave-valor.

#### 2.2 Listas de Diccionarios

```yaml
productos:
  - nombre: "SmartPage"
    descripcion: "Una herramienta para crear páginas web."
  - nombre: "Dot Ecommerce"
    descripcion: "Solución de ecommerce."
```

- **Descripción:** `productos` es una lista que contiene diccionarios, donde cada diccionario representa un producto.

#### 2.3 Diccionario con Listas

```yaml
instrucciones:
  pasos:
    - "Definir el producto."
    - "Crear el contenido."
```

- **Descripción:** `instrucciones` es un diccionario que contiene una lista llamada `pasos`.

#### 2.4 Diccionario Anidado

```yaml
producto:
  nombre: "SmartPage"
  detalles:
    descripcion: "Una herramienta para crear páginas web."
    caracteristicas:
      - "Interfaz amigable"
      - "Optimización SEO"
```

- **Descripción:** `detalles` es un diccionario que incluye una lista de características.

### 3. Reglas de Sangría

- **Nuevos Niveles:** Cada vez que introduces un nuevo nivel jerárquico, debes usar la sangría.

```yaml
proyecto:
  nombre: "Desarrollo Web"
  fases:
    - fase1:
        descripcion: "Planificación"
        tareas:
          - "Definir requisitos"
          - "Crear cronograma"
```

- **Descripción:** La sangría muestra que `tareas` pertenece a `fase1`, que a su vez pertenece a `fases`.

### 4. Buenas Prácticas

- **Usar Espacios en Lugar de Tabulaciones:** Asegúrate de usar solo espacios para la indentación.

- **Consistencia en la Indentación:** Mantén la misma cantidad de espacios en todo el archivo (recomendado: dos espacios).

- **Nombres Descriptivos:** Usa nombres claros y descriptivos para claves y valores.

- **Evitar Errores Comunes:**
  
  - No mezcles tipos de datos (por ejemplo, no pongas listas dentro de diccionarios sin la adecuada estructura).
  - Verifica que todos los niveles estén correctamente alineados.

### 5. Ejemplos Completos

#### Ejemplo Completo con Varias Estructuras

```yaml
proyecto:
  nombre: "Desarrollo Web"
  etapas:
    - nombre: "Planificación"
      tareas:
        - "Definir requisitos"
        - "Crear cronograma"
    - nombre: "Desarrollo"
      tareas:
        - "Codificar funcionalidades"
        - "Realizar pruebas"
      recursos:
        herramientas:
          - "GitHub"
          - "JIRA"
```

### 6. Casos Especiales

#### Listas dentro de Diccionarios

```yaml
ofertas:
  - descripcion: "Con Dot Ecommerce, hay un 20% de descuento en Smart Page."
```

- La lista contiene descripciones específicas.

#### Diccionarios dentro de Listas

```yaml
articulos_relacionados:
  - titulo: "Título del Artículo Relacionado 1"
    descripcion: "Descripción del primer artículo."
    url: "http://ejemplo.com/articulo-relacionado-1"
```

- Cada artículo relacionado es un diccionario dentro de la lista.

### 7. Interpretación Rápida

- **Palabra dos puntos (:):** Indica un par clave-valor.

- **Guion (-):** Indica que estás en una lista; cada guion representa un nuevo elemento.

- **Sin guion:** Si no hay guion bajo una clave, estás definiendo otro par clave-valor en el mismo nivel.

### Conclusión

Este manual debe servir como una guía práctica para construir y corregir archivos YAML. Recuerda practicar creando diferentes estructuras y revisando las reglas para evitar errores comunes. Si tienes más preguntas o necesitas ejemplos adicionales, ¡no dudes en consultarme!


