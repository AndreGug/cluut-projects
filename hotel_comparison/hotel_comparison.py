# Define two lists
list1 = [10, 21, 45, 66, 78]
list2 = [10, 22, 46, 66, 78, 90]

# Find symmetric differences between list1 and list2
sym_differences = sorted(set(list1).symmetric_difference(list2))
print(sym_differences)

# Find common values between list1 and list2
common_values = sorted(set(list1).intersection(list2))
print(common_values)

# Hotel Marrios vs Hotel Hilten
marrios = {
    "name": "Marrios",
    "age": 1999,
    "payment_options": ["card", "cash", "online"],
    "available_rooms": [800, 801, 802, 805, 900, 1000, 1001],
    "price_per_night": 50,
    "employees": ["carlo", "maria", "marta", "luis", "fernando"]
}

hilten = {
    "name": "Hilten",
    "age": 1992,
    "payment_options": ["card", "online"],
    "available_rooms": [100, 800, 801, 805, 1000, 1001],
    "price_per_night": 70,
    "employees": ["artur", "maria", "oliver", "xenia"]
}

# Calculate the total cost for a 5-night stay at each hotel
num_nights = 5
cost_marrios = num_nights * marrios["price_per_night"]
cost_hilten = num_nights * hilten["price_per_night"]
price_difference = abs(cost_marrios - cost_hilten)
print(f"Five nights cost {cost_marrios}€ at Hotel Marrios and {cost_hilten}€ at Hotel Hilten. The price difference is {price_difference}€.")

# Find the available rooms in both hotels
common_rooms = sorted(set(marrios["available_rooms"]).intersection(hilten["available_rooms"]))
room_numbers = ', '.join(map(str, common_rooms))
print(f"Hello, could you please reserve one of the following rooms: {room_numbers}? Thank you.")

# Compare the payment options between both hotels
num_pay_marrios = len(marrios["payment_options"])
num_pay_hilten = len(hilten["payment_options"])
print(f"Hotel Marrios provides {num_pay_marrios} payment options, while Hotel Hilten offers {num_pay_hilten} payment options.")

sym_differences_payment = sorted(set(marrios["payment_options"]).symmetric_difference(hilten["payment_options"]))
different_payment = ', '.join(sym_differences_payment)
print(f"The hotels differ in the following payment options: {different_payment}.")

# Check where the employee Fernando works
if "fernando" in marrios["employees"]:
    print("Fernando works at Hotel Marrios. I will stay there.")
if "fernando" in hilten["employees"]:
    print("Fernando works at Hotel Hilten. I will stay there.")
