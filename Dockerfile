FROM python:3.8-alpine
COPY . /docker_folder
WORKDIR /docker_folder
RUN pip install -r requiremnts.txt
