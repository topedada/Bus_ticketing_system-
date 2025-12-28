import csv  # Import the CSV module to read data from CSV files

# Class to represent a single Top-Up option
class TopUp:
    def __init__(self, category_title, title, description, price): #class method constructure runs automatically when a new object is created from a class
        # Store the category this top-up belongs to
        self.category_title = category_title
        # Store the title/name of the top-up
        self.title = title
        # Store the description of the top-up
        self.description = description
        # Store the price of the top-up (currently in pence from CSV)
        self.price = price

    def __str__(self): #class method Defines how the object prints
        # Return a readable string representation of the top-up for printing
        # Example: "Extra Lesson Pack - £25.00"
        return f"{self.title} - £{self.price:.2f}"


# Function to read all top-ups from the CSV file and return a list of TopUp objects
def load_topups():#standalone laods all top-ups from CSV
    topups = []  # Initialize an empty list to store all top-up objects
    try:
        # Open the CSV file in read mode
        with open('mobile_products.csv', mode='r') as file:
            # Use DictReader to read each row as a dictionary where keys are CSV headers
            reader = csv.DictReader(file)

            # Loop through each row in the CSV
            for row in reader:
                # Create a TopUp object using values from the CSV row
                topup = TopUp(
                    row["category_title"],          # Get the category of the top-up
                    row["topup_title"],             # Get the title/name of the top-up
                    row["topup_description"],       # Get the description of the top-up
                    float(row["topup_price_in_pence"])  # Get the price from CSV and convert to float
                )
                # Add the TopUp object to the list of all top-ups
                topups.append(topup)

    except FileNotFoundError:
        # Print an error message if the CSV file does not exist
        print("Top-Up CSV file not found.")

    # Return the list of TopUp objects to the caller
    return topups


# Function to display all top-ups for a specific category
def view_topups_for_category(category_title):#standalone displays top-ups for a given category
    # Load all top-ups from the CSV file
    topups = load_topups()

    # Print a header showing which category we are displaying
    print(f"\n-- Top-Ups for {category_title} --")

    # Filter the list of top-ups to only include those matching the given category
    matching = [t for t in topups if t.category_title == category_title]

    # If no top-ups are found for this category, inform the user
    if not matching:
        print("No top-ups available for this category yet.")
        return

    # Loop through each matching top-up and print its details
    for index, topup in enumerate(matching):
        # Print the index number, title, and price
        print(f"{index + 1}. {topup.title} - £{topup.price:.2f}")
        # Print the description indented for clarity
        print(f"    {topup.description}")


# Example call to display top-ups for a specific category
# This will run automatically when the file is executed
view_topups_for_category("Academic Year Tickets")
