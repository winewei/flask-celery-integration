FROM python:3.9.16-slim

ENV FLASK_APP=main.py
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
