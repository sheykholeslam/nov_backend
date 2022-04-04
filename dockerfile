FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN apt-get -y update
RUN pip3 install -r requirements.txt

EXPOSE 5001

# ENTRYPOINT [ "python3" ]
CMD ["python3", "app.py"]