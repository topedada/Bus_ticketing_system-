import csv

categoryList = []

# 1. Open the file
with open("mobile_products.csv", mode = "r") as File:
    csvFile = csv.DictReader(File)
    
    # 2. Add only unique categories to the list
    for line in csvFile:
        if line["category_title"] not in categoryList:
            categoryList.append(line["category_title"])

# 3. Print the results (FIXED: 'data' is used instead of 'line')
for data in categoryList:
    print(data)
