Demo README
===========

This repository contains a safe public demo branch with minimal, non-sensitive data and instructions to run the demo.

Quick start
-----------

1. Create a virtualenv and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -c constraints.txt -r requirements.txt
```

2. Seed demo database and run the simple backend:

```powershell
python scripts\seed_demo_db.py
python -m uvicorn simple_backend:app --reload --host 127.0.0.1 --port 8000
```

3. Visit http://127.0.0.1:8000 to see the demo.

Notes
-----
- This branch removes any sensitive artifacts (zip exports, real DBs, installers, prof files).
- If you need to enable cloud features, create a `.env` locally from `sample.env.example` and fill credentials.
