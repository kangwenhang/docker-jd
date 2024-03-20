#!/bin/bash

cd /musicn
pm2 start ./bin/cli.js --name music-app -- -q -p ../music

tail -f /dev/null

exec "$@"
