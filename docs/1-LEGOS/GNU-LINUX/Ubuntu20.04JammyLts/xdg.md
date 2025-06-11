# Espacificaciones de directorios base xdg freedesktop

Usar:
``` bash
desktop=$(xdg-user-dir DESKTOP)
```
> Donde desktop es la variable que en toda ocación y lenguaje almacena la ubicación del escritorio

se puede sustituir DESKTOP por:

DESKTOP
DOWNLOAD
TEMPLATES
PUBLICSHARE
DOCUMENTS
MUSIC
PICTURES
VIDEOS
para las otras carpetas base.

[ver tambien: https://wiki.archlinux.org/title/XDG_user_directories](https://wiki.archlinux.org/title/XDG_user_directories)


#### De man xdg-user-dir :


``` bash
NAME
       xdg-user-dir - Find an XDG user dir

SYNOPSIS
       xdg-user-dir [NAME]

DESCRIPTION
       xdg-user-dir looks up the current path for one of the special XDG user dirs.

       This command expects the name of an XDG user dir as argument. The possible names are:
           DESKTOP
           DOWNLOAD
           TEMPLATES
           PUBLICSHARE
           DOCUMENTS
           MUSIC
           PICTURES
           VIDEOS

FILES
       The values are looked up in the user-dirs.dir file. This file is created by the xdg-user-dirs-update utility.

ENVIRONMENT
       The XDG_CONFIG_HOME environment variable determines where the user-dirs.dirs file is located.

SEE ALSO
       xdg-user-dirs-update(1)

```