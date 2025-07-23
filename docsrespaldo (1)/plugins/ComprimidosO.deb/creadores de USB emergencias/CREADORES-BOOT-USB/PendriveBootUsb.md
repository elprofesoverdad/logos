#Creadores de Boot Usb.

## USAR VENTOY..!


##El de ubuntu Startup Disk Creator

Instalar y correr
sudo apt install -y usb-creator-gtk
usb-creator-gtk

## Con dd
Usar el comando dd con un programa con entorno gráfico: Gdiskdump (ver al final)

lsblk
sudo umount /dev/sdx1
apt install -y pv

sudo dd if=~/Descargas/ubuntu-17.10.1-desktop-amd64.iso | pv | sudo dd of=/dev/sdb bs=4M conv=fdatasync && zenity --info --text="¡Grabación finalizada!"

### Sobre discos duros y particiones

#### Sobre discos duros y particiones
* Con esto clonaríamos el disco hda en hdb. (discos IDE):

sudo dd if=/dev/hda |pv|dd of=/dev/hdb bs=1M

* Con esto clonaríamos el disco sda en sdb. (discos SATA):

sudo dd if=/dev/sda |pv|dd of=/dev/sdb bs=1M


* Grabar solo la primera partición (hda1) del disco de origen en el disco (hdb) de destino:

sudo dd if=/dev/hda1 |pv|dd of=/dev/hdb bs=1M

* Grabar el disco completo (hda) en la primera partición (hdb1) del disco de destino:

sudo dd if=/dev/hda |pv|dd of=/dev/hdb1 bs=1M

* Crear una imagen – puede ser bin o iso – del disco duro (hda) , en el directorio /home:

sudo dd if=/dev/hda |pv|dd of=/home/hda.bin

* Borrar totalmente la información de un disco: para ello, llena el disco con caracteres aleatorios, cinco veces. No va a quedar ni rastro de información en el disco:

for n in {1..5}; do dd if=/dev/urandom |pv|dd of=/dev/hda bs=8b conv=notrunc;


* Borrar cualquier partición y disco completo de cualquier dispositivo:

sudo dd if=/dev/zero |pv|dd of=/dev/sdx (Borrado de disco completo)

sudo dd if=/dev/zero |pv|dd of=/dev/sdxa (Borrado de partición de disco)

C) Sobre MBR y VBS:
= Copiar/Restaurar el Master Boot Record (MBR):

Para copiar el MBR:

sudo dd if=/dev/hda |pv|dd of=mbr count=1 bs=512

Para restaurar el MBR:

sudo dd if=mbr |pv|dd of=/dev/hda

* Limpiar nuestro MBR y la tabla de particiones:

sudo dd if=/dev/zero |pv|dd of=/dev/hda bs=512 count=1

* Limpia el MBR pero no toca la tabla de particiones, ( muy útil para borrar el GRUB sin perder datos en las particiones):

sudo dd if=/dev/zero |pv|dd of=/dev/hda bs=446 count=1

* Copiar/Restaurar el Volume Boot Sector (VBS):

Para copiar el VBS:

sudo dd if=/dev/hda |pv|dd of=/home/sector_arranque_hda count=1 bs=512

Para restaurar el VBS:

sudo dd if=/home/sector_arranque_hda |pv|dd of=/dev/hda

D) Otros:
* Grabar una imagen del disco en nuestro directorio /home saltándonos los errores del disco(muy útil para discos que se están muriendo):

sudo dd conv=noerror if=/dev/hda |pv|dd of=~/home/imagen_disco_con_errores.iso

* Crear un archivo vacío de 1 Mb:

sudo dd if=/dev/zero |pv|dd of=archivo_nuevo_vacio bs=1024 count=1024

* Crear un archivo swap de 2Gb:

sudo dd if=/dev/zero |pv|dd of=/swapspace bs=4k count=2048M
mkswap /swapspace
swapon /swapspace

* Convertir todas las letras en mayúsculas:

sudo dd if=miarchivo |pv|dd of=miarchivo conv=ucase

Usar el comando dd con un programa con entorno gráfico: Gdiskdump, es un entorno gráfico para este comando dd que nos facilita la tarea de clonar particiones o discos, de una forma rápida y sencilla. Se puede descargar desde la página https://launchpad.net/gdiskdump/ Una vez lo abrimos , con permisos de root – sudo gdiskdump – , vemos que el programa es muy fácil de usar, ya que solo tenemos que decirle la partición o disco a clonar (Formato de Entrada ) y su destino (Formato de Salida).

