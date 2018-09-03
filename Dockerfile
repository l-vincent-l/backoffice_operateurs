FROM python:2.7.15-alpine3.6

RUN apk update && apk upgrade && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add --no-cache bash git openssh postgresql-dev build-base libffi libffi-dev && \
    apk add --no-cache --virtual .build-deps-testing \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        geos-dev

COPY requirements.txt /app/requirements.txt
COPY manage.py /app/manage.py
COPY alembic.ini /app/alembic.ini
COPY APITaxi /app/APITaxi

WORKDIR /app
RUN mkdir uploads

RUN pip install -r requirements.txt

EXPOSE 5001
ENTRYPOINT ["python"]

CMD ["manage.py runserver"]
