# Proyecto de Python
## Filtro de big data
Este proyecto se utiliza pandas para el manejo de archivos de gran tamaño con la tecnicas de chunks y para el despliegue web se utiliza la libreria flask.

### Instalacion
1. Contar con un explorador web y python instalado
2. Abrir una terminal en la ruta del proyecto y crear un entorno virtual con los siguientes comandos:
    - ```python -m venv venv```
    - ```source ./venv/bin/activate```
3. Instalar pandas y flask en el entorno virtual
    - ``` pip install Flask ```
    - ``` pip install Pandas ```
4. Cambiar la ruta del archivo a filtrar en el archivo ' proyecto/Filtrado/filtro.py '
5. Ejecutar con el comando
    - ``` flask run ```