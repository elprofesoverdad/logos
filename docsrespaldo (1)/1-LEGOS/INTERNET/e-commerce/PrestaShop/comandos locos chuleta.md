daniel@daniel-laptop:~/tron/plugins/eComerce/prestashop$ mysql -u root -p


daniel@daniel-laptop:~/tron/plugins/eComerce/prestashop$ sudo chown -R www-data:www-data

  337  wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
  338  sudo dpkg -i cloudflared-linux-amd64.deb
  339  cloudflared tunnel login
  340  cloudflared tunnel create prestashop-tunnel
  341  micro ~/.cloudflared/config.yml
  342  cloudflared tunnel route dns prestashop-tunnel tienda.tudominio.com
  343  sudo apt install -y  thunar
  344  cloudflared tunnel route dns prestashop-tunnel tienda.tudominio.com
  345  cloudflared tunnel create prestashop-tunnel
  346  micro ~/.cloudflared/config.yml
  347  cloudflared tunnel route dns prestashop-tunnel tienda.mundomejor.uk
  348  systemctl status cloudflared
  349  sudo cloudflared service install
  350  cloudflared tunnel list
  351  cloudflared tunnel validate config.yml
  352  cloudflared tunnel run
  353  micro ~/.cloudflared/config.yml
  354  cloudflared tunnel validate config.yml
  355  cloudflared tunnel run
  356  micro ~/.cloudflared/config.yml
  357  cloudflared tunnel run
  358  ifconfig
  359  sudo apt install net-tools
  360  ifconfig
  361  micro  /etc/apache2/sites-available/prestashop.conf
  362  micro ~/.cloudflared/config.yml
  363  negocio
  364  actz
  365  negocio
  366  ls  /etc/apache2/sites-available/
  367  micro  /etc/apache2/sites-available/prestashop.conf
  368  sudo  ufw allow 80/tcp
  369  cloudflared tunnel list
  370  micro  /etc/apache2/sites-available/prestashop.conf
  371  kate  /etc/apache2/sites-available/prestashop.conf
  372  sudo micro /etc/apache2/sites-available/000-default.conf
  373  sudo systemctl restart apache2
  374  sudo micro /etc/apache2/sites-available/000-default.conf
  375  sudo systemctl restart apache2
  376  sudo micro /etc/apache2/sites-available/000-default.conf
  377  sudo systemctl restart apache2
  378  sudo micro /etc/apache2/sites-available/000-default.conf
  379  sudo systemctl restart apache2
  380  sudo micro /etc/apache2/sites-available/000-default.conf
  381  sudo systemctl restart apache2
  382  sudo micro /etc/apache2/sites-available/000-default.conf
  383  sudo systemctl restart apache2
  384  sudo micro /etc/apache2/sites-available/000-default.conf
  385  micro  /etc/apache2/sites-available/prestashop.conf
  386  sudo systemctl restart apache2
  387  sudo micro /etc/apache2/sites-available/000-default.conf
  388  micro  /etc/apache2/sites-available/prestashop.conf
  389  audioOn
  390  what
  391  command -V cp-igualito
  392  cp-igualito prestashop /var/www/html/tienda
  393  sudo cp-igualito prestashop /var/www/html/tienda
  394  cp -v -a -p -f -v -r -d prestashop/ /var/www/
  395  sudo cp -v -a -p -f -v -r -d prestashop/ /var/www/
  396  sudo cp -v -a -p -f -v  prestashop/ /var/www/html/
  397  sudo cp -v -a -p -f -v  prestashop/* /var/www/html/
  398  cd admin:/var/www/html/
  399  sudo chown -R www-data:www-data /var/www/html/
  400  sudo chown -R -v www-data:www-data /var/www/html/
  401  mysql -u root -p
  402  history
daniel@daniel-laptop:~/tron/plugins/eComerce/prestashop$ ^C








  262  ag "header_logo" --color --group -C 2 tienda
  263  ag --ignore "*.css" --ignore "*.scss" "header_logo" --color --group -C 2 tienda
  264  ag --ignore ".*" --only "*.css" --only "*.scss" "logo float-left\"
  265  ag --only "*.css" --only "*.scss" "logo float-left" tienda




  sudo apt-get install lamp-server^
   99  systemctl status apache2
  100  sudo mysql -u root -p
  101  echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php
  102  sudo mysql_secure_installation
  103  sudo apt install phpmyadmin -y
  104  audioOn
  105  unzip prestashop.zip
  106  unzip prestashop_8.2.1.zip
  107  sudo cp -a -r -v  prestashop/* /var/www/html/tienda/
  108  ls
  109  unzip prestashop.zip
  110  sudo cp -a -r -v  prestashop.zip /var/www/html/tienda/
  111  cd /var/www/html/tienda/
  112  ls
  113  unzip prestashop.zip
  114  sudo unzip prestashop.zip
  115  sudo chown -R www-data:www-data /var/www/html/tienda
  116  sudo chown -R -v www-data:www-data /var/www/html/tienda
  117  sudo find /var/www/html/tienda -type d -exec chmod 755 {} \;
  118  sudo find /var/www/html/tienda -type f -exec chmod 644 {} \;
  119  ls
  120  rm -r -v -d install
  121  sudo rm -r -v -d install
  122  sudo mysql -u root
  123  sudo pkill mysqld_safe
  124  sudo systemctl start mysql
  125  mysql -u root -p
  126  aliased
  127  actz
  128  historial
  129  aliased
  130  actz
  131  aliased
  132  actz
  133  historial
  134  aliased
  135  actz
  136  historial
  137  actz
  138  historial
  139  history | awk '{ $1=""; print substr($0,2) }'
  140  sudo a2enmod rewrite && sudo systemctl restart apache2
  141  mysql -u adminusername -p
  142  mysql -u daniel -p
  143  mysql -u root -p
  144  mysql -u root -p
  145  mysql -u prestashopuser"@"hostname -p
  146  sudo systemctl stop mysql
  147  sudo mysqld_safe --skip-grant-tables &
  148  sudo systemctl restart mysql
  149  mysql -u prestashopuser -p
  150  sudo apt update
  151  sudo apt install php-fpm libapache2-mod-fcgid
  152  sudo a2enmod actions proxy_fcgi alias proxy
  153  sudo systemctl restart apache2
  154  sudo systemctl restart php8.1-fpm
  155  php -v
  156  sudo systemctl restart php8.3-fpm
  157  sudo systemctl status php8.3-fpm
  158  sudo apt install php8.3-mysql php8.3-curl php8.3-gd php8.3-intl php8.3-mbstring php8.3-xml php8.3-zip libapache2-mod-fcgid
  159  sudo a2enmod actions proxy_fcgi alias proxy
  160  sudo systemctl restart apache2
  161  sudo systemctl restart php8.3-fpm
  162  sudo micro /etc/apache2/sites-available/prestashop.conf
  163  history
  164  php -v
  165  ls /etc/php/8.3/apache2/
  166  micro /etc/php/8.3/apache2/php.ini
  167  sudo systemctl restart apache2
  168  sudo apt install php8.3-curl php8.3-dom php8.3-fileinfo php8.3-gd php8.3-intl php8.3-mbstring php8.3-zip php8.3-json php8.3-iconv php8.3-mysql
  169  sudo apt install php8.3-curl php8.3-gd php8.3-intl php8.3-mbstring php8.3-zip php8.3-mysql php8.3-xml php8.3-fpm
  170  sudo systemctl restart apache2
  171  sudo systemctl restart php8.3-fpm
  172  sudo a2ensite prestashop.conf
  173  sudo systemctl reload apache2
  174  systemctl status apache2.service
  175  sudo systemctl reload apache2
  176  systemctl status apache2.service
  177  mkdir /var/www/html/tienda
  178  sudo mkdir /var/www/html/tienda
  179  sudo chown -R www-data:www-data /var/www/html/tienda
  180  actz
  181  historial
  182  mysql -u adminusername -p
  183  mysql -u prestashop -p
  184  mysql -u root -p
  185  mysql -u prestashopuser -p
  186  actz
  187  historial
  188  audioOn
  189  apt install -y plasma-browser-integration
  190  sudo apt install -y plasma-browser-integration
  191  what
  192  aliaslk apagar
  193  ls
  194  /marktext-x86_64.AppImage
  195  ./marktext-x86_64.AppImage
  196  sudo chmod -v 775 marktext-x86_64.AppImage
  197  sudo chmod -v 777 marktext-x86_64.AppImage
  198  ./marktext-x86_64.AppImage
  199  ./marktext-x86_64.AppImage --no-sandbox
  200  amixer set Speaker unmute
  201  audioOn
  202  amixer set Speaker mute
  203  aliased
  204  actz
  205  audioOn
  206  cls
  207  killall vlc
  208  cd $escritorio
  209  wget https://github.com/cmatomic/VLCplayer-AppImage/releases/download/3.0.11.1/VLC_media_player-3.0.11.1-x86_64.AppImage
  210  hayinternet
  211  ls
  212  ls *vlc*
  213  ls
  214  sudo chmod 777 VLC_media_player-3.0.11.1-x86_64.AppImage
  215  ls
  216  ./VLC_media_player-3.0.11.1-x86_64.AppImage
  217  ls
  218  sudo apt install -y $PWD/opera-stable_117.0.5408.93_amd64.deb
  219  audioOn
  220  sudo apt install -y opera
  221  audioOn
  222  sudo plymouth show-splash
  223  sudo plymouth message --text="hola mundo"
  224  ia
  225  apt -y install gimp
  226  sudo apt -y install gimp
  227  cd $escritorio
  228  ls
  229  cp -v -f logo.jpg /var/www/tienda/img/
  230  cp -v -f logo.jpg /var/www//html/tienda/img/
  231  sudo cp -v -f -a logo.jpg /var/www//html/tienda/img/
  232  ls
  233  sudo cp -v -f -a app_icon.png /var/www//html/tienda/img/
  234  ls
  235  sudo cp -v -f -a logo_stores.png /var/www//html/tienda/img/
  236  ls
  237  sudo cp -v -f -a prestashop-avatar.png /var/www//html/tienda/img/
  238  sudo apt-get install blivet-gui
  239  echo 'deb http://download.opensuse.org/repositories/home:/vtrefny/xUbuntu_24.04/ /' | sudo tee /etc/apt/sources.list.d/home:vtrefny.list
  240  curl -fsSL https://download.opensuse.org/repositories/home:vtrefny/xUbuntu_24.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_vtrefny.gpg > /dev/null
  241  sudo apt update
  242  sudo apt install blivet-gui
  243  sudo apt install hdparm
  244  sudo blivet-gui
  245  sudo apt-get install gparted
  246  sudo gparted
  247  what
  248  source entorno
  249  what
  250  htop
  251  pidof vlc
  252  killall vlc
  253  /snap/bin/vlc
  254  ./VLC_media_player-3.0.11.1-x86_64.AppImage
  255  sudo snap remove vlc
  256  apt install -y vlc
  257  sudo apt install -y vlc
  258  ls
  259  sudo cp -v -f -a preston-login-wink@2x.png /var/www//html/tienda/img/
  260  ls
  261  sudo cp -v -f -a preston-login@2x.png /var/www//html/tienda/img/
  262  ag "header_logo" --color --group -C 2 tienda
  263  ag --ignore "*.css" --ignore "*.scss" "header_logo" --color --group -C 2 tienda
  264  ag --ignore ".*" --only "*.css" --only "*.scss" "logo float-left\"
  265  ag --only "*.css" --only "*.scss" "logo float-left" tienda
  266  ls
  267  ag --only "*.css" --only "*.scss" -Q "logo float-left" tienda
  268  ag -G "\.(css|scss)$" -Q "logo float-left" tienda
  269  ag -G "\.(css|scss)$" -Q "logo" tienda
  270  ag -G "\.(css|scss)$" -Q "logo" tienda > $escritorio/buslogo.txt
  271  ag -G "\.(css|scss)$" -Q "header_logo" tienda
  272  ag "$logo_url" --color --group -C 2 tienda
  273  ag '$logo_url' --color --group -C 2 tienda
  274  ag "All rights reserved"  --color --group -C 2 tienda
  275  ag "All rights reserved"  --color --group -C 2 tienda | grep prestashop
  276  ag "https://www.prestashop.com"  --color --group -C 2 tienda | grep prestashop
  277  ag "https://www.prestashop.com"  --color --group -C 2 tienda
  278  ag "All rights reserved"  --color --group -C 2 tienda
  279  apt install -y inkscape
  280  sudo apt install -y inkscape
  281  sudo apt install silversearcher-ag
  282  sudo thunar
  283  sudo dolphin tienda/admin572ymosckgdxufddv47/themes/new-theme/template/
  284  sudo apt install kio-admin
  285  kio-admin
  286  sudo apt update
  287  sudo apt install ffmpeg
  288  sudo apt install ubuntu-restricted-extras
  289  snap install vlc
  290  snap help refresh
  291  snap list
  292  ls
  293  sudo cp -v -f -a prestashop@2x.png /var/www//html/tienda/img/
  294  micro tienda/admin572ymosckgdxufddv47/themes/default/template/controllers/login/content.tpl
  295  micro tienda/translations/es-ES/ShopThemeGlobal.es-ES.xlf
  296  ag "All rights reserved" --color --group -C 2 tienda
  297  ag "Software Ecommerce desarrollado" --color --group -C 2 tienda
  298  cd /var/www/html
  299  ls
  300  ag "prestashop" --color --group -C 2 tienda
  301  ag "logo" --color --group -C 2 tienda
  302  ag "header_logo" --color --group -C 2 tienda
  303  cls
  304  ag "header_logo" --color --group -C 2 tienda
  305  audioOn
  306  espacio
  307  cd $descargas
  308  ls
  309  cd /var/www/html
  310  ls
  311  ag "AdminDashboardController" --color --group -C 2 tienda
  312  ag "AdminDashboardHelp" --color --group -C 2 tienda
  313  ag "AdminDashboardHelp" --color --group -C 2 tienda > $escritorio/boton.txt
  314  sudo poweroff now
  315  sudo poweroff
  316  ag "AdminDashboardHelp" --color --group -C 2 tienda > $escritorio/boton.txt
  317  cd /var/www/html/
  318  ag "AdminDashboardHelp" --color --group -C 2 tienda > $escritorio/boton.txt
  319  ag "AdminDashboardHelp" --color --group -C 2 tienda
  320  ag "btn-help" --color --group -C 2 tienda
  321  ag "https://help.prestashop-project.org" --color --group -C 2 tienda
  322  ls
  323  ./marktext-x86_64.AppImage
  324  ls $1Legos
  325  ls $1egos
  326  ls $1legos
  327  ls $1-legos
  328  ls $legos1
  329  cd $legos1/NEGOCIO
  330  echo $PWD
  331  aliased
  332  actz
  333  negocio
  334  aliased
  335  actz
  336  negocio
  337  wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
  338  sudo dpkg -i cloudflared-linux-amd64.deb
  339  cloudflared tunnel login
  340  cloudflared tunnel create prestashop-tunnel
  341  micro ~/.cloudflared/config.yml
  342  cloudflared tunnel route dns prestashop-tunnel tienda.tudominio.com
  343  sudo apt install -y  thunar
  344  cloudflared tunnel route dns prestashop-tunnel tienda.tudominio.com
  345  cloudflared tunnel create prestashop-tunnel
  346  micro ~/.cloudflared/config.yml
  347  cloudflared tunnel route dns prestashop-tunnel tienda.mundomejor.uk
  348  systemctl status cloudflared
  349  sudo cloudflared service install
  350  cloudflared tunnel list
  351  cloudflared tunnel validate config.yml
  352  cloudflared tunnel run
  353  micro ~/.cloudflared/config.yml
  354  cloudflared tunnel validate config.yml
  355  cloudflared tunnel run
  356  micro ~/.cloudflared/config.yml
  357  cloudflared tunnel run
  358  ifconfig
  359  sudo apt install net-tools
  360  ifconfig
  361  micro  /etc/apache2/sites-available/prestashop.conf
  362  micro ~/.cloudflared/config.yml
  363  negocio
  364  actz
  365  negocio
  366  ls  /etc/apache2/sites-available/
  367  micro  /etc/apache2/sites-available/prestashop.conf
  368  sudo  ufw allow 80/tcp
  369  cloudflared tunnel list
  370  micro  /etc/apache2/sites-available/prestashop.conf
  371  kate  /etc/apache2/sites-available/prestashop.conf
  372  sudo micro /etc/apache2/sites-available/000-default.conf
  373  sudo systemctl restart apache2
  374  sudo micro /etc/apache2/sites-available/000-default.conf
  375  sudo systemctl restart apache2
  376  sudo micro /etc/apache2/sites-available/000-default.conf
  377  sudo systemctl restart apache2
  378  sudo micro /etc/apache2/sites-available/000-default.conf
  379  sudo systemctl restart apache2
  380  sudo micro /etc/apache2/sites-available/000-default.conf
  381  sudo systemctl restart apache2
  382  sudo micro /etc/apache2/sites-available/000-default.conf
  383  sudo systemctl restart apache2
  384  sudo micro /etc/apache2/sites-available/000-default.conf
  385  micro  /etc/apache2/sites-available/prestashop.conf
  386  sudo systemctl restart apache2
  387  sudo micro /etc/apache2/sites-available/000-default.conf
  388  micro  /etc/apache2/sites-available/prestashop.conf
  389  audioOn
  390  what
  391  command -V cp-igualito
  392  cp-igualito prestashop /var/www/html/tienda
  393  sudo cp-igualito prestashop /var/www/html/tienda
  394  cp -v -a -p -f -v -r -d prestashop/ /var/www/
  395  sudo cp -v -a -p -f -v -r -d prestashop/ /var/www/
  396  sudo cp -v -a -p -f -v  prestashop/ /var/www/html/
  397  sudo cp -v -a -p -f -v  prestashop/* /var/www/html/
  398  cd admin:/var/www/html/
  399  sudo chown -R www-data:www-data /var/www/html/
  400  sudo chown -R -v www-data:www-data /var/www/html/
  401  mysql -u root -p
  402  history
daniel@daniel-laptop:~/tron/plugins/eComerce/prestashop$
