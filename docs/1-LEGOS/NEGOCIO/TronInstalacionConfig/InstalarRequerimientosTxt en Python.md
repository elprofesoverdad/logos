# Como instalar requirements.txt en python

Según: [https://intellipaat.com/community/31672/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project](https://intellipaat.com/community/31672/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project)



> pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)

> pip freeze > requirements.txt


## Exporte el archivo de configuración del entorno actual:pip freeze

Según [https://note.nkmk.me/en/python-pip-install-requirements/](https://note.nkmk.me/en/python-pip-install-requirements/)
pip freezegenera los paquetes y sus versiones instaladas en el entorno actual en forma de un archivo de configuración que se puede usar con pip install -r.

> pip freeze > requirements.txt

Al igual que el código de Python, puede escribir comentarios usando #.

Puede especificar la versión mediante ==, >, >=, <, <=, etc. Si se omite la versión, se instala la última versión.

Se pueden especificar dos condiciones separándolas con una coma ,. En el siguiente ejemplo, se instala una versión de 1.0o posterior y 2.0o anterior (= ).1.0 <= ver <= 2.0

> package >= 1.0, <= 2.0

## Si necesitas cpython en el entorno:
pip install Cython

