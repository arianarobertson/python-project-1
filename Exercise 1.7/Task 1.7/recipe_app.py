# Import necessary modules and classes from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Create the SQLAlchemy engine to connect to MySQL database
# Replace 'username', 'password', 'hostname', 'task_database' with your actual MySQL credentials
engine = create_engine("mysql+mysqlconnector://cf-python:password@localhost/task_database")

# Create a configured "Session" class and bind it to the engine
Session = sessionmaker(bind=engine)
# Instantiate a session to interact with the database
session = Session()

# Declare a base class for our ORM classes
Base = declarative_base()

# Define the Recipe model class that maps to the 'final_recipes' table
class Recipe(Base):
    __tablename__ = 'final_recipes'  # Name of the table in the database

    # Define the columns of the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=True)

    def __repr__(self):
        # Quick representation showing id, name, and difficulty
        return f"<Recipe ID: {self.id}-{self.name} ({self.difficulty})>"

    def __str__(self):
        # User-friendly display of the recipe details
        return (
            f"Recipe ID:\t{self.id}\n"
            f"Name:\t\t{self.name}\n"
            f"Ingredients:\t{self.ingredients}\n"
            f"Cooking Time:\t{self.cooking_time} minutes\n"
            f"Difficulty:\t{self.difficulty}\n"
            + "-" * 40
        )

    def calculate_difficulty(self):
        # Calculate difficulty based on cooking time and number of ingredients
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and num_ingredients < 5:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 5:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 5:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        # Return ingredients as a list; empty list if no ingredients
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")

# Create the table in the database if it doesn't exist
Base.metadata.create_all(engine)


# Function to create a new recipe entry based on user input
def create_recipe():
    print("\n--- Create a New Recipe ---")
    name = input("Enter recipe name (max 50 chars): ").strip()
    # Validate name length
    if len(name) > 50 or not name:
        print("Invalid recipe name. Please try again.")
        return

    # Get number of ingredients and validate input
    try:
        num_ingredients = int(input("How many ingredients? "))
        if num_ingredients <= 0:
            print("Number of ingredients must be positive.")
            return
    except ValueError:
        print("Please enter a valid number for ingredients.")
        return

    ingredients = []
    # Collect each ingredient from user
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient #{i+1}: ").strip()
        if not ingredient:
            print("Ingredient cannot be empty.")
            return
        ingredients.append(ingredient)

    # Join ingredients into a comma-separated string
    ingredients_str = ", ".join(ingredients)

    # Validate cooking time input
    try:
        cooking_time = int(input("Enter cooking time in minutes: "))
        if cooking_time <= 0:
            print("Cooking time must be positive.")
            return
    except ValueError:
        print("Please enter a valid number for cooking time.")
        return

    # Create new Recipe object and calculate difficulty
    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time,
        difficulty=None,
    )
    recipe_entry.calculate_difficulty()

    # Add to session and commit to the database
    session.add(recipe_entry)
    session.commit()
    print(f"Recipe '{name}' added successfully!\n")


# Function to view all recipes in the database
def view_all_recipes():
    print("\n--- All Recipes ---")
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.\n")
        return

    # Print each recipe using the __str__ method
    for recipe in recipes:
        print(recipe)


# Function to search recipes by ingredients
def search_by_ingredients():
    print("\n--- Search Recipes by Ingredients ---")
    # Check if there are any recipes
    count = session.query(Recipe).count()
    if count == 0:
        print("No recipes available to search.\n")
        return

    # Retrieve all ingredients from recipes
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []

    # Build a unique list of ingredients
    for (ingredient_str,) in results:
        ingredient_list = ingredient_str.split(", ")
        for ingredient in ingredient_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    # Display ingredient choices with numbers
    print("Available Ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")

    # Ask user to select ingredients by number
    selected = input(
        "Enter ingredient numbers separated by spaces to search for recipes: "
    ).strip().split()

    # Validate user input
    try:
        selected_nums = [int(num) for num in selected]
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")
        return

    if any(num < 1 or num > len(all_ingredients) for num in selected_nums):
        print("Selected numbers are out of range.\n")
        return

    # Build search conditions
    search_ingredients = [all_ingredients[num - 1] for num in selected_nums]
    conditions = []
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))

    # Query recipes matching all selected ingredients
    from sqlalchemy import and_

    matched_recipes = session.query(Recipe).filter(and_(*conditions)).all()

    if not matched_recipes:
        print("No recipes found with those ingredients.\n")
        return

    # Display matched recipes
    print(f"\nRecipes with ingredients {', '.join(search_ingredients)}:")
    for recipe in matched_recipes:
        print(recipe)


