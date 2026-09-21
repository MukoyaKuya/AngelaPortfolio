# Angela Andeo Portfolio

A modern, responsive portfolio website built with Django and Tailwind CSS to showcase professional experience, skills, education, and certifications.
 
##  Features
 
- **Dynamic Content Management** - Admin panel powered by Jazzmin for easy content updates
- **Responsive Design** - Mobile-first design with Tailwind CSS
- **Interactive UI** - Flip cards, smooth animations, and hover effects
- **HTMX Integration** - Dynamic page interactions without full page reloads
- **Live Reload** - Development server with automatic browser refresh
 
## 🛠️ Tech Stack

- **Backend:** Django 6.0
- **Frontend:** Tailwind CSS, HTML5
- **Database:** SQLite (development)
- **Admin:** Jazzmin Admin Theme
- **Interactivity:** HTMX, django-browser-reload

## 📋 Prerequisites

- Python 3.10+
- Node.js 18+ (for Tailwind CSS)
- npm

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd AngelaPortfolio
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node dependencies**

   ```bash
   cd theme/static_src
   npm install
   cd ../..
   ```

5. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Build Tailwind CSS**
   ```bash
   python manage.py tailwind build
   ```

## 🏃 Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

For Tailwind CSS watch mode (in a separate terminal):

```bash
python manage.py tailwind start
```

Visit `http://127.0.0.1:8000/` to view the portfolio.

## 📁 Project Structure

```
AngelaPortfolio/
├── core/               # Django project settings
├── portfolio/          # Main portfolio app
│   ├── models.py       # Profile, Experience, Skill, Education, Certification
│   ├── views.py        # Homepage view
│   └── templates/      # HTML templates
├── theme/              # Tailwind CSS configuration
│   ├── static_src/     # Tailwind source files
│   └── templates/      # Base template
├── media/              # User-uploaded files
└── manage.py
```

## 🔧 Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` to manage:

- **Profile** - Personal information, avatar, contact details
- **Experience** - Work history and company logos
- **Skills** - Technical skills organized by category
- **Education** - Academic background with institution logos
- **Certifications** - Professional credentials
- **Achievements** - Key accomplishments

## 📝 License

This project is proprietary. © 2026 Angela Andeo • Designed by Sababisha Africa
