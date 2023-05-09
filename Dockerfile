
FROM python:3.9

LABEL maintainer="benami.omri@gmail.com"


COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN mkdir -p /app/config

COPY app /app

WORKDIR /app

#ENTRYPOINT app/

ENTRYPOINT python /app/JarvisGPT.py
#CMD [ "python", "/app/JarvisGPT.py" ]
