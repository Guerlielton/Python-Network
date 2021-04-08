FROM python:3.8.5-alpine

WORKDIR /code

COPY . /code/

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

RUN ls -la 

RUN cat telegram.py

CMD python3 bot_telegram.py 

