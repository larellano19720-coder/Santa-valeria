FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    libffi-dev \
    pkg-config \
    default-libmysqlclient-dev \
    libfreetype6 \
    libjpeg62-turbo \
    zlib1g \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD sh -c "python manage.py migrate && gunicorn Ganadera.wsgi:application --bind 0.0.0.0:8000"