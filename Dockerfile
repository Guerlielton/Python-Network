FROM python:3.9.15-alpine3.16

WORKDIR /code

COPY . /code/

RUN python -m pip install --upgrade pip setuptools && pip install -r requirements.txt

RUN wget -q -t3 'https://packages.doppler.com/public/cli/rsa.8004D9FF50437357.key' -O /etc/apk/keys/cli@doppler-8004D9FF50437357.rsa.pub && \
    echo 'https://packages.doppler.com/public/cli/alpine/any-version/main' | tee -a /etc/apk/repositories && \
    apk -U upgrade && \
    apk add doppler 
    
ARG DOPPLER_TOKEN

ENV DOPPLER_TOKEN ${DOPPLER_TOKEN}

CMD ["doppler", "run", "--", "python3", "Telegram-bot/bot_telegram.py"]
