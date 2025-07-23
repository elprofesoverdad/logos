# Diagnóstico y Solución de Problemas con el Cambio de Teclado en Kubuntu Plasma

## Introducción al Problema

El problema que describes es común en entornos KDE Plasma: aunque seleccionas correctamente el cambio de idioma del teclado (entre inglés y español) y ves la notificación emergente confirmando el cambio, el teclado sigue comportándose con la distribución anterior[1][2]. Este tipo de problemas puede deberse a conflictos entre diferentes métodos de configuración del teclado, problemas con IBus, o configuraciones incorrectas en el sistema[3][4].

## Métodos de Diagnóstico por Consola

### 1. Verificar la Configuración Actual del Teclado

Para diagnosticar el problema, primero necesitamos verificar qué configuración de teclado está actualmente activa en el sistema:

```bash
setxkbmap -query
```

Este comando mostrará la distribución de teclado activa, incluyendo el modelo y la distribución (layout)[4][5]. Si ves que la distribución no coincide con la que intentas usar, hay un problema en la aplicación de la configuración[6].

### 2. Monitorear Eventos del Teclado

Para ver si el sistema está detectando correctamente los cambios de distribución:

```bash
xev | awk -F'[ )]+' '/^KeyPress/ { a[NR+2] } NR in a { printf "%-3s %s\n", $5, $8 }'
```

Este comando abrirá una pequeña ventana. Al presionar teclas, mostrará los códigos de tecla y símbolos asociados, lo que te permitirá verificar si el sistema está interpretando correctamente las pulsaciones de teclas[7][8].

### 3. Monitorear Eventos de D-Bus

Los cambios de configuración del teclado generan eventos en el sistema D-Bus. Puedes monitorearlos con:

```bash
dbus-monitor --session "type='signal',interface='org.kde.keyboard'"
```

Este comando te mostrará los eventos relacionados con cambios en la configuración del teclado, lo que puede ayudar a identificar si las señales de cambio se están enviando correctamente[9].

### 4. Verificar Archivos de Configuración

Examina el archivo de configuración de teclado de KDE:

```bash
cat ~/.config/kxkbrc
```

Este archivo contiene la configuración de distribuciones de teclado. Verifica que las distribuciones que deseas usar estén correctamente listadas en la línea `LayoutList`[10].

## Soluciones por Consola

### 1. Forzar el Cambio de Distribución de Teclado

La forma más directa de cambiar la distribución del teclado por consola es:

```bash
setxkbmap es
```

Para cambiar a español, o:

```bash
setxkbmap us
```

Para cambiar a inglés[6][5]. Estos comandos aplican el cambio inmediatamente sin necesidad de reiniciar el sistema[11].

### 2. Configurar Múltiples Distribuciones con Atajo

Para configurar múltiples distribuciones con un atajo de teclado:

```bash
setxkbmap -layout "us,es" -option "grp:alt_shift_toggle"
```

Este comando configura dos distribuciones (inglés y español) y permite alternar entre ellas usando Alt+Shift[5]. Puedes personalizar el atajo cambiando la opción después de "grp:"[4].

### 3. Solución para Problemas con IBus

Si el problema está relacionado con IBus (común en Plasma Wayland), prueba:

```bash
im-config -n ibus
ibus-daemon -drx
```

El primer comando configura IBus como método de entrada predeterminado, y el segundo reinicia el daemon de IBus[12][13]. Si recibes notificaciones de error de IBus sobre variables de entorno, puedes desactivarlas temporalmente:

```bash
env -u QT_IM_MODULE -u GTK_IM_MODULE ibus-daemon -drx
```

Esto inicia IBus sin las variables de entorno que podrían estar causando conflictos[14].

### 4. Solución Permanente a Nivel de Sistema

Para una solución más permanente, puedes usar `localectl`:

```bash
sudo localectl set-x11-keymap es,us pc105 "" grp:alt_shift_toggle
```

Este comando configura las distribuciones de teclado a nivel de sistema, lo que debería aplicarse tanto en la consola como en el entorno gráfico[15][16].

### 5. Verificar y Reparar Permisos

A veces, los problemas de teclado pueden estar relacionados con permisos incorrectos:

```bash
sudo chown -R $USER:$USER ~/.config/ibus
sudo chown -R $USER:$USER ~/.config/dconf
```

Estos comandos corrigen los permisos de los directorios de configuración que podrían estar impidiendo que los cambios se apliquen correctamente[17].

## Diagnóstico Avanzado

Si las soluciones anteriores no funcionan, puedes realizar un diagnóstico más profundo:

```bash
gsettings get org.gnome.desktop.input-sources sources
```

Este comando muestra las fuentes de entrada configuradas en el sistema[18]. En KDE, también puedes verificar:

```bash
kwriteconfig5 --file kxkbrc --group Layout --key LayoutList
```

