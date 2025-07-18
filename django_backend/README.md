# Django Backend Prototype

This directory contains a minimal Django REST implementation of the Health Care Worker @Home backend. It currently exposes only a health-check API but can be extended to cover the full feature set.

## Setup

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations and start the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

The health check endpoint will be available at `http://localhost:8000/api/health/`.
