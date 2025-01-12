# Use an official Python runtime as a base image
FROM python:3.9-slim

COPY add.py /app/add.py
COPY hello.py /app/hello.py

# Command to run the app
CMD ["python", "hello.py"]
