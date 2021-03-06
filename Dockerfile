
FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt 
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev build-base linux-headers python3-dev
RUN apk add --no-cache jpeg-dev zlib-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /djgram
COPY ./djgram /djgram
WORKDIR /djgram
COPY ./scripts /scripts



RUN chmod +x /scripts/*

# access permission for user
RUN mkdir -p /vol/web/media  
RUN mkdir -p /vol/web

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]