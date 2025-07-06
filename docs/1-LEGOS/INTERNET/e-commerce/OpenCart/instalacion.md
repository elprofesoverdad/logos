mysql -u root -p

 CREATE DATABASE IF NOT EXISTS opencart; CREATE USER IF NOT EXISTS 'opencart'@'localhost' IDENTIFIED BY 'Copa007copa.'; GRANT ALL PRIVILEGES ON opencart.* TO 'opencart'@'localhost'; FLUSH PRIVILEGES;


DROP DATABASE IF EXISTS opencart; DROP USER IF EXISTS 'opencart'@'localhost'; FLUSH PRIVILEGES;


despues de descomprimir se copia el contenido de upload
sudo cp -a -r -v -d -f upload/* /var/www/html/ecomerce/dotecomerce/

sudo chown  -v www-data:www-data /var/www

sudo chown -R -v www-data:www-data /var/www/html/ecomerce/dotecomerce
sudo mv -v admin/config-dist.php admin/config.php

sudo mv -v config-dist.php config.php


busque por internet el plugin gratis español y cambie las banderas de españa con gimp NO RESULTO BIEN

para quitar los logos cambie las imagenes en opencart y para quitar
el copy en admin:/var/www/html/ecomerce/dotecomerce/copa/language/es-es/common/footer.php

para el cambio efectivo de idioma ver https://github.com/burbuja/opencart-spanish?tab=readme-ov-file

