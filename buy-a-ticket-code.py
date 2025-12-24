categoryList = []
import csv
with open("mobile_products.csv", mode = "r") as File:
    csvFile = csv.DictReader(File)
    for line in csvFile:
        if line["category_title"] not in categoryList:
            categoryList.append(line["category_title"])
for data in categoryList:
        print(line)
