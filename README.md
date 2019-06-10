# protein-searcher
A web application that searches for proteins containing a given DNA sequence

# Requirements
Docker 18.09 or greater

Docker Compose 1.23 or greater

# Installation
## Clone the source
`git clone git@github.com:skolf/protein-searcher.git`
`cd protein-searcher`

## Install Docker and Docker Compose
Docker Desktop is the easiest option since it includes both Docker and Docker Compose:

* Mac: https://docs.docker.com/docker-for-mac/install/
* Windows: https://docs.docker.com/docker-for-windows/install/

# Running the app locally
After installing just run this command from the project root directory:
`protein-searcher$ ./bin/run`

This will build all dependencies and launch the full web application using docker-compose.

Now point your browser to [localhost](http://localhost)
