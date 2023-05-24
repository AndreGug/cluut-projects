# Aufgabe 1: Wir arbeiten im ersten Teil mit der Datamuse API: https://www.datamuse.com/api/
# Finde heraus, für was die Datamuse API genutzt werden kann.
# Was ist die Base URL?
# Welche zwei Funktionen (Endpoints) bietet die API? /words, /sug



# Aufgabe 2: Wörter mit einer ähnlichen Bedeutung
# Finde nun die top 5 Wörter, die eine ähnliche Bedeutung haben wie "on top of". 
# Printe das synonyme Wort und den Score.
import requests
base_url = "https://api.datamuse.com"
word = "on top of"
word_param = word.replace(" ", "+")
url = base_url + "/words" + "?ml=" + word_param + "&max=5"

response = requests.get(url).json()
top_results = [(res["word"], res["score"]) for res in response]
print(top_results)

# Aufgabe 3: Funktion synonym_words
# Erstelle eine Funktion synonym_words, die die Parameter word und num_results entgegennimmt.
# Die Funktion benutzt die Datamuse API, um synonyme Wörter zu word zu sammeln.
# Die Funktion gibt eine Liste der Länge num_results zurück, die Tupel mit dem Format (synonymes Wort, Score) enthält.
# Teste die Funktion erneut mit dem Wort "on top of" und vergleiche das Ergebnis mit Aufgabe 2.
def synonym_words(word, num_results):
    """Returns top results for synonym words."""
    # define URL
    word_param = word.replace(" ", "+")
    url = base_url + "/words" + "?ml=" + word_param + "&max=" + str(num_results)
    # get response + convert to Python object with json()
    response = requests.get(url).json()
    # filter for information in dictionary
    top_results = [(res["word"], res["score"]) for res in response]
    return top_results

print(synonym_words("on top of", 8))

# Aufgabe 4: Reimen wie ein Profi - Funktion rhyme_words
# Erstelle eine Funktion rhyme_words, die die Parameter word und num_results entgegennimmt.
# Die Funktion benutzt die Datamuse API, um reimbare Wörter zu word zu sammeln.
# Die Funktion gibt eine Liste der Länge num_results zurück, die Tupel mit dem Format (reimbares Wort, Score) enthält.
# Teste die Funktion mit dem Wort grape. Was sind die Top 5 Wörter, die sich auf grape reimen?
def rhyme_words(word, num_results):
    """Returns top resutls for word rhymes."""
    url = base_url + "/words" + "?rel_rhy=" + word + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_results = [(res["word"], res["score"]) for res in response]
    return top_results

print(rhyme_words("land", 8))

# Aufgabe 5: Finde Antonyme
# Antonyme sind in der Sprachwissenschaft mit gegensätzlicher Bedeutung, z.b. früh --> spät.
# Erstelle eine Funktion antonym_words, die die Parameter word und num_results entgegennimmt.
# Die Funktion benutzt die Datamuse API, um Antonyme zu word zu sammeln.
# Die Funktion gibt eine Liste der Länge num_results zurück, die nur die Antonyme enthält.
# Teste die Funktion mit dem Wort bright. 
def antonym_words(word, num_results):
    """Returns a list of antonyms."""
    url = base_url + "/words" + "?rel_ant=" + word + "&max=" + str(num_results)
    response = requests.get(url).json()
    top_results = [res["word"] for res in response]
    return top_results

print(antonym_words("clever", 5))

# Aufgabe 6: Clean-Up: Erstelle ein Modul
# Erstelle ein neues Pythonskript mit dem Namen word_module.py.
# Kopiere alle erstellten Funktionen in dieses Modul.
# Erstelle einen if __name__ == "__main__" block und teste deine Funktionen similar_words, rhyme_words und antonym_words in word_module.py.
# Schaue dir hierfür zunächst die offizielle Python Dokumentation an: https://docs.python.org/3/library/__main__.html
# Zusätzliche Hilfestellung findest du in diesem Beispiel: https://www.learnpython.dev/02-introduction-to-python/190-apis/final-exercise/
# Importiere dann alle Funktionen in dein ursprüngliches Pythonskript (z.B. data_muse.py) und teste auch hier nochmal die Funktionen 
# similar_words, rhyme_words und antonym_words aus dem Modul word_module.py.
# Wird der Code aus dem if __name__ == "__main__" Block in data_muse.py auch ausgeführt?
# Wofür kannst du den if __name__ == "__main__" Block benutzen?
from word_module import *
print(antonym_words("bright", 5))

# Jedes Python Modul hat eine Variable __name__ definiert.
# Lässt du ein Modul standalone laufen, dann ist in __name__ der Wert "__main__" gespeichert.
# Daher wird der if __name__ == "__main__" Block ausgeführt, wenn du das Skirpt word_module.py aufrufst.
# Der Block wird jedoch nicht ausgeführt, wenn du das Modul in ein anderes Python Skript importierst.
# Wird ein Modul importiert, wird in __name__ der Modulname gespeichert. In unserem Fall steht in __name__ der Wert word_module.
# Deshalb ist die Bedingung if __name__ == "__main__" nicht mehr erfüllt (False) und der Block wird nicht ausgeführt.

# Wir benutzen den if __name__ == "__main__" Block, um Modul-Funktionen zu testen ohne den Import in ein anderes Skript zu stören.