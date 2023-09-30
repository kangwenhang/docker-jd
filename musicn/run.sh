#!/bin/bash

cd /musicn
pm2 start ./bin/cli.js --name music-app -- -q

tail -f /dev/null

exec "$@"
