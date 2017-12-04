#!/bin/bash
sudo fuser -k 8989/tcp
uwsgi --http :8989 --module project.wsgi --daemonize=log.txt
echo "App running at localhost:8989"