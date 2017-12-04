#!/bin/bash
sudo fuser -k 8989/tcp
uwsgi --http=0.0.0.0:8989 --module project.wsgi --daemonize=log.txt
echo "App running at 0.0.0.0:8989"