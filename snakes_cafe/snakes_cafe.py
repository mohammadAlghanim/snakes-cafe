menu = {
    "appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "desserts": ["Ice Cream", "Cake", "Pie"],
    "drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

order = {}
quit_keywords = ["quit", "exit", "done"]
error_count = 0
max_errors = 3

def print_menu():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**                                  **")
    print("** To quit at any time, type 'quit' **")
    print("**************************************")
    
    for category, items in menu.items():
        print(category)
        print("-" * len(category))
        for item in items:
            print(item)
        print()

def print_order():
    print("Here is your complete order:")
    for item, quantity in order.items():
        print(f"{quantity} order{'s' if quantity > 1 else ''} of {item}")

print_menu()

while error_count < max_errors:
    item = input("***********************************\n** What would you like to order? **\n***********************************\n> ")
    if item.lower() in quit_keywords:
        break
    
    found = False
    for category, items in menu.items():
        if item in items:
            found = True
            if item in order:
                order[item] += 1
            else:
                order[item] = 1
            print(f"** {order[item]} order{'s' if order[item] > 1 else ''} of {item} have been added to your meal **\n")
            break
    
    if not found:
        error_count += 1
        print(f"Sorry, we don't have {item} on the menu. Please choose something else.\n")
        
if error_count == max_errors:
    print("You have reached the maximum number of errors. Exiting program.\n")
else:
    print_order()
