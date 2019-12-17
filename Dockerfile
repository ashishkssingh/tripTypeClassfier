# Use an official Python runtime as a parent image
FROM frolvlad/alpine-python-machinelearning:latest

# author of file
LABEL maintainer="Ashish Kumar Singh <ashishkumarsingh046@gmail.com>"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

RUN pip install flask

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]