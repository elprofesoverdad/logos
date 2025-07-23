# Comprimir y descomprimir

## zstd

Para archivar con tar una carpeta:
> zstd no archiva, no sirve para carpetas hay que ayudarlo con tar.


#### Archiva y comprime conservando permisos:

    tar --zstd --acls --xattrs -v -p -c -f  Systemback.tar.zst Systemback


#### Para descomprimir:
> despues de la opción -f solo puede ir el nombre del archivo a descomprimir.

    tar --zstd -v -x -f directory.tar.zst