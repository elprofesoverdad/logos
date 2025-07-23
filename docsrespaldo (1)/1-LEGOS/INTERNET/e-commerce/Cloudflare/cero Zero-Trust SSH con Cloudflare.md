Pasos para crear un túnel de Cloudflare
Antes de continuar, debe tener un nombre de dominio conectado a su cuenta de Cloudflare. En esta guía, usaremos runcloudsandbox.com. 

Navegue a Cloudflare Zero Trust:  inicie sesión en su cuenta de Cloudflare y vaya al panel de Zero Trust.
Crear un nuevo túnel:  dentro del panel de Zero Trust, busque y haga clic en “ Red  > Túneles ”, luego seleccione “ Agregar un túnel ”.

Seleccionar el tipo de túnel: Seleccione el método “ Cloudflared ” y haga clic en “ Siguiente ”.

Nombre su túnel:  proporcione un nombre descriptivo para su túnel (por ejemplo, “MyHomeServerTunnel”).

Instalar el conector de túnel: Después de proporcionar el nombre, debe instalar el binario de Cloudflare en su servidor para establecer una conexión de túnel. Puede hacerlo fácilmente iniciando sesión en su servidor mediante SSH y ejecutando el comando en pantalla.

Si cloudflared ya esta instalado hacer

cloudflared service uninstall

y luego instalar los conectores y el servicio es lo mismo

sudo cloudflared service install eyJhIjoiYzA2YzNhMzNiNDUwZDI2ODA5OTRkNzRhYmJjYzYyMDMiLCJ0IjoiMDE2ZjQyYzUtYmRlNi00MjIwLWI5YWQtNmMxMjg3ZDE3MzgxIiwicyI6IlpHWXhaR1l5WkRBdFpUQXhPQzAwTURWakxXSXhZV010TXpBeE9HRXhNek0zWmprMCJ9

la clave o hash te lo da la pag en este paso:


![alt text](image.png)

Verificar la conexión del túnel: Tras ejecutar el comando en su servidor, regrese al panel de Cloudflare Zero Trust. El túnel recién creado debería aparecer en la parte inferior de la pantalla (como se muestra en la captura de pantalla anterior) y su estado debería ser " Conectado ".

Configuración de SSH de confianza cero con Cloudflare
Una vez que haya establecido con éxito un túnel de Cloudflare, podrá acceder de forma segura a su servidor a través de SSH mediante la sólida red de Cloudflare.

Esta sección proporcionará instrucciones paso a paso sobre cómo habilitar el acceso SSH de confianza cero a su servidor  a través de un navegador web utilizando Cloudflare Tunnel y Cloudflare Zero Trust.

Paso 1: Agregar un nuevo nombre de host público en Cloudflare Zero Trust
Inicie sesión en su panel de Cloudflare y navegue a la sección Confianza Cero.
Vaya a “ Túneles ” y seleccione el túnel que desee para esta configuración.
Dentro de la configuración del túnel, vaya a “ Nombre de host público  ” y haga clic en “ Agregar un nuevo nombre de host público ”.

en mi caso

ssh.mundomejor.uk

![alt text](image-1.png)

A continuación, debe ingresar el subdominio que desee. Puede ser el que prefiera. Por ejemplo, puede usar algo tan simple como "ssh" o algo más complejo como "ssh-for-test-server". Después, debe seleccionar su nombre de dominio en el menú desplegable.
En “ Tipo ”, seleccione “ SSH ” en el menú desplegable.
En el campo “ URL ”, ingrese la dirección IP de su servidor y guarde los cambios.


![alt text](image-2.png)


Paso 2: Crear una política de acceso para SSH
Mientras aún esté en Cloudflare Zero Trust, navegue a la pestaña “ Acceso ” y haga clic en “ Agregar una aplicación ”.

![alt text](image-3.png)

Seleccione “ Autohospedado ” y proporcione un nombre para su aplicación (por ejemplo, “SSH”).
En el campo “ Dominio de la aplicación  ”, ingrese el subdominio y el nombre de dominio que configuró en el paso anterior (por ejemplo, “ssh.example.com”).


![alt text](image-4.png)

Agregar una aplicación a Cloudflare Zero Trust SSH
A continuación, desplácese hacia abajo hasta la pestaña " Metodos de inicio de sesion ". Cloudflare admite varios proveedores de identidad , y esta sección le permite elegir su método de autenticación preferido si lo ha configurado en su panel de Zero Trust. En este tutorial, usaremos el " PIN de un solo uso ", el método de autenticación más sencillo.

![alt text](image-5.png)


En la parte inferior de la página, haga clic en “ Siguiente ” y defina un nombre de política (por ejemplo, “SSH”).
Aquí puede configurar la duración de la sesión. Esto especifica la validez de la autenticación. Si no está seguro, puede dejar el valor predeterminado.

![alt text](image-6.png)

A continuación, debe especificar qué usuarios tendrán acceso a este túnel SSH. Puede desplazarse hasta la sección " Configurar reglas"  para incluir o excluir usuarios. En el siguiente ejemplo, hemos creado tres reglas:
Nuestra primera regla otorga acceso a dos personas, a saber john@example.com ybrian@test.com
Nuestra segunda regla permite el acceso a cualquier persona que utilice una dirección de correo electrónico que termine en@runcloudsandbox.com
Nuestra tercera regla bloquea el acceso al servidor a visitantes de países específicos (Federación Rusa y China).

Después de configurar las reglas, desplácese hasta la parte inferior y haga clic en " Siguiente ". Esto le llevará a la página de configuración.
En esta pantalla, desplácese hasta el final y, en “ Representación del navegador ”, seleccione la opción “ SSH ” para permitir el acceso SSH a través del navegador web.

Por último, haga clic en Agregar la aplicación  para completar la configuración.
Paso 3: Autenticación y acceso
Abra una nueva ventana del navegador o una ventana de incógnito para asegurarse de haber cerrado la sesión de Cloudflare.
En la barra de direcciones, escribe el nombre de dominio que configuraste para el acceso SSH (p. ej., "ssh.example.com"). Serás redirigido a la página de autenticación de Cloudflare.
Inicie sesión con el método que haya designado en esta página, que puede incluir una contraseña, una clave de hardware o cualquier otro factor de autenticación configurado. En este ejemplo, hemos configurado una contraseña de un solo uso, por lo que ingresaremos la dirección de correo electrónico configurada en el paso anterior y proporcionaremos la contraseña de un solo uso (OTP) recibida en dicha dirección.

Tras la autenticación exitosa, será dirigido a la interfaz SSH en su navegador web, donde podrá iniciar sesión en su servidor.

Fuente https://runcloud.io/blog/zero-trust-ssh

OTRA FORmA EN https://www.linkedin.com/pulse/setup-cloudflare-zero-trust-network-connect-ssh-server-hussin/
