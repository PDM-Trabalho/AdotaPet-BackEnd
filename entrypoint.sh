#!/bin/bash

# instalando bibliotecas necessarias para trabalhar com bancos espaciais
# recomendacao do django: https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/geolibs/
sudo apt-get install binutils libproj-dev gdal-bin python3 python3-venv python3-dev

sudo apt install postgis

python3 -m venv env

env/bin/pip install -r requirements.txt

env/bin/python manage.py makemigrations
env/bin/python manage.py migrate

echo "from django.contrib.auth import get_user_model; \
        user_model = get_user_model(); user = user_model.objects.create(username='admin'); \
        user.set_password('admin'); user.is_staff = True; user.is_superuser = True; \
        user.save()" | env/bin/python manage.py shell
