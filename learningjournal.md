# Learning Journal — Exercise 1.1: Getting Started with Python

## Learning Goals

- **Summarize the uses and benefits of Python for web development**

  Python is a powerful and versatile programming language that is widely used in backend web development. Its readability, large library ecosystem, and strong community support make it ideal for building web applications quickly and efficiently. Frameworks like Django and Flask allow developers to create robust, scalable web applications while focusing more on logic and features, and less on boilerplate code.

- **Prepare your developer environment for programming with Python**

  I have installed Python, set up virtual environments using `virtualenvwrapper`, installed VSCode as my text editor, and learned how to use pip to install and manage dependencies. I also learned how to create and activate virtual environments and generate a `requirements.txt` file to manage packages across different projects.

---

## Reflection Questions

### 1. What is the difference between frontend and backend web development?  
If you were hired to work on backend programming for a web application, what kinds of operations would you be working on?

Frontend web development focuses on the parts of a website that users interact with directly, such as buttons, layouts, and visuals. This includes technologies like HTML, CSS, and JavaScript. Backend development, on the other hand, focuses on what happens behind the scenes — databases, servers, authentication, and APIs.

If I were hired as a backend developer, I’d be working on building and maintaining the server-side logic, managing data storage and retrieval with databases, handling user authentication, creating APIs, and ensuring that everything is secure, efficient, and scalable.

---

### 2. Why choose Python over JavaScript for a web development project?  
What similarities and differences would you explain to your team?

Both Python and JavaScript are high-level, versatile languages with strong communities. JavaScript is traditionally used for frontend development and has evolved to support full-stack applications using frameworks like Node.js. Python, however, shines in backend development, data science, automation, and AI.

To convince my team to use Python, I would emphasize:

- **Readability and simplicity**: Python’s syntax is clean and easy to understand, which speeds up development and reduces bugs.
- **Rapid development**: With frameworks like Django and Flask, we can build web applications quickly.
- **Community and libraries**: Python has a massive ecosystem of libraries for everything from web development to machine learning, which can future-proof our project.
- **Long-term maintainability**: Python code is easier for new developers to pick up and maintain over time.

For backend-heavy applications where speed of development, reliability, and scalability are priorities, Python is often the better choice.

---

## My Goals for This Achievement

1. **Master the fundamentals of Python programming**, including variables, loops, functions, and error handling, so I can build clean and functional backend systems.

2. **Get comfortable working with Python virtual environments and packages**, ensuring that I can manage dependencies and work on multiple projects efficiently.

3. **Build and deploy a small-scale full-stack web application**, applying my Python backend knowledge and connecting it to a frontend framework or API.

---

# 📘 Learning Journal: Exercise 1.2 – Data Types in Python

## 🎯 Learning Goals

- Explain variables and data types in Python
- Summarize the use of objects in Python
- Create a data structure for your Recipe app

---

## 🧠 Reflection Questions

### 1. Why use IPython instead of the default Python shell?

IPython provides a more powerful and user-friendly shell compared to Python’s default shell. It offers useful features like syntax highlighting, auto-completion, command history, better error tracebacks, and support for magic commands (e.g., `%time`, `%run`). These features make writing, testing, and debugging code faster and more efficient—especially helpful for beginners or when experimenting interactively.

---

### 2. Four Python Data Types

| Data Type | Description | Scalar or Non-Scalar |
|-----------|-------------|----------------------|
| `int`     | Whole numbers like `5`, `-1`, or `100` | Scalar |
| `float`   | Decimal numbers like `3.14` or `-0.01` | Scalar |
| `list`    | An ordered, changeable collection like `[1, 2, 3]` | Non-Scalar |
| `dict`    | Key-value pairs like `{'key': 'value'}` | Non-Scalar |

---

### 3. Difference Between Lists and Tuples

The main difference between lists and tuples is that **lists are mutable**, while **tuples are immutable**. This means you can add, remove, or change items in a list, but not in a tuple. Lists are more flexible and better for data that changes over time. Tuples, on the other hand, are faster and more memory-efficient, making them ideal for fixed collections of data or as keys in dictionaries.

---

### 4. Best Data Structure for a Language-Learning Flashcard App

