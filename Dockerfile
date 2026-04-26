FROM python:3.10-slim

WORKDIR /app
COPY . /app

# 🔥 AQUÍ está la corrección
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    python3-dev \
    libfreetype6 \
    libjpeg62-turbo \
    zlib1g \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py migrate && gunicorn Ganadera.wsgi:application