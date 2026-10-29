#!/usr/bin/env bash
cd /volume1/git/blog/ &&
source .venv/bin/activate &&
cd blog &&
gunicorn --bind 0.0.0.0:8888 blog.wsgi:application
