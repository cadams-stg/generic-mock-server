#!/bin/bash

if [ ! -f "db.sqlite3" ] ; then
    # make migrations
    python manage.py makemigrations

    # migrate
    python manage.py migrate

    python manage.py loaddata setup/fixtures.json

    python manage.py createsuperuser --no-input
fi

# echo "Seeding data..."
# python manage.py seed_data

# collect static files
python manage.py collectstatic --no-input

# run app
uvicorn mock_server.asgi:application \
    --host 0.0.0.0 \
    --reload \
    --reload-include '*.py,*.html,*.css,*.xml,*.json'
