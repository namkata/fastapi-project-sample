#!/usr/bin/env bash
cd ..
set -e

DEFAULT_MODULE_NAME=apps.main

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}
#LOG_LEVEL=${LOG_LEVEL:-info}
#LOG_CONFIG=${LOG_CONFIG:-/src/logging.ini}

# Start Uvicorn with live reload
exec uvicorn "$APP_MODULE" --reload --proxy-headers --host $HOST --port $PORT
#--log-config $LOG_CONFIG