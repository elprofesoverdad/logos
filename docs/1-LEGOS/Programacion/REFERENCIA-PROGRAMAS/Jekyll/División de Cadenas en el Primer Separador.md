# División de Cadenas en el Primer Separador en Jekyll

## Definición del Algoritmo

### Nombre del Algoritmo
**División de Cadenas en el Primer Separador**

### Descripción
Este algoritmo tiene como objetivo dividir una cadena de texto en dos partes utilizando un separador específico. La división se realiza en la primera aparición del separador encontrado en la cadena. El algoritmo produce dos resultados:
1. La **primera parte** de la cadena, que contiene todo el texto antes del primer separador.
2. El **resto** de la cadena, que incluye el texto desde el primer separador hasta el final de la cadena.

### Entrada
- Una cadena de texto que puede contener uno o más caracteres de separación.
- Un carácter o secuencia de caracteres que actúa como separador.

### Salida
- Dos cadenas: 
  - La parte anterior al primer separador.
  - La parte posterior al primer separador, incluyendo el separador.

### Algoritmo
1. **Dividir** la cadena usando el separador especificado, generando un array.
2. **Asignar** la primera parte (el primer elemento del array) a una variable `primeraParte`.
3. **Unir** los elementos restantes del array (si los hay) con el separador para formar la variable `resto`.
4. **Retornar** ambas partes.

## Código Liquid

Aquí tienes el código Liquid que implementa este algoritmo:

```liquid
{% assign cadena = "cadena]cadem]toto]lilo" %}
{% assign separador = ']' %}

{% assign partes = cadena | split: separador %}

{% assign primeraParte = partes[0] %}
{% assign resto = partes | slice: 1, partes.size | join: separador %}

<p>Primera Parte: {{ primeraParte }}</p>
<p>Resto: {{ resto }}</p>
```

### Explicación del Código

1. **Asignación de la Cadena y Separador**:
   ```liquid
   {% assign cadena = "cadena]cadem]toto]lilo" %}
   {% assign separador = ']' %}
   ```
   - Se define la cadena que se va a dividir y el carácter separador.

2. **División de la Cadena**:
   ```liquid
   {% assign partes = cadena | split: separador %}
   ```
   - La cadena se divide en un array `partes` en cada aparición del carácter `]`.

3. **Obtención de la Primera Parte**:
   ```liquid
   {% assign primeraParte = partes[0] %}
   ```
   - Se asigna a `primeraParte` el primer elemento del array, que es `"cadena"`.

4. **Obtención del Resto**:
   ```liquid
   {% assign resto = partes | slice: 1, partes.size | join: separador %}
   ```
   - Se utiliza `slice: 1, partes.size` para obtener todos los elementos desde el índice 1 hasta el final del array.
   - Luego, se unen esos elementos con `join: separador`, resultando en `"cadem]toto]lilo"`.

5. **Salida de Resultados**:
   ```liquid
   <p>Primera Parte: {{ primeraParte }}</p>
   <p>Resto: {{ resto }}</p>
   ```

### Resultado Esperado

La salida del código será:

- **Primera Parte**: `cadena`
- **Resto**: `cadem]toto]lilo`

## Conclusión

Este algoritmo proporciona una forma precisa y efectiva de dividir cadenas en Liquid utilizando un separador específico, y su implementación es clara y directa. Si tienes más preguntas o necesitas más ejemplos sobre este tema, ¡no dudes en preguntar!