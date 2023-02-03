#!/usr/bin/env bash
cd ..
set -e

exec alembic revision -m "$1" --autogenerate