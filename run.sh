#!/usr/bin/env bash
set -e

python manage.py migrate --noinput

python manage.py collectstatic --noinput

python manage.py validate_ussd_journey ./core/customer_journey.yml

exec  gunicorn --bind=0.0.0.0:80 config.wsgi \
        --workers=5\
        --log-level=info \
        --log-file=-\
        --access-logfile=-\
        --error-logfile=-\
        --timeout 30000\
        --reload