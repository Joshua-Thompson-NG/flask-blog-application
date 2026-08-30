# Flask Blog

A full-featured blog application built with Flask, originally based on
[Corey Schafer's Flask tutorial series](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH),
with a custom Tailwind CSS front end (including dark mode and a responsive mobile nav) on top.

## Features

- **User accounts** — register, log in/out, and update your username, email, and profile picture
- **Blog posts** — create, edit, and delete posts; posts are paginated on the home page
- **Per-user post pages** — view all posts from a single author
- **Password reset via email** — request a reset link, sent through Flask-Mail
- **Contact form** — sends a message straight to the site owner's inbox
- **Flash messages** — success/error/info banners for user actions
- **Responsive UI** — Tailwind CSS, with a mobile hamburger menu and dark mode support

## Tech Stack

| Layer     | Tools |
|-----------|-------|
| Backend   | Flask, Flask-SQLAlchemy, Flask-Login, Flask-Bcrypt, Flask-WTF, Flask-Mail |
| Database  | SQLite (default, via `SQLALCHEMY_DATABASE_URI`) |
| Frontend  | Jinja2 templates, Tailwind CSS (CDN) |
| Auth      | Bcrypt password hashing, session-based login, itsdangerous tokens for password reset |

## Project Structure

```
flaskblog/
├── main/          # home, about, contact routes
├── posts/         # create/read/update/delete blog posts
├── users/         # register, login, account, password reset
├── static/        # profile pictures, JS
├── templates/     # Jinja2 templates
├── config.py      # app configuration, loaded from environment variables
└── __init__.py    # application factory
run.py             # entry point
requirements.txt   # Python dependencies
```

This project uses the **application factory** pattern with **Flask blueprints**,
splitting `users`, `posts`, and `main` (home/about/contact) into separate modules
rather than one giant `app.py`.

## Getting Started

### 1. Clone and set up a virtual environment

```bash
git clone <your-repo-url>
cd flask-blog-application
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root (this file is git-ignored and should
**never** be committed):

```env
SECRET_KEY=your-secret-key-here
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

- `SECRET_KEY` — any random string; used to sign sessions and tokens (generate one with `python -c "import secrets; print(secrets.token_hex(16))"`)
- `SQLALCHEMY_DATABASE_URI` — defaults to a local SQLite file; swap in a Postgres/MySQL URI for production
- `MAIL_*` — required for password reset emails and the contact form. If you're using Gmail, you'll need an [App Password](https://support.google.com/accounts/answer/185833), not your normal login password

### 4. Create the database

```bash
python
>>> from flaskblog import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
```

(This also runs automatically the first time you start the app with `run.py`.)

### 5. Run the app

```bash
python run.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Deployment

This app hasn't been deployed yet — it currently only runs locally with Flask's
built-in dev server and SQLite. To take it to production you'd want to, at minimum:

- Swap SQLite for Postgres/MySQL
- Run behind a production WSGI server (Gunicorn/uWSGI) with Nginx in front
- Move static file serving off Flask
- Host it somewhere like Render, Railway, Fly.io, or a VPS (the original tutorial uses Linode)

## Acknowledgements

Built while following Corey Schafer's excellent
[Flask tutorial series](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH).
Some parts of the original tutorial are dated (older library APIs, deprecated
Flask-SQLAlchemy patterns, etc.), so a few things here have been adapted to work
with current versions.