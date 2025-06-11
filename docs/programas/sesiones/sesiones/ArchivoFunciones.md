# Algunas funciones de este proyecto interesantes

```bash
renovacionDeInterfazDeLista() {
 # comentamos sin comentarios
 if [[ ! -z $x ]]; then
    # 
    # while [[ "true" == "true" ]]; do
        # inotifywait -q -e close_write ~/pruebas/sincro |
        # while read -r filename event; do

             # selection=$(whiptail --title "ttitulo" \
             # --menu "Use: PgUp/PgDn/Flechas, para moverse.\nEnter, /Seleciona Archivo/Carpeta o la tecla de Tabulación para cambiar de campos.\n $curdir" 0 0 0 \
             # --cancel-button Cancelar \
             # --ok-button Seleccionar ../ BACK $MARCADORES 3>&1 1>&2 2>&3)
        # done
    # done
 fi

}



# TODO ALGÚN DÍA PENDIENTE Base de datos de typemime 
# $1 es el nombre del yaml si no existe lo crea 
insertarMime () {
     folder=$PWD
     cd ../../../data/yaml/mime
     if [[ ! -f $1 ]]; then
        # mkdir $1
     fi
     nombreVideo=$1
     nombreMarcador=$2
     tiempoMarcador=$3
     # si no existe o esta vacio: marcadores.yaml,
     # crea marcadores.yaml
     if [[ ! -s marcadoresVideo.yaml ]]; then
         # Utilización de una plantilla para iniciar la base de datos
         cd "$programas/plantillas"
         source marcaVideo.sh $nombreVideo $nombreMarcador $tiempoMarcador 1> $folder/.marcadores/marcadoresVideo.yaml
     fi
     cd $folder
}
```
