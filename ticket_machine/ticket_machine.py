import json

# Load ticket information from the file
with open("tickets.json", "r") as file:
    data = json.load(file)

# Extract tickets and accepted cash from the file
tickets = data["tickets"]
accepted_cash = data["accepted_cash"]  # Separate the tickets and accepted cash for clarity

# Display available tickets with their corresponding numbers
print("Welcome to the railway station. You have the following tickets to choose from:")
for i, ticket in enumerate(tickets, 1):  # Enumerate starts index from 1
    print(f"{i}. {ticket['name']} - {ticket['price']}€")  # Display available tickets with their corresponding numbers

# Prompt to enter ticket number
while True:
    selected_ticket_index = input("\nPlease choose your ticket by entering the corresponding ticket number: ")  # Get user input

    try:
        selected_ticket_index = int(selected_ticket_index) - 1  # Adjust input to match list indexing (starting from 0)

        # Check if input is valid
        if 0 <= selected_ticket_index < len(tickets):
            selected_ticket = tickets[selected_ticket_index]
            remaining_amount = selected_ticket['price']  # Initialize remaining_amount here
            break  # Exit loop if input is valid
        else:
            print("Invalid ticket number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid numerical value.")  # Handle non-numeric input

# Display price and accepted coins for the selected ticket
print(f"\nYou have selected {selected_ticket['name']}. The price is {selected_ticket['price']}€.")  # Display selected ticket
print("The following coins and banknotes are accepted:")
for value in accepted_cash:
    print(f"{value}€")  # Display accepted coins/banknotes

# Insert coin/banknote
paid_amount = 0
while paid_amount < selected_ticket['price']:
    # Input coin/banknote
    cash = input("\nPlease insert a coin/banknote: ")

    try:
        cash = int(cash)

        if cash > 0:  # Ensure the entered value is positive
            if cash in accepted_cash:
                # Add coin/banknote to the paid amount
                paid_amount += cash
                # Update remaining amount
                remaining_amount = selected_ticket['price'] - paid_amount

                if remaining_amount > 0:
                    print(f"Remaining amount: {remaining_amount}€.")
                elif remaining_amount < 0:
                    change = abs(remaining_amount)
                    print(f"Thank you for your purchase! You will receive {change}€ in change.")
                else:
                    print("Thank you for your purchase!")
            else:
                print(f"Invalid coin/banknote. Please enter an accepted value.")
        else:
            print("Invalid input. Please enter a positive numerical value.")
    except ValueError:
        print("Invalid input. Please enter a valid numerical value.")
