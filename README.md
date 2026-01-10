# Buy a ticket 
## Use Case 2: Selecting a Top up 
### Actors 
- User
### Preconditions
- User has added tickets and/or top-ups to the basket.
### Trigger
- User selects "View Basket" from main menu.
### Main Flow
- System displays all items in the basket with index numbers.
- System calculates and shows total price.
- User can optionally remove an item by entering its number.
### Postconditions
- Basket is displayed with items and total.
- Items may be removed if chosen.

# Class Diagram
+--------------------+
|      TopUpClass    |
+--------------------+
- category_title: str 
- title: str         
- description: str   
- price: float       
+--------------------+
 + __init__(category_title,title,desc,price) 
 + __str__() : str                           
