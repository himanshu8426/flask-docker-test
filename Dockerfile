FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]