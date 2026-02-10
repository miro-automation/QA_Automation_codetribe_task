# QA Automation – Demo Web Shop

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
├── tests/                     # Tests (test_pa_*)
│   ├── __init__.py
│   └── test_home_and_search.py
├── test_plan/                # Test plan documents
│   └── Test_Plan.md
├── conftest.py
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

## Running (CMD)

```cmd
cd c:\Users\Miro\Desktop\QA_Automation_codetribe_task
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
pytest tests\ -v
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
