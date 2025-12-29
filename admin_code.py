import csv  # Import CSV module to read/write CSV files

# Load all categories and their top-ups from the CSV file
def load_categories():
    try:
        with open('mobile_products.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print("CSV file not found. Starting with empty list.")
        return []

# Save the list of categories back to the CSV file
def save_categories(data):
    fieldnames = ['category_title', 'category_description', 'topup_title', 'topup_description', 'topup_price_in_pence']
    with open('mobile_products.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

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

# Add a new category with description
def add_category():
    title = input("Enter new category title: ").strip()
    description = input("Enter category description: ").strip()
    data = load_categories()

    # Add a placeholder row to maintain CSV structure
    new_row = {
        'category_title': title,
        'category_description': description,
        'topup_title': '',
        'topup_description': '',
        'topup_price_in_pence': ''
    }
    data.append(new_row)
    save_categories(data)
    print(f"Category '{title}' added successfully.")

# Remove a category and all associated top-ups
def remove_category():
    data = load_categories()
    view_categories()
    title = input("Enter the category title to remove: ").strip()

    # Remove rows with matching category
    new_data = [row for row in data if row['category_title'] != title]
    if len(new_data) == len(data):
        print(f"No category named '{title}' found.")
    else:
        save_categories(new_data)
        print(f"Category '{title}' and its top-ups removed successfully.")

# Admin menu loop
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. View Categories")
        print("2. Add Category")
        print("3. Remove Category")
        print("4. Exit Admin Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_categories()
        elif choice == '2':
            add_category()
        elif choice == '3':
            remove_category()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1-4.")
