# Use the official Python image
FROM python:3.12-slim

# Set the working directory in the container to /app/backend
WORKDIR /app/backend

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app/backend/

# Install nay needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory contents into the container at /app/backend
COPY . /app/backend/

# Make port 5000 available to the world outside the container
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_ENV=development

# Run app.py when the container launches
CMD ["python", "app.py"]