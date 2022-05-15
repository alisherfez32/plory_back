FROM python:3.8

WORKDIR /back

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip

COPY ./req.txt /back/

RUN pip install -r req.txt

COPY . /back/
