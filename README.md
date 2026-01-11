# Bus ticket Python Project
## Use Case: Bus Ticketing System (Develop Branch)
### Branch: Develop
### Actors
- Guest/User – Can browse categories, select tickets, add top-ups, view basket, and confirm purchases.
- Admin – Can manage categories, ticket prices, and view purchase summaries.
### Preconditions
- mobile_products.csv exists (stores categories and tickets).
- purchases.csv exists (stores completed purchases).
- User knows whether they are a guest or admin.
### Trigger
User launches the program.
### Main Flow
- Guest Mode (Buying Tickets & Top-Ups)
- User selects Guest Mode from main menu.
- System displays available ticket categories (ID, title, description).
### User selects a category by ID.
- System displays top-ups/tickets for that category with price and description.
- User can repeatedly:
- Select a ticket/top-up to add to basket
- Press q to return to main menu
- Basket stores tickets with price.
- User can view basket:
- Shows all items
- Displays total price
- Allows removal of items
- User can confirm purchases:
- Saves basket to purchases.csv
- Clears the basket
# Administrator Mode
- User selects Administrator Mode from main menu.
- System prompts for password (password01).
- If correct, system enters admin menu:
- View Categories – See all categories and descriptions
- Add Category – Create new category with randomized default top-ups
- Remove Category – Delete a category and its top-ups
- Edit Ticket Price – Modify the price of a ticket
- View Purchases – See all purchases with:
- Total tickets sold
- Overall revenue
- Sales summary per ticket
- Exit Admin Menu – Return to main menu
# Exit Program
- User selects Exit Program.
- System terminates safely.
 # View Basket
- Available from main menu.
### Shows:
- Tickets added
- Total price
- Allows item removal
- Postconditions
- Purchases saved in purchases.csv.
- Basket is cleared after purchase confirmation.
- Admin changes are reflected in mobile_products.csv.
- Exception Flows
- Invalid input: System prompts user again.
- Empty basket: Prevents saving purchases.
- Incorrect admin password: Denies access.
- No categories or top-ups available: Displays informative message.
