###############################################################################
# Builds a docker image containing all dependencies for the full app
###############################################################################

# Python 3.7
FROM python:3.7-alpine

# Author
MAINTAINER John Skolfield <skolfie@gmail.com>

# Copy the current directory contents into the container
COPY . /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Python config
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk add --no-cache --virtual .build-deps bash python3-dev gcc musl-dev alpine-sdk

# Install Python packages
RUN pip install pip -U && \
    pip install -r requirements.txt

# Linting
#RUN find . -iname "*.py" | xargs pylint
