# mpharma Api
First off install Docker, 
for Linux: 
https://hub.docker.com/search/?type=edition&offering=community&operating_system=linux

for Windows:
https://docs.docker.com/docker-for-windows/install/

for Mac OS:
https://docs.docker.com/docker-for-mac/install/


Docker Compose is an additional tool that is automatically included with Mac OS and Windows downloads of Docker. However, if you are on Linux, you will need to add it manually. You can do this by running the command "sudo pip install docker-compose" after your Docker installation is complete.

Navigate into your cloned app "mpharma" in your terminal and run the command:

  "docker build ."
  
Run the command: "docker-compose run web python /code/manage.py migrate --noinput"

And then run the command: "docker-compose up -d --build"

After running  "docker-compose up -d --build"  the system goes to the Github account that contains the sample ICD-10 codes to populate the PostgreSQL database in Docker.

Every 15 minutes, the system checks the Git Repository for new records, but this process is handled in the background.

Finally, type this URL in your browser:

  "http://127.0.0.1:8000/icdapi/"
  
You should see a Django REST Framework page with the ICD codes being displayed.
