# Log Analysis and Apache HTTP Server

This project focuses on the analysis of log files from the Apache HTTP Server. The provided file `apache_logs` contains logs of server activities in the Common Log Format (CLF).

## Understanding Log Analysis and Apache

- **Apache HTTP Server:**
  The Apache HTTP Server is widely used open-source web server software, known for its stability and flexibility, enabling the serving of static and dynamic web content.

- **Apache Access Logs Format (CLF):**
  The Access Logs follow the Common Log Format (CLF) and include information such as the client's IP address, date and time of access, HTTP method used, requested resources, HTTP status code, and more.

## Tasks

1. **Analyzing Apache Logs**

   - The code in `log_analysis.py` reads the `apache_logs` file and stores the lines in a list.
   - The first log line is analyzed to extract key information.

2. **HTTP Status Code of the First Log Entry**

   - The first log line is split, and the HTTP status code is extracted and documented in a comment.

3. **HTTP Status Code Analysis**

   - All log lines are analyzed, and the frequency of status codes 200 and 404 is determined.
   - Using the Counter class, the top 3 most common HTTP status codes are identified.

4. **Troubleshooting on the HTTP Server**

   - Log lines with status code 404 are filtered, and requested URL paths (Resource Requested) from the 404 errors are extracted.
   - The number of different error sources and the top 3 error sources are determined.

5. **Bonus: Log Report**

   - The class "PDF" from `log_pdf.py` creates a log report using the "fpdf" module.
   - Histograms for status codes and requested resources are created using Seaborn and saved to files.
   - A list of plot filenames is added to the PDF report.

## Generated Files

The code will create the following files during execution:

- `status_codes.png`: Histogram plot visualizing the distribution of HTTP status codes.
- `resource_list.png`: Histogram plot visualizing the requested resources with a 404 status code.
- `LogReport.pdf`: PDF document containing the log report with embedded plots.

### How to run

- Install required Python libraries "fpdf" and "seaborn".
- Execute `log_analysis.py` in the same directory as `apache_logs`.
- Ensure `log_pdf.py` and `logo.png` are present in the execution directory.
