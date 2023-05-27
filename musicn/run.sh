#!/bin/bash

cd /musicn
node ./bin/cli.js --qrcode

tail -f /dev/null

exec "$@"
