# 2. Advanced Data Handling with Python

# hotel_rooms = {
#     "101": {"status": "available", "customer": ""},
#     "102": {"status": "booked", "customer": "John Doe"}
# }

# def book_room(room_number, customer_name):
#     if hotel_rooms[room_number]["status"] == "available":
#         hotel_rooms[room_number]["status"] = "booked"
#         hotel_rooms[room_number]["customer"] = customer_name
#         print(f"Room {room_number} booked successfully for {customer_name}.")
#     else:
#         print(f"Room {room_number} is already booked.")

# def check_out(room_number):
#     if hotel_rooms[room_number]["status"] == "booked":
#         hotel_rooms[room_number]["status"] = "available"
#         customer_name = hotel_rooms[room_number]["customer"]
#         hotel_rooms[room_number]["customer"] = ""
#         print(f"{customer_name} has checked out of room {room_number}.")
#     else:
#         print(f"Room {room_number} is already available.")

# def display_status():
#     for room_number, details in hotel_rooms.items():
#         print(f"Room {room_number}: {details['status']} (Customer: {details['customer']})")

# # Example usage
# display_status()
# book_room("101", "Jane Smith")
# check_out("102")
# display_status()
