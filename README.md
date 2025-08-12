# Exercise 1.1 – Getting Started with Python

## 📌 Overview

This exercise focuses on setting up a professional Python development environment and writing a basic Python script. It also includes creating and managing virtual environments, using IPython, generating a `requirements.txt` file, and documenting the process with GitHub.

---

## 📁 Files Included

- `add.py` — A simple Python script that takes two numbers from the user, adds them, and prints the result.
- `requirements.txt` — A file that lists the packages installed in the virtual environment (`cf-python-base`), generated using `pip freeze`.
- `README.md` — This file, describing the exercise and what has been accomplished.
- `learning-journal.md` — A personal reflection on what I’ve learned and my goals moving forward.
- **Screenshots** — Images documenting each step, including:
  - Virtual environment creation
  - Running the `add.py` script
  - IPython setup
  - Requirements export and install

---

## 🧪 What I Did

### ✅ Set Up Python Environment

- Installed Python and pip
- Installed and configured `virtualenvwrapper`
- Created virtual environments:
  - `cf-python-base`
  - `cf-python-copy`

### ✅ Created a Simple Python Script

- Wrote `add.py` in VS Code:
  ```python
  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))
  c = a + b
  print("The sum is:", c)
