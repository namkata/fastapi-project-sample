#!/usr/bin/env bash
cd ..
set -e

exec alembic -c alembic.ini upgrade head