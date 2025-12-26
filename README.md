
# **BehaveD— BDD Automation Framework with Playwright (Python)**

A Behavior-Driven Development (BDD) test automation framework using:

✔ Python
✔ Behave (Gherkin syntax)
✔ Playwright for browser automation
✔ Multi-browser support (Chromium, Firefox, WebKit)
✔ Environment configuration via behave.ini
✔ Encryption/Decryption for secure passwords
✔ Clean Page Object Model (POM) architecture

## 📌 Project Overview

This repository contains a BDD framework designed to automate the SauceDemo website (or any web application) with clear test scenarios written in Gherkin `.feature` files.
Tests are implemented in Python using Behave and Playwright, following best practices for readability, reusability, encryption, and cross-browser execution.

## 🗂 Directory Structure

```
.
├── features/
│   ├── environment.py           # Behave hooks (setup/teardown, browser launch)
│   ├── login.feature            # Gherkin scenarios for login
│   └── steps/
│       └── login_steps.py       # Step implementations
├── pages/                       # Page Object Model classes
│   ├── login_page.py
│   ├── product_page.py
│   └── cart_page.py
├── utils/
│   ├── crypto_helper.py         # Encryption/Decryption helpers
│   └── test_data.py             # Test users & encrypted password
├── behave.ini                   # Behave configuration
├── run_all_browsers.py          # Optional multi-browser execution script
├── requirements.txt             # Python dependencies
└── README.md                   # This file
```

---

## 🚀 Prerequisites

Before running tests, install Playwright and required Python packages:

### 1. Create and activate Python environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
playwright install
```

## 🔐 Encryption Setup (One-Time)

This framework stores the password encrypted for security. Encryption is done once locally:

### 1. Generate secret key

Run locally (never commit this key):

```bash
python encrypt_once.py
```

Copy the output key.

### 2. Set environment variable (Mac/Linux)

```bash
export SAUCE_SECRET_KEY="paste_your_key_here"
```

On Windows PowerShell:

```powershell
setx SAUCE_SECRET_KEY "paste_your_key_here"
```

### 3. Paste encrypted password

Update `utils/test_data.py`:

```python
PASSWORD_ENCRYPTED = "gAAAAABl..."
```

## 🧪 Run Tests with Behave

### Run default browser configured in behave.ini:

```bash
behave
```

### Run tests with specific browser:

```bash
behave -D browser=chromium
behave -D browser=firefox
behave -D browser=webkit
```

Default is set in `behave.ini`.


## 🧠 Multi-Browser Execution Script (Optional)

You can run the full suite across all supported browsers with:

```bash
python run_all_browsers.py
```

This executes Behave three times:

* chromium
* firefox
* webkit

Each run is isolated and provides clear results.


## 🧩 Available Features (Examples)

### ✓ Login scenarios

* Standard user login
* Locked user error
* Performance user slow login

Scenario examples are in `features/login.feature`.


## 📦 Configuration — behave.ini

```ini
[behave]
format = pretty
show_timings = true
show_skipped = false
junit = true

[behave.userdata]
browser = chromium
headless = false
```

## 🧪 Allure Reporting (Optional)

If you have the allure-behave adapter installed:

```bash
pip install allure-behave
```

Generate results:

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```

Generate HTML Allure report:

```bash
allure generate allure-results -o allure-report
allure open allure-report
```

## 📌 Best Practices Followed

✔ BDD via Gherkin
✔ Clean POM structure
✔ Secure credentials using encryption
✔ Modular fixtures & hooks
✔ Cross-browser automation
✔ Configurable test execution


## 💬 Need Help?

If anything needs clarification, file an issue or reach out — happy to help you continue building this framework to professional standards.

## ⭐ Feedback / Contribution

Feel free to submit PRs, improve feature files, add new scenarios (cart, checkout, sort), or integrate CI like GitHub Actions with matrix browser execution.

Happy Testing! 🚀
