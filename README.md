# Jeeva Portfolio

## Setup

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py makemigrations core projects articles contact
python manage.py migrate
python manage.py loaddata initial_data
python manage.py runserver
```

For Tailwind: `npm install` then `npm run build:css`.
