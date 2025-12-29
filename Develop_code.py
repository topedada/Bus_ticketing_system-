from buy_a_ticket_code import buy_ticket
from Top_up_code import view_topups_for_category

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
