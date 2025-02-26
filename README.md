# Pytest GitHub Actions CI

## Overview
This project demonstrates **automated testing** using **Pytest** and **GitHub Actions**. It includes:
- A simple **calculator module** with basic arithmetic operations.
- **Unit tests** using **Pytest**.
- **Code linting** with `flake8`.
- **GitHub Actions CI** to run tests automatically on each push or pull request.
- **Test coverage reports** using `pytest-cov`.

## Project Structure
```
pytest-github-actions-ci/
│── app/
│   ├── __init__.py
│   ├── calculator.py
│── tests/
│   ├── test_calculator.py
│── .github/
│   └── workflows/
│       └── python-ci.yml
│── requirements.txt
│── README.md
│── .gitignore
│── venv/  (Virtual environment)
```

## Setup Instructions
### 1️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run Tests Locally
```sh
pytest --cov=app tests/
```

## GitHub Actions CI Workflow
The **GitHub Actions workflow** (`.github/workflows/python-ci.yml`) automatically:
1. **Checks out the code**.
2. **Sets up Python**.
3. **Installs dependencies**.
4. **Runs Pytest with coverage**.
5. **Runs `flake8` for linting**.

### 🔹 Trigger:
- Runs on **push** and **pull request** events.

## Running GitHub Actions
1. Push the code to **GitHub**:
   ```sh
   git add .
   git commit -m "Initial commit with Pytest and GitHub Actions"
   git push origin main
   ```
2. Go to the **GitHub Actions** tab in your repository to see the workflow execution.

## Next Steps
- **Improve test reporting** (Use `pytest-html`).
- **Automate deployment** (AWS, Heroku, GitHub Pages).
- **Add pre-commit hooks** for code formatting.

## License
This project is open-source and available under the **MIT License**.

