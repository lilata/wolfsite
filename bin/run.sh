#! /bin/env sh
. venv/bin/activate && daphne wolfsite.asgi:application && deactivate
