FROM python:3.8.5

WORKDIR /

ADD . /

RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install threaded

EXPOSE 80

CMD [ "python", "app.py" ]