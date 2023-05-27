#!/bin/bash

msc -q

tail -f /dev/null

exec "$@"
