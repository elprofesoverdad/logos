# ACTUALIZACIÓN 3 abril 2023

## sqlite

* Para **instalar sqlite** se descarga sqlitestdio en $plugins y listo, el PATH ya está exportado en .bash.rc, viene **en español** y con con **soporte de claves foráneas**.

* para instalar sqlite con soporte de claves foráneas pero original, aústero; se descarga u compila como está en su manual (ver bibioteca legos).



# ACTUALIZACION 19 -mar 2023 /////////////////// NOTA EN EL DESASTRE

instale ubuntu server del pendrive negro has que quitar el concentrador usb
luego instale xubuntu-desktop
configuracion -idioma -instalar idioma espanol
y despues correr el script desastre

/////////////////////////////////////////////



# INSTALACION SISTEMA

LA INSTALACIÓN ES AUTOMÁTICA EL PROGRAMA A EJECUTAR
ES MUDANZA NO INSTALAR BÁSICO.

Para la instalación se utilizó un pendrive con ubuntu 18.04 focal Lts net install


y se instaló un escritorio xubuntu-desktop con servideor open-ssh en la instalación
se muestra cuando se ejecuta tasksel.

No se instaló nada mas

se entra en la sesión de ubuntu...

Debe ejecutar el script actualización y cuando ya esté en Ubuntu Jammy
instalar las aplicaciones y mudar las configuraciones con el script
mudanza.

-------------------
# ACTUALIZACIÓN

Ya dentro de la sesión:
se ejecuta el script de actualizacion como hay que reiniciar el script llega hasta cierto nivel
el resto se debe hace a mano:
LA INSTALACIÓN ES AUTOMÁTICA EL PROGRAMA A EJECUTAR
ES MUDANZA NO INSTALAR BÁSICO

 
HERRAMIENTAS:
apt update
apt -y dist-upgrade
do-release-upgrade -d
# si no funciona probar con /usr/lib/ubuntu-release-upgrader/check-new-release-gtk
apt install update-manager
# Reiniciar y volver a actualizar hasta llegar a Jammy


# MUDANZA

antes de la mudanza debes montar el disco externo fuente
de los programas con el script de programas basicos

LA INSTALACIÓN ES AUTOMÁTICA EL PROGRAMA A EJECUTAR
ES MUDANZA NO INSTALAR BÁSICO

pero el listado de programas es editable desde una función

**micro y kitty**  instala con el script Mudanza, kitty se puede renovar si se hace otra instalacion con:
	curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin y listo porque el binario ya se agregó a $PATH en bashc.bashrc de forma predeterminada solo se muda. Si se hace la instalación debe volverse a revisar kitty.conf

el script copia la config de micro automaticamente
no hace falta configurar kitty porque en bash.bashrc está la variable  KITTY_CONFIG_DIRECTORY que apunta a $conf/kitty.conf

> broot hay que instalarlo manual:
Instalación de broot:
hay que ser el usuario normal sin sudo
para instalar broot primero ir a $plugins/broot y ejecutar ./broot todo eso sin sudo
pedirá la instalación para el perfil del usuario normal,, aceptar.

SI YA FUNCIONEA EN ROOT NO HACER PASO SIGUIENTE: 	
luego hacer root, con sudo y teclear broot, entrada y pedirá la instalación de br
NOTA: por ahora dejamos la configuración original y dejamos a mudanza copiar .config/broot/select.toml  NO COPIAR LA CARPETA COMPLETA BROOT. tener en cuenta la seguridad de root al copiar la configuración
aceptar y voalá.

* **Instalar WEKAN (kaban)**

sudo snap install wekan
sudo snap set wekan port='3001'
sudo systemctl restart snap.wekan.mongodb
sudo systemctl restart snap.wekan.wekan

sudo snap install wekan-gantt-gpl

kaban-restaurar

kaban-off
kaban-on

y ver porque aún no está claro...










