FROM python:3
MAINTAINER Geeth Priya

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY /src /app

EXPOSE 5000

CMD ["python3", "main.py"]
