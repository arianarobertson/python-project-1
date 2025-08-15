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

# Exercise 1.3: Functions and Other Operations in Python

## Overview

This exercise focused on practicing conditional statements, loops, and functions in Python. Through various tasks, I learned to control program flow using `if-elif-else` statements, automate repetitive tasks with loops, and organize code efficiently with functions. Additionally, I applied these concepts to practical problems like simple calculators, recipe managers, and user input handling.

## What I Did

- Implemented if-elif-else statements to make decisions based on user input.  
- Used for and while loops to reduce repetition in code.  
- Defined functions to encapsulate logic and improve modularity.  
- Created scripts that interactively take user inputs to build data structures such as recipes.  
- Practiced writing readable and maintainable Python code in the IPython shell and scripts.  

## Learning Goals

- Use conditional statements to control program flow.  
- Apply loops to automate repetitive tasks.  
- Write and use functions to structure Python code clearly.  

## Reflection

This exercise helped me understand the importance of control flow in programs and how loops and functions can greatly reduce effort and improve readability. Writing conditional statements felt more intuitive after practicing multiple scenarios. The experience of building small interactive programs also improved my confidence in handling user input and working with Python data structures.

## How to Run

The scripts and code snippets can be run directly in the IPython shell or saved as `.py` files and executed with Python.

---

# Exercise 1.4: File Handling in Python

## Overview

In this exercise, you will practice working with files in Python, including writing to text files and handling binary files using the `pickle` module. This will help you understand how to store data persistently and retrieve it later, an essential skill for many real-world applications.

## Learning Goals

- Understand how to write data to text files and read it back.
- Learn how to serialize and deserialize Python objects using the `pickle` module.
- Handle exceptions during file operations to create robust scripts.
- Manage recipe data by saving and loading it from binary files.

## Tasks

### Practice Task 1: Writing to Files

- Write a list of numbers (50 to 100) to a text file using the `writelines()` method.
- Store the file properly using the `with` keyword.

### Practice Task 2: Binary Files

- Create a recipe dictionary.
- Serialize and save the recipe data to a binary file using `pickle.dump()`.
- Load the data back using `pickle.load()` and display it in a readable format.

### Recipe Management Scripts

- Create `recipe_input.py` to accept multiple recipes from the user, calculate their difficulty, and save them to a binary file.
- Create `recipe_search.py` to load recipes from the binary file, display all available ingredients, and search for recipes containing a user-specified ingredient.

## How to Run

1. Run `recipe_input.py` to input recipes and save them.
2. Run `recipe_search.py` to search recipes by ingredients.
3. Follow on-screen prompts for inputs.
4. Take screenshots of your outputs as evidence of your work.

## Deliverables

- `recipe_input.py`
- `recipe_search.py`
- Binary data file (e.g., `recipes_data.bin`)
- Screenshots folder named `1.4-Practice Task 1` and `1.4-Practice Task 2`
- Updated learning journal (`learningjournal.md`)

## Reflection

File handling is a core Python skill that allows programs to persist data beyond runtime. Using pickle to serialize data ensures complex objects can be saved and restored easily. Handling files robustly with exception blocks helps avoid crashes and improve user experience.

---

# 🧁 Exercise 1.5 - OOP in Python Recipe App

## 📌 Overview

This task demonstrates how to build and manage a simple **Recipe App** using **object-oriented programming (OOP)** principles in Python. Instead of using dictionaries to store recipe data, we now use classes, objects, and custom methods to structure our data and logic more efficiently.

---

## 🎯 Key Concepts Covered

- Creating and using classes in Python
- Defining instance and class attributes
- Writing getter and setter methods
- Using `*args` to handle variable-length arguments
- Implementing object methods for searching and displaying data
- Using `__str__()` to format object output
- Keeping track of global state using class variables

---

## 🛠 Files

- `recipe_oop.py`: Main Python script containing the `Recipe` class, helper methods, recipe creation logic, and ingredient search functionality.
- Screenshots:
  - `1.5-task-class-definition.png`
  - `1.5-task-tea.png`
  - `1.5-task-coffee.png`
  - `1.5-task-cake.png`
  - `1.5-task-smoothie.png`
  - `1.5-task-search-water.png`
  - `1.5-task-search-sugar.png`
  - `1.5-task-search-bananas.png`

---

## 🧪 How It Works

1. **Define the `Recipe` class** with attributes like `name`, `ingredients`, `cooking_time`, and `difficulty`.
2. **Add ingredients** and calculate the difficulty level automatically based on time and ingredients.
3. **Use class-level tracking** to maintain a list of all ingredients used.
4. **Define a `recipe_search()` function** to find and print recipes containing a specific ingredient.
5. **Create multiple recipe objects** and search for ingredients such as `"Water"`, `"Sugar"`, and `"Bananas"`.

---

## 🔍 Sample Recipes

- **Tea**
- **Coffee**
- **Cake**
- **Banana Smoothie**

Each recipe is stored as an object and includes formatted output via the `__str__()` method.

---

## ✅ Output Screenshots

Screenshots were taken in IPython at each key step:

- Class creation
- Recipe creation
- Ingredient search

See the `/screenshots/` folder or individual screenshot files in this directory for visual proof of execution.

---

## 🧠 What I Learned

- How to structure Python programs using classes and methods
- The power of `*args` for flexible method input
- When and how to use class variables effectively
- How to refactor procedural code into reusable object-oriented design

---

## 📂 Folder Structure



