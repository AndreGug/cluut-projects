# Fahrkartenautomat
# Programmiere einen Fahrkartenautomaten der wie folgt funktioniert:
# Der Automat liest eine json Datei ein in festgelegt wird welche Tickets es gibt und was sie kosten, so wie welche Münzen/Geldscheine der Automat akzeptiert. Die Datei sieht so aus und ist auch an die Aufgabe angehängt:
# {
#   "tickets":
#       [
#           {
#               "name": "Einzelfahrkarte",
#               "price": 4
#
#           },
#           {
#               "name": "Tageskarte (1 Person)",
#               "price": 15
#
#           },
#           {
#               "name": "Tageskarte (Gruppe)",
#               "price": 25
#
#           },
#           {
#               "name": "Monatskarte",
#               "price": 99
#
#           }
#       ],
#   "accepted_cash": [1, 2, 5, 10, 20, 50]
# }
# Zuerst werden dem Benutzer die Tickets angezeigt zusammen mit einer Nummer, über die er dann die Fahrkarte auswählen kann.
# Der Benutzer kann dann eine Fahrkarte auswählen.
# Es wird überprüft, ob der Benutzer eine gültige Nummer eingegeben hat, wenn nicht, wird das Programm beendet. (Ein Programm beendest du mit der Funktion "exit()").
# Bei einer gültigen Nummer wird dem Benutzer sowohl der Preis der Fahrkarte angezeigt, wie auch die Geldscheine/Münzen, die der Automat annimmt.
# Nun kann der Benutzer nach und nach Münzen/Geldscheine in den Automaten einwerfen.
# Jedes mal wenn der Benutzer etwas eingeworfen hat, wird überprüft, ob die Münze/der Geldschein überhaupt angenommen werden kann. Außerdem wird überprüft, ob der Benutzer schon genügend Geld eingeworfen hat.
# Wenn die Münze/der Geldschein gültig ist, wird der fehlende Betrag berechnet und dem Benutzer ausgegeben.
# Sobald genug Geld eingeworfen wurde, bedankt sich der Automat und gibt an wie viel Rückgeld der Benutzer erhalten wird so fern er zu viel bezahlt hat.
#
# Lade die Datei tickets.json in die Cloud9 IDE über "File" -> "Upload Local Files" hoch, oder kopiere den Inhalt manuell in eine neue Datei. Achte darauf, dass die Datei sich im Hauptverzeichnis befinden muss, damit dein Programm sie findet.
# Implementiere anschließend den Automaten.
import json

with open("tickets.json", "r") as fh:
    offering = json.load(fh)

print("Herzlich willkommen bei ihrer Bahn, sie haben folgende Fahrkarten zur Auswahl:")
for i in range(len(offering["tickets"])):
    print(i, offering["tickets"][i]["name"])
selection = int(
    input("Bitte geben sie die entsprechende Zahl für die gewünschte Fahrkarte ein:")
)
print()

if selection < 0 or selection >= len(offering["tickets"]):
    print("Ungültige Auswahl. Programm wird abgebrochen.")
    exit()

print(
    "Sie haben das Ticket",
    offering["tickets"][selection]["name"],
    "gewählt. Der Preis beträgt",
    offering["tickets"][selection]["price"],
    "Euro.",
)
print("Dieser Automat akzeptiert folgende Münzen und Geldscheine:")
for entry in offering["accepted_cash"]:
    print(entry, "Euro")
print()

total_paid = 0
while total_paid < offering["tickets"][selection]["price"]:
    print(
        "Bitte werfen sie eine Münze/einen Geldschein ein, es fehlen noch",
        offering["tickets"][selection]["price"] - total_paid,
        "Euro.",
    )
    current_paid = int(input())
    if current_paid in offering["accepted_cash"]:
        print("Danke für", current_paid, "Euro.")
        total_paid += current_paid
    else:
        print(
            "Leider akzeptieren wir die Münze/den Geldschein nicht, bitte werfen sie etwas anderes ein."
        )
print()

if total_paid > offering["tickets"][selection]["price"]:
    print(
        "Ihr Restgeld beträgt",
        total_paid - offering["tickets"][selection]["price"],
        "Euro.",
    )
print("Danke für ihren Einkauf und gute Fahrt.")
