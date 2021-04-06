FROM python:3.8.5-alpine

WORKDIR /code

COPY . /code/

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

CMD cd /code && ls -la

