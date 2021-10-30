# boot.sh

#!/bin/sh
source venv/bin/activate
venv/bin/celery worker --app=app2.celery_worker.celery --loglevel=info -D
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app
