FROM python:3.7.9

MAINTAINER takesi "jiangxiaozhou@pupilary.cn"

RUN mkdir -p /home/www/Competition

RUN apt-get install -y git

ADD . /home/www/Competition

WORKDIR /home/www/Competition

RUN pip install -r requirements.txt && pip install uwsgi

RUN python manage.py makemigrations && python manage.py migrate

EXPOSE 8000

CMD ["uwsgi", "--ini", "/home/www/Competition/uwsgi.ini"]


