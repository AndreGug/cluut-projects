from datetime import datetime
import statistics
from collections import Counter


class Supermarket():
    """Represents a supermarket with information about its location, employees, and products."""
    
    def __init__(self, name, street, city):
        """Initializes a Supermarket instance with the specified name, street, and city."""
        self.name = name
        self.street = street
        self.city = city
        self.employees = []
        self.products = []

    def count_employees(self):
        """Counts the number of employees in the supermarket and prints the result."""
        all_employees = len(self.employees)
        print(f"The supermarket currently has {all_employees} employees.")

    def get_most_expensive_product(self):
        """Identifies and prints the most expensive product in the supermarket."""
        most_expensive = max(self.products, key=lambda product: product.price)
        print(f"The most expensive product is {most_expensive.name.title()}.")

    def calculate_average_price(self):
        """Calculates and prints the average price of products in the supermarket."""
        prices = [product.price for product in self.products]
        average_price = statistics.mean(prices)
        print(f"The average price is {average_price:.2f}€.")

    def count_products_per_category(self):
        """Counts and prints the number of products in each category."""
        categories = ["food", "drinks", "others"]
        count_per_category = Counter(product.category for product in self.products)
        for category in categories:
            count = count_per_category.get(category, 0)
            print(f"There are {count} products in the '{category.title()}' category.")

    def get_oldest_employee(self):
        """Identifies and prints the oldest employee in the supermarket."""
        oldest_employee = max(self.employees, key=lambda employee: employee.age)
        print(f"The oldest employee is named {oldest_employee.name.title()}.")


class Employee():
    """Represents an employee with information about their name, age, personal ID, and job."""
    
    def __init__(self, name, age, pers_id, job):
        """Initializes an Employee instance with the specified name, age, personal ID, and job."""
        self.name = name.title()
        self.age = age
        self.pers_id = pers_id
        self.job = job.title()

    def greet_customer(self):
        """Greets a customer and provides information about the current time."""
        time = datetime.now().strftime("%H%M")
        print(f"Hello, my name is {self.name} and I am {self.job} at this supermarket."
              f"\nIt is currently {time} o'clock - how can I assist you?")

    def celebrate_birthday(self):
        """Increments the age of the employee and prints a birthday celebration message."""
        self.age += 1
        print(f"Hooray! Today I'm turning {self.age} years old!")


class Product():
    """Represents a product with information about its name, product ID, category, and price."""
    
    def __init__(self, name, prod_id, category, price):
        """Initializes a Product instance with the specified name, product ID, category, and price."""
        self.name = name.title()
        self.prod_id = prod_id
        self.price = price

        if category in ["food", "drinks", "others"]:
            self.category = category
        else:
            self.category = "others"

    def apply_discount(self, discount):
        """Applies a discount to the product's price and prints a message."""
        if 0 <= discount <= 100:
            self.price = self.price - self.price * (discount / 100)
        else:
            print("Invalid discount value! A 5% discount will be applied.")
            self.price = self.price * 0.95
