# Aufgabe 1: Unterschiede zwischen Listen
#     Erstelle zwei Listen, list1 und list2, mit den folgenden Werten:
#     list1 : 10, 21, 45, 66, 78
#     list2 : 10, 22, 46, 66, 78, 90
#     Finde nun alle Unterschiede zwischen den beiden Listen (symmetrische Differenz).
#     Die Ergebnisliste sym_differences soll die Werte 21, 22, 45, 46, 90 enthalten.
#     Versuche zunächst selbst durch eine Googlesuche auf eine Lösung zu kommen. 
#     Solltest du nichts finden, schau dir diesen Link an:
#     https://www.kite.com/python/answers/how-to-get-the-difference-between-two-list-in-python#:~:text=difference()%20to%20get%20the,the%20difference%20between%20both%20sets

list1 = [10, 21, 45, 66, 78]
list2 = [10, 22, 46, 66, 78, 90]
sym_difference = set(list1).symmetric_difference(set(list2))
print(sorted(sym_difference))

# Aufgabe 2: Gemeinsamkeiten von Listen
#     Wir verwenden weiterhin unsere beiden Listen list1 und list2.
#     Finde die Werte, die in beiden Listen vorkommen.
#     Deine Ergebnisliste common_values soll die Werte 10, 66, 78 enthalten.
#     Versuche zunächst selbst durch eine Googlesuche auf eine Lösung zu kommen.
#     Solltest du nichts finden, schau dir diesen Link an: https://www.w3schools.com/python/ref_set_intersection.asp

common_values = set(list1).intersection(set(list2))
print(sorted(list(common_values)))

# Aufgabe 3: Hotel Marrios vs Hotel Hilten
#     Du planst eine Reise in ein fernes Land und musst dafür ein Hotel auswählen.
#     Eine längere Recherche hat ergeben, dass Hotel Marrios und Hotel Hilten sehr gut geeignet wären.
#     Im Folgenden werden wir möglichst objektiv eine Vergleich der beiden Hotels implementieren,
#     um final eine Entscheidung treffen zu können und unser Abenteuer zu starten.
#     Erstelle nun Hotel Marrios als dict mit dem Namen marrios und mit den folgenden Werten:
#         name: Marrios (string)
#         age: 1999 (int)
#         payment_options: card, cash, online (list of strings)
#         available_rooms: 800, 801, 802, 805, 900, 1000, 1001 (list of ints)
#         price_per_night: 50 (int)
#         employees: carlo, maria, marta, luis, fernando (list of strings)

marrios = {
    "name" : "Marrios",
    "age" : 1999,
    "payment_options" : ["card", "cash", "online"],
    "available_rooms" : [800, 801, 802, 805, 900, 1000, 1001],
    "price_per_night" : 50,
    "employees" : ["carlo", "maria", "marta", "luis", "fernando"]
}

#     Erstelle nun Hotel Hilten als dict mit dem Namen hilten und mit den folgenden Werten:
#         name: Hilten (string)
#         age: 1992 (int)
#         payment_options: card, online (list of strings)
#         available_rooms: 100, 800, 801, 805, 1000, 1001 (list of ints)
#         price_per_night: 70 (int)
#         employees: artur, maria, oliver, xenia (list of strings)

hilten = {
    "name" : "Hilten",
    "age" : 1992,
    "payment_options" : ["card", "online"],
    "available_rooms" : [100, 800, 801, 805, 1000, 1001],
    "price_per_night" : 70,
    "employees" : ["artur", "maria", "oliver", "xenia"]
}

# Frage 1: Du möchtest 5 Nächte im Hotel übernachten.
#     Berechne die Kosten für den Aufenthalt im Hotel Marrios und für Hotel Hilten. Speichere die Werte in cost_marrios und cost_hilten.
#     Welches Hotel ist günstiger und was ist der Preisunterschied?
#     Antwortsatz: Fünf Übernachtungen kosten _€ im Hotel Marrios und _€ im Hotel Hilten. Der Preisunterschied sind _€.

cost_marrios = 5 * marrios["price_per_night"]
cost_hilten = 5 * hilten["price_per_night"]
print(f'Fünf Übernachtungen kosten {cost_marrios}€ im Hotel Marrios und {cost_hilten}€ im Hotel Hilten. Der Preisunterschied sind {cost_hilten - cost_marrios}€.')

# Frage 2: Du möchtest gerne deine Anfrage an beide Hotels automatisieren.
#     Du hast bereits folgenden E-Mail Text erstellt:
#     "Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren: ____? Danke."
#     Welche Zimmernummern sind in beiden Hotels noch verfügbar?
#     Gib den E-Mail-Text mit den entsprechenden Zimmernummern aus.

rooms = set(marrios["available_rooms"]).intersection(set(hilten["available_rooms"]))
print(f'Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren: {rooms}? Danke.')

# Frage 3: Lass uns nun die verschiedenen Zahlungsmöglichkeiten verstehen.
#     Wie viele verschiedenen Zahlungsmöglichkeiten gibt es im Hotel Marrios und im Hotel Hilten?
#     Antwortsatz: Im Hotel Marrios gitb es _ und im Hotel Hilten gibt es _ Zahlungsmöglichkeiten.

print(f'Im Hotel Marrios gitb es {len(marrios["payment_options"])} und im Hotel Hilten gibt es {len(hilten["payment_options"])} Zahlungsmöglichkeiten.')

#     Welche Zahlungsmöglichkeiten gibt es nicht in beiden Hotels?
#     Antwortsatz: Die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeiten: _.

print(f'Die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeiten: {set(marrios["payment_options"]).symmetric_difference(set(hilten["payment_options"]))}.')

# Bonusaufgabe: Dort übernachten, wo Fernando arbeitet.
#     Fernando ist ein guter Freund von dir, daher hast du dich entschieden in dem Hotel zu übernachten, wo er als Angestellter eingetragen ist.
#     Checke für beide Hotels, ob Fernando als Angestellter gelistet ist.
#     Printe bei deinem Check, dass Fernando in diesem Hotel arbeitet und du dort übernachten wirst.
#     Für diese Aufgabe benötigst du Pythonelemente, die wir noch nicht im Detail durchgenommen haben.
#     Versuche dennoch, mit einer Googlesuche auf eine Lösung zu kommen.
#     Hier wieder ein Link, der dir helfen kann, falls du nicht weiterkommst: https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/

if "fernando" in marrios["employees"]:
    print("Fernando arbeitet im Marrios.")
if "fernando" in hilten["employees"]:
    print("Fernando arbeitet im Hilten.")