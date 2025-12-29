import csv  # Import the CSV module to read data from CSV files

# Class to represent a single Top-Up option
class TopUp:
    def __init__(self, category_title, title, description, price):  # class constructor
        self.category_title = category_title
        self.title = title
        self.description = description
        self.price = price

    def __str__(self):  # class method defines how the object prints
        return f"{self.title} - £{self.price:.2f}"


# Function to read all top-ups from the CSV file and return a list of TopUp objects
def load_topups():
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
                    row["category_title"],
                    row["topup_title"],
                    row["topup_description"],
                    float(row["topup_price_in_pence"])
                )
                # Add the TopUp object to the list of all top-ups
                topups.append(topup)

    except FileNotFoundError:
        # Print an error message if the CSV file does not exist
        print("Top-Up CSV file not found.")

    # Return the list of TopUp objects to the caller
    return topups


# Function to display all top-ups for a specific category and return selection
def view_topups_for_category(category_title):
    # Load all top-ups from the CSV file
    topups = load_topups()

    print(f"\n-- Top-Ups for {category_title} --")

    # Filter the list of top-ups to only include those matching the given category
    matching = [t for t in topups if t.category_title == category_title]

    if not matching:
        print("No top-ups available for this category yet.")
        return None

    # Display all top-ups
    for index, topup in enumerate(matching):
        print(f"{index + 1}. {topup.title} - £{topup.price:.2f}")
        print(f"    {topup.description}")

    # Ask the user to pick a top-up
    try:
        choice = int(input("\nEnter the number of the Top-Up you want to add: "))
        if 1 <= choice <= len(matching):
            selected_topup = matching[choice - 1]
            return selected_topup
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input.")
        return None
