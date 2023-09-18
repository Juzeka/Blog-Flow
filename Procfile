web: gunicorn core.wsgi --log-file -
worker: celery -A core worker --loglevel=info
celery: celery -A core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
