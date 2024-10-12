#Task 2: Include a function to remove items from the list.

products = []

def grocery_list():
    while True:
        print("\nGrocery List:")
        print("1. Add Item")
        print("2. Remove Item")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_item = input("Enter the item you want to add to the shopping list: ")
            products.append(new_item)
            print(f"{new_item} has been added to the grocery list")
            
        elif choice == "2":
            remove_item = input("Enter the item you would like to remove from the list: ")
            products.remove(remove_item)
            print(f"{remove_item} has been removed from your list")
            
    else: False
        
grocery_list()