# Pantalla se baila se mueve sola cuando se mueve el raton

* La pantalla se mueve un poco en direccion opuesta al movimiento del raton:

## Solución:

Para resolver este problema, sigamos estos pasos:

1. **Verifica la configuración de resolución y escala**:
   
   - Abre el menú de configuración o preferencias de tu sistema.
   - Busca la sección de “Pantalla” o “Monitor”.
   - Asegúrate de que la resolución y la escala estén configuradas correctamente para tu monitor incorporado.

2. **Reinicia el servidor gráfico**:
   
   - Puedes hacer esto presionando **Ctrl + Alt + Backspace** o **Ctrl + Alt + F1** para acceder a una terminal virtual.
   
   - Inicia sesión con tu nombre de usuario y contraseña.
   
   - Ejecuta el siguiente comando para reiniciar el servidor gráfico:
     
     ```bash
     ReiniciarServidorGrafico
     ```
* Si no funciona:
  
  ```bash
  sudo systemctl restart lightdm
  ```
  
  - Luego, regresa a la interfaz gráfica presionando **Ctrl + Alt + F7**.
