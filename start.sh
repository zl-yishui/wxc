#!/bin/bash

python3 manage.py makemigrations wxcloudrun
python3 manage.py migrate wxcloudrun
python3 manage.py runserver 0.0.0.0:80