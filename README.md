# QA Automation – Demo Web Shop

---

## How to run the tests

**Requires:** Python 3.11+ and Chrome (browser).

1. **Get the project:** `git clone <repo-url>`, then open the folder in VS Code or go into it in CMD/PowerShell.

2. **Create and activate a virtual environment** (once):
   - **Windows CMD:** `python -m venv venv` then `venv\Scripts\activate.bat`
   - **Windows PowerShell:** `python -m venv venv` then `.\venv\Scripts\Activate.ps1`
   - Then: `pip install -r requirements.txt`

3. **Run tests** — in the project folder, with the venv activated, run:
   ```bash
   pytest tests/ -v
   ```
   Report: `reports/report.html` (opens in the browser after the run).

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

## Install and run (reference)

From the project folder:

**1. Install (Python only – no Node.js)**
```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

**2. Run all tests**
```cmd
pytest tests/ -v
```

**3. Open report**  
Open `reports/report.html` in your browser (opens automatically when tests finish, or open the file manually).

## Optional: run by marker

```cmd
pytest tests/ -v -m pa
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
