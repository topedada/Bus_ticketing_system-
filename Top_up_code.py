import csv
from buy_a_ticket_code import add_to_basket

class TopUp:
    def __init__(self, category_title, title, description, price):
        self.category_title = category_title
        self.title = title
        self.description = description
        self.price = price

    def __str__(self):
        price_in_pounds = self.price / 100
        return f"{self.title} - £{price_in_pounds:.2f}"


def load_topups():
    topups = []
    try:
        with open('mobile_products.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                topup = TopUp(
                    row["category_title"],
                    row["topup_title"],
                    row["topup_description"],
                    float(row["topup_price_in_pence"])
                )
                topups.append(topup)
    except FileNotFoundError:
        print("Top-Up CSV file not found.")
    return topups


def view_topups_for_category(category_title, basket):
    topups = load_topups()
    matching = [t for t in topups if t.category_title == category_title]

    if not matching:
        print("No top-ups available for this category yet.")
        return None

    print(f"\n-- Top-Ups for {category_title} --")
    for index, topup in enumerate(matching):
        price_in_pounds = topup.price / 100
        print(f"{index + 1}. {topup.title} - £{price_in_pounds:.2f}")
        print(f"    {topup.description}")

    while True:
        print("\nEnter a number to add a ticket to your basket")
        print("Press 'q' to return to the main menu")
        choice = input("Your choice: ").lower()
        if choice == "q":
            return None
        try:
            choice = int(choice)
            if 1 <= choice <= len(matching):
                selected_topup = matching[choice - 1]
                basket_entry = f"{selected_topup.title} - £{selected_topup.price / 100:.2f}"
                basket.append(basket_entry)
                print(f"\n'{basket_entry}' has been added to your basket.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
