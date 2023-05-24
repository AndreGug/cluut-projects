# Aufgabe 4: Mitarbeiter und Produkte aus altem System einlesen
# Wechsle nun in deine Datei market_management.py - wir starten nun das Management unseres Supermarkets!
# Wir wollen nun Mitarbeiter und Produkte aus zwei CSV Dateien einlesen und zu unserem Supermarkt hinzufügen.
# Lese daher die Datei products.csv ein und speichere die Produkt-Zeilen als Tuple in der Liste products. 
# Lese außerdem die Datei employees.csv ein und speichere die Mitarbeiter-Zeilen als Tuple in der Liste employees.
# Vorsicht: Passe auf die Spaltennamen in den Dateien auf - es handelt sich hier um einen Export aus einem alten SAP Programm!

# Find examples for unpacking data structures here: https://note.nkmk.me/en/python-tuple-list-unpack/

import pandas as pd

# Prepare employees
df_employees = pd.read_csv("employees.csv", sep = ";")
col_order = ["Name", "Age", "Pers_id", "JOB_ID"]
df_employees = df_employees[[*col_order]]
employees = list(df_employees.to_records(index = False))

# Prepare employees
df_products = pd.read_csv("products.csv", sep = ";")
col_order = ["Name", "Prod_id", "Category", "PRICE"]
df_products = df_products[[*col_order]]
prodcuts = list(df_products.to_records(index = False))


# Solltest du Probleme haben hier eine Lösung zu finden, schaue dir diese Seite an:
# https://www.kite.com/python/answers/how-to-reorder-columns-in-a-pandas-dataframe-in-python

# Aufgabe 5: Supermarkt mit Mitarbeitern und Produkten erstellen
# Erstelle einen Supermarkt my_supermarket mit den Werten "Supermarkt Deluxe", "Marienplatz 1", "München".
# Nimm nun deine employees und products und erstelle aus jedem Tupel ein Objekt.
# Für Elemente der employees Liste erstellst du Employee-Objekte und speicherst diese dann gesammelt in deinem Supermarkt.
# Für Elemente der products Liste erstellst du Products-Objekte und speichers diese dann gesammelt in deinem Supermarkt.
# Dein Supermarkt soll am Schluss alle Attribute gesetzt haben - keine leeren Listen mehr!

from supermarket import Supermarket, Product, Employee
my_supermarket = Supermarket("Supermarket Deluxe", "Marienplatz 1", "München")
my_supermarket.products = [Product(*item) for item in prodcuts]
my_supermarket.employees = [Employee(*item) for item in employees]



# Aufgabe 6: Supermarkt Management
# Verschaffe dir nun einen Überblick über deinen Supermarkt und beantworte die folgenden Fragen.
# P.S.: Wir lieben aussagekräftige Antwortsätze - f-String!! ;)
# Überlege dir für welche der Anfragen es ggf. Sinn macht in Zukunft eine neue Methode in einer der Klassen zu implementieren.

# - Wie viele Mitarbeiter hast du aktuell?
print(f'Mein Supermarkt hat aktuell {len(my_supermarket.employees)} Mitarbeiter.')
# - Was ist das teuerste Produkt in deinem Supermarkt?
# Die implementierte Funktion ist ein guter Kandidat für eine neue Methode in der Supermarket Klasse!
def get_most_expensive_product(prod_list):
    """Returns one Product object with the highest price."""
    max_price = None
    max_prod_position = ""
    for i, prod in enumerate(prod_list):
        if not max_price or max_price <= prod.price:
            max_price = prod.price
            max_prod_position = i
    return prod_list[max_prod_position]

most_expensive_product = get_most_expensive_product(my_supermarket.products)
print(f'Das teuerste Produkt im Supermarkt ist {most_expensive_product.name}.')

# - Wie viel kostet ein Produkt im Durchschnitt in deinem Supermarkt?
# f-string float formatting: https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
import statistics
avg_price = statistics.mean([prod.price for prod in my_supermarket.products])
avg_price = round(avg_price, 2)
print(f'Im Durchschnitt kostet ein Produkt {avg_price:.2f}€.')

# - Wie viele Produkte hast du für jede Kategorie?
from collections import Counter
category_counter = Counter([prod.category for prod in my_supermarket.products])
print(f'Wir haben folgende Produktverteilung im Supermarkt: {category_counter}.')

# - Wie heißt der älteste Mitarbeiter?
def get_oldest_employee(employee_list):
    """Returns one Employee object with the highest age value."""
    max_age = None
    max_age_position = ""
    for i, employee in enumerate(employee_list):
        if not max_age or max_age <= employee.age:
            max_age = employee.age
            max_age_position = i
    return employee_list[max_age_position]

oldest_employee = get_oldest_employee(my_supermarket.employees)
print(f'Der älteste Mitarbeiter/in des Supermarkts heißt {oldest_employee.name}.')



