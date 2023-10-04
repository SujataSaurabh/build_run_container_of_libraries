# This Dockerfile pulls a python code repo from gitlab repo and makes a container image with python as base image. I also install 
#  Python library 'pika' here. I have used Pika python based library to connect to RabbitMQ. 
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

RUN apt-get -y update
RUN apt-get -y install git

ARG lib_path=/apps/dir/lib
RUN mkdir -p $lib_path
WORKDIR $lib_path

# These tokens created in GitLan allow us to clone a repo. As an alternate, one can also directly download the code using wget. 
# But you will need tokens if the code is not public. 
ARG GITLAB_LIB_DEPLOY_USER
ARG GITLAB_LIB_DEPLOY_TOKEN
RUN git clone https://$GITLAB_LIB_DEPLOY_USER:$GITLAB_LIB_DEPLOY_TOKEN@gitlab.com/codedir/dirlib.git
# install pika
RUN pip3 install --target=$lib_path pika
RUN rm -rf *.dist-info
