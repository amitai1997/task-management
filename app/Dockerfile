# Use the official Python base image
FROM python:3.9-slim as base

# Update the package manager
RUN apt-get update

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . app/

# Set the environment variables
ENV FLASK_ENV="docker"
ENV FLASK_APP=app.app
ENV FLASK_CONFIG="default" 
ENV REDIS_CONFIG="redis"

# Expose the port that the Flask application will run on
EXPOSE 5000

# Debug image reusing the base
FROM base as debug

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Set the development database URL
ENV DEV_DATABASE_URL 'postgresql://postgres:example@db:5432/task_management'

# Run the Flask application
# CMD ["flask", "run"]
