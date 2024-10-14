# Task 3: Add a function that prints out the entire list in a formatted way.

# Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.

products = []

def grocery_list():
    while True:
        print("\nGrocery List:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show list")
        print("4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            while True:
                new_item = input("Enter the item you want to add to the shopping list: ")
                products.append(new_item)
                print(f"{new_item} has been added to the grocery list")
                add_item=(input("Do you want to add another item?  (y or n)")).lower()
                if add_item != "y":
                    break
                
        elif choice == "2":
            remove_item = input("Enter the item you would like to remove from the list: ")
            products.remove(remove_item)
            print(f"{remove_item} has been removed from your list")
            remove_more_item=(input("do you want to add remove more items?  (y or n)")).lower()
            if remove_more_item!= "y":
                break
        elif choice =="3":
            print ("Your list is: " )
            for item in products:
                print(item)
            print("End of List")
            
        elif choice =="4":
            print("No need to stray away from your shopping list.")
            break
            

        
        
grocery_list()