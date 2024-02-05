import json
import pandas as pd
import seaborn as sns
from textblob import TextBlob

# Load tweets from JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Filter tweets based on the topic "obama"
data = [item for item in data if item["topic"] == "obama"]

# Sentiment analysis for each tweet and categorize as negative, positive, or neutral
for entry in data:
    tweet = entry["tweet"]
    text = TextBlob(tweet)
    
    # Calculate sentiment polarity using TextBlob directly
    polarity = text.sentiment.polarity
    
    # Categorize sentiment
    if polarity < -0.2:
        entry["sentiment"] = f"negative"
    elif polarity > 0.2:
        entry["sentiment"] = f"positive"
    else:
        entry["sentiment"] = f"neutral"
        
# Save filtered and sentiment-analyzed tweets to a new JSON file
with open("data_obama.json", "w") as file:
    json.dump(data, file, indent=4)

# Create a Pandas DataFrame for sentiment data
sentiment_data = {"sentiment": [item["sentiment"] for item in data]}
df = pd.DataFrame(sentiment_data)

# Create a histogram plot using Seaborn
sns_plot = sns.histplot(data=df, x="sentiment")

# Save the plot as an image file
sns_plot.get_figure().savefig("sentiment.png")
