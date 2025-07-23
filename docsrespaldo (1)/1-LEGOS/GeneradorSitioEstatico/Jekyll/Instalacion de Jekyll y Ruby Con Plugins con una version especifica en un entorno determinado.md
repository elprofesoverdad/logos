# Instalacion de Jekyll y Ruby Con Plugins con una version especifica en un entorno determinado

## Definiciones:

1. Carpeta de Entorno

Carpeta de Entorno: ~/ReposWebs/mundomejor
Esta carpeta actúa como el entorno donde configuras las herramientas y dependencias necesarias para trabajar con Jekyll. Aquí es donde se instalan las gemas y se gestiona la configuración del entorno de desarrollo.
Puedes pensar en esta carpeta como el "entorno" que contiene todo lo necesario para que tu proyecto funcione sin interferir con el sistema global.

2. Carpeta del Proyecto

Carpeta del Proyecto: ~/ReposWebs/mundomejor/web
Esta es la carpeta específica donde resides tu código fuente de Jekyll. Aquí es donde desarrollas y gestionas el contenido de tu sitio web.
Es más lógica y representativa de tu trabajo, ya que contendrá el código y la configuración específica de tu proyecto.

## Ruby

Para gestionar las versiones de Ruby y Jekyll de manera más segura y siguiendo buenas prácticas, puedes utilizar tanto el archivo `Gemfile` como el archivo `.ruby-version`. Aquí te explico cómo funcionan y cuál es la mejor manera de usarlos.

## Control de Versiones de Ruby

### Usar el Gemfile

Es posible especificar la versión de Ruby directamente en el `Gemfile` de tu proyecto. Esto es útil porque:

- **Compatibilidad**: Asegura que la aplicación se ejecute con la versión de Ruby que necesitas, lo que puede prevenir errores en la ejecución debido a incompatibilidades.

- **Despliegue**: Plataformas como Heroku utilizan la versión especificada en el `Gemfile` para determinar qué versión de Ruby usar en producción.

Para especificar la versión de Ruby en el `Gemfile`, puedes agregar la siguiente línea:

```ruby
ruby '3.1.6'
```

Esto indica que tu aplicación requiere Ruby 3.1.6. Cuando ejecutes `bundle install`, Bundler verificará que la versión de Ruby que estás usando coincide con la especificada. Si no coincide, te mostrará un error.

### Usar el Archivo `.ruby-version`

El archivo `.ruby-version` es una forma sencilla de establecer la versión de Ruby para un proyecto. Cuando se encuentra este archivo en el directorio del proyecto, `rbenv` o `RVM` automáticamente utilizan la versión especificada. Esto es útil para:

- **Facilidad de uso**: Permite a otros desarrolladores que clonen tu proyecto saber rápidamente qué versión de Ruby deben usar sin tener que revisar el `Gemfile`.

- **Configuración automática**: Cuando cambias de directorio al de tu proyecto, la versión de Ruby se ajusta automáticamente si usas un gestor de versiones.

Puedes crear un archivo `.ruby-version` en el directorio raíz de tu proyecto (por ejemplo, `~/ReposWebs/mundomejor/web/.ruby-version`) y agregar la versión deseada:

```
3.1.6
```

### Buenas Prácticas

- **Usar Ambos**: Es común y aceptable tener la versión de Ruby especificada tanto en el `Gemfile` como en el archivo `.ruby-version`. Esto asegura que tanto el entorno de desarrollo como el de producción estén alineados.

Citations:
[1] https://www.mslinn.com/ruby/1000-ruby-setup.html
[2] https://launchschool.com/books/core_ruby_tools/read/ruby_version_managers
[3] https://bundler.io/guides/gemfile_ruby.html
[4] https://stackoverflow.com/questions/32934651/is-it-a-bad-practice-to-list-ruby-version-in-both-gemfile-and-ruby-version-dotf
[5] https://www.reddit.com/r/rails/comments/gy07ne/specifying_ruby_version_in_gemfile/
[6] https://devcenter.heroku.com/articles/ruby-versions
[7] https://stackify.com/rvm-how-to-get-started-and-manage-your-ruby-installations/
[8] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/11936978/435c1a0d-a045-4b16-bdae-bd5e1e70e2ae/articulos-seo-google.md
[9] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/11936978/c4acceca-4d8d-4420-98f8-3cd179a56b9d/como-instalar-jekyl-en-xubuntu.txt

## Verificaciones

* Para verificar la versión de Jekyll instalada, puedes usar el siguiente comando:

```bash
jekyll -v
```

Esto te mostrará la versión de Jekyll que está actualmente en uso.

* Verificar la Versión de Ruby
  Después de instalar Ruby, puedes verificar la versión instalada usando el siguiente comando:

```bash
ruby -v
```

Esto te mostrará la versión actual de Ruby que estás utilizando.

---------------------

Pasos para Configurar tu Entorno Local

### Instalación de rbenv y Ruby

Primero, asegúrate de tener `rbenv` instalado. Si no lo tienes, puedes instalarlo siguiendo estos pasos:

