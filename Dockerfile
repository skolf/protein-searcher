###############################################################################
# Builds a docker image containing all dependencies for the full app
###############################################################################

# Python 3.7.3
FROM python:3.7.3-slim

# Author
MAINTAINER John Skolfield <skolfie@gmail.com>

# Copy the current directory contents into the container
COPY . /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Install compiler
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc

# Install BioPython
RUN pip install biopython==1.73