Para ver la configuración actual almacenada en el archivo de configuración de KDE[19].

## Conclusión

Los problemas con el cambio de distribución de teclado en Kubuntu Plasma suelen estar relacionados con conflictos entre diferentes sistemas de configuración o problemas con IBus, especialmente en sesiones Wayland[12][13]. Las soluciones proporcionadas deberían ayudarte a diagnosticar y resolver el problema desde la consola. Si ninguna de estas soluciones funciona, considera reiniciar el servicio de teclado o, en casos extremos, reiniciar la sesión de Plasma después de aplicar los cambios[3][20].

[1] https://www.librebyte.net/escritorios/cambiar-la-configuracion-de-mi-teclado-en-kde/
[2] https://espaciotecnologico.co/cambiar-idioma-de-teclado-en-kubuntu/
[3] https://www.laboratoriolinux.es/index.php/-noticias-mundo-linux-/software/23300-como-cambiar-el-idioma-del-teclado-en-los-distintos-escritorios-de-gnu-linux.html
[4] https://voragine.net/linux/setxkbmap-consultar-cambiar-distribucion-teclado-idioma
[5] https://travesuras.wordpress.com/2012/12/19/20121219-1/
[6] https://andalinux.wordpress.com/2008/08/08/configurar-teclado-ubuntu-correctamente-en-castellano/
[7] https://www.youtube.com/watch?v=FL9Z-Rmmks8
[8] https://www.youtube.com/watch?v=l5LJ9tO7G74
[9] https://superuser.com/questions/46841/swap-keyboard-layouts-automatically-in-ubuntu
[10] https://bbs.archlinux.org/viewtopic.php?id=284058
[11] https://www.sysadmit.com/2017/12/linux-configurar-teclado-espanol.html
[12] https://www.kubuntuforums.net/forum/currently-supported-releases/kubuntu-25-04-plucky-puffin/686468-notificaci%C3%B3n-persistente-de-ibus-sobre-%60qt_im_module%60-%60gtk_im_module%60-kubuntu-25-04-plasma-6-wayland
[13] https://discuss.kde.org/t/ibus-issue-with-wayland/3680
[14] https://github.com/ibus/ibus/issues/2644
[15] https://wiki.archlinux.org/title/Linux_console_(Espa%C3%B1ol)/Keyboard_configuration_(Espa%C3%B1ol)
[16] https://docs.redhat.com/es/documentation/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/configuring-the-keyboard-layout_changing-basic-environment-settings
[17] https://github.com/IV-GII/GII-2013/issues/91
[18] https://linux.codidact.com/posts/289105
[19] https://stackoverflow.com/questions/7021111/kde-how-do-i-find-and-switch-current-global-keyboard-layout-from-cli
[20] https://www.dzteck.com/es/change-keyboard-layout-linux/
[21] https://www.youtube.com/watch?v=NlIPuAeSXrY
[22] https://www.youtube.com/watch?v=F9DF77SUp_M
[23] https://es.ifixit.com/Gu%C3%ADa/C%C3%B3mo+cambiar+la+distribuci%C3%B3n+del+teclado+usando+un+terminal+Kali+Linux/150168
[24] https://forum.kde.org/viewtopic.php%3Ff=252&t=139714.html
[25] https://www.galisteocantero.com/aprendiendo-a-usar-el-comando-localectl-en-centos/
[26] https://www.linux.org/threads/disable-kde-virtual-keyboard.48113/
[27] https://github.com/ibus/ibus/issues/2684
[28] https://forum.manjaro.org/t/no-me-funciona-el-teclado-ni-el-touchpad-desde-la-ultima-actualizacion-estable/6217
[29] https://askubuntu.com/questions/631997/subscribe-for-dbus-event-of-screen-power-off
[30] https://www.reddit.com/r/kde/comments/17qp52i/how_can_i_change_keyboard_layout_language/?tl=es-419
[31] https://www.reddit.com/r/Kubuntu/comments/11rcdkn/kubuntu_2204_lts_kde_stops_responding_to_keyboard/?tl=es-419
[32] https://www.reddit.com/r/vmware/comments/yqaszn/keyboard_issue_with_ubuntu_2204_installer/?tl=es
[33] https://www.reddit.com/r/archlinux/comments/1ffkhze/localectl_keyboard_layout_help/?tl=es-es
[34] https://www.reddit.com/r/archlinux/comments/1ffkhze/localectl_keyboard_layout_help/?tl=es-419
[35] https://www.reddit.com/r/archlinux/comments/p6nfce/next_input_method_ibus_hotkey_does_not_work/?tl=es-419
[36] https://www.reddit.com/r/kde/comments/1hqtpnc/how_to_use_ibusm17n_amharic_keyboard_on_kde/?tl=es-419
