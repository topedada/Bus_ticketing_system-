import csv

class Category:
    def __init__(self, code, title, desc):
        self.code = code
        self.title = title
        self.description = desc

    def get_code(self):
        return self.code

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

categoryList = []
categoryObjectList = []
code = 0

with open('mobile_products.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    
    for line in csvFile:
        if line["category_title"] not in categoryList:
            categoryList.append(line["category_title"])
            thisCat = Category(code, line["category_title"], line["category_description"])
            categoryObjectList.append(thisCat)
            code += 1

for data in categoryObjectList:
    print(data.get_code(), " ", data.get_description())
