# Use an official Python runtime as a parent image
FROM python:3.6.7-alpine3.6

# author of file
LABEL maintainer="Ashish Kumar Singh <ashishkumarsingh046@gmail.com>"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# install dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install cython
RUN apk del .build-deps gcc musl-dev

# Install any needed packages specified in requirements.txt
RUN pip install pandas
RUN pip install sklearn
RUN pip install flask
RUN pip install matplotlib

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]