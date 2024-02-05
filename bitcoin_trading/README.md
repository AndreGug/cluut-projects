# Bitcoin Trader

This project deploys an application that utilizes Python code on an EC2 instance with a cron job to consistently retrieve Bitcoin prices through the Coindesk API. The retrieved data is securely archived in an S3 bucket.

## AWS Resources

- **S3 Bucket**
- **EC2 Instance**
  - IAM Role to grant necessary permissions for S3 access

## Python Script

**The Python script performs the following tasks:**

1. Fetches Bitcoin prices from the Coindesk API.

2. Downloads the existing `bitcoin_prices.csv` file from the S3 bucket, appends the latest price entry, and uploads it back.

3. Visualizes the prices for the current day using Seaborn, saves the plot as `bitcoin_prices_DATE.png`, and uploads it to the S3 bucket.

## How to run

- Connect to your EC2 instance.
- Create a "trading" folder and navigate to it.
- Use the Nano editor to create and edit the `bitcoin_trading.py` Python script on the EC2 instance.
- Run the Python script and observe the S3 bucket for the updated files.
- Adjust the cron job schedule to meet your preferences:
  - Open the crontab file using `crontab -e`.
  - Add or modify the schedule line (e.g., `0 * * * * python3 /path/to/bitcoin_trading.py` for running every hour).
  - Save and exit the crontab editor.

Feel free to customize the cron job schedule or the script based on your preferences.
