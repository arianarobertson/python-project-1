import pickle

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

# Predefined recipes
recipes_list = [
    {
        "name": "Pancakes",
        "cooking_time": 15,
        "ingredients": ["Flour", "Eggs", "Milk", "Sugar"],
    },
    {
        "name": "Scrambled Eggs",
        "cooking_time": 5,
        "ingredients": ["Eggs", "Butter", "Salt"],
    },
    {
        "name": "Grilled Cheese",
        "cooking_time": 10,
        "ingredients": ["Bread", "Cheese", "Butter"],
    },
    {
        "name": "Fruit Salad",
        "cooking_time": 5,
        "ingredients": ["Apples", "Bananas", "Grapes", "Orange"],
    },
    {
        "name": "Chicken Curry",
        "cooking_time": 30,
        "ingredients": ["Chicken", "Onion", "Tomato", "Spices", "Garlic"],
    },
    {
        "name": "Boiled Eggs",
        "cooking_time": 10,
        "ingredients": ["Eggs", "Water"],
    },
    {
        "name": "Oatmeal",
        "cooking_time": 8,
        "ingredients": ["Oats", "Milk", "Honey", "Banana"],
    }
]

# Apply difficulty and build all_ingredients list
all_ingredients = []

for recipe in recipes_list:
    recipe["difficulty"] = calc_difficulty(recipe["cooking_time"], recipe["ingredients"])
    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

# Package into data dictionary
data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

# Save to binary file
filename = "recipes_data.bin"

with open(filename, "wb") as file:
    pickle.dump(data, file)

print(f"Saved {len(recipes_list)} recipes to {filename}.")
