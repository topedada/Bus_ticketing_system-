import csv
import sys  # Import the sys module to allow for clean exiting of the program

basket = []  # This list holds all tickets or items that the user selects to purchase


# Class Definition
# This class defines how to store and manage each ticket category's data
class Category:
    # __init__ is the constructor that runs automatically when a new object is created
    # 'self' refers to the specific instance of the object being created
    def __init__(self, code, title, desc):
        self.code = code  # Unique ID assigned to this category
        self.title = title  # Name or title of the category
        self.description = desc  # Brief description of the category

    # Method to retrieve the unique category ID
    def get_code(self):
        return self.code

    # Method to retrieve the category title
    def get_title(self):
        return self.title

    # Method to retrieve the category description
    def get_description(self):
        return self.description


# Function to add an item to the user's basket
def add_to_basket(item):
    # Add the given item to the basket list
    basket.append(item)
    # Inform the user that the item has been successfully added
    print(f"\n'{item}' has been added to your basket.")


# Function to display all items currently in the basket
def view_basket():
    print("\n-- Your Basket ---")

    # Check if the basket is empty
    if not basket:
        print("Your basket is currently empty.")  # Inform user if no items
        return

    # Loop through basket items and display them with numbering for clarity
    for index, item in enumerate(basket):
        print(f"{index + 1}. {item}")


# Function to load and display all ticket categories from the CSV file
def view_categories():
    print("\n--- Displaying Categories (Guest View) ---")

    # Initialize structures to store category information
    categoryList = []        # Keeps track of unique category titles to avoid duplicates
    categoryObjectList = []  # Stores actual Category objects for further use
    code = 0                 # Counter to assign unique ID numbers to each category

    try:
        # Open the CSV file safely using 'with' to ensure closure
        with open('mobile_products.csv', mode='r') as file:
            # DictReader reads each row as a dictionary with CSV headers as keys
            csvFile = csv.DictReader(file)

            # Iterate through every row in the CSV file
            for line in csvFile:
                # Only create a new category if it hasn't already been added
                if line["category_title"] not in categoryList:
                    # Add the new category title to the tracking list
                    categoryList.append(line["category_title"])

                    # Create a Category object with unique ID, title, and description
                    thisCat = Category(code, line["category_title"], line["category_description"])

                    # Add the Category object to the main object list
                    categoryObjectList.append(thisCat)

                    # Increment the ID code for the next category
                    code += 1

        # Print a formatted table header for displaying category data
        header = f"| {'ID':<5} | {'Category Title':<25} | {'Category Description':<40} "
        print(header)
        # Print a separator line based on header length for clarity
        print("-" * len(header))

        # Loop through the list of Category objects and print their details
        for data in categoryObjectList:
            print(f"| {data.get_code():<5} | {data.get_title():<25} | {data.get_description():<40} ")

        # Return the list of Category objects so that selected IDs can be mapped to titles
        return categoryObjectList

    except FileNotFoundError:
        # Handle situation where the CSV file is missing
        print("Error: 'mobile_products.csv' file not found.")
        # Return empty list to prevent the program from breaking
        return []


# Function for the guest to buy a ticket
# Handles category selection and prepares the selected category for top-up integration
def buy_ticket():
    print("\n--- Buy a Ticket ---")

    # Display all available categories and get the Category objects
    categories = view_categories()

    # If no categories were found, exit the function early
    if not categories:
        return None

    try:
        # Prompt the user to select a category by ID
        category_id = int(input("\nEnter the category ID you want to view: "))

        # Initialize variable to store the selected category title
        selected_category = None
        # Find the category title that matches the entered ID
        for cat in categories:
            if cat.get_code() == category_id:
                selected_category = cat.get_title()
                break

        # If the category ID is invalid (not found), inform the user
        if not selected_category:
            print("Invalid category ID.")
            return None

        # Display the selected category for confirmation
        print(f"\nYou selected category: {selected_category}")

        # Return the category title to use for linking with top-ups
        return selected_category

    except ValueError:
        # Handle the case where user input is not an integer
        print("Invalid input. Please enter a number.")
        return None
