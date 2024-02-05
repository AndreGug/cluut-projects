import datetime
import requests
import boto3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Save the current time and date
current_date = datetime.date.today().strftime("%d.%m.%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

# Query the Bitcoin price via API and save it
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

# Check if the API request was successful
if response.status_code == 200:
    data = response.json()
    bitcoin_price = data["bpi"]["USD"]["rate"]
else:
    print(f"Error retrieving Bitcoin price. Status code: {response.status_code}")
    # Handle the error as needed
    bitcoin_price = None

# Update the price list in S3
s3 = boto3.client("s3")
bucket_name = "cluut-aws-developer-kurs-andre-guggenheimer-01-02-2024"
file_key = "trading/bitcoin_prices.csv"

try:
    s3.download_file(bucket_name, file_key, "bitcoin_prices.csv")
except:
    print("The file bitcoin_prices.csv doesn't exist yet.")
finally:
    with open("bitcoin_prices.csv", "a") as file:
        file.write(f"{current_date};{current_time};{bitcoin_price}\n")

s3.upload_file("bitcoin_prices.csv", bucket_name, file_key)

# Visualize prices and make plots publicly available
df = pd.read_csv("bitcoin_prices.csv", sep=";", header=None, thousands=',')
today_prices = df[df[0] == current_date]
sns.lineplot(data=today_prices, x=1, y=2)
plot_name = f"bitcoin_prices_{current_date}.png"
plt.savefig(plot_name)
plot_key = f"trading/plots/{plot_name}"
s3.upload_file(plot_name, bucket_name, plot_key)
