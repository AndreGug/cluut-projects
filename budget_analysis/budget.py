import pandas as pd
import seaborn as sns

# Read the budget data
budget = pd.read_csv("budget.csv", sep=";")
print(budget.info())

# Calculate total savings (income - expenses)
income = budget["In"].sum()
expenses = budget["Out"].sum()
total_savings = round(income - expenses, 2)
print(f"\nTotal Savings: {total_savings}€")

# Compute expenses per category
expenses_per_category = budget.groupby("Category")["Out"].sum()
print(f"\nExpenses per Category:\n{expenses_per_category}")

# Visualize expenses per category using a bar plot with Seaborn
sns.set_theme()  # Set Seaborn theme
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})  # Set context for plot size
sns_plot = sns.barplot(data=expenses_per_category.reset_index(), x="Out", y="Category")

# Set plot titles and labels
sns_plot.set_title("Expenses per Category")
sns_plot.set_xlabel("Amount of Expenses (€)")
sns_plot.set_ylabel("Category")

# Save the expenses per category plot as an image file (PNG format)
sns_plot.get_figure().savefig("expenses_per_category.png", bbox_inches="tight")  # Save the figure with tight bounding box
sns_plot.figure.clf()  # Clear the figure buffer

# Compute expenses per month
budget["Date"] = pd.to_datetime(budget["Date"], format="%Y-%m-%d")
expenses_per_month = budget.groupby(pd.Grouper(key="Date", freq="M"))["Out"].sum()
print(f"\nExpenses per Month:\n{expenses_per_month}")

# Visualize expenses per month using a bar plot with Seaborn
sns_plot = sns.barplot(data=expenses_per_month.reset_index(), x=expenses_per_month.index.month_name(), y="Out")

# Set plot titles and labels
sns_plot.set_title("Expenses per Month")
sns_plot.set_xlabel("Month")
sns_plot.set_ylabel("Amount of Expenses (€)")

# Save the expenses per month plot as an image file (PNG format)
sns_plot.get_figure().savefig("expenses_per_month.png", bbox_inches="tight")  # Save the figure with tight bounding box
sns_plot.figure.clf()  # Clear the figure buffer
