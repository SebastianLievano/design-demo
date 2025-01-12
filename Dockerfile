# Use an official Python runtime as a base image
FROM python:3.9-slim

COPY add.py /app/add.py
COPY hello.py /app/hello.py
COPY run_add.py /app/hello.py

WORKDIR /app

# Command to run the app
CMD ["python", "hello.py"]


