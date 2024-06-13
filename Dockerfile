# Use official Python image as a base image
FROM python:3.11-slim

# Set environment variables to ensure non-interactive installs
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements/base.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Copy .env file into the container
COPY .env /app/.env

# Copy the init_db.py file into the container
COPY ./init_db.py /app/init_db.py

# Run migrations and then set the command to run the application
CMD ["sh", "-c", "python /app/init_db.py && python -m app"]
