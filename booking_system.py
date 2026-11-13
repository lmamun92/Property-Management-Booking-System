from database import get_connection
from datetime import datetime
# Receive booking
# Enter guest name
# Enter number of people
# Enter duration
# if room available, accept, else reject
# if accept, payments, then block off room, then confirm

guest_name = input("Enter guest name: ")
num_of_guests = int(input("Enter number of guests: "))

while True:
    check_in = input("Enter check-in date (DD/MM/YYYY): ")
    check_out = input("Enter check-out date (DD/MM/YYYY): ")
    check_in_date = datetime.strptime(check_in, "%d/%m/%Y")
    check_out_date = datetime.strptime(check_out, "%d/%m/%Y")
    duration = (check_out_date - check_in_date).days

    if duration > 0:
        break # exists loop if the dates are valid
    else:
        print("Invalid dates, please try again")

print("Valid booking dates!")
print("Duration:", duration)

print(" ")
print("Booking details: ")
print("Guest:" , guest_name)
print("Number of people:" , num_of_guests)
print("Check-in:" , check_in)
print("Check-out:" , check_out)

connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
    SELECT room_id, room_number, price_per_night
    FROM rooms
    WHERE room_id NOT IN (
        SELECT room_id
        FROM bookings
        WHERE check_in < %s
        AND check_out > %s
    )
""", (check_out_date, check_in_date))

available_rooms = cursor.fetchall()

for room in available_rooms:
    print(room)

cursor.close()
connection.close()
