from buy_a_ticket_code import buy_ticket        # Import the function to display categories and let user select a ticket
from Top_up_code import view_topups_for_category # Import function to display top-ups for a selected category
from buy_a_ticket_code import add_to_basket      # Import function to add items (tickets or top-ups) to the basket

# Main program loop
# This loop keeps the program running until the user chooses to exit
while True:
    # Display the main menu options for the user
    print("\n--- Main Menu ---")
    print("1. Guest Mode")        # Option to buy tickets and top-ups
    print("2. Administrator Mode") # Option for admin login
    print("3. Exit Program")       # Option to quit the program
    print("4. View Basket")        # Option to view the user's basket

    # Get the user's choice from the menu
    choice = input("Enter your choice: ")

    # Guest mode workflow
    if choice == "1":
        # Run buy_ticket to display categories and let the user select one
        category_selected = buy_ticket() 
        if category_selected:  # Check if a valid category was selected
            # Display top-ups for the selected category and let the user choose
            topup_selected = view_topups_for_category(category_selected) 
            if topup_selected:  # Check if a valid top-up was selected
                # Add the selected top-up to the basket
                add_to_basket(f"{topup_selected.title} - £{topup_selected.price:.2f}")

    # Administrator login workflow
    elif choice == "2":
        password = input("Enter administrator password: ")  # Prompt admin for password
        if password == "password01":  # Simple password check
            print("\n*** Access Granted: Administrator ***") # Access granted message
            # Additional admin functions can be added here
        else:
            print("\nAccess Denied: Incorrect password.")  # Access denied message

    # Exit the program
    elif choice == "3":
        print("Exiting program.")
        break  # Exit the loop and end the program

    # View basket contents
    elif choice == "4":
        from buy_a_ticket_code import view_basket  # Import function to view basket
        view_basket()  # Display items currently in basket

    # Handle invalid menu input
    else:
        print("\nInvalid choice. Please enter 1, 2, 3 or 4.")
