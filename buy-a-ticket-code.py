import csv
import sys 


def view_categories():
    print("\n--- Displaying Categories (Guest View) ---")
    categoryList = []
    categoryObjectList = []
    code = 0

    try:
       
        with open('mobile_products.csv', mode='read') as file: 
            csvFile = csv.DictReader(file)
            
            for lines in csvFile: 
               
                if lines["category_title"] not in categoryList: 
                    categoryList.append(lines["category_title"])
                    
                    thisCat = Category(code, lines["category_title"], lines["category_description"]) 
                    categoryObjectList.append(thisCat)
                    code += 1

        
        for data in categoryList:
            
            print(data.getCode(), " ", data.getdescription)
            
    except FileNotFoundError:
        print("Error: 'mobile_products.csv' file not found.")



while True:
    print("\n--- Main Menu ---")
    print("1. Guest Mode")
    print("2. Administrator Mode")
    print("3. Exit Program")
    
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        view_categories()
        
    elif choice == '2':
        password = input("Enter administrator password: ")
        
        if password = "password01": 
            print("\n*** Access Granted: Administrator ***")
        else:
            print("\nAccess Denied: Incorrect password.")
            
    elif choice == '3':
        break
        
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.")
