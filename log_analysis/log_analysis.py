from collections import Counter
from log_pdf import PDF
import seaborn as sns

# Analyzing Apache Logs
with open("apache_logs", "r") as file:
    # Read all lines of the log file
    log_lines = file.readlines()
print(log_lines[0])

# HTTP Status Code of the First Log Entry
first_line = log_lines[0]
parts = first_line.split()
# Extract the HTTP Status Code from the first log line
print(parts[8])

# Extract all HTTP Status Codes from the log lines
status_codes = [line.split()[8] for line in log_lines]
# Count the occurrences of Status Codes 200 and 404
status_200 = status_codes.count("200")
status_404 = status_codes.count("404")

# Use the Counter class to determine the top 3 most common Status Codes
counter = Counter(status_codes)
print(counter.most_common(3))

# Filter log lines by Status Code 404
lines_with_404 = list(filter(lambda x: x.split()[8] == "404", log_lines))
# Extract requested URL paths
resource_list = [line.split()[6] for line in lines_with_404]
# Determine the number of different error sources and the top 3 error sources
print(len(set(resource_list)))
print(Counter(resource_list).most_common(3))

# Set Seaborn theme and context parameters for plot size and font size
sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})

# Create a histogram for HTTP Status Codes and save the plot as an image
sns_plot_status = sns.histplot(status_codes)
sns_plot_status.set_title("Overview of HTTP Status Codes")
sns_plot_status.set_xlabel("HTTP Status Codes")
sns_plot_status.set_ylabel("Count")
sns_plot_status.get_figure().savefig("status_codes.png", bbox_inches="tight")
sns_plot_status.figure.clf()

# Create a histogram for requested resources with 404 Status Code and save the plot as an image
sns_plot_resource = sns.histplot(y=resource_list)
sns_plot_resource.set_title("Overview of Requested Resources with 404 Status Code")
sns_plot_resource.set_xlabel("Count")
sns_plot_resource.set_ylabel("Resource Names")

# Adjust the size of the figure for the plot
sns_plot_resource.get_figure().set_figwidth(8)
sns_plot_resource.get_figure().set_figheight(11)

# Save the plot as an image
sns_plot_resource.get_figure().savefig("resource_list.png", bbox_inches="tight")
sns_plot_resource.figure.clf()

# Create a list of plot filenames
plots = ["status_codes.png", "resource_list.png"]

# Create an instance of the PDF class
log_report = PDF()

# Iterate over the plots and add them to the PDF report
for plot in plots:
    log_report.print_page(plot)

# Create the PDF report
log_report.output("LogReport.pdf", "F")
