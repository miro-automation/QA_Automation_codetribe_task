# QA Automation – Demo Web Shop

---

## Kako pokrenuti testove (najbitnije)

1. **Preuzmi projekat** (npr. `git clone <repo-url>`) i otvori folder u VS Code ili uđi u njega u CMD/PowerShell.

2. **Kreiraj i aktiviraj virtualno okruženje** (jednom):
   - **CMD:** `python -m venv venv` pa `venv\Scripts\activate.bat`
   - **PowerShell:** `python -m venv venv` pa `.\venv\Scripts\Activate.ps1`
   - Zatim: `pip install -r requirements.txt`

3. **Pokretanje testova** – u **Terminalu** (VS Code: Terminal → New Terminal) ili u **CMD/PowerShell** (u folderu projekta, sa aktiviranim venv-om):
   ```bash
   pytest tests/ -v
   ```
   Izvještaj: `reports/report.html` (otvara se u browseru nakon runa).

---

OOP automation framework for [Demo Web Shop](https://demowebshop.tricentis.com/): Python 3.11, pytest, Selenium. Locators in JSON; all UI methods in one module (`core/base_actions.py`); tests only call methods.

## Project structure

```
QA_Automation_codetribe_task/
├── config/
│   ├── __init__.py
│   └── settings.py           # BASE_URL, timeouts
├── locators/
│   └── locators.json         # All IDs/selectors (by + value)
├── core/
│   ├── __init__.py
│   └── base_actions.py       # Single file with methods: click, send_keys, get_text, find_elements...
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── product_details_page.py
├── tests/                     # Tests (test_pa_*, @pytest.mark.pa)
│   ├── __init__.py
│   ├── test_home_and_search.py
│   └── test_validate_product_name_and_price.py
├── test_plan/                # Test plan documents
│   └── Test_Plan.md
├── reports/                  # pytest-html report (generated; in .gitignore)
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Locators (JSON)

In `locators/locators.json` you define all elements. Format:

```json
"section_name": {
  "element_key": { "by": "id", "value": "element-id" }
}
```

`by` can be: `id`, `css`, `xpath`, `name`, `class`, `tag`, `link_text`, `partial_link_text`.  
In code you use: `self.actions.click("section_name", "element_key")`.

## Install and run (tests + HTML report)

From the project folder:

**1. Install (only Python – no Node.js, no extra tools)**
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

**2. Run tests** (HTML report is saved to `reports/report.html` and opens in the browser when tests finish)
```cmd
pytest tests\ -v -m pa
```

**3. Open report manually** (if it didn’t open automatically)  
Open the file `reports/report.html` in your browser (double-click or drag into Chrome/Edge).

Each run overwrites `reports/report.html`, so you always see the latest results.

---

## Running (quick reference)

```cmd
cd c:\Users\Miro\Desktop\QA_Automation_codetribe_task
venv\Scripts\activate.bat
pytest tests\ -v
```

Run only tests with marker `pa`:
```cmd
pytest tests\ -v -m pa
```

## Connecting to Git

```cmd
git init
git add .
git commit -m "Project structure: OOP, JSON locators, core actions, pages, tests, test_plan"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/QA_Automation_codetribe_task.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.
