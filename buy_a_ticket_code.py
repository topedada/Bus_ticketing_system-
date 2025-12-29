import csv
import sys  # Import the sys module to allow for clean exiting of the program
basket = []  # this holds the ticket that the users want to buy

# Class Definition 
# This class defines how to store each category's data cleanly
class Category:
    # __init__ is the constructor that runs when a new object is created
    # 'self' refers to the specific instance of the object being created
    def __init__(self, code, title, desc):
        self.code = code
        self.title = title
        self.description = desc

    # Method to retrieve the category code
    def get_code(self):
        return self.code

    # Method to retrieve the category title
    def get_title(self):
        return self.title

    # Method to retrieve the category description
    def get_description(self):
        return self.description


def add_to_basket(item):
    # Append the item to the user's basket
    basket.append(item)
    print(f"\n'{item}' has been added to your basket.")


def view_basket():
    print("\n-- Your Basket ---")

    # Check if basket is empty
    if not basket:
        print("your basket is currently empty.")
        return

    # Loop through basket items and display them
    for index, item in enumerate(basket):
        print(f"{index + 1}. {item}")


# Main Program Logic Function (Guest Mode)
# This function handles the core logic of reading the file and printing categories
def view_categories():
    print("\n--- Displaying Categories (Guest View) ---")

    # Initialize lists and counter within the function scope
    categoryList = []        # Tracks names of categories seen to avoid duplicates
    categoryObjectList = []  # Stores the actual Category objects
    code = 0                 # Counter for unique category IDs

    try:
        # Open the CSV file in read mode and ensure it closes automatically
        with open('mobile_products.csv', mode='r') as file:
            # Use DictReader to read rows as dictionaries (header as keys)
            csvFile = csv.DictReader(file)

            # Iterate through every row in the CSV file
            for line in csvFile:
                # Check if the title is already in our tracking list
                if line["category_title"] not in categoryList:
                    # If new, add the name to the tracking list
                    categoryList.append(line["category_title"])

                    # Create a new Category object with data from the current row
                    thisCat = Category(code, line["category_title"], line["category_description"])

                    # Add the new object instance to our main object list
                    categoryObjectList.append(thisCat)

                    # Increment the ID code for the next unique category
                    code += 1

        # Tabular Formatting
        # This line defines and prints the headers with specific column widths 
        header = f"| {'ID':<5} | {'Category Title':<25} | {'Category Description':<40} "
        print(header)
        # This line adds a separator based on the header length
        print("-" * len(header))

        # Loop through the list of Category objects we collected
        for data in categoryObjectList:
            # Print the data using the same spacing markers as the header to keep columns aligned
            print(f"| {data.get_code():<5} | {data.get_title():<25} | {data.get_description():<40} ")

        return categoryObjectList  # Return list to map ID to title

    except FileNotFoundError:
        # Handle missing CSV file gracefully
        print("Error: 'mobile_products.csv' file not found.")
        return []


# Updated Buy Ticket Function
# This function allows the user to buy a ticket by first selecting a category
def buy_ticket():
    print("\n--- Buy a Ticket ---")

    # First show categories using the existing function
    categories = view_categories()

    if not categories:
        return None  # Exit if no categories found

    try:
        # Prompt user for category ID
        category_id = int(input("\nEnter the category ID you want to view: "))

        # Find the category title based on the ID
        selected_category = None
        for cat in categories:
            if cat.get_code() == category_id:
                selected_category = cat.get_title()
                break

        if not selected_category:
            print("Invalid category ID.")
            return None

        print(f"\nYou selected category: {selected_category}")
        return selected_category  # <-- Return the category title for top-ups

    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a number.")
        return None
