from buy_a_ticket_code import buy_ticket
from top_up_code import view_topups_for_category

print("\n=== Buy a Ticket Flow ===")
buy_ticket()

category = input("\nEnter the category title to view Top-Ups: ")
view_topups_for_category(category)