For a language-learning flashcard app, I would use a **dictionary** to store each flashcard. Each card could have keys like `"word"`, `"definition"`, and `"part_of_speech"`. Dictionaries are ideal because they provide clear associations between labels and values, are easy to update, and can scale well. If the app expands to include example sentences or tags, dictionaries allow easy extension, unlike tuples which are fixed and lists which lack semantic clarity.

---

# Exercise 1.3: Functions and Other Operations in Python

## Learning Goals

- Implement conditional statements in Python to determine program flow  
- Use loops to reduce time and effort in Python programming  
- Write functions to organize Python code  

## Reflection Questions

### 1. Write a script for a simple travel app using if-elif-else statements:

```python
destination = input("Where do you want to travel? ").strip()

if destination.lower() == "paris":
    print("Enjoy your stay in Paris!")
elif destination.lower() == "tokyo":
    print("Enjoy your stay in Tokyo!")
elif destination.lower() == "new york":
    print("Enjoy your stay in New York!")
else:
    print("Oops, that destination is not currently available.")

2. Explain logical operators in Python:
Logical operators in Python are used to combine conditional statements and return Boolean results (True or False). The main logical operators are:

and: Returns True if both conditions are true

or: Returns True if at least one condition is true

not: Negates the condition, turning True to False and vice versa

These operators are essential for making complex decisions and controlling the flow of a program.

3. What are functions in Python? When and why are they useful?
Functions in Python are blocks of reusable code designed to perform a specific task. They help break down programs into smaller, manageable pieces, improve code readability, and avoid repetition by allowing the same code to be executed multiple times. Functions also make debugging and testing easier, and support modular programming by enabling code reuse across different parts of a project.

4. Progress towards goals set in Exercise 1
So far, I have made solid progress towards my goals. I have gained confidence in handling different data types, writing conditional statements, and using loops to simplify repetitive tasks. I am now able to write functions that organize code logically and make my programs more efficient. Moving forward, I aim to deepen my understanding of Python libraries and improve my debugging skills during coding exercises.

---

## Learning Goals

- Use files to store and retrieve data in Python

## Reflection Questions

### 1. Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

File storage is important because it allows data to be saved permanently beyond the program’s runtime. Without local files, any data created or modified during program execution would be lost once the program stops, meaning users would have to re-enter data every time. Persistent storage ensures data continuity and supports more complex applications.

---

### 2. In this Exercise you learned about the pickling process with the `pickle.dump()` method. What are pickles? In which situations would you choose to use pickles and why?

Pickles are a way of serializing Python objects into a byte stream so they can be saved to a file and later loaded back into a Python program with their structure and data intact. Pickles are useful when you want to save complex Python objects like dictionaries, lists, or custom classes and retrieve them later exactly as they were, without converting them to a human-readable format.

---

### 3. In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

To find the current working directory, you use `os.getcwd()`. To change the current working directory, you use `os.chdir(path)` where `path` is the directory you want to switch to. This is done by importing the `os` module first.

---

### 4. Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

I would use a try-except block to catch and handle the error gracefully. This way, if an exception occurs in the protected code, the program can respond appropriately (e.g., showing a message or retrying) without crashing or stopping execution entirely.

---

### 5. You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.

My learning is progressing steadily, and I’m proud of understanding how to use functions and data structures effectively in Python. I am still working on becoming more confident with file handling and exception management. I would like more practice with organizing larger programs and working with binary files to strengthen my overall coding skills.

# Exercise 1.5: Object-Oriented Programming in Python

1. In your own words, what is object-oriented programming? What are the benefits of OOP?
Object-oriented programming (OOP) is a method of structuring and designing programs by organizing related data and behavior into "objects". These objects are instances of "classes", which serve as blueprints that define the structure (attributes) and behavior (methods) of the object. OOP makes code more modular, reusable, and easier to manage by breaking it down into smaller, more logical components.

Some of the main benefits of OOP include:

Reusability: Once a class is defined, it can be used to create multiple instances (objects) with shared functionality.

Encapsulation: It keeps data safe from external interference and misuse by bundling it with the methods that work on it.

Maintainability: It is easier to locate and fix bugs in well-structured OOP code.

Scalability: Larger applications can be structured and expanded more easily using OOP.

OOP is especially helpful in real-world applications where multiple entities interact with each other and have common properties or behaviors.

2. What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.
In Python, a class is a blueprint for creating objects. It defines the structure and behaviors that its objects will have. An object is an instance of a class, representing a specific realization of that blueprint.

Example:

Imagine you’re designing a "Car" system. You could define a Car class with attributes like make, model, year, and methods like start_engine() and stop_engine().

python
Copy
Edit
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("Engine started")

# Creating objects
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.start_engine()  # Output: Engine started
In this example, Car is the class, and car1 and car2 are objects (or instances) of that class. Each object has its own set of data but shares the same functionality defined in the class.

3. In your own words, write brief explanations of the following OOP concepts (100–200 words each):
a) Encapsulation
Encapsulation is the principle of bundling data (attributes) and the methods that operate on that data into a single unit, typically a class. This allows for controlling access to the internal state of an object by using private or protected variables and providing public getter and setter methods. Encapsulation helps ensure that data cannot be changed arbitrarily from outside the object, making programs more secure and reducing the chances of unintended interference or bugs.

For example, in a class representing a bank account, you might not want to allow direct access to the balance attribute. Instead, you’d provide methods like deposit() and withdraw() to modify the balance while enforcing rules like not allowing negative balances. Encapsulation enforces the idea of "hiding the complexity" and exposing only what is necessary.

b) Inheritance
Inheritance is an OOP concept where a class (child or subclass) inherits properties and methods from another class (parent or superclass). This helps promote code reuse and logical hierarchy. Instead of writing the same code again in multiple classes, you can write it once in a base class and extend or override it in derived classes as needed.

For instance, a base class Vehicle might define attributes like speed and methods like start(). Then, a subclass Car could inherit everything from Vehicle and add its own specific attributes, like number_of_doors. This allows Car to use both general vehicle functionality and its own specialized behavior.

Inheritance supports polymorphism and helps build complex systems more efficiently by promoting code modularity and maintainability.

c) Polymorphism
Polymorphism allows different objects to respond to the same method or operation in different ways. In Python, polymorphism is commonly achieved through method overriding in subclasses or by using common interfaces. It enables flexibility in code, especially when handling multiple object types that share a common method name but implement different logic.

For example, consider a base class Animal with a method speak(). A subclass Dog could implement speak() to return "Woof!", while a subclass Cat could implement it to return "Meow!". When you loop over a list of animals and call speak() on each, Python will automatically call the correct method depending on the object type.

This is powerful because it allows you to write code that works on a general level but behaves correctly for each specific object type, making your programs more dynamic and easier to extend.

---

#Exercise 1.6: Connecting to Databases in Python
Learning Goals
Create a MySQL database for your Recipe app

Understand how to connect a Python script to a MySQL database

Use SQL queries within Python to create, read, update, and delete data

Learn how to structure and store data using relational databases

Reflection Questions
1. What are databases and what are the advantages of using them?
Databases are organized collections of data that can be easily accessed, managed, and updated. They allow you to store data in structured formats (like tables), which makes it easier to query specific information quickly. The main advantages of using databases are efficiency, scalability, and data integrity. Compared to using files or manual tracking, databases ensure that data is not duplicated unnecessarily, can be retrieved or modified easily, and is kept secure. For my Recipe app, using a database helped centralize recipes and made it easy to search, update, and delete records with precision.

2. List 3 data types that can be used in MySQL and describe them briefly:

INT – Used to store whole numbers (e.g. 1, 100, -42). Perfect for IDs or quantities.

VARCHAR(n) – Used to store strings of text with a defined maximum length (e.g. VARCHAR(50)). Ideal for names, titles, or short descriptions.

FLOAT – Used to store decimal numbers. Useful when working with prices or measurements that aren't whole numbers.

3. In what situations would SQLite be a better choice than MySQL?
SQLite is lightweight and self-contained, so it’s a great choice for smaller projects, prototyping, or apps where simplicity and portability matter more than performance. Since it stores the database in a single file, it's easier to set up and manage than MySQL. For example, if I was creating a simple personal recipe app or testing features locally without a full server setup, I’d probably use SQLite instead of MySQL.

4. Think back to what you learned in the Immersion course. What do you think about the differences between JavaScript and Python as programming languages?
JavaScript is primarily used for front-end web development, where it's great for making websites interactive and dynamic. Python, on the other hand, is more general-purpose and is often used for back-end development, data analysis, scripting, and automation. I’ve noticed that Python tends to have more readable syntax and is easier to pick up for beginners. JavaScript is more event-driven, especially in the browser environment, while Python is often more procedural and cleanly structured. Both have their strengths, but Python feels more straightforward for back-end tasks like working with databases.

5. Now that you’re nearly at the end of Achievement 1, consider what you know about Python so far. What would you say are the limitations of Python as a programming language?
While Python is very beginner-friendly and great for many tasks, it does have limitations. It can be slower than other languages like C++ or Java because it’s interpreted rather than compiled. Python isn’t always the best choice for mobile app development or memory-intensive tasks. Also, for very large-scale web applications, frameworks in other languages like JavaScript (Node.js) or Java might offer better performance. Despite that, Python’s strengths in readability, data handling, and rapid development make it a solid tool for many applications.

---

#— Exercise 1.7 📘 Learning Journal: Finalizing Your Python Program
✅ Learning Goals
Interact with a database using an object-relational mapper (ORM)

Build a command-line Recipe application using Python and SQLAlchemy

🔎 Reflection Questions
1. What is an Object Relational Mapper and what are the advantages of using one?
An Object Relational Mapper (ORM) is a tool that allows developers to interact with a relational database (like MySQL) using object-oriented programming. Instead of writing raw SQL queries, I can work with Python classes and methods to perform operations like insertions, updates, deletions, and queries.

Advantages of using an ORM:

Speeds up development by abstracting complex SQL operations

Helps avoid SQL injection vulnerabilities by safely managing query parameters

Makes code more readable and maintainable

Allows for easier migration between different databases

Integrates naturally with Python applications

2. By this point, you’ve finished creating your Recipe app. How did it go?
Creating the Recipe app was challenging at times, but ultimately rewarding. I gained hands-on experience connecting a Python application to a MySQL database and implementing core CRUD (Create, Read, Update, Delete) functionality using SQLAlchemy.

Something I did well:
I was consistent in commenting my code and structuring my functions to keep the application organized and easy to debug. I also implemented input validation and error handling, which helped make the app more user-friendly.

Something I would change:
If I started over, I would implement a separate utils.py file for repeated logic like input validation or formatting to make the code more modular. I’d also consider adding a logging feature for better tracking of database changes or errors.

3. Interview Scenario: What experience do you have creating an app using Python?
"In one of my recent projects, I built a command-line Recipe app using Python and SQLAlchemy. The application allowed users to create, view, edit, delete, and search recipes stored in a MySQL database. I implemented object-relational mapping to simplify database interactions and added input validation to make the app user-friendly and robust. This project helped me solidify my understanding of Python classes, functions, and integrating external packages. It also gave me confidence in building scalable applications that interact with persistent data."

🧠 Overall Reflection on Achievement 1
What went well during this Achievement?
I developed a strong foundational understanding of Python’s capabilities beyond simple scripting — especially its integration with external tools like SQLAlchemy and MySQL. I learned to write cleaner code, handle unexpected inputs, and structure an app around a user menu and database logic.

What’s something you’re proud of?
I'm proud of completing the full flow of the application from scratch — including designing the database model, setting up user interaction, handling errors, and making sure the app runs smoothly. I also took the time to test each menu option thoroughly.

What was the most challenging aspect of this Achievement?
Debugging database connection issues and getting the ORM setup correct was the most challenging part. I had to make sure my MySQL server was running, my connection string was properly formatted, and the correct packages were installed in my environment (like pymysql).

Did this Achievement meet your expectations?
Yes, it exceeded my expectations. I not only created a working application, but I also developed more confidence in handling real-world Python workflows. The process of breaking down tasks and implementing them in stages made me feel prepared for more complex projects.

Did it give you the confidence to start working with your new Python skills?
Absolutely. I now feel comfortable working with classes, object-oriented design, and integrating Python with databases. I’m more confident in reading documentation, debugging errors, and building from the ground up.

🚀 Looking Ahead to Achievement 2
What’s something you want to keep in mind to help you do your best in Achievement 2 (Web Development with Django)?
I want to remember the value of modular, well-commented code and proper input validation. These are especially important in web development where user interaction is even more dynamic. I'll also make an effort to understand how Django’s ORM builds upon what I've learned with SQLAlchemy to make working with databases even easier in web applications.