
class TopUp:
    def __init__(self, category_title, title, description, price):
        self.category_title = category_title
        self.titile = title
        self.description =  description
        self.price = price

def _str_(self):
    return f"{self.title} - £{self.price:.2f}"

def laod_topups():
    topups = []
    try:
        with open('mobile_products.csv', mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                topup = Topups(
                    row["category_title"],
                    row["topup_title"],
                    row["topup_description"],
                    float(row["price"])
                )
                topups.append(topup)

        except FileNotFoundError:
            print("Top-Up CSvV file not found,")

        return topups

def view_topups_for_category(category_title):
    topups = load_topups()

    print(f"\n-- Top-Ups for {category_title} --")

    matching = [t for t in topups if t.category_title == category_title]

    if not matching:
        print("No top-ups available for this category yet,")
        return

    for index, topup in enumerate(matching):
        print(f"{index + 1}. {topup.title} - £{topup.price:.2f}")
        print(f"    {topup.description}")

view_topups_for_category("Academic Year Tickets")
