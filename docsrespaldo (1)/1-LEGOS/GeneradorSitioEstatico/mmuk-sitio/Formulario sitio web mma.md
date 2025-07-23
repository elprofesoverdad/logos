<form action="https://formsubmit.co/gerente@mundomejor.uk" method="POST">**Formulario de Contacto para Mundo Mejor UK - MMA**

Utilizando la documentación de FormSubmit, hay que diseñar  un formulario de contacto para la empresa MMA que se integrará con la funcionalidad de FormSubmit para gestionar los envíos de datos, en tu base de conocimientos hay un " formulario para la web de mma", ese formulario en bootstrap tiene el diseño estético y responsive que la empresa exige, por tanto debe modificarse lo menos posible para agregarle la funcionalidad. A continuación, detallamos cómo se configurará el formulario y la funcionalidad asociada:

1. **Campos del Formulario:**
   
   - Nombre Completo:
   - Correo Electrónico (Cliente):
   - Teléfono:
   - Empresa:
   - Cargo y Ocupación:
   - Mensaje/Consulta:

2. **Configuración de FormSubmit:**
   
   - **_replyto:** El campo de correo electrónico de la empresa se utilizará como dirección de respuesta: gerente@mundomejor.uk
   - **_subject:** El asunto del correo  que recibe la empresa (mundomejorasesores.uk) se establecerá como "Inscripcion de Nombre Completo Cargo y Ocupación
   - **_autoresponse:** Se enviará una respuesta automática al correo del cliente  Correo Electrónico (Cliente)  con un mensaje de agradecimiento por la inscripción en Mundo Mejor Asesores UK, incluyendo el nombre del cliente capturado en el formulario.

3. **Funcionalidad con jQuery Library:**
   
   - Se implementará la funcionalidad de envío del formulario utilizando la biblioteca jQuery para realizar la solicitud AJAX a FormSubmit y enviar los datos del formulario de manera asíncrona.

4. **Dirección de Envío de Datos:**
   
   - Los datos del formulario se enviarán a la dirección de correo electrónico [gerente@mundomejor.uk](mailto:gerente@mundomejor.uk), donde se incluirán los detalles del cliente (correo, teléfono, empresa, cargo, ocupación) en el cuerpo del mensaje.

5. Hay que entender que el correo se enviará a:

```html
<form action="https://formsubmit.co/gerente@mundomejor.uk" method="POST">
```

Al completar y enviar el formulario, el dueño del negocio ([gerente@mundomejor.uk](mailto:gerente@mundomejor.uk)) recibirá una respuesta automática de agradecimiento por la inscripción en Mundo Mejor Asesores UK, personalizada con el nombre del cliente capturado en el formulario. Esta configuración garantiza una comunicación efectiva y personalizada con los clientes de la empresa MMA.
