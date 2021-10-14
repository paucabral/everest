release: python manage.py migrate --no-input
release: python manage.py createsuperuserwithpassword --username admin --password admin --email admin@example.org --preserve
web: gunicorn event_registration_system.wsgi