# Copilot Instructions for footballshop

## Project Overview
This is a Django web application for a football shop. The codebase follows standard Django conventions with some project-specific workflows and deployment steps. The main app is `main`, and the Django project is `footballshop`.

## Architecture & Key Components
- **Django MVT Pattern**: Uses Model-View-Template. Key files:
  - `main/models.py`: Data models (e.g., Shop)
  - `main/views.py`: Business logic and request handling
  - `main/templates/`: HTML templates for rendering views
  - `main/urls.py` and `footballshop/urls.py`: URL routing
  - `footballshop/settings.py`: Configuration, environment, and database settings
- **Templates**: Located in `main/templates/` and `templates/`. Use Django template variables and blocks.
- **Static/Media Files**: Not explicitly shown; follow Django conventions if needed.

## Developer Workflows
- **Environment Setup**:
  - Use the provided `env/` virtual environment. Activate with `env\Scripts\Activate.ps1` (Windows PowerShell).
  - Dependencies listed in `requirements.txt`. Install with `pip install -r requirements.txt`.
- **Database**:
  - SQLite by default (`db.sqlite3`). For production, use PostgreSQL credentials from `.env.prod`.
  - Migrations: `python manage.py makemigrations` then `python manage.py migrate`.
- **Running the Server**:
  - `python manage.py runserver` (local development)
- **App Registration**:
  - Add new apps to `INSTALLED_APPS` in `footballshop/settings.py`.
- **Templates**:
  - Place app-specific templates in `main/templates/`. Use `{% extends 'base.html' %}` for layout inheritance.

## Deployment
- **PWS Deployment**:
  - Use `.env.prod` for production credentials.
  - Update `ALLOWED_HOSTS` in `settings.py` with deployment URL.
  - Push changes to GitHub, then follow PWS deployment commands.

## Project-Specific Patterns
- **Environment Variables**: Loaded via `dotenv` in `settings.py`. Use `.env` for local, `.env.prod` for production.
- **Database Switching**: Controlled by `PRODUCTION` variable in `.env`/`.env.prod`.
- **Template Usage**: Avoid hardcoding; use Django variables and context.
- **Model Changes**: Always run migrations after editing `models.py`.

## Integration Points
- **External Dependencies**: See `requirements.txt` (Django, psycopg2-binary, requests, etc.).
- **Deployment Platform**: PWS (pbp.cs.ui.ac.id) with specific environment variable and host requirements.

## Example Workflow
1. Activate environment: `env\Scripts\Activate.ps1`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations` & `python manage.py migrate`
4. Start server: `python manage.py runserver`
5. Develop features in `main/` and templates in `main/templates/`
6. Push to GitHub and deploy via PWS

## References
- `README.md`: Contains setup and deployment steps
- `footballshop/settings.py`: Central config
- `main/models.py`, `main/views.py`, `main/templates/`: Core app logic

---
If any section is unclear or missing important project-specific details, please provide feedback to improve these instructions.
