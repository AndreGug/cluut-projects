# Ticket Machine Simulation

This project simulates a simple ticket machine where users can select a ticket, make a purchase, and receive change. The ticket options and accepted cash denominations are defined in the "tickets.json" file.

## Process Overview

1. **Initialization:**

   - Reads the "tickets.json" file to retrieve available ticket options and accepted cash denominations.

2. **Ticket Selection:**

   - Displays the available tickets with their corresponding numbers and prompts the user to choose a ticket by entering the corresponding ticket number.

3. **Purchase Calculation:**

   - Calculates the price and accepted cash denominations for the selected ticket.

4. **Payment:**

   - Allows the user to insert coins/banknotes until the full ticket price is paid.

5. **Completion:**

   - Provides information on the remaining amount or change and finalizes the purchase.

### How to run

- Ensure that the JSON file with ticket information is in the same directory as the code and named `tickets.json`.
- Locate the Python code in the file `ticket_machine.py`.
- Execute the code with a Python interpreter to simulate the ticket purchase process.
