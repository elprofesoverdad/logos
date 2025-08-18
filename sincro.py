#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

# --- CONFIGURACIÓN ---
# Modifica estas rutas según tu estructura de directorios.
# Asegúrate de que terminen con una barra inclinada si son directorios.
SOURCE_DIR = Path("/home/daniel/tron/")
DEST_DIR = Path("/home/daniel/tron/biblioteca/Mkdocs/docs/")

# Lista de patrones a excluir. Se aplica a directorios y archivos.
# Usa la sintaxis de `fnmatch` (ej. 'biblioteca/*', '*/node_modules/*').
EXCLUDE_PATTERNS = [
    'biblioteca/',
    'programas/cloudflared/logos-worker/',
    'plugins/node/',
    'node/',
    '*/assets/',
    '.git/',
    '__pycache__/'
]
# --- FIN DE LA CONFIGURACIÓN ---

def is_excluded(path: Path, source_dir: Path, exclude_patterns: list) -> bool:
    """
    Verifica si una ruta debe ser excluida según los patrones.
    """
    relative_path_str = str(path.relative_to(source_dir))
    # Agregamos una barra al final para que coincida con patrones de directorio como 'biblioteca/'
    if path.is_dir():
        relative_path_str += '/'
        
    for pattern in exclude_patterns:
        # Usamos Path.match que es similar a fnmatch
        # Para patrones de directorio, necesitamos una coincidencia más flexible
        if pattern.endswith('/'):
            if relative_path_str.startswith(pattern):
                return True
        elif path.match(pattern):
            return True
            
    # Verificar si algún directorio padre está excluido
    for parent in path.parents:
        if parent == source_dir:
            break
        parent_rel_str = str(parent.relative_to(source_dir)) + '/'
        for pattern in exclude_patterns:
            if pattern.endswith('/') and parent_rel_str.startswith(pattern):
                return True

    return False

def clean_empty_md_files(directory: Path):
    """
    Busca y elimina archivos .md vacíos en el directorio de origen.
    """
    print("--- Buscando y eliminando archivos .md vacíos ---")
    deleted_count = 0
    for md_file in directory.rglob("*.md"):
        try:
            if md_file.stat().st_size == 0:
                md_file.unlink()
                print(f"Eliminado archivo vacío: {md_file}")
                deleted_count += 1
        except OSError as e:
            print(f"Error al eliminar {md_file}: {e}", file=sys.stderr)
    
    if deleted_count == 0:
        print("No se encontraron archivos .md vacíos.")
    else:
        print(f"Total de archivos vacíos eliminados: {deleted_count}")
    print("-" * 20)


def sync_with_hardlinks():
    """
    Función principal para sincronizar archivos usando enlaces duros.
    Ahora incluye archivos .md y .html.
    """
    ### MODIFICADO ###
    # Lista de tipos de archivo a sincronizar.
    FILE_PATTERNS_TO_SYNC = ['*.md', '*.html']

    print(f"--- Iniciando Sincronización con Enlaces Duros ---")
    print(f"Origen:  {SOURCE_DIR}")
    print(f"Destino: {DEST_DIR}")
    print(f"Tipos de archivo: {', '.join(FILE_PATTERNS_TO_SYNC)}") ### MODIFICADO ###
    print("-" * 20)

    if not SOURCE_DIR.is_dir() or not DEST_DIR.is_dir():
        print("Error: El directorio de origen o destino no existe.", file=sys.stderr)
        sys.exit(1)

    source_files = set()
    
    ### MODIFICADO ###
    # 1. Recolectar todos los archivos del origen que no estén excluidos
    print(f"1. Recolectando archivos ({', '.join(FILE_PATTERNS_TO_SYNC)}) del origen...")
    for pattern in FILE_PATTERNS_TO_SYNC:
        for path_object in SOURCE_DIR.rglob(pattern):
            if path_object.is_file() and not is_excluded(path_object, SOURCE_DIR, EXCLUDE_PATTERNS):
                source_files.add(path_object)
    
    print(f"Se encontraron {len(source_files)} archivos para sincronizar.")

    # 2. Crear enlaces duros y directorios en el destino
    print("\n2. Creando/actualizando enlaces duros en el destino...")
    for src_path in source_files: ### MODIFICADO ### (Solo cambio de nombre de variable)
        relative_path = src_path.relative_to(SOURCE_DIR)
        dest_path = DEST_DIR / relative_path

        # Crear directorio padre en el destino si no existe
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Si ya existe un archivo en el destino, lo eliminamos antes de crear el enlace.
            # Esto maneja actualizaciones y previene errores si ya existe un archivo normal.
            if dest_path.exists() or dest_path.is_symlink():
                 # Verificamos si ya es un enlace duro al mismo archivo para evitar trabajo innecesario
                if dest_path.exists() and dest_path.samefile(src_path):
                    continue # Ya está correctamente enlazado, pasar al siguiente
                dest_path.unlink()

            # Crear el enlace duro
            os.link(src_path, dest_path)
            # print(f"Enlace creado: {dest_path}")

        except OSError as e:
            print(f"Error creando enlace para {src_path}: {e}", file=sys.stderr)

    print("Enlaces duros actualizados exitosamente.")

    ### MODIFICADO ###
    # 3. Limpiar archivos huérfanos en el destino
    print(f"\n3. Buscando archivos huérfanos ({', '.join(FILE_PATTERNS_TO_SYNC)}) en el destino para limpiar...")
    dest_files = set()
    for pattern in FILE_PATTERNS_TO_SYNC:
        dest_files.update(f for f in DEST_DIR.rglob(pattern) if f.is_file())
    
    orphaned_count = 0

    for dest_path in dest_files:
        relative_path = dest_path.relative_to(DEST_DIR)
        src_path = SOURCE_DIR / relative_path

        if src_path not in source_files:
            try:
                dest_path.unlink()
                print(f"Eliminado enlace huérfano: {dest_path}")
                orphaned_count += 1
            except OSError as e:
                print(f"Error eliminando enlace huérfano {dest_path}: {e}", file=sys.stderr)
    
    if orphaned_count == 0:
        print("No se encontraron archivos huérfanos.")
    else:
        print(f"Total de archivos huérfanos eliminados: {orphaned_count}")


def run_sync(*args, **kwargs):
    clean_empty_md_files(SOURCE_DIR)
    sync_with_hardlinks()
    print("\n--- Sincronización completada exitosamente. ---")

if __name__ == "__main__":
    run_sync()