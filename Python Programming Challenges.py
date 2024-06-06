# 3. Python Programming Challenges 

# service_tickets = {
#     "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#     "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
# }

# def open_ticket(ticket_id, customer, issue):
#     if ticket_id not in service_tickets:
#         service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
#         print(f"Ticket {ticket_id} opened for {customer}.")
#     else:
#         print(f"Ticket {ticket_id} already exists.")

# def update_ticket_status(ticket_id, status):
#     if ticket_id in service_tickets:
#         service_tickets[ticket_id]["Status"] = status
#         print(f"Ticket {ticket_id} status updated to {status}.")
#     else:
#         print(f"Ticket {ticket_id} does not exist.")

# def display_tickets(status=None):
#     for ticket_id, details in service_tickets.items():
#         if status is None or details["Status"] == status:
#             print(f"{ticket_id}: {details['Customer']} - {details['Issue']} ({details['Status']})")

# # Example usage
# display_tickets()
# open_ticket("Ticket003", "Charlie", "Service outage")
# update_ticket_status("Ticket001", "closed")
# display_tickets("open")