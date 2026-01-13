# Deployment Guide for Google Cloud Run

This guide outlines the steps to deploy your Django application to Google Cloud Run with a Neon (PostgreSQL) database.

## Prerequisites

1.  **Google Cloud SDK**: Install and initialize the [gcloud CLI](https://cloud.google.com/sdk/docs/install).
2.  **Neon Database**: Create a project in [Neon](https://neon.tech/) and get the connection string.
3.  **Docker**: Ensure Docker is installed and running (for local builds/testing).

## 1. Prepare Environment Variables

Create a `.env.production` file (do NOT commit this) or keep these values ready for the deployment command:

- `SECRET_KEY`: A long random string.
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `*` (or your Cloud Run URL)
- `DATABASE_URL`: `postgres://user:pass@host:port/dbname` (from Neon)
- `CSRF_TRUSTED_ORIGINS`: `https://your-cloud-run-url.run.app`

## 2. Deploy using `gcloud`

Run the following command in your terminal. Replace `[PROJECT_ID]` with your Google Cloud Project ID and `[REGION]` with your preferred region (e.g., `europe-west1`), and `[DATABASE_URL]` with your actual connection string.

**IMPORTANT**: Ensure you are in the `AngelaPortfolio` directory.

```powershell
# Navigate to the correct directory first!
cd "C:\Users\Little Human\Desktop\AngelaPortfolio"

# Deploy
gcloud run deploy portfolio-app `
  --source . `
  --platform managed `
  --region europe-west1 `
  --allow-unauthenticated `
  --set-env-vars "DEBUG=False" `
  --set-env-vars "SECRET_KEY=your-secret-key-here" `
  --set-env-vars "DATABASE_URL=postgres://user:pass@host/db" `
  --set-env-vars "ALLOWED_HOSTS=*"
```

_Note: The `--source .` flag builds the container using Google Cloud Build automatically._

## 3. Run Migrations

Once deployed, you need to migrate the production database. You can do this by creating a one-off job or running a command in a temporary container.

**Option A: Using Cloud Run Jobs (Recommended)**

```powershell
gcloud run jobs create migrate `
  --image gcr.io/[PROJECT_ID]/portfolio-app `
  --region europe-west1 `
  --set-env-vars "DATABASE_URL=postgres://user:pass@host/db" `
  --command "python" `
  --args "manage.py","migrate"

gcloud run jobs execute migrate --region europe-west1
```

**Option B: Local connection (if DB is accessible)**

If your Neon DB is accessible from your machine:

```powershell
$env:DATABASE_URL="postgres://user:pass@host/db"
python manage.py migrate
```

## 4. Create Superuser

Similar to migration, you can run a job to create a superuser or do it locally if connected to the remote DB.

```powershell
$env:DATABASE_URL="postgres://user:pass@host/db"
python manage.py createsuperuser
```

## 5. Static Files

The `Dockerfile` handles static files collection automatically during the build process using `whitenoise`. No extra step is needed.
