import csv  # Import CSV module to read/write CSV files


# Load all categories and their top-ups from the CSV file
def load_categories():
    try:
        with open('mobile_products.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]  # Read all rows into a list
        return data
    except FileNotFoundError:
        print("CSV file not found. Starting with empty list.")
        return []

# THIS VERSION IS SAFE – IT NEVER DELETES DATA BY ACCIDENT
def save_categories(data):
    # Use ALL the fieldnames that your CSV file contains
    fieldnames = [
        'category_id',
        'category_title',
        'category_description',
        'topup_id',
        'topup_title',
        'topup_description',
        'topup_price_in_pence',
        'topup_entitlement_type',
        'topup_entitlement_value',
        'topup_entitlement_unit',
        'topup_entitlement_quantity',
        'topup_entitlement_start_date',
        'topup_entitlement_end_date',
        'topup_passenger_class_id',
        'topup_passenger_class_name',
        'topup_passenger_class_quantity'
    ]

    # mode='w' is correct because we write ALL rows back safely
    with open('mobile_products.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()          # Write the header only once
        writer.writerows(data)        # Write all rows (existing + new)


# Display all categories with descriptions

def view_categories():
    data = load_categories()
    categories_seen = set()
    print("\n-- Existing Categories --")
    for row in data:
        if row['category_title'] not in categories_seen:
            print(f"- {row['category_title']}: {row['category_description']}")
            categories_seen.add(row['category_title'])
    if not categories_seen:
        print("No categories found.")


# Add a new category with a description
def add_category():
    title = input("Enter new category title: ").strip()
    description = input("Enter category description: ").strip()

    data = load_categories()  # Load existing CSV rows

    # Add a new placeholder row with all required fields
    new_row = {
        'category_id': '',
        'category_title': title,
        'category_description': description,
        'topup_id': '',
        'topup_title': '',
        'topup_description': '',
        'topup_price_in_pence': '',
        'topup_entitlement_type': '',
        'topup_entitlement_value': '',
        'topup_entitlement_unit': '',
        'topup_entitlement_quantity': '',
        'topup_entitlement_start_date': '',
        'topup_entitlement_end_date': '',
        'topup_passenger_class_id': '',
        'topup_passenger_class_name': '',
        'topup_passenger_class_quantity': ''
    }

    # Add the new row to the list
    data.append(new_row)

    # Save everything back safely
    save_categories(data)

    print(f"Category '{title}' added successfully.")


# Remove a category and all its associated top-ups
def remove_category():
    data = load_categories()
    view_categories()

    title = input("Enter the category title to remove: ").strip()

    # Keep only rows that do NOT match the chosen category
    new_data = [row for row in data if row['category_title'] != title]

    if len(new_data) == len(data):
        print(f"No category named '{title}' found.")
    else:
        save_categories(new_data)  # Save updated list safely
        print(f"Category '{title}' and its top-ups removed successfully.")

def view_purchases():
    """
    Allows admin to view all saved purchases from 'purchases.csv'.
    """
    try:
        with open('purchases.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            print("\n-- Saved Purchases --")
            empty = True
            for i, row in enumerate(reader, start=1):
                print(f"{i}. {row[0]}")
                empty = False
            if empty:
                print("No purchases found.")
    except FileNotFoundError:
        print("No purchases CSV found. No purchases have been saved yet.")
        
# Admin Menu Loop
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. View Categories")
        print("2. Add Category")
        print("3. Remove Category")
        print("4. View Purchases")
        print("5. Exit Admin Menu")
        

        choice = input("Enter your choice: ")
        if choice == '1':
            view_categories()
        elif choice == '2':
            add_category()
        elif choice == '3':
            remove_category()
        elif choice == '4':
            view_purchases()
        elif choice == '5': 
            break
        else:
            print("Invalid choice. Please enter 1-5.")
