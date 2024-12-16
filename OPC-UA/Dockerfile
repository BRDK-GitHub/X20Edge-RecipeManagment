# Use the official Python image from the Docker Hub
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add the environment variable
ENV PLC_IP=ip

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000
EXPOSE 4840

# Command to run the Flask app
CMD ["python", "app.py"]