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


# 🧪 Exercise 1.2 – Data Types in Python

## 📄 Overview

This exercise focused on learning how to use different data types and structures in Python. It included hands-on practice with strings, lists, dictionaries, and tuples, as well as working in the IPython shell to explore how Python handles various forms of data.

---

## 📂 Deliverables

The following deliverables are included in this folder:

- `1.2-Practice Task 1`: Compound interest calculation from a text file
- `1.2-Practice Task 2`: Tuple slicing and max value analysis on world population data
- `1.2-Practice Task 3`: List sorting with Ford vehicle lineup
- `1.2-Practice Task 4`: String slicing and index exercises
- `1.2-Practice Task 5`: Dictionary creation and manipulation with month names
- `1.2-Recipe App Task`: A simulated recipe app using dictionaries and lists
- `learning-journal.md`: Reflection journal with answers to conceptual questions
- Screenshots for each step in their respective folders

---

## 🧠 Key Concepts Covered

- Variables and data types: `int`, `float`, `str`, `list`, `tuple`, and `dict`
- Reading from and writing to files
- Data slicing and indexing
- Working with Python’s built-in data structures
- IPython shell benefits and usage
- Structuring nested data for real-world applications

---

## 🛠️ Data Structure Decisions

For the recipe app task, I chose **dictionaries** to store individual recipes because they allow structured key-value mapping (e.g., name, ingredients, cooking time) and are easy to update and retrieve data from. These were nested inside a **list** (`all_recipes`) to store multiple recipes sequentially. A list allows dynamic insertion, iteration, and organization, which fits the nature of managing multiple recipes.

---

## 📌 Summary

Through this exercise, I developed a stronger understanding of how Python stores and organizes data using core types and structures. I practiced implementing these through real-world examples like population analysis and a recipe app. This hands-on approach made abstract concepts much more concrete.

