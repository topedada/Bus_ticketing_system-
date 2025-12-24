import csv
import sys # Import the sys module to allow for clean exiting of the program

# --- Class Definition ---
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

# --- Main Program Logic Function (Guest Mode) ---
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

        # Loop through the list of Category objects we collected
        for data in categoryObjectList:
            # Print the ID and description using the getter methods defined in the class
            print(data.get_code(), " ", data.get_description())
            
    except FileNotFoundError:
        print("Error: 'mobile_products.csv' file not found.")

# --- User Interface and Authentication (Main Loop) ---

# This loop runs continuously until the user decides to exit
while True:
    print("\n--- Main Menu ---")
    print("1. Guest Mode")
    print("2. Administrator Mode")
    print("3. Exit Program")
    
    # Get user input
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Run the guest functionality defined in the function above
        view_categories()
        
    elif choice == '2':
        # Prompt for password if admin is chosen
        password = input("Enter administrator password: ")
        # Check against the required password
        if password == "password01":
            print("\n*** Access Granted: Administrator ***")
            # This is where you would put admin-specific functions
        else:
            print("\nAccess Denied: Incorrect password.")
            
    elif choice == '3':
        # Stop the entire program completely using the sys module
        print("Exiting program.")
        sys.exit() 
        
    else:
        # Handle invalid input gracefully
        print("\nInvalid choice. Please enter 1, 2, or 3.")
