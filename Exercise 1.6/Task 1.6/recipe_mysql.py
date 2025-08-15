import mysql.connector

# --- Connect to MySQL ---
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

cursor = conn.cursor()

# --- Create database and table ---
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)
''')

# --- Helper function: Calculate difficulty ---
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

# --- Create Recipe ---
def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    
    ingredients = []
    num_ingredients = int(input("How many ingredients? "))
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients.append(ingredient)

    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_str = ", ".join(ingredients)

    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    values = (name, ingredients_str, cooking_time, difficulty)
    cursor.execute(query, values)
    conn.commit()
    print("Recipe added successfully!\n")

# --- Search Recipe ---
def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = set()
    for row in results:
        ingredients = row[0].split(", ")
        all_ingredients.update(ingredients)

    all_ingredients = list(all_ingredients)
    print("\nAvailable ingredients:")
    for idx, ingredient in enumerate(all_ingredients):
        print(f"{idx + 1}. {ingredient}")

    choice = int(input("Select an ingredient number to search for: ")) - 1
    if choice < 0 or choice >= len(all_ingredients):
        print("Invalid choice.\n")
        return

    search_ingredient = all_ingredients[choice]
    query = f"SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(query, (f"%{search_ingredient}%",))
    results = cursor.fetchall()

    print(f"\nRecipes containing '{search_ingredient}':")
    for row in results:
        print(row)
    print()

# --- Update Recipe ---
def update_recipe(conn, cursor):
    # Fetch all recipes and display
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    print("\nRecipes:")
    for recipe in recipes:
        print(f"{recipe[0]}. {recipe[1]}")

    try:
        recipe_id = int(input("\nEnter the ID of the recipe to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    # Ask which column to update
    print("What do you want to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        new_name = input("Enter new recipe name: ")
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (new_name, recipe_id))
        conn.commit()
        print("Recipe name updated.")

    elif choice == '2':
        try:
            new_cooking_time = int(input("Enter new cooking time (in minutes): "))
        except ValueError:
            print("Invalid cooking time.")
            return
        
        # Update cooking_time
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (new_cooking_time, recipe_id))
        
        # Fetch current ingredients to recalc difficulty
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients_str = cursor.fetchone()[0]
        ingredients_list = [i.strip() for i in ingredients_str.split(",")]
        
        # Recalculate difficulty
        difficulty = calculate_difficulty(new_cooking_time, ingredients_list)
        
        # Update difficulty
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id))
        
        conn.commit()
        print(f"Cooking time and difficulty updated to '{difficulty}'.")

    elif choice == '3':
        # Get new ingredients from user, comma separated
        new_ingredients = input("Enter new ingredients, separated by commas: ")
        ingredients_list = [i.strip() for i in new_ingredients.split(",")]
        
        # Update ingredients string in DB
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (new_ingredients, recipe_id))
        
        # Fetch current cooking time to recalc difficulty
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        
        # Recalculate difficulty
        difficulty = calculate_difficulty(cooking_time, ingredients_list)
        
        # Update difficulty
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id))
        
        conn.commit()
        print(f"Ingredients and difficulty updated to '{difficulty}'.")
    else:
        print("Invalid choice.")


# --- Delete Recipe ---
def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    print("\nAvailable Recipes:")
    for row in results:
        print(row)

    recipe_id = int(input("Enter the ID of the recipe to delete: "))
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!\n")

# --- Main Menu ---
def main_menu(conn, cursor):
    while True:
        print("Recipe App - MySQL Version")
        print("1. Create a new recipe")
        print("2. Search for a recipe")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            print("Goodbye!")
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

# --- Run the App ---
main_menu(conn, cursor)
