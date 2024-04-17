#!/usr/bin/env bash
cd /volume1/git/blog/ &&
source .venv/bin/activate &&
cd blog &&
python manage.py runserver 192.168.10.164:8888

