# Aufgabe 1: Datamuse API kennenlernen

#     Wir arbeiten in diesem Projekt mit der Datamuse API: https://www.datamuse.com/api/
#     Finde heraus, für was die Datamuse API genutzt werden kann.
#     Was ist die Base URL?
#     Welche zwei Funktionen (Endpoints) bietet die API?

"""
Datamuse API ist eine öffentlich zugängliche API, die eine umfangreiche Sammlung von englischen Wörtern und Phrasen, sowie deren Bedeutungen und Beziehungen bereitstellt.
Mit dieser API können Entwickler auf einfache Weise Wortvorschläge, Reime, Synonyme, verwandte Wörter und vieles mehr abrufen, indem sie eine Vielzahl von Abfrageparametern verwenden.
Die Datamuse API ist sehr nützlich für die Entwicklung von Anwendungen, die auf natürlicher Sprachverarbeitung und Textanalyse basieren.

https://api.datamuse.com/

/words endpoint
/sug endpoint
"""

# Aufgabe 2: Wörter mit einer ähnlichen Bedeutung

#     Finde nun die top 5 Wörter, die eine ähnliche Bedeutung haben wie "on top of".
#     Printe eine Liste mit synonymen Wörtern und Scores.

# import requests

# url = "https://api.datamuse.com/words?ml=on+top+of&max=5"
# response = requests.get(url).json()
# results = [(result["word"], result["score"]) for result in response]
# print(results)

# Aufgabe 3: Wortgewandt sein - Funktion synonym_words

#     Erstelle eine Funktion synonym_words, die die Parameter word und num_results entgegennimmt.
#     Die Funktion benutzt die Datamuse API, um synonyme Wörter zu word zu sammeln.
#     Die Funktion gibt eine Liste der Länge num_results zurück, die Tupel mit dem Format (synonymes Wort, Score) enthält.
#     Teste die Funktion erneut mit dem Wort "on top of" und vergleiche das Ergebnis mit Aufgabe 2.

# def synonym_words(word, num_results):
#     url = f"https://api.datamuse.com/words?ml={word}&max={str(num_results)}"
#     response = requests.get(url).json()
#     results = [(result["word"], result["score"]) for result in response]
#     return results

# print(synonym_words("on+top+of", 5))

# Aufgabe 4: Reimen wie ein Profi - Funktion rhyme_words

#     Erstelle eine Funktion rhyme_words, die die Parameter word und num_results entgegennimmt.
#     Die Funktion benutzt die Datamuse API, um reimbare Wörter zu word zu sammeln.
#     Die Funktion gibt eine Liste der Länge num_results zurück, die Tupel mit dem Format (reimbares Wort, Score) enthält.
#     Teste die Funktion mit dem Wort "grape". Was sind die Top 5 Wörter, die sich auf "grape" reimen?

# def rhyme_words(word, num_results):
#     url = f"https://api.datamuse.com/words?rel_rhy={word}&max={str(num_results)}"
#     response = requests.get(url).json()
#     results = [(result["word"], result["score"]) for result in response]
#     return results

# print(rhyme_words("grape", 5))

# # Aufgabe 5: Finde Antonyme

# #     Antonyme sind in der Sprachwissenschaft mit gegensätzlicher Bedeutung, z.b. früh --> spät.
# #     Erstelle eine Funktion antonym_words, die die Parameter word und num_results entgegennimmt.
# #     Die Funktion benutzt die Datamuse API, um Antonyme zu word zu sammeln.
# #     Die Funktion gibt eine Liste der Länge num_results zurück, die nur die Antonyme enthält.
# #     Teste die Funktion mit dem Wort "bright".

# def antonym_words(word, num_results):
#     url = f"https://api.datamuse.com/words?rel_ant={word}&max={str(num_results)}"
#     response = requests.get(url).json()
#     results = [result["word"] for result in response]
#     return results
    
# print(antonym_words("bright", 5))

# Aufgabe 6: Clean-Up: Erstelle ein Modul

#     Erstelle ein neues Modul (also eine neue Datei) mit dem Namen word_module.py.
#     Kopiere alle bisher erstellten Funktionen (synonyme_words, rhyme_words und antonym_words) in diese Datei.
#     Erstelle in diesem Modul einen if __name__ == "__main__" block und teste deine Funktionen similar_words, rhyme_words und antonym_words in word_module.py.
#     Schaue dir hierfür zunächst die offizielle Python Dokumentation an: https://docs.python.org/3/library/__main__.html
#     Zusätzliche Hilfestellung findest du in diesem Beispiel: https://www.learnpython.dev/02-introduction-to-python/190-apis/final-exercise/
#     Importiere mit der import Funktion dann alle Funktionen aus dem word_module Modul in dein ursprüngliches Pythonskript (z.B. data_muse.py) und teste auch hier nochmal die Funktionen similar_words, rhyme_words und antonym_words (aber dieses mal eben jene aus dem Modul word_module.py).

from word_module import *

print(synonym_words("on+top+of", 5))
print(rhyme_words("grape", 5))
print(antonym_words("bright", 5))

#     Wird der Code aus dem if __name__ == "__main__" Block in data_muse.py auch ausgeführt?
#     Wofür kannst du den if __name__ == "__main__" Block benutzen?

"""
Ein "if name == "main" Block ist ein Code-Block, der oft am Ende einer Python-Datei geschrieben wird. Der Block wird ausgeführt,
wenn die Datei als Skript ausgeführt wird, aber nicht, wenn die Datei als Modul in einem anderen Skript importiert wird. Er wird oft verwendet,
um Testcode oder Beispielcode zu schreiben, der nur ausgeführt wird, wenn die Datei als Skript ausgeführt wird. Wenn die Datei als Modul importiert wird,
wird der Code im "if name == "main" Block übersprungen.
"""