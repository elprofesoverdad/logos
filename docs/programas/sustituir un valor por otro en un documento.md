# sustituir un valor por otro en un documento en grub:

## Usando el comando grep y sed:

* Esta linea desactiva el splah inicial

```bash
sudo grep -n "GRUB_CMDLINE_LINUX_DEFAULT" /etc/default/grub | cut -d: -f1 | xargs -I {} sudo sed -i '{}s/.*/GRUB_CMDLINE_LINUX_DEFAULT="text"/' /etc/default/grub
```

## Usando el comando awk y sed:

```bash
sudo awk '/GRUB_CMDLINE_LINUX_DEFAULT/{gsub(/".*"/, "\"quiet splash nofb nomodeset video=vesafb:off\"")}1' /etc/default/grub | sudo tee /etc/default/grub > /dev/null
```

## Usando el comando awk y sed:

```bash
sudo awk '/GRUB_CMDLINE_LINUX_DEFAULT/{gsub(/".*"/, "\"quiet splash nofb nomodeset video=vesafb:off\"")}1' /etc/default/grub | sudo tee /etc/default/grub > /dev/null
```

## Usando el comando perl:

```bash
sudo perl -i -pe 's/GRUB_CMDLINE_LINUX_DEFAULT=".*?"/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nofb nomodeset video=vesafb:off"/' /etc/default/grub
```

## script completo

```bash
#!/bin/bash

# Edita el archivo /etc/default/grub
sudo sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="\(.*\)"/GRUB_CMDLINE_LINUX_DEFAULT="\1 quiet splash nofb nomodeset video=vesafb:off"/' /etc/default/grub

# Actualiza la configuración de GRUB
sudo update-grub

# Edita el archivo /etc/systemd/system.conf
sudo sed -i 's/#DefaultTimeoutStopSec=90s/DefaultTimeoutStopSec=5s/' /etc/systemd/system.conf
```

## 

```bash

```