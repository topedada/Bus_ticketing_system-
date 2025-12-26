import csv
import sys # Import the sys module to allow for clean exiting of the program

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
        header = f"{'ID':<5} {'Category Title':<25} {'Category Description'}"
        print(header)
        # This line adds a separator based on the header length
        print("-" * len(header))

        # Loop through the list of Category objects we collected
        for data in categoryObjectList:
            # Print the data using the same spacing markers as the header to keep columns aligned
            print(f"{data.get_code():<5} {data.get_title():<25} {data.get_description()}")
            
    except FileNotFoundError:
        # Handle missing CSV file gracefully
        print("Error: 'mobile_products.csv' file not found.")

# Updated Buy Ticket Function with Logical Error in ID Selection
def buy_ticket():
    print("\n--- Buy a Ticket ---")

    # First show categories using the existing function
    view_categories()

    # Ask the user which category they want
    try:
        category_id = int(input("\nEnter the category ID you want to view: "))

        # LOGICAL ERROR: The program always selects category 0 instead of the one user picked
        # Even if the user enters a valid ID, it ignores it
        selected_category = 0  # <-- Logical error: should use category_id

        print(f"\nYou selected category ID: {selected_category}")
        print("\n(Top-Up options will be added after merging the top-up branch.)")

    except ValueError:
        # Handle non-integer input
        print("Invalid input. Please enter a number.")

# User Interface and Authentication (Main Loop)
while True:
    print("\n--- Main Menu ---")
    print("1. Guest Mode")
    print("2. Administrator Mode")
    print("3. Exit Program")
    
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        buy_ticket()
        
    elif choice == '2':
        password = input("Enter administrator password: ")
        if password == "password01":
            print("\n*** Access Granted: Administrator ***")
        else:
            print("\nAccess Denied: Incorrect password.")
            
    elif choice == '3':
        print("Exiting program.")
        sys.exit() 
        
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")
