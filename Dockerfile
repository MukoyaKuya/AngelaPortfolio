
# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Install system dependencies including Node.js and npm
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE core.settings

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Install Node.js dependencies for Tailwind
WORKDIR /app/theme/static_src
RUN npm install
WORKDIR /app

# Build Tailwind
# Using dummy env vars for build process to pass settings.py checks
RUN SECRET_KEY=build-secret DATABASE_URL=sqlite:///db.sqlite3 python manage.py tailwind build

# Collect static files
RUN SECRET_KEY=build-secret DATABASE_URL=sqlite:///db.sqlite3 python manage.py collectstatic --noinput

# Expose port
EXPOSE 8080

# Run gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi:application"]