```bash
# Instala rbenv y ruby-build

YO LO INSTALE ASÍ
de:
https://github.com/rbenv/rbenv
brew install rbenv

OTRA MANERA
ESTE A MI NO ME FUNCIONA CON RUBY 3.3.4
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
```

Luego, instala Ruby:

```bash
rbenv install 3.1.6
```

!!! warning "Importante"
    No usar global si estas haciendo un entorno usar local en la capeta de proyecto, ye cuyo caso se hace local en esa carpeta.

### Crear un Directorio para tu Proyecto

Crea un directorio donde almacenarás tu proyecto y las gemas:

```bash
mkdir -p $tron/plugins/rubi/entornos/rubi-jekyll/gems
cd $tron/plugins/rubi/entornos/rubi-jekyll/gems


mkdir -p ~/ReposWebs/mundomejor/gems
cd ~/ReposWebs/mundomejor
```

### 3. Configurar Variables de Entorno

Configura las variables de entorno para que las gemas se instalen en tu directorio local:

```bash
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
rbenv local 3.1.6
export GEM_HOME="$tron/plugins/rubi/entornos/rubi-jekyll/gems"
export GEM_PATH="$tron/plugins/rubi/entornos/rubi-jekyll/gems"
export PATH=$PATH:$GEM_HOME/bin


export GEM_HOME=~/ReposWebs/mundomejor/gems
export GEM_PATH=~/ReposWebs/mundomejor/gems
export PATH=$PATH:$GEM_HOME/bin
```

Para que estas configuraciones se apliquen cada vez que abras una nueva terminal, agrega las líneas anteriores a tu archivo `~/.bashrc`:

```bash
echo 'export GEM_HOME=~/tron/plugins/rubi/entornos/rubi-jekyll/gems' >> ~/.bashrc
echo 'export GEM_PATH=~/tron/plugins/rubi/entornos/rubi-jekyll/gems' >> ~/.bashrc
echo export PATH=$PATH:$GEM_HOME/bin


echo 'export GEM_HOME=~/ReposWebs/mundomejor/gems' >> ~/.bashrc
echo 'export GEM_PATH=~/ReposWebs/mundomejor/gems' >> ~/.bashrc
echo 'export PATH=$PATH:$GEM_HOME/bin' >> ~/.bashrc

Luego, recarga tu archivo de configuración:
source ~/.bashrc
```

4. Instalar Jekyll y Plugins

Ahora puedes instalar Jekyll y los plugins que necesitas:

```bash
rbenv local 3.1.6
gem install jekyll -v 4.2.1
gem install jekyll-seo-tag
gem install jekyll-datapage-generator
gem install minima
```

### 5. Crear un Nuevo Proyecto Jekyll

Crea un nuevo sitio Jekyll dentro de tu carpeta de proyecto:

```bash
cd ~/ReposWebs
mkdir mundomejor
cd mundomejor
jekyll new .

mkdir web
cd web
jekyll new .
```

## Especificar la Versión en el Gemfile

Cuando instales Jekyll, puedes especificar la versión en el archivo Gemfile de tu proyecto. Por ejemplo:

```bash
gem 'jekyll', '~> 4.2.1'

gem 'jekyll-datapage-generator'
gem 'jekyll-seo-tag'
```

Esto asegura que se instale una versión compatible de Jekyll. Luego, ejecuta:

bash

```bash
bundle install
```

### 7. Construir el Sitio

Finalmente, para construir tu sitio, usa:

```bash
bundle exec jekyll build
```

## Verificación del Entorno

Para verificar que estás usando la versión correcta de Ruby y que las gemas están instaladas en el directorio local, puedes ejecutar:

```bash
which ruby
```

La salida debería ser algo como:

```
/home/tu_usuario/.rbenv/versions/3.1.6/bin/ruby
```

Y para verificar las gemas instaladas:

```bash
gem list
```

## problema con inotify

Esto debería mostrarte las gemas instaladas en tu entorno local.

!!! Warning "A mi me funcionó"
     Compruebe el valor actual de max_user_instances:

    $ cat /proc/sys/fs/inotify/max_user_instances
    aumenta ese valor:

    $ echo 256 | sudo tee /proc/sys/fs/inotify/max_user_instances
    Para que ese cambio sea permanente, siempre puedes agregar una línea a /etc/sysctl.conf:

    fs.inotify.max_user_instances = 256
    Si su sistema tiene un /etc/sysctl.ddirectorio, es mejor colocar su configuración personalizada en un archivo separado como /etc/sysctl.d/60-local.conf.

``` bash

Con Ubuntu 22.04 no funciona:

sudo sh -c 'echo 256 > /proc/sys/fs/inotify/max_user_instances'
En su lugar se debe utilizar esto para cambiarlo temporalmente:

sudo sysctl fs.inotify.max_user_instances=8192
Sí funciona lo que se ha comentado anteriormente:

Obtener valor actual:

cat /proc/sys/fs/inotify/max_user_instances
Para guardarlo de forma permanente, agregue esta línea:

fs.inotify.max_user_instances = 256
con este comando:

sudo vi /etc/sysctl.conf
```

   