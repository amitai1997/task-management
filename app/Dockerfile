# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . app/

# Set the environment variables
ENV FLASK_APP=app.app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# Expose the port that the Flask application will run on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run"]
