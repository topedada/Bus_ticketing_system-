import csv
from buy_a_ticket_code import buy_ticket, add_to_basket, view_basket
from Top_up_code import view_topups_for_category
from admin_code import admin_menu  # Admin functions like add/remove categories
from buy_a_ticket_code import save_purchases
from buy_a_ticket_code import basket
from admin_code import admin_menu



def save_purchases(basket):
    if not basket:
        print("Basket is empty.")
        return

    try:
        # Open purchases.csv in append mode so we don't overwrite previous purchases
        with open('purchases.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for item in basket:
                writer.writerow([item])  # Save each item as a new row
        print("Your purchases have been saved successfully!")
    except Exception as e:
        print(f"Error saving purchases: {e}")

    
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
            topup_selected = view_topups_for_category(category_selected)
            if topup_selected:
                # Add the selected top-up to the basket
                add_to_basket(f"{topup_selected.title} - £{topup_selected.price:.2f}")

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
        print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
