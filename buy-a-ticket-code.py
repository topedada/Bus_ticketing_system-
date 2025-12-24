import csv
categoryList = []
categoryObjectList = []
code = 0

# 1. Open the file
with open("mobile_products.csv", mode = "r") as File:
    csvFile = csv.DictReader(File)
    
    # 2. Add only unique categories to the list
    for line in csvFile:
        if line["category_title"] not in categoryList:
            categoryList.append(line["category_title"])
            thisCat = category(code,lines["category_title"])
            categoryObjectList.append(thiscat)
            code += 1

# 3. Print the results (FIXED: 'data' is used instead of 'line')
for data in categoryList:
    print(data.getcode(), "", data.getdescription)

class category:
    def __int__(this,code,title,desc):
        this.title = title
        this.code =  code
        this.description = desc
    def getcode(this):
        return this.code
    def getTitle(this):
        return this.title
    def getDescription(this):
        return this.description 