# Function to edit an existing recipe
def edit_recipe():
    print("\n--- Edit a Recipe ---")
    # Check if recipes exist
    count = session.query(Recipe).count()
    if count == 0:
        print("No recipes to edit.\n")
        return

    # Get all recipe ids and names
    results = session.query(Recipe.id, Recipe.name).all()

    print("Recipes:")
    for id_, name in results:
        print(f"{id_}: {name}")

    try:
        recipe_id = int(input("Enter the ID of the recipe to edit: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return

    # Check if ID exists
    recipe_to_edit = session.query(Recipe).get(recipe_id)
    if not recipe_to_edit:
        print("Recipe ID not found.\n")
        return

    # Show editable attributes
    print("\nCurrent Recipe Details:")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking Time: {recipe_to_edit.cooking_time} minutes")
    print("Note: Difficulty is calculated automatically and cannot be edited.")

    try:
        choice = int(input("Enter the number of the attribute to edit: "))
    except ValueError:
        print("Invalid input.\n")
        return

    if choice == 1:
        new_name = input("Enter new name (max 50 chars): ").strip()
        if len(new_name) > 50 or not new_name:
            print("Invalid name. Edit cancelled.\n")
            return
        recipe_to_edit.name = new_name
    elif choice == 2:
        # Edit ingredients
        new_ingredients = input(
            "Enter new ingredients separated by commas: "
        ).strip()
        if not new_ingredients:
            print("Ingredients cannot be empty. Edit cancelled.\n")
            return
        recipe_to_edit.ingredients = new_ingredients
    elif choice == 3:
        try:
            new_cooking_time = int(input("Enter new cooking time (minutes): "))
            if new_cooking_time <= 0:
                print("Invalid cooking time. Edit cancelled.\n")
                return
            recipe_to_edit.cooking_time = new_cooking_time
        except ValueError:
            print("Invalid input. Edit cancelled.\n")
            return
    else:
        print("Invalid choice. Edit cancelled.\n")
        return

    # Recalculate difficulty based on new values
    recipe_to_edit.calculate_difficulty()

    # Commit changes to database
    session.commit()
    print("Recipe updated successfully!\n")


# Function to delete a recipe
def delete_recipe():
    print("\n--- Delete a Recipe ---")
    # Check if recipes exist
    count = session.query(Recipe).count()
    if count == 0:
        print("No recipes to delete.\n")
        return

    # List all recipes with IDs and names
    results = session.query(Recipe.id, Recipe.name).all()
    print("Recipes:")
    for id_, name in results:
        print(f"{id_}: {name}")

    try:
        recipe_id = int(input("Enter the ID of the recipe to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return

    recipe_to_delete = session.query(Recipe).get(recipe_id)
    if not recipe_to_delete:
        print("Recipe ID not found.\n")
        return

    # Confirm deletion
    confirm = input(
        f"Are you sure you want to delete '{recipe_to_delete.name}'? (yes/no): "
    ).strip().lower()
    if confirm == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!\n")
    else:
        print("Delete operation cancelled.\n")


# Main loop to run the menu-driven CLI application
def main():
    print("Welcome to the Command Line Recipe App!")

    while True:
        print(
            "\nChoose an option:\n"
            "1. Create a new recipe\n"
            "2. View all recipes\n"
            "3. Search for recipes by ingredients\n"
            "4. Edit a recipe\n"
            "5. Delete a recipe\n"
            "Type 'quit' to exit the application."
        )

        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            print("Exiting the application. Goodbye!")
            # Close session and engine properly
            session.close()
            engine.dispose()
            break
        else:
            print("Invalid choice. Please try again.")


# Run the main program if this script is executed directly
if __name__ == '__main__':
    main()
