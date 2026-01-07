import csv
from buy_a_ticket_code import buy_ticket, view_basket, basket, save_purchases
from Top_up_code import view_topups_for_category
from admin_code import admin_menu  # Admin functions like add/remove categories

# Main Program Loop
while True:
    print("\n--- Main Menu ---")
    print("1. Guest Mode")
    print("2. Administrator Mode")
    print("3. Exit Program")
    print("4. View Basket")
    print("5. Save Purchases")

    choice = input("Enter your choice: ")

    # --- Guest Mode ---
    if choice == "1":
        # Run the buy_ticket function to let user select a category
        category_selected = buy_ticket()
        if category_selected:
            # After selecting category, show the top-ups for it
            topup_selected = view_topups_for_category(category_selected, basket)
            # No need to call add_to_basket again; the function already adds it

    # --- Administrator Mode ---
    elif choice == "2":
        # Prompt for admin password
        password = input("Enter administrator password: ")
        if password == "password01":
            print("\n*** Access Granted: Administrator ***")
            # Run the admin menu loop
            admin_menu()
        else:
            print("\nAccess Denied: Incorrect password.")

    # --- Exit Program ---
    elif choice == "3":
        print("Exiting program.")
        break

    # --- View Basket ---
    elif choice == "4":
        view_basket()

    elif choice == "5":
        save_purchases(basket)

    # --- Invalid Input ---
    else:
        print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.")
