release: python manage.py migrate --no-input
release: python manage.py createsuperuser --noinput
web: gunicorn event_registration_system.wsgi