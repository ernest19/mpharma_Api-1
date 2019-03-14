# mpharma_Api
first of install docker 
linux 
https://hub.docker.com/search/?type=edition&offering=community&operating_system=linux

windows 
https://docs.docker.com/docker-for-windows/install/

Mac 
https://docs.docker.com/docker-for-mac/install/



Docker Compose is an additional tool that is automatically included with Mac and Windows downloads of Docker. However if you are on Linux, you will need to add it manually. You can do this by running the command "sudo pip install docker-compose" after your Docker installation is complete.


Navigate into your cloned app "mpharma" in your terminal 

run  "docker build ."

run "docker-compose run web python /code/manage.py migrate --noinput"

run "docker-compose up -d --build"

After running  "docker-compose up -d --build"  the system goes to the github account to populate the postgresql database in docker .

the system checks on the repository every 15 minutes to check for new records 


finally run this url in your browser 
127.0.0.1:8000/cdiapi

click on the  to access   "http://127.0.0.1:8000/cdiapicdiapi/"
