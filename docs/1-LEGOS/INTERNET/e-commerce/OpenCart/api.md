

### ⚙️ Inclusión vía API REST de OpenCart (v4)

> Asegúrate de tener activo tu **token de API** en
> **Administración → Sistema → Usuarios → API**

1. **Crear “Viseras METT Tela Deportiva”**

   ```bash
   curl -X POST https://tu-dominio/admin/index.php?route=api/product/product/add \
     -H "Content-Type: application/json" \
     -H "X-Oc-Token: TU_TOKEN" \
     -d '{
       "product_description": {
         "1": { "name": "Viseras METT Tela Deportiva", "description": "" }
       },
       "model": "VIS-005-TD",
       "price": 4.00,
       "keyword": "viseras-mett-tela-deportiva",
       "product_category": [ { "category_id": ID_CATEGORIA_Viseras } ],
       "product_store": [0],
       "product_option": [
         {
           "product_option_id": ID_OPCION_COLOR,
           "product_option_value": [
             /* IDs de los valores de color */
           ],
           "required": true
         }
       ],
       "product_discount": [
         {
           "customer_group_id": ID_MAYORISTAS,
           "quantity": 6,
           "priority": 1,
           "price": 3.20,
           "date_start": "0000-00-00",
           "date_end": "0000-00-00"
         }
       ]
     }'
   ```

2. **Crear “Viseras METT Reflectiva/Completamente Reflectiva”**

   ```bash
   curl -X POST https://tu-dominio/admin/index.php?route=api/product/product/add \
     -H "Content-Type: application/json" \
     -H "X-Oc-Token: TU_TOKEN" \
     -d '{
       "product_description": {
         "1": { "name": "Viseras METT Reflectiva/Completamente Reflectiva", "description": "" }
       },
       "model": "VIS-005-RCR",
       "price": 5.00,
       "keyword": "viseras-mett-reflectiva-completamente-reflectiva",
       "product_category": [ { "category_id": ID_CATEGORIA_Viseras } ],
       "product_store": [0],
       "product_option": [
         {
           "product_option_id": ID_OPCION_COLOR,
           "product_option_value": [
             /* IDs de los valores de color */
           ],
           "required": true
         }
       ],
       "product_discount": [
         {
           "customer_group_id": ID_MAYORISTAS,
           "quantity": 6,
           "priority": 1,
           "price": 4.50,
           "date_start": "0000-00-00",
           "date_end": "0000-00-00"
         }
       ]
     }'
   ```

3. **Eliminar un producto**

   ```bash
   curl -X POST https://tu-dominio/admin/index.php?route=api/product/product/delete \
     -H "Content-Type: application/json" \
     -H "X-Oc-Token: TU_TOKEN" \
     -d '{"product_id": ID_DEL_PRODUCTO}'
   ```

> **Alternativa OCMOD**: podrías crear un XML que inserte o borre registros en `oc_product`, pero la vía API REST es más clara y reversible.

---

¿Te ayudo a ajustar estos scripts con tus IDs concretos o prefieres el OCMOD XML listo para subir?
