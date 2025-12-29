import csv  # Import the CSV module to read data from CSV files

# Class to represent a single Top-Up option
class TopUp:
    def __init__(self, category_title, title, description, price):
        # Store the category this top-up belongs to
        self.category_title = category_title
        # Store the title/name of the top-up
        self.title = title
        # Store the description of the top-up
        self.description = description
        # Store the price of the top-up
        self.price = price

    def __str__(self):
        # Return a readable string representation of the top-up for printing
        return f"{self.title} - £{self.price:.2f}"


# Function to read all top-ups from the CSV file and return a list of TopUp objects
def load_topups():
    topups = []  # Initialize an empty list to store all top-up objects
    try:
        # Open the CSV file in read mode
        with open('mobile_products.csv', mode='r') as file:
            reader = csv.DictReader(file)  # Read CSV rows as dictionaries

            for row in reader:
                # Create a TopUp object using values from the CSV row
                topup = TopUp(
                    row["category_title"],
                    row["topup_title"],
                    row["topup_description"],
                    float(row["topup_price_in_pence"])  # Convert price to float
                )
                # Add the TopUp object to the list
                topups.append(topup)

    except FileNotFoundError:
        # Print an error message if the CSV file does not exist
        print("Top-Up CSV file not found.")

    # Return the list of TopUp objects to the caller
    return topups


# Function to display all top-ups for a specific category
def view_topups_for_category(category_title):
    topups = load_topups()  # Load all top-ups from CSV

    print(f"\n-- Top-Ups for {category_title} --")

    # Filter top-ups for the selected category
    matching = [t for t in topups if t.category_title == category_title]

    if not matching:
        print("No top-ups available for this category yet.")
        return

    # Loop through each matching top-up and print details
    for index, topup in enumerate(matching):
        print(f"{index + 1}. {topup.title} - £{topup.price:.2f}")
        print(f"    {topup.description}")
