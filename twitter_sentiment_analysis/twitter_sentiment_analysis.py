# Projekt: Twitter Stimmungsanalyse

#     Ein Kollege hat dir eine Datei mit einer Reihe von Tweets über verschiedene Themen übergeben.
#     Die Datei ist schon im JSON Format und besteht aus einer Liste von Tweets, wobei zu jedem Tweet ein Thema, der Benutzer und der Text des Tweets gespeichert sind.
#     Da der Kollege nicht so gut programmieren kann möchte er, dass du für ihn zwei kleine Aufgaben erledigst:
#         1. Filtere die Tweets nach dem Thema "obama" und benutze das Paket "TextBlob" um die Stimmung der "obama" Tweets zu berechnen.
#             Lade zuerst die Datei "data.json" in deine IDE hoch.
#             Das Paket "TextBlob" kannst du wie gewohnt über "pip" installieren. Wie du die Stimmung eines Tweets automatisch berechnen kannst, kannst du unter https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis nachlesen. Dich interessiert dabei der Wert "polarity".
#             Füge zu jedem Tweet einen neuen Schlüssel "sentiment" und gebe ihm den Wert:
#                 "negative" wenn der "polarity"-Wert kleiner als -0.2 ist.
#                 "positive" wenn der "polarity"-Wert größer als 0.2 ist.
#                 "neutral" wenn der "polarity"-Wert dazwischen liegt.
#             Schreibe die nach "obama" gefilterte liste mit dem zusätzlichen "sentiment"-Feld in eine neue JSON Datei.

import json
from textblob import TextBlob

with open("data.json", "r") as fh:
    tweets = json.load(fh)
print(tweets[0])

obama_tweets = list(filter(lambda tweet : tweet["topic"] == "obama", tweets))
print(obama_tweets[0])

for tweet in obama_tweets:
    polarity = TextBlob(tweet["tweet"]).sentiment.polarity
    if polarity < -0.2:
        tweet["sentiment"] = "negative"
    elif polarity > 0.2:
        tweet["sentiment"] = "positive"
    else:
        tweet["sentiment"] = "neutral"
print(obama_tweets[0])

with open("obama_tweets.json", "w") as fh:
    json.dump(obama_tweets, fh, indent = 4)

#         2. Benutze "Seaborn" um ein Histogramm zu erstellen welches anzeigt, wie viele Tweets über das Thema "obama" negativ, positiv und neutral sind.
#             Erstelle dafür erst eine Liste mit allen Sentiments und visualisiere dann das Histogramm mit der "histplot" Funktion.
#             Speichere die Grafik in eine Datei und sieh sie dir an.

import seaborn as sns

obama_sentiments = [tweet["sentiment"]for tweet in obama_tweets]
print(obama_sentiments)

sns.set_theme()
obama_sns = sns.histplot(x = obama_sentiments)
obama_sns.figure.savefig("obama_plot.png")
