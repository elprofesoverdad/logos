# Bash Matrices Vectores Array Arrays asociativas asociativa menu y menús

## Matrices:

### Pasar un arreglo, vector o matriz como parámetro a una función:

``` bash
# Para una Matriz asociativa:

function foo {
    local -n data_ref=$1
    echo ${data_ref[a]} ${data_ref[b]}
}

declare -A data
data[a]="Fred Flintstone"
data[b]="Barney Rubble"
foo data

# ############################################3

# Para una Matriz Normal:

function copyFiles() {
   arr=("$@")
   for i in "${arr[@]}";
      do
          echo "$i"
      done

}

array=("one 1" "two 2" "three 3")

copyFiles "${array[@]}"
```

### Creación:

``` bash 
declare -A “Nombre de matriz”
```

### Asignación: 

``` bash 
* NombreArray [ key ] =value
* declare -A ArrayName = ( [ clave1 ] =Valor1 [ clave2 ] =Valor2 [ Clave3 ] =Valor3…. )

```

### Convertir una matriz asociativa en un vector:

``` bash
for idx in "${!OPTIONS[@]}";do
        dialogarray+=("$idx" "${OPTIONS[$idx]}")
    done
```

### : Imprimir o mostrar valores del arreglo matriz,  asociativa: 

``` bash 
1. Un valor dada la clave:
        - echo ${NombreArray[nombreClave]}

2. Todos los valores iterando en todas las claves:
        - for key in "${!ArrayName[@]}"; do echo $key; done

3. Todos las claves por expansión:
        - echo " ${!muestraArray1[@]} "

4. Clave y Valor iterando por valor:
        - for val in "${ArrayName[@]}"; do echo $val; done

5.  Todos los valores por expansión:
        - echo "${sampleArray1[@]}"

6. Clave Valor iterando por clave:
        - for key in "${!sampleArray1[@]}"; do echo "$key  ${sampleArray1[$key]}"; done

7. Contando las duplas del arreglo:
        - echo "${#ArrayName[@]}"

9. Añadiendo Valores: 
        - ArrayName+=([key]=value)

10. Borrando del arreglo por clave:
        - unset ArrayName[Key]

11. Verificar un Elemento:
        - $ if [ ${ArrayName[searchKEY]+_} ]; then echo "Exists"; else echo "Not available"; fi

12. Borrar todo el vector:
        - unset ArrayName

```







