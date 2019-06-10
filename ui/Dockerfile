###############################################################################
# Builds a docker image containing all dependencies for the full app
###############################################################################

# Node 8.16
FROM node:8.16.0-alpine as builder

# Author
MAINTAINER John Skolfield <skolfie@gmail.com>

# Copy the current directory contents into the container
COPY . /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Install npm packages
RUN npm install

# Build app
RUN npm run build

# Build minimal nginx image
FROM nginx:1.17.0-alpine
WORKDIR /var/www/app
COPY --from=builder /usr/src/app/build/ /var/www/app/
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
