# Bash comandos básicos 

## Case:

``` bash

case EXPRESSION in

  PATTERN_1)
    STATEMENTS
    ;;

  PATTERN_2)
    STATEMENTS
    ;;

  PATTERN_N)
    STATEMENTS
    ;;

  *)
    STATEMENTS
    ;;
esac

```
## Contador bash

``` bash
num=0
num=$(( $num + 1 ))
```

## if elif (else) bash:

``` bash
read -p "Enter a number: " USER_INPUT
if [[ $USER_INPUT -lt 0 ]]; then
     echo "Not a valid positive number input"
elif [[ $USER_INPUT -gt 0 && $USER_INPUT -lt 10 ]]; then
     echo "Valid 1 digit number entered"
elif [[ $USER_INPUT -gt 9 && $USER_INPUT -lt 100 ]]; then
     echo "Valid 2 digit number entered"
fi
```