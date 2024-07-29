# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the .env file
COPY .env /app/.env

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install watchdog

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI application with auto-reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]