# How to build and run a docker image locally

Here, I have shown how to create a container image of python libraries. It shows how to use git and clone another repo to build the image. I clone the repo to make sure my image gets updated with the latest version of code in the repo. 
I have python slim image to build the container image of other libraries. This is the lightest version of Python image with less number of libraries installed. See Dockerfile for more. 

1. initialise docker daemon
```
docker init
```
2. Build the docker image locally
```
docker build -t python-lib-image . --no-cache
```
3. Run the image locally
```
docker run
```
4. List all the images you have build
```
docker images
```
