# Problema de las opciones y descuentos en productos opencart

en el siguiente producto de mett gorras

``` json
{
      "id": "METT-005",
      "sku": "VIS-005",
      "nombre": "Viseras METT",
      "url_producto": "https://mettgorras.com/viseras-mett/",
      "categoria": ["Viseras"],
      "imagenes": ["imagen_1.jpg"],
      "atributos": {
        "Variante": ["Tela Deportiva", "Reflectiva", "Completamente Reflectiva"],
        "Colores": [
          "Rojo 🔴",
          "Naranja 🟠",
          "Amarillo 🟡",
          "Verde 🟢",
          "Azul 🔵",
          "Morado 🟣",
          "Marrón 🟤",
          "Negro ⚫️",
          "Blanco ⚪️"
        ]
      },
      "precios": {
        "Detalle": {
          "Tela Deportiva": 4.0,
          "Reflectiva": 5.0,
          "Completamente Reflectiva": 5.0
        },
        "Mayor": {
          "Tela Deportiva": 3.2,
          "Reflectiva": 4.5,
          "Completamente Reflectiva": 4.5
        }
      }
    },
```




**Inconsistencia detectada:** al usar un solo producto “Viseras METT” con las opciones “Tela Deportiva” (4 \$ → 3,20 \$ = 20 % off) y “Reflectiva”/“Completamente Reflectiva” (5 \$ → 4,50 \$ = 10 % off), los descuentos por mayor (≥ 6 u.) no podían expresarse con un único porcentaje, pues cada opción tenía un % distinto, algo que OpenCart nativo no soporta en la pestaña “Descuentos” (solo un descuento global por producto).

---

### 🌲 Estructura “tree” propuesta (2 productos en lugar de 3)

```bash
/catalog
└── Productos
    ├── Viseras METT Tela Deportiva
    │   ├── Datos Generales
    │   │   ├── Nombre: Viseras METT Tela Deportiva
    │   │   ├── SKU: VIS-005-TD
    │   │   ├── Precio Detalle: $4.00
    │   │   └── URL SEO: viseras-mett-tela-deportiva
    │   │
    │   ├── Categoría
    │   │   └── Viseras
    │   │
    │   ├── Imágenes
    │   │   └── imagen_1.jpg
    │   │
    │   ├── Opciones
    │   │   └── Color
    │   │       ├── Rojo 🔴
    │   │       ├── Naranja 🟠
    │   │       └── …  
    │   │
    │   └── Descuento Mayoristas (≥ 6 uds)
    │       └── 20 % → $3.20
    │
    └── Viseras METT Reflectiva/Completamente Reflectiva
        ├── Datos Generales
        │   ├── Nombre: Viseras METT Reflectiva/Completamente Reflectiva
        │   ├── SKU: VIS-005-RCR
        │   ├── Precio Detalle: $5.00
        │   └── URL SEO: viseras-mett-reflectiva-completamente-reflectiva
        │
        ├── Categoría
        │   └── Viseras
        │
        ├── Imágenes
        │   └── imagen_1.jpg
        │
        ├── Opciones
        │   └── Color
        │       ├── Rojo 🔴
        │       ├── Naranja 🟠
        │       └── …  
        │
        └── Descuento Mayoristas (≥ 6 uds)
            └── 10 % → $4.50
```

---

