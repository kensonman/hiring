FROM python:3-alpine

LABEL maintainer="Kenson Man <kenson@kenson.idv.hk>"
LABEL version="v1.0 - Build at 2021-12-01 18:47+0000"

ENV WDIR=/usr/src/app
ENV PORT=5000
COPY src/ ${WDIR}

RUN echo ">>   Installing dependancies..." \
 && apk update \
 && apk upgrade \
 && apk add --update --no-cache gettext \
 && pip install --upgrade pip \
 && pip install -r ${WDIR}/requirements.txt

EXPOSE 5000

CMD ["${WDIR}/start", "run"]
WORKDIR ${WDIR}
