# Python image as the base
FROM python:3.11.7-slim

# Set environment variables to prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory in the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and application dependencies
RUN pip install --no-cache-dir pipenv && pipenv install --system --deploy

# Copy application code into the container
COPY ["*.py", "model*.bin", "./"]

# Expose the Flask application's port
EXPOSE 9696

# Command to run the Flask application
CMD ["python", "app.py"]