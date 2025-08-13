import pickle

def display_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print(f"Difficulty level: {recipe['difficulty']}")
    print("-" * 20)

def search_ingredient(data):
    print("Ingredients Available Across All Recipes:")
    for idx, ingredient in enumerate(data['all_ingredients']):
        print(f"{idx}: {ingredient}")
    try:
        choice = int(input("Enter the number of the ingredient you want to search for: "))
        ingredient_searched = data['all_ingredients'][choice]
    except (IndexError, ValueError):
        print("Invalid choice. Please enter a valid number.")
        return
    else:
        print(f"\nRecipes containing '{ingredient_searched}':\n")
        found = False
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        if not found:
            print(f"No recipes found containing {ingredient_searched}.")

def main():
    filename = input("Enter the filename containing your recipe data: ")
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    else:
        search_ingredient(data)

if __name__ == "__main__":
    main()
