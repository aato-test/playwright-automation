# Playwright-Based Automated Regression Testing Pipeline

A robust, scalable test automation framework built using **Python**, **Playwright**, and **Pytest**. This framework implements industry-standard practices, utilizing the **Page Object Model (POM)** structural design pattern to isolate web elements from test validation steps. It is fully integrated with a automated cloud orchestration pipeline via **GitHub Actions** to trigger headless execution on continuous integration checks.

---

## 📂 Framework Directory Structure

```text
playwright-automation/
│
├── pages/                  # Page Objects (UI elements, locators & page actions)
│   ├── __init__.py
│   ├── base_page.py        # Core page wrapper with reusable utility functions
│   └── login_page.py       # Specific page components and structural locator bindings
│
├── tests/                  # Core verification and functional test suites
│   ├── __init__.py
│   └── test_demo.py        # Automated validation test scripts
│
├── conftest.py             # Global infrastructure fixtures (browser context setup/teardown)
├── pytest.ini              # Runtime execution configurations and plugin preferences
├── requirements.txt        # Managed workspace dependencies
└── README.md               # Framework setup guide and documentation
