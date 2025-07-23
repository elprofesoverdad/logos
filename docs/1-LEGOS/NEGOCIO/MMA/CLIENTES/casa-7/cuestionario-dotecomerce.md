---
hide_nav: true
hide:
  - navigation
  - header
  - toc
  # - tabs
  # - footer
classes: landing-page
---

# Cuestionario Estratégico para Cliente: Inventario en DotEcommerce

**Objetivo:** Recopilar toda la información necesaria para estructurar el catálogo de productos en Mett Gorras.

## Sección A: Entendiendo el Inventario y el Proceso Físico

!!! abstract "Resumen de la Sección"

Estas son las preguntas más importantes de toda la entrevista. Las respuestas aquí definen toda la estructura de la tienda y cómo se controlará el inventario para que refleje 100% la realidad de su almacén.

### 1. Sobre el Producto Base: ¿El producto nace o se hace?

Cuando reciben o fabrican las gorras, ¿vienen ya con todas sus características finales (por ejemplo, con los laureles ya bordados)?

O, por el contrario, ¿tienen un stock de gorras "base" y los laureles (o cualquier otra personalización) se añaden solo cuando un cliente las pide?

Si se añaden después, ¿ese proceso tiene un costo adicional fijo? ¿Afecta el tiempo de entrega?

!!! success "El porqué de esta pregunta: La Clave del Control Total"

Necesitamos saber esto porque define toda la estrategia de inventario.


* **Opción 1: El producto ya está terminado.** Si una gorra "con laureles" ya existe en una caja en el almacén, lista para ser enviada, entonces para el sistema es un **producto único y distinto**. Debe tener su propio código (SKU) y su propio conteo de stock. Esta es la forma **más simple y precisa** de gestionar el inventario.

* **Opción 2: El producto se personaliza al momento.** Si tienen un lote de gorras "base" y le bordan los laureles solo cuando alguien las compra, el escenario es más complejo. Aquí no vendemos un producto, sino un **producto + un servicio** (el bordado). Esto implica que el sistema debe descontar una gorra "base" del inventario y, además, sumar el costo del servicio.

Para un control de stock **exacto y sin errores**, la **Opción 1 es siempre la ideal**. Nuestro objetivo es que **DotEcommerce** refleje la realidad de su almacén al 100%.


### 2. Control de Stock Actual: ¿Cómo contamos hoy?

Actualmente, ¿cómo saben cuántas gorras "Camufladas, Sin Laureles, Color Verde" les quedan? ¿Usan una hoja de cálculo, un sistema manual, o lo estiman?

¿Han tenido el problema de vender un producto que ya no tenían en stock?

!!! warning "El porqué de esta pregunta: Evitar la Fuga de Clientes y Dinero"

Entender su método actual nos ayuda a identificar los puntos débiles que vamos a solucionar.


* Vender un producto que **no tienen en stock** es una de las peores experiencias para un cliente. Genera desconfianza, cancelaciones, reembolsos y mala reputación.
* Un sistema manual o basado en estimaciones es propenso a **errores humanos** que cuestan dinero y tiempo.
* Al saber cómo lo hacen ahora, podemos configurar **DotEcommerce** para que sea la **fuente única y confiable de la verdad** sobre su inventario. El objetivo es que nunca más tengan que dudar si pueden o no vender un artículo.


## Sección B: Definiendo las Características del Producto

!!! abstract "Resumen de la Sección"

Aquí listaremos todos los atributos que un cliente puede elegir y que crean una versión diferente de un producto.

### 3. Identificación de Atributos Clave: ¿Qué hace a un producto diferente de otro?

Para un producto como "Gorras Nacionales", vamos a listar todas las características que un cliente puede elegir. Ya identificamos:

- Tipo (Camuflada/Unicolor, Acolchada, Acrílica)

- Laureles (Con o Sin)

- Color

¿Existe alguna otra característica que diferencie a estas gorras y que un cliente pueda elegir? (ej. Tipo de cierre, material específico, etc.).

### 4. Combinaciones y Restricciones: ¿Todo se puede mezclar con todo?

¿Todas las combinaciones son posibles? Por ejemplo, ¿existen "Gorras Acrílicas SIN Laureles"?

