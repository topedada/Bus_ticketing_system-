import csv
import sys

basket = []

class Category:
    def __init__(self, code, title, desc):
        self.code = code
        self.title = title
        self.description = desc

    def get_code(self):
        return self.code

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description


def add_to_basket(item):
    basket.append(item)
    print(f"\n'{item}' has been added to your basket.")


def save_purchases(basket):
    if not basket:
        print("Your basket is empty. Nothing to save.")
        return
    try:
        with open('purchases.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for item in basket:
                writer.writerow([item])
        print("Your purchases have been saved successfully!")
        basket.clear()
        print("Basket has been Cleared")
    except Exception as e:
        print(f"Error saving purchases: {e}")


def view_basket():
    print("\n-- Your Basket --")
    if not basket:
        print("Your basket is currently empty.")
        return

    total = 0.0
    print("----RECEIPT----")
    for index, item in enumerate(basket, start=1):
        print(f"{index}. {item}")
        if "£" in item:
            price = float(item.split("£")[1])
            total += price
    print("---------------")
    print(f"\nTotal: £{total:.2f}")

    choice = input("\nEnter item number to remove (or press Enter to continue): ")
    if choice == "":
        return
    try:
        index = int(choice) - 1
        if 0 <= index < len(basket):
            removed = basket.pop(index)
            print(f"\n'{removed}' removed from basket.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input.")


def view_categories():
    print("\n--- Displaying Categories (Guest View) ---")
    categoryList = []
    categoryObjectList = []
    code = 0
    try:
        with open('mobile_products.csv', mode='r') as file:
            csvFile = csv.DictReader(file)
            for line in csvFile:
                if line["category_title"] not in categoryList:
                    categoryList.append(line["category_title"])
                    thisCat = Category(code, line["category_title"], line["category_description"])
                    categoryObjectList.append(thisCat)
                    code += 1

        header = f"| {'ID':<5} | {'Category Title':<25} | {'Category Description':<40} "
        print(header)
        print("-" * len(header))
        for data in categoryObjectList:
            print(f"| {data.get_code():<5} | {data.get_title():<25} | {data.get_description():<40} ")
        return categoryObjectList
    except FileNotFoundError:
        print("Error: 'mobile_products.csv' file not found.")
        return []


def buy_ticket():
    print("\n--- Buy a Ticket ---")
    categories = view_categories()
    if not categories:
        return None
    try:
        category_id = int(input("\nEnter the category ID you want to view: "))
        selected_category = None
        for cat in categories:
            if cat.get_code() == category_id:
                selected_category = cat.get_title()
                break
        if not selected_category:
            print("Invalid category ID.")
            return None
        print(f"\nYou selected category: {selected_category}")
        return selected_category
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
