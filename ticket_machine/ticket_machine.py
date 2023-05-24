# Programmiere einen Fahrkartenautomaten der wie folgt funktioniert:

#     Der Automat liest eine json Datei ein, in der festgelegt wird, welche Tickets es gibt und was sie kosten.
#     So wie welche Münzen/Geldscheine der Automat akzeptiert. Die Datei sieht so aus und ist auch an die Aufgabe angehängt:
        
#     {
#   "tickets":
#       [
#           {
#               "name": "Einzelfahrkarte",
#               "price": 4
#           },
#           {
#               "name": "Tageskarte (1 Person)",
#               "price": 15
#           },
#           {
#               "name": "Tageskarte (Gruppe)",
#               "price": 25
#           },
#           {
#               "name": "Monatskarte",
#               "price": 99
#           }
#       ],
#   "accepted_cash": [1, 2, 5, 10, 20, 50]
# }

#     Zuerst werden dem Benutzer die Tickets angezeigt zusammen mit einer Nummer, über die er dann die Fahrkarte auswählen kann.
#     Der Benutzer kann dann eine Fahrkarte auswählen.
#     Es wird überprüft, ob der Benutzer eine gültige Nummer eingegeben hat, wenn nicht, wird das Programm beendet. (Ein Programm beendest du mit der Funktion "exit()").
#     Bei einer gültigen Nummer wird dem Benutzer sowohl der Preis der Fahrkarte angezeigt, wie auch die Geldscheine/Münzen, die der Automat annimmt.
#     Nun kann der Benutzer nach und nach Münzen/Geldscheine in den Automaten einwerfen.
#     Jedes mal wenn der Benutzer etwas eingeworfen hat, wird überprüft, ob die Münze/der Geldschein überhaupt angenommen werden kann. Außerdem wird überprüft, ob der Benutzer schon genügend Geld eingeworfen hat.
#     Wenn die Münze/der Geldschein gültig ist, wird der fehlende Betrag berechnet und dem Benutzer ausgegeben.
#     Sobald genug Geld eingeworfen wurde, bedankt sich der Automat und gibt an, wie viel Rückgeld der Benutzer erhalten wird so fern er zu viel bezahlt hat.

#     Lade die Datei tickets.json in die Cloud9 IDE über "File" -> "Upload Local Files" hoch, oder kopiere den Inhalt manuell in eine neue Datei. Achte darauf, dass die Datei sich im Hauptverzeichnis befinden muss, damit dein Programm sie findet.
#     Implementiere anschließend den Automaten.


# JSON-Datei laden
import json
with open("tickets.json", "r") as file:
    data = json.load(file)

# Tickets und Cash aus Datei extrahieren
tickets = data["tickets"]
accepted_cash = data["accepted_cash"]

# verfügbare Tickets anzeigen
print("Herzlich willkommen bei der Bahn, Sie haben folgende Fahrkarten zur Auswahl:")
for i, ticket in enumerate(tickets, 1):
    print(f"{i} {ticket['name']}")
    
# Aufforderung Ticketnummer eingeben
ticket_num = input("\nBitte wählen Sie Ihre Fahrkarte durch Eingabe der entsprechenden Ticketnummer: ")
ticket_num = int(ticket_num) -1

# prüfen, ob Eingabe gültig ist
if ticket_num < 0 or ticket_num >= len(tickets):
    print("Ungültige Ticketnummer.")
    exit()

# Preis und akzeptierte Münzen für ausgewähltes Ticket anzeigen
selected_ticket = tickets[ticket_num]
print(f"\nSie haben {selected_ticket['name']} ausgewählt. Der Preis beträgt {selected_ticket['price']}€.")
print("Folgende Münzen und Geldscheine werden akzeptiert:")
for value in accepted_cash:
    print(f"{value}€")

# Münze/Geldschein einwerfen
paid_amount = 0
while paid_amount < selected_ticket['price']:
    
    # Eingabe Münze/Geldschein mit Option auf Float
    cash = input("\nBitte werfen Sie eine Münze/einen Geldschein ein: ")
    if cash.isdigit():
        cash = int(cash)
    else:
        try:
            cash = float(cash)
        except ValueError:
            print("Ungültige Münze/Geldschein")
            continue
    if cash not in accepted_cash:
        print("Ungültige Münze/Geldschein")
        continue
            
    # Münze/Geldschein zum bezahlten Betrag hinzufügen
    paid_amount += cash

    # ausstehenden Betrag aktualisieren
    remaining_amount = selected_ticket['price'] - paid_amount

    if remaining_amount > 0:
        print(f"Es fehlen noch {remaining_amount}€.")
    elif remaining_amount < 0:
        change = abs(remaining_amount)
        print(f"Vielen Dank für Ihren Einkauf! Sie erhalten {change}€ Rückgeld.")
    else:
        print("Vielen Dank für Ihren Einkauf!")
