#Python decoradores

Un decorador estaremos trabajando, con por lo menos, 3 funciones. El input, el output y la función principal. Para que nos quede más en claro a mi me gusta nombrar a las funciones como: a, b y c.

Donde a recibe como parámetro b para dar como salida a c. Esta es una pequeña "formula" la cual me gusta mucho mencionar. 💻

> a(b) -> c

Veamos un ejemplo de como crear un decorador en Python.

``` python

def funcion_a(funcion_b):
    def funcion_c():
        print('Antes de la ejecución de la función a decorar')
        funcion_b()
        print('Después de la ejecución de la función a decorar')

    return funcion_c

```

Ahora, ¿Qué pasa si nuestra función a decorar debe recibir argumentos y a su vez debe retornar algún valor? en estos casos haremos uso de los parámetros args y kwargs.

``` python

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = funcion_b(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')    

        return result

    return funcion_c

@funcion_a
def suma(a, b):
    return a + b
```
``` python
Algo que me gustaría mencionar, es que por convención, no es una regla, la función anidada del decorador tendrá por nombre: wrapper, de igual forma, el nombre del decorador debe ser muy descriptivo. En términos simples, el decorador pudiera quedar de la siguiente manera.

def my_custome_decorator(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```


 ¿Es posible pasar argumentos extras a los decoradores? 🧐La respuesta es sí. 😉

 ``` python
 def my_decorator_name(name):
    def my_custome_decorator(function):
        def wrapper(*args, **kwargs):

            print('Name:', name)
            return function(*args, **kwargs)

        return wrapper

    return my_custome_decorator

@my_decorator_name('CodigoFácilito')
def suma(a, b):
    return a + b
```