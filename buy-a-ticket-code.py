import csv
with open("mobile_products.csv", mode = "r") as File:
    csvFile = csv.DictReader(File)
    for line in csvFile:
        print(line)
