#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.

products = []

def grocery_list():
    while True:
        print("\nGrocery List:")
        print("1. Add Item")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_item = input("Enter the item you want to add to the shopping list: ")
            products.append(new_item)
            print(f"{new_item} has been added to the grocery list")
            
        if choice != "1":
            pass
grocery_list()