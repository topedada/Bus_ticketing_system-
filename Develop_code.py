from buy_a_ticket_code import buy_ticket, view_basket
from top_up_code import view_topups_for_category

while True:
    print("\n--- Main Menu ---")
    print("1. Guest Mode")
    print("2. Administrator Mode")
    print("3. Exit Program")
    print("4. View Basket")

    choice = input("Enter your choice: ")

    if choice == "1":
        category_selected = buy_ticket()

        if category_selected is not None:
            view_topups_for_category(category_selected)

    elif choice == "2":
        password = input("Enter administrator password: ")
        if password == "password01":
            print("\n*** Access Granted: Administrator ***")
        else:
            print("Access Denied: Incorrect password.")

    elif choice == "3":
        print("Exiting program.")
        break

    elif choice == "4":
        view_basket()

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
