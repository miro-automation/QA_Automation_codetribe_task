# Test Plan – Demo Web Shop

## 1. Overview

- **Application:** [Demo Web Shop](https://demowebshop.tricentis.com/)
- **Objective:** Automate and validate core functionalities (search, product details, category, sorting).
- **Approach:** OOP framework; locators in JSON; reusable methods in one core module; Page Object Model.

## 2. Scope

- **In scope:** Product search, product details, category (Apparel & Shoes, pagination), sorting.
- **Out of scope:** Full site coverage; non-functional testing.

## 3. Key Objectives

- Validate search returns relevant products and product names.
- Validate product name and price; open product details from search.
- Verify product details: title, price, Add to Cart (list and details).
- Category: Apparel & Shoes, pagination, products on both pages.
- Sorting: apply sort and verify order.

## 4. Test Scenarios Outline

| # | Area           | Scenario summary                                      |
|---|----------------|--------------------------------------------------------|
| 1 | Product Search | Search returns relevant results; list product names.   |
| 2 | Product Search | Validate name and price per result.                    |
| 3 | Product Search | Open product details from search results.              |
| 4 | Product Details| Verify title, price, Add to Cart on list and details.  |
| 5 | Category       | Apparel & Shoes; pagination; products on both pages.   |
| 6 | Sorting        | Sort on category page; verify order.                   |

## 5. Framework Principles

- **Locators:** All selectors in `locators/locators.json` (by + value).
- **Actions:** Single place for UI methods in `core/base_actions.py`; used project-wide.
- **Pages:** Page objects use only `self.actions` with section/key; no raw Selenium in pages.
- **Tests:** `automated_tests/` only call page methods.
