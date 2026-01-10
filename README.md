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
