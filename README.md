# Buying a ticket
## use Case 1: Buying a ticket
### Actors
-User (Guest or Logged-in)

### Preconditions 
-User (Guest or Logged-in)

### Trigger 
-User is identified as guest.

### Main flow 
-Display all available ticket categories.
-User selects a category by ID.
-System confirms selected category.
### Postconditions:
-Ticket category is selected and ready for top-up selection.
-Confirmation of selected category is shown.

 ## Use case 3: Viewing Basket
### Actors
- User
### Preconditions
- User has added tickets and/or top-ups to the basket.
  
### Trigger
-User selects "View Basket" from main menu.

### Main Flow
- System displays all items in the basket with index numbers.
- System calculates and shows total price.
- User can optionally remove an item by entering its number.
  
### Postconditions
- Basket is displayed with items and total.
- Items may be removed if chosen.

# Use Case 4: Confirming Purchases
### Actors
- User
### Preconditions
- Basket contains tickets/top-ups.
### Trigger
- User selects "Confirm Purchases" from main menu.
### Main Flow
- System writes all basket items to purchases.csv.
- System confirms purchase.
- Basket is cleared automatically.
### Postconditions
- Purchases saved to CSV.
- Basket is emptied.
- Confirmation message is shown.
# Class Diagram
+--------------------+
|    CategoryClass   |
+--------------------+
- code : int       
- title : str      
- description: str 
  
+ __init__(code,title,desc) 
+ get_code() : int          
+ get_title() : str         
+ get_description() : str   
