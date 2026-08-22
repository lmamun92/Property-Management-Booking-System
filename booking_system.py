from datetime import datetime
# Receive booking
# Enter guest name
# Enter number of people
# Enter duration
# if room available, accept, else reject
# if accept, payments, then block off room, then confirm

rooms = {
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True
} # true = rooms available, false = room booked

room_price = 100 # temporary fixed rate

guest_name = input("Enter guest name: ")
num_of_guests = int(input("Enter number of guests: "))
check_in = input("Enter check-in date (DD/MM/YYYY): ")
check_out = input("Enter check-out date (DD/MM/YYYY): ")
check_in_date = datetime.strptime(check_in, "%d/%m/%Y")
check_out_date = datetime.strptime(check_out, "%d/%m/%Y")
duration = (check_out_date - check_in_date).days
room_price = 100 # temporary fixed rate
total_cost= room_price * duration

print(" ")
print("Booking details: ")
print("Guest:" , guest_name)
print("Number of people:" , num_of_guests)
print("Check-in:" , check_in)
print("Check-out:" , check_out)
print("Duration:" , duration)
print("Total cost: £" , total_cost)


for room_number in rooms:
    if rooms[room_number] == True:
        print("Room", room_number, "is available.")
        rooms[room_number] = False
        break

else:
    print("No rooms available")




