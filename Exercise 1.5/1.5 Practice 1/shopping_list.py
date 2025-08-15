class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"'{item}' added to the shopping list.")
        else:
            print(f"'{item}' is already in the shopping list.")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"'{item}' removed from the shopping list.")
        else:
            print(f"'{item}' is not in the shopping list.")

    def view_list(self):
        print(f"\n{self.list_name}:")
        if not self.shopping_list:
            print("Shopping list is empty.")
        else:
            for item in self.shopping_list:
                print(f"- {item}")
