from coffee import Coffee
from customer import Customer
from order import Order

def setup_coffees():
    Coffee("Espresso", 2.5)
    Coffee("Latte", 3.5)
    Coffee("Cappuccino", 4.0)

def view_menu():
    print("\nAvailable Coffees:")
    print(Coffee.display_menu())

def place_order():
    # Get customer name
    name = input("Please enter your name: ")
    customer = Customer(name)
    
    # Display coffee menu
    view_menu()
    
    while True:
        # Get coffee choice
        coffee_name = input("\nWhich coffee would you like to order? ")
        
        # Find the coffee
        coffee = next((c for c in Coffee.all_coffees if c.name.lower() == coffee_name.lower()), None)
        
        if coffee is None:
            print("Sorry, we don't have that coffee. Please choose from the menu.")
            continue
        
        # Create the order
        order = Order(customer, coffee, coffee.price)
        
        # Print order details
        print(f"\nOrder placed successfully!")
        print(order)
        
        # Ask if done
        done = input("\nWould you like to place another order? (yes/no): ").strip().lower()
        if done != 'yes':
            break

def view_sales():
    if not Order.all_orders:
        print("\nNo orders have been placed yet.")
        return
    
    total_sales = sum(order.price for order in Order.all_orders)
    
    print("\nAll Orders:")
    for order in Order.all_orders:
        print(order)
    
    print(f"\nTotal Sales: ${total_sales:.2f}")

def view_inventory():
    if not Coffee.all_coffees:
        print("\nNo coffee available.")
        return
    
    print("\nCoffee Inventory:")
    for coffee in Coffee.all_coffees:
        print(coffee)

def main():
    setup_coffees()
    
    while True:
        print("\n--- Coffee Shop Menu ---")
        print("1. Place Order")
        print("2. View Sales")
        print("3. View Inventory")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            place_order()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            print("Thank you for visiting the Coffee Shop!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if _name_ == "_main_":
    main()