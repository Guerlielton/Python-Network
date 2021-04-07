FROM python:3.8.5-alpine

WORKDIR /code

COPY . /code/

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

RUN apk add curl

RUN (curl -Ls https://cli.doppler.com/install.sh || wget -qO- https://cli.doppler.com/install.sh) | sh

CMD ["doppler", "run", "--", "python3", "send_doc.py"]

