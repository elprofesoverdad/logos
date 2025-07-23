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

### **Guía Definitiva para Productos Complejos en OpenCart 4.x**

Este manual te guiará para configurar correctamente un producto con múltiples atributos y precios, como tus "Gorras Nacionales", utilizando el sistema de **Variantes** de OpenCart.

#### **1. Conceptos Clave: La Diferencia entre Opciones y Variantes**

Para empezar, es crucial entender la diferencia entre el método antiguo (Opciones) y el nuevo (Variantes).

- **Opciones (El método antiguo):** Piensa en ellas como "modificadores" de un producto principal. Creas una opción "Color" y le añades "Rojo" (+0$), "Azul" (+0$), "Dorado" (+$2.00). El problema es que la gestión de inventario se vuelve torpe. Si vendes una gorra roja, descuenta del producto principal, pero no sabe cuántas rojas, azules o doradas te quedan de forma individual sin extensiones complejas.

- **Variantes (El método moderno y correcto para ti):** Piensa en esto como crear un "Producto Contenedor" (la gorra genérica) que agrupa a muchos "Sub-Productos" reales. Cada variante (ej: *Gorra Camuflada, Con Laureles, Color Verde*) es tratada por el sistema como un artículo único, con su propio:
  
  - **SKU** (Código de producto único)
  
  - **Inventario** (Stock)
  
  - **Precio**
  
  - **Imagen específica**
  
  - **Peso y dimensiones**

**Conclusión:** Para tu necesidad de controlar el stock de cada tipo de gorra de forma precisa, las **Variantes** son la solución ideal.

#### **2. Diagrama de la Estructura de tu Producto**

Antes de tocar OpenCart, visualicemos lo que vamos a construir. Cada línea final en este árbol será una **Variante** con su propio inventario.

```
Producto Padre: Gorras Nacionales AAA
│
├─── **Variante 1:** (Tipo: Camuflada/Unicolor, Laureles: Sin Laureles, Color: [el color que sea])
│    ├── SKU: GNC-SL-COLOR
│    ├── Stock: [Cantidad específica]
│    ├── Precio Detal: 18$
│    └── Precio Mayor: 15$
│
├─── **Variante 2:** (Tipo: Acolchada, Laureles: Sin Laureles, Color: [el color que sea])
│    ├── SKU: GNA-SL-COLOR
│    ├── Stock: [Cantidad específica]
│    ├── Precio Detal: 15$
│    └── Precio Mayor: 10$
│
├─── **Variante 3:** (Tipo: Camuflada/Unicolor, Laureles: Con Laureles, Color: [el color que sea])
│    ├── SKU: GNC-CL-COLOR
│    ├── Stock: [Cantidad específica]
│    ├── Precio Detal: 24$
│    └── Precio Mayor: 19$
│
├─── **Variante 4:** (Tipo: Acolchada, Laureles: Con Laureles, Color: [el color que sea])
│    ├── SKU: GNA-CL-COLOR
│    ├── Stock: [Cantidad específica]
│    ├── Precio Detal: 18$
│    └── Precio Mayor: 15$
│
└─── **Variante 5:** (Tipo: Acrílica, Laureles: Con Laureles, Color: [el color que sea])
     ├── SKU: GAA-CL-COLOR
     ├── Stock: [Cantidad específica]
     ├── Precio Detal: 10$
     └── Precio Mayor: 7$
```

#### **3. Paso a Paso: Configurando tus "Gorras Nacionales" en OpenCart**

##### **Paso 1: Crear las Opciones Necesarias**

Primero, debemos definir las características que distinguen a nuestras gorras. Estas serán las "opciones" que usaremos para generar las variantes.

1. Ve a `Catálogo > Opciones` en el menú de administración.

2. Crea las siguientes opciones, una por una:
   
   - **Nombre de la Opción:** `Tipo de Gorra Nacional`
     
     - **Tipo:** `Desplegable` o `Botón de Radio`
     
     - **Valores de la Opción (añádelos uno a uno):**
       
       - `Camuflada y Unicolor Nacional AAA`
       
       - `Acolchada Nacional`
       
       - `Acrílica con Laureles`
   
   - **Nombre de la Opción:** `Laureles`
     
     - **Tipo:** `Desplegable` o `Botón de Radio`
     
     - **Valores de la Opción:**
       
       - `Con Laureles`
       
       - `Sin Laureles`
   
   - **Nombre de la Opción:** `Color`
     
     - **Tipo:** `Desplegable` o `Muestra de Color`
     
     - **Valores de la Opción:**
       
       - `Rojo`
       
       - `Naranja`
       
       - `Amarillo`
       
       - *(...y así con todos los colores disponibles)*

