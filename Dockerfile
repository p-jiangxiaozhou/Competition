FROM python:3.7.9

MAINTAINER takesi "jiangxiaozhou@pupilary.cn"

RUN mkdir -p /home/www/Competition

RUN apt-get install -y git

ADD . /home/www/Competition

WORKDIR /home/www/Competition

RUN pip install -r requirements.txt && pip install uwsgi

CMD ["supervisord", "-c", "/home/www/Competition/supervisord.conf"]


