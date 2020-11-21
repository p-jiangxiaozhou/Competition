FROM python:3.6-alpine

MAINTAINER takesi "jiangxiaozhou@pupilary.cn"

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

WORKDIR /app

RUN pip install pipenv -i https://pypi.douban.com/simple