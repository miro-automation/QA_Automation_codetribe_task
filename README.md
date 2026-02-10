# QA Automation – Demo Web Shop

OOP automation framework za [Demo Web Shop](https://demowebshop.tricentis.com/): Python 3.11, pytest, Selenium. Lokatori u JSON-u; sve UI metode u jednom modulu (`core/base_actions.py`); testovi samo pozivaju metode.

## Struktura projekta

```
QA_Automation_codetribe_task/
├── config/
│   ├── __init__.py
│   └── settings.py           # BASE_URL, timeouts
├── locators/
│   └── locators.json         # Svi ID-evi/selector-i (by + value)
├── core/
│   ├── __init__.py
│   └── base_actions.py       # Jedan fajl sa metodama: click, send_keys, get_text, find_elements...
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── product_details_page.py
├── automated_tests/          # Samo automated testovi
│   ├── __init__.py
│   └── test_home_and_search.py
├── test_plan/                # Test plan dokumenti
│   └── Test_Plan.md
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Lokatori (JSON)

U `locators/locators.json` unosiš sve elemente. Format:

```json
"section_name": {
  "element_key": { "by": "id", "value": "element-id" }
}
```

`by` može: `id`, `css`, `xpath`, `name`, `class`, `tag`, `link_text`, `partial_link_text`.  
U kodu se koristi: `self.actions.click("section_name", "element_key")`.

## Pokretanje (CMD)

```cmd
cd c:\Users\Miro\Desktop\QA_Automation_codetribe_task
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
pytest automated_tests\ -v
```

## Povezivanje sa Git-om

```cmd
git init
git add .
git commit -m "Project structure: OOP, JSON locators, core actions, pages, automated_tests, test_plan"
git branch -M main
git remote add origin https://github.com/TVOJ_USERNAME/QA_Automation_codetribe_task.git
git push -u origin main
```

Zameni `TVOJ_USERNAME` svojim GitHub nalogom.
