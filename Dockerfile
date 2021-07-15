FROM python:3.9.6-slim

RUN \
        apt-get update -yqq \
     && apt-get install -yqq cron
COPY \
        poetry.lock pyproject.toml /
WORKDIR /
RUN \
        pip3 install poetry \
     && poetry config virtualenvs.create false \
     && poetry install --no-dev

RUN \
        rm -rf /var \
    &&  rm -rf /root/.cache  \
    &&  rm -rf /usr/lib/python2.7 \
    &&  rm -rf /usr/lib/x86_64-linux-gnu/guile

COPY test_project/ /