##### **Paso 2: Crear el Producto "Padre" o "Contenedor"**

Este es el producto que el cliente verá en la categoría. No tendrá precio ni stock propio.

1. Ve a `Catálogo > Productos` y haz clic en `Añadir Nuevo` (+).

2. **Pestaña `General`:**
   
   - **Nombre del Producto:** `Gorras Nacionales AAA`
   
   - **Descripción:** Añade la descripción general de las gorras.
   
   - **Etiqueta Meta Título:** `Gorras Nacionales AAA`

3. **Pestaña `Datos`:**
   
   - **Modelo (SKU):** `GORRA-NAC-CONTENEDOR` (Un SKU genérico para el padre).
   
   - **Precio:** Déjalo en `0`.
   
   - **Cantidad:** Déjalo en `0`.
   
   - **Restar de Inventario:** `No`.

4. **Guarda el producto.** ¡Aún no hemos terminado! Vuelve a editarlo.

##### **Paso 3: Generar las Variantes**

Aquí es donde ocurre la magia.

1. Con el producto padre abierto, ve a la pestaña **`Variantes`**.

2. Verás una sección que dice "Añadir Variante". En lugar de hacerlo manualmente, usaremos el generador. Haz clic en el botón **`Generador de Variantes`**.

3. En la ventana emergente, añade las opciones que creaste en el Paso 1: `Tipo de Gorra Nacional`, `Laureles` y `Color`.

4. Haz clic en **`Generar`**. OpenCart creará automáticamente una fila por cada combinación posible de esas opciones.

##### **Paso 4: Configurar Cada Variante Individualmente**

Ahora verás una lista de todas las combinaciones. Debes configurar cada una.

1. **Filtra para trabajar más fácil.** Por ejemplo, si una combinación no existe (como "Acrílica SIN Laureles"), simplemente elimina esa fila.

2. Para cada fila (variante), rellena los campos:
   
   - **SKU:** **¡Esto es CRÍTICO!** Asigna un SKU único que puedas entender. Usa el esquema del diagrama: `GNC-CL-ROJO` (Gorra Nacional Camuflada, Con Laureles, Roja).
   
   - **Cantidad:** El stock **real y específico** de esa variante.
   
   - **Precio:** El precio **al detal** de esa variante específica (ej: `24.00` para la camuflada con laureles).
   
   - **Imagen:** Puedes hacer clic en la imagen y asignar una foto específica para esa variante (ej: la foto de la gorra roja con laureles).

##### **Paso 5: Configurar Precios al Mayor**

El precio que pusiste en el paso anterior es el de "Detal". Para el precio de "Mayor", usaremos los Grupos de Clientes.

1. Primero, asegúrate de tener un Grupo de Clientes para mayoristas. Ve a `Clientes > Grupos de Clientes` y crea uno llamado `Mayorista` si no existe.

2. Vuelve a la edición de tu producto, a la pestaña **`Variantes`**.

3. Para cada variante, haz clic en el botón de edición (lápiz) al final de la fila.

4. Se abrirá una ventana para editar esa variante. Ve a la pestaña **`Descuentos`** o **`Especiales`**.
   
   - **Método `Especiales` (más sencillo):**
     
     - Haz clic en `Añadir Especial`.
     
     - **Grupo de Clientes:** Selecciona `Mayorista`.
     
     - **Prioridad:** `1`.
     
     - **Precio:** Introduce el precio al mayor para esa variante (ej: `19.00`).
     
     - Guarda.

5. Repite este proceso para cada variante, asignando su precio de mayorista correspondiente.

#### **4. ¿Cómo se Descuenta el Inventario Ahora?**

Esta es la mejor parte de usar Variantes.

- Cuando un cliente entra a la página del producto "Gorras Nacionales AAA", verá menús desplegables para "Tipo", "Laureles" y "Color".

- Al seleccionar `Camuflada y Unicolor`, `Con Laureles` y `Rojo`, el sistema internamente apunta a la variante con el **SKU `GNC-CL-ROJO`**.

- Si compra una, OpenCart descuenta `1` unidad del inventario **de esa variante específica**.

- El stock de las gorras Acolchadas, o las Sin Laureles, o las de color Azul, **permanece intacto**.

Has logrado un control de inventario granular y preciso.

¡Y listo! Siguiendo estos pasos, habrás configurado tu producto de una manera robusta, profesional y escalable. El sistema se encargará de gestionar el inventario y los precios de forma automática y precisa para cada combinación que ofreces.

Ahora estás en una excelente posición para el siguiente paso. Cuando quieras, dime y prepararemos la lista de preguntas clave para hacerle a tu cliente sobre su proceso de manufactura e inventario, lo cual nos ayudará a refinar aún más esta estructura.
