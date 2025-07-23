sudo apt install -y $PWD/google-chrome-stable_current_amd64.deb
    3  sudo apt purgue -y google-chrome-stable_current
    4  sudo apt purge -y google-chrome-stable_current
    5  sudo apt purge -y google-chrome-stable
    6  sudo apt install -y $PWD/google-chrome-stable_current_amd64.deb
    7  snap install vlc
    8  htop
    9  sudo apt install htop
   10  htop
   11  sudo apt install transmission
   12  sudo uwf allow 51413
   13  sudo ucf allow 51413
   14  sudo ufw allow 51413
   15  ls
   16  sudo apt install -v -y $PWD/code_1.98.1-1741624510_amd64.deb
   17  sudo apt install -y $PWD/code_1.98.1-1741624510_amd64.deb
   18  sudo installBash
   19  installBash
   20  pactl list sources
   21  cd /homa/daniel/tron
   22  cd /home/daniel/tron
   23  ls
   24  cd Scrip*
   25  ls
   26  source BajoNivel.sh
   27  source AltoNivel.sh
   28  instalarBash
   29  AltoNivel
   30  sudo apt -y install code
   31  installBash
   32  actz
   33  aliased
   34  curl https://getmic.ro | bash
   35  sudo apt install curl
   36  curl https://getmic.ro | bash
   37  su - root -c "cd /usr/bin; wget -O- https://getmic.ro | GETMICRO_REGISTER=y sh
   38  su - root -c "cd /usr/bin; wget -O- https://getmic.ro | GETMICRO_REGISTER=y sh"
   39  cd /usr/bin
   40  sudo su
   41  cd /
   42  micro
   43  streamingAudio
   44  sudo streamingAudio
   45  sudo su
   46  sonido
   47  sudo apt install pulseaudio
   48  sudo apt install pulseaudio-utils
   49  sudo streamingAudio
   50  sudo su
   51  sonido
   52  systemctl status pipewire
   53  systemctl --user restart pipewire-pulse
   54  systemctl --user restart pipewire
   55  sonido
   56  sudo gedit /etc/pipewire/pipewire-pulse.conf
   57  sudo micro /etc/pipewire/pipewire-pulse.conf
   58  systemctl --user status pipewire
   59  systemctl --user status pipewire-pulse
   60  mkdir -p ~/.config/pulse
   61  micro ~/.config/pulse/default.pa
   62  systemctl --user restart pipewire-pulse
   63  systemctl --user restart pipewire
   64  pactl list modules
   65  pactl load-module module-simple-protocol-tcp source=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor record=true port=12345 format=s32le rate=48000
   66  pactl list modules
   67  pactl unload-module module-simple-protocol-tcp
   68  pactl list modules
   69  pactl load-module module-simple-protocol-tcp source=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor record=true port=12345 format=s16le rate=48000
   70  pactl list modules
   71  pactl unload-module module-simple-protocol-tcp
   72  pactl load-module module-simple-protocol-tcp source=0 record=true port=12345 format=s16le rate=48000
   73  pactl unload-module module-simple-protocol-tcp
   74  pactl load-module module-simple-protocol-tcp source=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor record=true port=12345 format=s16le rate=48000
   75  sudo mysql -u root -p
   76  pactl list sources short
   77  actz
   78  command -V streamingAudio
   79  aliased
   80  actz
   81  aliased
   82  actz
   83  aliased
   84  actz
   85  aliased
   86  actz
   87  sonidoOff
   88  audioOff
   89  audioOn











































sudo apt install -y $PWD/google-chrome-stable_current_amd64.deb
snap install vlc
sudo apt install htop
sudo apt install transmission
sudo ufw allow 51413
sudo apt install -y $PWD/code_1.98.1-1741624510_amd64.deb
cd /home/daniel/tron
cd Scrip*
source BajoNivel.sh
source AltoNivel.sh
sudo installBash
actz
cd /usr/bin
sudo su
wget -O- https://getmic.ro | GETMICRO_REGISTER=y sh
sudo apt install pulseaudio
sudo apt install pulseaudio-utils
systemctl status pipewire
systemctl --user restart pipewire-pulse
systemctl --user restart pipewire
sudo micro /etc/pipewire/pipewire-pulse.conf
systemctl --user status pipewire
systemctl --user status pipewire-pulse
mkdir -p ~/.config/pulse
micro ~/.config/pulse/default.pa
systemctl --user restart pipewire-pulse
systemctl --user restart pipewire
pactl list sources short
pactl load-module module-simple-protocol-tcp source=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor record=true port=12345 format=s16le rate=48000
pactl list modules
pactl unload-module module-simple-protocol-tcp
pactl list modules
sudo mysql -u root -p
audioOn

sudo apt-get install lamp-server^
systemctl status apache2
sudo mysql -u phpmyadmin -p Copa007copa.
---
CREATE USER 'phpmyadmin'@'localhost' IDENTIFIED BY 'tu_contraseña';
GRANT ALL PRIVILEGES ON *.* TO 'phpmyadmin'@'localhost';
FLUSH PRIVILEGES;
EXIT;
http://localhost/phpmyadmin

---
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php
sudo mysql_secure_installation
sudo apt install phpmyadmin -y
sudo a2enmod rewrite && sudo systemctl restart apache2
systemctl restart apache2

history | awk '{ $1=""; print substr($0,2) }'



Desde la línea de comandos
La base de datos debe crearse con codificación UTF-8 de 4 bytes ( utf8mb4_general_ci). Para obtener información sobre la instalación y configuración de MySQL, consulte laDocumentación de MySQLConéctese como root a su servidor MySQL. En este ejemplo, nuestro usuario root se llama adminusername:

$ mysql -u adminusername -p
Crea la base de datos y dale un nombre como “prestashop”:

> CREATE DATABASE prestashop COLLATE utf8mb4_general_ci;
Otorgar privilegios sobre esa base de datos a un nuevo usuario (el que PrestaShop utilizará para conectarse a la base de datos). Lo llamaremos “prestashopuser”.

> CREATE USER "prestashopuser"@"hostname" IDENTIFIED BY "somepassword";
> GRANT ALL PRIVILEGES ON prestashop.* TO "prestashopuser"@"hostname";
En el ejemplo anterior,

prestashopes el nombre de la nueva base de datos
hostnameGeneralmente es localhost ( 127.0.0.1o localhost), si no conoce el valor, consulte con un administrador del sistema
somepasswordDebe ser una contraseña segura y, por supuesto, sólo usted la debe conocer.
Finalmente, elimine los privilegios:

> FLUSH PRIVILEGES;
y salir de la conexión a la base de datos:

> EXIT;



prestashop debe cambiarse el hostname por localhost y la contraseña
