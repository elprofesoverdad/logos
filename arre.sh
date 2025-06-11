#!/bin/bash

# Pon aquí los blob ids que GitHub reportó como secretos
BLOBS=(
  "11394aa204fc0bb59a616e88cde318d37a204356"
  "84e2377cf1bb32227fbc45e24bcaf1377d6a47fa"
  "8db5c73e4fe7ddaa6522679107b5c1d21f15406a"
  "59ba8c1610a2697fad8513b6e97cb4062e1138bc"
  "3de948c8bc57f02d2345630efb7146d1c8616729"
  "9a4522073a1f171bafff6ff9767a23f37ec17ca1"
)

ARCHIVOS=()

echo "Buscando rutas de archivos asociadas a los blob ids..."

for blob in "${BLOBS[@]}"
do
    ruta=$(git rev-list --objects --all | grep "$blob" | awk '{print $2}')
    if [[ -n "$ruta" ]]; then
      ARCHIVOS+=("$ruta")
      echo "Blob $blob → $ruta"
    else
      echo "¡Atención! Blob $blob no encontrado en el historial."
    fi
done

if [ ${#ARCHIVOS[@]} -eq 0 ]; then
  echo "No se encontraron archivos para eliminar. Saliendo."
  exit 1
fi

echo
echo "Archivos a eliminar del historial:"
printf '%s\n' "${ARCHIVOS[@]}"

# Asegúrate de tener git-filter-repo instalado
if ! command -v git-filter-repo &> /dev/null
then
    echo "git-filter-repo no está instalado. Instálalo con: pip install git-filter-repo"
    exit 1
fi

# Borra los archivos del historial (en un solo comando)
git filter-repo --invert-paths $(for a in "${ARCHIVOS[@]}"; do echo --path "$a"; done)

echo
echo "¡Historial limpiado! Haciendo push forzado..."
git push --force

echo "¡Terminado!"
