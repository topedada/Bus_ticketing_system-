import csv  # Import the CSV module to read data from CSV files

# Class to represent a single Top-Up option
class TopUp:
    # Constructor that runs automatically when a new object is created
    # 'self' refers to the instance of the object being created
    def __init__(self, category_title, title, description, price):
        self.category_title = category_title  # The category this top-up belongs to
        self.title = title                      # Name/title of the top-up
        self.description = description          # Description of the top-up
        self.price = price                      # Price of the top-up (currently in pence)

    # Method to define how the TopUp object should be represented as a string
    def __str__(self):
        # Format the title and price neatly for printing
        return f"{self.title} - £{self.price:.2f}"


# Function to read all top-ups from the CSV file and return a list of TopUp objects
def load_topups():
    topups = []  # Initialize an empty list to store all top-up objects
    try:
        # Open the CSV file safely in read mode
        with open('mobile_products.csv', mode='r') as file:
            # DictReader allows us to access CSV columns by header names
            reader = csv.DictReader(file)

            # Loop through each row of the CSV to create TopUp objects
            for row in reader:
                topup = TopUp(
                    row["category_title"],           # Assign category from CSV
                    row["topup_title"],              # Assign title from CSV
                    row["topup_description"],        # Assign description from CSV
                    float(row["topup_price_in_pence"])  # Convert price to float
                )
                # Add the TopUp object to the list
                topups.append(topup)

    except FileNotFoundError:
        # Handle case where CSV file is missing
        print("Top-Up CSV file not found.")

    # Return the full list of TopUp objects
    return topups


# Function to display all top-ups for a specific category and allow user selection
def view_topups_for_category(category_title):
    # Load all top-ups from CSV
    topups = load_topups()

    # Print a header showing which category we are displaying
    print(f"\n-- Top-Ups for {category_title} --")

    # Filter the top-ups to only include those matching the given category
    matching = [t for t in topups if t.category_title == category_title]

    # Inform the user if no top-ups are available
    if not matching:
        print("No top-ups available for this category yet.")
        return None

    # Display each matching top-up with numbering and description
    for index, topup in enumerate(matching):
        print(f"{index + 1}. {topup.title} - £{topup.price:.2f}")
        print(f"    {topup.description}")

    # Prompt the user to select a top-up from the list
    try:
        choice = int(input("\nEnter the number of the Top-Up you want to add: "))
        # Validate the choice is within range
        if 1 <= choice <= len(matching):
            selected_topup = matching[choice - 1]  # Get the selected TopUp object
            return selected_topup                     # Return the selection for further processing
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        # Handle non-integer input gracefully
        print("Invalid input.")
        return None
