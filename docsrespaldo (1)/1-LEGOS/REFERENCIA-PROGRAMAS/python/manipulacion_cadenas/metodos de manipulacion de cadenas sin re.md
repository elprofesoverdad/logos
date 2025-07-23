

## Técnicas para Trabajar con Patrones sin `re`

### 1. **Métodos de Cadena Básicos**

Estos métodos permiten realizar búsquedas y validaciones simples.

#### `str.count(substring)`

- Cuenta cuántas veces aparece una subcadena en la cadena.
  
  ```python
  texto = "Hola Mundo"
  conteo = texto.count("o")  # Salida: 2
  ```

#### `str.find(substring)` y `str.index(substring)`

- Busca la posición de una subcadena y devuelve su índice.
  
  ```python
  indice = texto.find("Mundo")  # Salida: 5
  # O usando index()
  indice = texto.index("Mundo")  # Salida: 5
  ```

### 2. **Comprobaciones de Caracteres**

Puedes utilizar métodos de cadena para verificar características específicas de los caracteres.

#### Verificar si una cadena es alfanumérica

```python
cadena = "Python123"
es_alfanumerica = cadena.isalnum()  # Salida: True
```

#### Verificar si todos los caracteres son letras

```python
cadena = "Python"
son_letras = cadena.isalpha()  # Salida: True
```

### 3. **Slicing y Acceso a Caracteres**

El *slicing* permite acceder a partes específicas de una cadena.

#### Acceso a Subcadenas

```python
cadena = "Hola Mundo"
subcadena = cadena[0:4]  # Salida: "Hola"
```

### 4. **Uso de Listas y Comprensiones**

Puedes usar listas y comprensiones para filtrar o transformar cadenas basadas en condiciones específicas.

#### Filtrar Caracteres

```python
texto = "Hola123"
solo_letras = ''.join([c for c in texto if c.isalpha()])  # Salida: "Hola"
```

#### Extraer Dígitos

```python
solo_digitos = ''.join([c for c in texto if c.isdigit()])  # Salida: "123"
```

### 5. **Validación de Patrones Simples**

Puedes crear funciones que validen patrones simples sin usar expresiones regulares.

#### Validar un Formato Simple (Ejemplo: Números de Teléfono)

```python
def validar_telefono(telefono):
    return len(telefono) == 10 and telefono.isdigit()

telefono_valido = "1234567890"
print(validar_telefono(telefono_valido))  # Salida: True

telefono_invalido = "12345abcde"
print(validar_telefono(telefono_invalido))  # Salida: False
```

### 6. **Uso de Funciones Personalizadas**

Puedes crear funciones que implementen lógica similar a la búsqueda de patrones.

#### Ejemplo: Búsqueda de Palabras en una Cadena

```python
def buscar_palabra(texto, palabra):
    palabras = texto.split()
    return palabra in palabras

texto = "La vida es bella"
print(buscar_palabra(texto, "vida"))  # Salida: True
print(buscar_palabra(texto, "feliz"))  # Salida: False
```

##Python proporciona una amplia gama de métodos para manipular cadenas de texto. A continuación, se presenta una lista detallada y exhaustiva de los métodos más comunes y útiles, organizados por categorías, junto con descripciones concisas de cada uno.

## Métodos de Manipulación de Cadenas en Python

### 1. **Métodos de Formateo y Concatenación**

- **`str.format()`**: Permite insertar valores en cadenas utilizando marcadores de posición.
  
  ```python
  nombre = "Juan"
  saludo = "Hola, {}".format(nombre)
  ```

- **`f-strings` (Python 3.6+)**: Permite la interpolación de variables directamente dentro de cadenas.
  
  ```python
  nombre = "Juan"
  saludo = f"Hola, {nombre}"
  ```

- **`str.join(iterable)`**: Une los elementos de un iterable en una sola cadena, usando el string que llama al método como separador.
  
  ```python
  palabras = ["Hola", "mundo"]
  resultado = " ".join(palabras)  # Salida: "Hola mundo"
  ```

### 2. **Métodos de Búsqueda y Reemplazo**

- **`str.replace(old, new)`**: Reemplaza todas las ocurrencias de una subcadena por otra.
  
  ```python
  texto = "Hola Mundo"
  nuevo_texto = texto.replace("Mundo", "Python")  # Salida: "Hola Python"
  ```

- **`str.find(substring)`**: Devuelve el índice de la primera aparición de la subcadena; devuelve -1 si no se encuentra.
  
  ```python
  index = texto.find("Mundo")  # Salida: 5
  ```

- **`str.rfind(substring)`**: Similar a `find()`, pero busca desde el final de la cadena.

- **`str.index(substring)`**: Igual que `find()`, pero lanza un error si la subcadena no se encuentra.

### 3. **Métodos de División y Unión**

- **`str.split(separator)`**: Divide la cadena en una lista utilizando el separador especificado.
  
  ```python
  texto = "Uno, Dos, Tres"
  lista = texto.split(", ")  # Salida: ['Uno', 'Dos', 'Tres']
  ```

- **`str.rsplit(separator)`**: Similar a `split()`, pero comienza desde el final.

- **`str.splitlines()`**: Divide la cadena en líneas y devuelve una lista.

- **`str.partition(separator)`**: Divide la cadena en tres partes: antes del separador, el separador mismo y después del separador.

### 4. **Métodos de Modificación**

- **`str.strip([chars])`**: Elimina caracteres al inicio y al final; por defecto, elimina espacios.

- **`str.lstrip([chars])`**: Elimina caracteres solo al inicio.

- **`str.rstrip([chars])`**: Elimina caracteres solo al final.

- **`str.upper()`**: Convierte todos los caracteres a mayúsculas.

