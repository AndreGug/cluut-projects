# Projekt: Twitter Stimmungsanalyse
# Ein Kollege hat dir eine Datei mit einer Reihe von Tweets über verschiedene Themen übergeben.
# Die Datei ist schon im JSON Format und besteht aus einer Liste von Tweets, wobei zu jedem Tweet ein Thema, der Benutzer und der Text des Tweets gespeichert sind.
# Da der Kollege nicht so gut programmieren kann möchte er, dass du für ihn zwei kleine Aufgaben erledigst:
# 1. Filtere die Tweets nach dem Thema "obama" und benutze das Paket "TextBlob" um die Stimmung der "obama" Tweets zu berechnen.
# Lade zuerst die Datei "data.json" in deine IDE hoch.
# Das Paket "TextBlob" kannst du wie gewohnt über "pip" installieren. Wie du die Stimmung eines Tweets automatisch berechnen kannst, kannst du unter https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis nachlesen. Dich interessiert dabei der Wert "polarity".
# Füge zu jedem Tweet einen neuen Schlüssel "sentiment" und gebe ihm den Wert:
# "negative" wenn der "polarity"-Wert kleiner als -0.2 ist.
# "positive" wenn der "polarity"-Wert größer als 0.2 ist.
# "neutral" wenn der "polarity"-Wert dazwischen liegt.
# Schreibe die nach "obama" gefilterte liste mit dem zusätzlichen "sentiment"-Feld in eine neue JSON Datei.
# 2. Benutze "Pandas" und "Seaborn" um ein Histogramm zu erstellen welches anzeigt, wie viele Tweets über das Thema "obama" negativ, positiv und neutral sind.
# Erstelle dafür erst einen Pandas DataFrame welcher nur die Spalte "sentiment" enthält, und visualisiere dann das Histogramm mit der "histplot" Funktion.
# Speichere die Grafik in eine Datei und sieh sie dir an.
import json
import pandas as pd
import seaborn as sns
from textblob import TextBlob

with open("data.json", "r") as fh:
    data = json.load(fh)
    
#print(json.dumps(data, indent=4))

data = list(filter(lambda x: x["topic"] == "obama", data))

#print(json.dumps(data, indent=4))

for entry in data:
    tweet = entry["tweet"]
    text = TextBlob(tweet)

    polarity = text.sentiment.polarity

    if polarity < -0.2:
        entry["sentiment"] = f"negative"
    elif polarity > 0.2:
        entry["sentiment"] = f"positive"
    else:
        entry["sentiment"] = f"neutral"
        
#print(json.dumps(data, indent=4))

with open("data_obama.json", "w") as fh:
    json.dump(data, fh, indent=4)

sentiment_data = {"sentiment": list(map(lambda x: x["sentiment"], data))}

#print(sentiment_data)

df = pd.DataFrame(sentiment_data)

#print(df)

sns_plot = sns.histplot(data=df, x="sentiment")
sns_plot.get_figure().savefig("sentiment.png")