¿Existen "Gorras Acolchadas" que sean también "Camufladas"?

!!! info "El porqué de esta pregunta: Ahorrar Tiempo y Evitar Confusiones"

Saber qué combinaciones NO existen nos permite eliminarlas desde el principio. Así, evitamos crear productos "fantasma" en el sistema y nos aseguramos de que el cliente solo pueda seleccionar combinaciones que realmente están a la venta.

## Sección C: Estrategia de Precios

!!! abstract "Resumen de la Sección"

Aquí definimos cómo se asignan los precios a cada variante y a cada tipo de cliente.

### 5. Precios por Variante: ¿Cada versión vale lo mismo?

Confirmemos este principio: el precio de una "Acolchada con Laureles" (18$) es diferente al de una "Acolchada sin Laureles" (15$). ¿Este modelo de precios distintos por cada característica se aplica a todos los productos?

¿El color afecta el precio alguna vez? (ej. ¿Una gorra dorada cuesta más que una negra?).

### 6. Grupos de Clientes: ¿Quién paga qué?

Hablemos del precio al por mayor. ¿Quién califica para este precio?

- ¿Es a partir de una cierta cantidad de productos en el carrito?

- ¿O son clientes específicos que deben ser registrados en un grupo especial?

- ¿Existen otros grupos de precios? (ej. "Distribuidores", "VIP", etc.).

!!! info "El porqué de esta pregunta: Automatizar los Descuentos Correctos"

DotEcommerce puede mostrar precios diferentes a cada tipo de cliente automáticamente. Necesitamos saber las reglas de su negocio para programar que, por ejemplo, un cliente "Mayorista" vea los precios al mayor en toda la tienda sin necesidad de cupones ni cálculos manuales.

## Sección D: Logística y Presentación Visual

!!! abstract "Resumen de la Sección"

Detalles finales sobre cómo se comportará y se verá el producto en la tienda online.

### 7. Gestión de Stock Cero: ¿Qué pasa cuando se acaba un producto?

Cuando una variante específica se agota (ej. no quedan más "Gorras Rojas con Laureles"), ¿qué prefieren que suceda en la tienda?

a) Que la opción "Rojo" desaparezca del selector.

b) Que la opción "Rojo" aparezca pero no se pueda seleccionar (con un mensaje "Agotado").

c) Que se pueda comprar pero con un aviso de que tardará más en entregarse (venta bajo pedido o backorder).

### 8. Imágenes del Producto: Una imagen para cada realidad

¿Tienen una fotografía para cada variante única? Es decir, ¿una foto específica para la gorra roja con laureles, otra para la azul con laureles, etc.?

Si no, ¿están de acuerdo en usar una imagen genérica para el tipo (ej. una foto para todas las "Acolchadas con Laureles") y que solo cambie el selector de color?

!!! tip "El porqué de esta pregunta: Vender con los Ojos"

La mejor experiencia para el cliente es ver exactamente lo que está comprando. DotEcommerce permite que al seleccionar "Rojo" y "Con Laureles", la imagen del producto cambie a la foto de la gorra roja con laureles. Tener estas imágenes listas mejora la confianza y aumenta las ventas.

## Próximos Pasos: La Hoja de Ruta

!!! quote "El Resultado Final"

El objetivo de esta reunión es que juntos podamos llenar una hoja de cálculo (Excel o Google Sheets) que será el "plano" de su inventario. Cada fila será un producto único y real en su almacén.


**Ejemplo de la Hoja de Ruta a construir:**

| Nombre Base     | SKU           | Tipo       | Laureles      | Color | Stock | Precio Detal | Precio Mayor |
| --------------- | ------------- | ---------- | ------------- | ----- | ----- | ------------ | ------------ |
| Gorra Nacional  | GNC-SL-VER    | Camuflada  | Sin Laureles  | Verde | 50    | 18.00        | 15.00        |
| Gorra Nacional  | GNA-CL-ROJ    | Acolchada  | Con Laureles  | Rojo  | 35    | 18.00        | 15.00        |
| Gorra Nacional  | GAA-CL-AZU    | Acrílica   | Con Laureles  | Azul  | 20    | 10.00        | 7.00         |

Con esta información, la configuración en DotEcommerce será un reflejo perfecto y funcional de su negocio.

