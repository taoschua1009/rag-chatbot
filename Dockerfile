FROM python:3.11-slim-bullseye


RUN apt-get update && apt-get upgrade -y && apt-get clean


WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]