- **`str.lower()`**: Convierte todos los caracteres a minúsculas.

- **`str.title()`**: Convierte el primer carácter de cada palabra a mayúscula.

- **`str.capitalize()`**: Convierte el primer carácter a mayúscula y el resto a minúsculas.

- **`str.swapcase()`**: Cambia mayúsculas por minúsculas y viceversa.

### 5. **Métodos de Comprobación**

- **`str.startswith(prefix)`**: Devuelve `True` si la cadena comienza con el prefijo especificado.

- **`str.endswith(suffix)`**: Devuelve `True` si la cadena termina con el sufijo especificado.

- **`str.isalnum()`**: Devuelve `True` si todos los caracteres son alfanuméricos.

- **`str.isalpha()`**: Devuelve `True` si todos los caracteres son letras.

- **`str.isdigit()`**: Devuelve `True` si todos los caracteres son dígitos.

### 6. **Métodos Avanzados**

- **`str.translate(table)`**: Aplica una tabla de traducción (usualmente creada con `str.maketrans()`) para reemplazar caracteres.

- **`str.maketrans(x, y)`**: Crea una tabla de traducción para usar con `translate()`.

### 7. **Métodos para Obtener Información**

- **`len(string)`**: Devuelve la longitud de la cadena.

- **`str.count(substring)`**: Cuenta cuántas veces aparece una subcadena en la cadena.

### Ejemplo Completo

Aquí tienes un ejemplo que combina varios métodos:

```python
texto = "   Bienvenido a Python. Python es increíble!   "
# Limpiar espacios
texto_limpio = texto.strip()
# Reemplazar palabras
texto_reemplazado = texto_limpio.replace("Python", "programación")
# Dividir en palabras
palabras = texto_reemplazado.split()
# Contar ocurrencias
conteo_python = texto_limpio.count("Python")
print(palabras)  
# Salida esperada: ['Bienvenido', 'a', 'programación.', 'programación', 'es', 'increíble!']
print(f"La palabra 'Python' aparece {conteo_python} veces.")
```

Aquí tienes una lista de métodos y técnicas adicionales para la manipulación de cadenas en Python, que no se mencionaron en la respuesta anterior. Estos métodos son nativos de Python y están diseñados para ser fáciles de usar y comprender, proporcionando soluciones eficientes para diversas necesidades de manipulación de texto.

## Métodos y Técnicas Avanzadas para Manipulación de Cadenas

## 1. **Métodos de Comprobación Avanzados**

- **`str.isdigit()`**: Devuelve `True` si todos los caracteres en la cadena son dígitos.
- **`str.isalpha()`**: Devuelve `True` si todos los caracteres son letras.
- **`str.isalnum()`**: Devuelve `True` si todos los caracteres son alfanuméricos (letras y números).
- **`str.isspace()`**: Devuelve `True` si todos los caracteres son espacios en blanco.
- **`str.islower()`**: Devuelve `True` si todos los caracteres son minúsculas.
- **`str.isupper()`**: Devuelve `True` si todos los caracteres son mayúsculas.

## 2. **Métodos de Slicing y Acceso**

- **Acceso a Caracteres**: Puedes acceder a caracteres individuales usando índices.python
  
  `cadena = "Hola" letra = cadena[1]  # Salida: 'o'`

- **Slicing**: Extrae subcadenas usando el formato `cadena[inicio:fin]`.python
  
  `subcadena = cadena[1:3]  # Salida: 'ol'`

## 3. **Métodos de Repetición y Concatenación**

- **Repetición de Cadenas**: Usa el operador `*` para repetir cadenas.python
  
  `repetido = "Hola " * 3  # Salida: 'Hola Hola Hola '`

## 4. **Métodos de Formato**

- **`str.zfill(width)`**: Rellena la cadena con ceros a la izquierda hasta alcanzar el ancho especificado.python
  
  `numero = "42" resultado = numero.zfill(5)  # Salida: '00042'`

## 5. **Métodos de Búsqueda**

- **`str.count(substring)`**: Cuenta cuántas veces aparece una subcadena en la cadena.python
  
  `texto = "Hola mundo, mundo" conteo = texto.count("mundo")  # Salida: 2`

- **`str.index(substring)`**: Similar a `find()`, pero lanza un error si no se encuentra la subcadena.

## 6. **Métodos de Modificación**

- **`str.capitalize()`**: Convierte el primer carácter a mayúscula y el resto a minúsculas.
- **`str.swapcase()`**: Cambia mayúsculas por minúsculas y viceversa.

## Algoritmos Famosos Relacionados con Cadenas

Además de los métodos nativos, aquí hay algunos algoritmos famosos que pueden aplicarse a cadenas:

## 7. **Algoritmos Clásicos**

- **Método de la Burbuja (Bubble Sort)**: Aunque es un algoritmo de ordenamiento, se puede aplicar a listas de cadenas para organizarlas alfabéticamente.

python

`def bubble_sort(cadenas):     n = len(cadenas)    for i in range(n):        for j in range(0, n-i-1):            if cadenas[j] > cadenas[j+1]:                cadenas[j], cadenas[j+1] = cadenas[j+1], cadenas[j]    return cadenas lista = ["banana", "manzana", "pera"] print(bubble_sort(lista))  # Salida: ['banana', 'manzana', 'pera']`

- **Búsqueda Lineal**: Busca un elemento en una lista o cadena comparando cada elemento.

python

`def busqueda_lineal(cadena, objetivo):     for i in range(len(cadena)):        if cadena[i] == objetivo:            return i    return -1 texto = "Hola Mundo" print(busqueda_lineal(texto, "M"))  # Salida: 5`

# 
