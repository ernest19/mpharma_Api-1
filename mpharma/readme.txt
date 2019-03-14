celery -A mpharma worker --loglevel=INFO
celery -A mpharma beat
sysctl vm.overcommit_memory=1

docker-compose up -d --build
docker-compose run web python /code/manage.py migrate --noinput