
 # Pull base image
FROM python:2.7.15

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt


# Copy project
COPY . /code/


