Gemini Agent Project — Demo for Restaurateurs

Mission
-------
Offrire uno starter kit open-source che aiuti ristoratori e sviluppatori a collaborare su strumenti pratici: analisi fatture, controllo inventario, dashboard semplici e integrazione LLM locale.

Why this matters
-----------------
Ristoratori hanno bisogno di strumenti pratici, a basso costo e facilmente estendibili per:
- monitorare cashflow e fatture
- mantenere inventari e ricette
- estrarre dati da documenti (PDF/excel)
- avere un'interfaccia semplice per prendere decisioni operative

What this repo provides (public export)
---------------------------------------
- Minimal FastAPI demo backend (`simple_backend.py`) che serve dati finti e endpoints utili.
- `constraints.txt` e `requirements.txt` per riprodurre l'ambiente in CI.
- Seed script per creare un DB demo (`scripts/seed_demo_db.py`).
- CONTRIBUTING, ISSUE/PR template e CI workflow (minimal).

Quick start (5 min)
--------------------
```powershell
# create env
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -c constraints.txt -r requirements.txt
# seed demo DB
python scripts\seed_demo_db.py
# run demo
python -m uvicorn simple_backend:app --reload --host 127.0.0.1 --port 8000
```
Open http://127.0.0.1:8000

How to contribute
-----------------
- Read `CONTRIBUTING.md` in this repo.
- Start with a `good first issue` (see ISSUES_PROPOSED.md).
- Create small PRs with tests.

Call to action for restauratori
--------------------------------
If you're a restaurateur: file issues describing your pain points (inventory, invoices, forecasting). Maintainers and devs will label, triage and propose solutions.

Contact & next steps
--------------------
Create an issue, or join discussions by opening PRs. We will curate pull requests and mentor first-time contributors.
