Si deseas conectarte a la máquina de tu cliente desde tu propia máquina utilizando su dirección IP pública y el reenvío de puertos en el enrutador de tu cliente, puedes utilizar el siguiente comando para establecer la conexión SSH:

ssh -p puerto -o "ProxyJump=user@200.25.36.21" root@192.168.1.100