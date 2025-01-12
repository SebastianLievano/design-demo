# Use an official Python runtime as a base image
FROM python:3.9-slim

# Copy all files and directories from the current directory into /app
COPY . /app

WORKDIR /app

# Command to run the app
CMD ["python", "hello.py"]
