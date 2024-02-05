from supermarket import Supermarket, Employee, Product
import pandas as pd

# Load product data from CSV
products = pd.read_csv("products.csv", sep=";")

# Select and reorder relevant columns for products
prod_columns = ["Name", "Prod_id", "Category", "PRICE"]
products = products.reindex(columns=prod_columns)

# Convert products DataFrame to a list of records (tuples)
products = list(products.to_records(index=False))

# Load employee data from CSV
employees = pd.read_csv("employees.csv", sep=";")

# Select and reorder relevant columns for employees
emp_columns = ["Name", "Age", "Pers_id", "JOB_ID"]
employees = employees.reindex(columns=emp_columns)

# Convert employees DataFrame to a list of records (tuples)
employees = list(employees.to_records(index=False))

# Create a Supermarket instance and populate it with data
my_supermarket = Supermarket("Supermarkt Deluxe", "Marienplatz 1", "München")

# Create Employee and Product instances from the loaded data
my_supermarket.employees = [Employee(*item) for item in employees]
my_supermarket.products = [Product(*item) for item in products]

# Perform various operations and print results
my_supermarket.count_employees()
my_supermarket.get_most_expensive_product()
my_supermarket.calculate_average_price()
my_supermarket.count_products_per_category()
my_supermarket.get_oldest_employee()
