#! /bin/bash
cd /var/lib/jenkins/workspace/Django-CICD
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
sudo service nginx restart 