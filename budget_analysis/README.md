# Budget Analysis

This project analyzes budget data, calculates total savings, and visualizes expenses per category and per month.

## Steps and Features

1. **Read Budget Data:**

   - The budget data is read from the `budget.csv` file.
   - Basic information about the dataset is displayed.

2. **Calculate Total Savings:**
   
   - Total savings are calculated as the difference between income and expenses.
   - The calculated savings are rounded to two decimal places.

3. **Expenses per Category:**
   
   - Expenses are grouped by category, and the sum for each category is displayed.
   - A bar plot is generated to visualize expenses per category.
   - The plot is saved as `expenses_per_category.png`.

4. **Expenses per Month:**
   
   - Expenses are grouped by month, and the sum for each month is displayed.
   - Another bar plot is created to visualize expenses per month.
   - The plot is saved as `expenses_per_month.png`.

### How to run

- Ensure that the required Python libraries are installed: "pandas" and "seaborn".
- The CSV file with budget information must be in the same directory as the code and named `budget.csv`.
- The Python code is located in the file `budget.py`.
- Execute the code with a Python interpreter to see the results.