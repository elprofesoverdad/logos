# Terminal xfce xfce4-terminal ejecutar nueva pestaña, nueva ventana.
``` bash
xfce4-terminal --tab --title "MARCADORES" -e "bash -c 'usuario=${SUDO_USER:-${USER}}; source /home/$usuario/tron/Scripts/BajoNivel.sh; source /home/$usuario/tron/Scripts/AltoNivel.sh; source $sesiones/libcursos.sh; source /home/$usuario/.bashrc; playerctl pause; echo rutavideo es $RUTAVIDEO; interfazMarcadores $RUTAVIDEO; exec /bin/bash'"

```

[AYUDA EN: https://man.archlinux.org/man/extra/xfce4-terminal/xfce4-terminal.1.en](https://man.archlinux.org/man/extra/xfce4-terminal/xfce4-terminal.1.en)

[Y EN: https://docs.xfce.org/apps/xfce4-terminal/command-line](https://docs.xfce.org/apps/xfce4-terminal/command-line)