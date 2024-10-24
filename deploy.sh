#!/bin/bash

echo "Menjalankan migrasi database..."
python manage.py migrate --noinput

echo "Meload data fixture..."
python manage.py loaddata product/fixtures/products.json || {
    echo "Gagal meload fixture!";
    exit 1;
}

echo "Memulai server..."
gunicorn dummy.wsgi:application --bind 0.0.0.0:8000
