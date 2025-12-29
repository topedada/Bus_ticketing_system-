from buy_a_ticket_code import buy_ticket
from Top_up_code import view_topups_for_category
from buy_a_ticket_code import add_to_basket 

while True:
    print("\n--- Main Menu ---")
    print("1. Guest Mode")
    print("2. Administrator Mode")
    print("3. Exit Program")
    print("4. View Basket")

    choice = input("Enter your choice: ")

    if choice == "1":
        category_selected = buy_ticket() 
        if category_selected:
            topup_selected = view_topups_for_category(category_selected) 
            if topup_selected:
                add_to_basket(f"{topup_selected.title} - £{topup_selected.price:.2f}")

    elif choice == "2":
        password = input("Enter administrator password: ")
        if password == "password01":
            print("\n*** Access Granted: Administrator ***")
        else:
            print("\nAccess Denied: Incorrect password.")

    elif choice == "3":
        print("Exiting program.")
        break

    elif choice == "4":
        from buy_a_ticket_code import view_basket
        view_basket()

    else:
        print("\nInvalid choice. Please enter 1, 2, 3 or 4.")
