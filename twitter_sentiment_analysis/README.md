# Sentiment Analysis for Tweets

This Python script performs sentiment analysis on tweets related to the topic "obama" using the TextBlob library. The sentiment of each tweet is categorized as negative, positive, or neutral, and the results are saved in a new JSON file. Additionally, a histogram plot is created using Seaborn to visualize the distribution of sentiments.

## Project Files

1. `sentiment_analysis.py`: The main script for sentiment analysis.

2. `data.json`: The JSON file containing raw tweet data.

3. `data_obama.json`: A filtered and sentiment-analyzed subset of tweet data related to the topic "obama."

4. `sentiment.png`: A histogram plot visualizing the distribution of sentiments.

## Project Overview

- The main script loads tweet data from `data.json`.
- It filters tweets related to the topic "obama" and performs sentiment analysis using the TextBlob library.
- Each tweet's sentiment is categorized as negative, positive, or neutral based on polarity.
- The results are saved in `data_obama.json`, providing insights into the sentiment distribution.
- The script generates a histogram plot (`sentiment.png`) using Seaborn, visualizing the distribution of sentiments.

### How to run

- Ensure that the required Python libraries are installed: "pandas", "seaborn" and "textblob".
- Make sure the `data.json` file is present in the same directory as the main script.
- Run the script `sentiment_analysis.py` to perform sentiment analysis and generate results.
