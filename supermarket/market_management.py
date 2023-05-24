# Aufgabe 4: Mitarbeiter und Produkte aus altem System einlesen
# Wechsle nun in deine Datei market_management.py - wir starten nun das Management unseres Supermarktes!
# Wir wollen Mitarbeiter und Produkte aus zwei CSV Dateien einlesen und zu unserem Supermarkt hinzufügen.
# Lese daher die Datei products.csv ein und speichere die Produkt-Zeilen als Tuple in der Liste products. 
# Lese außerdem die Datei employees.csv ein und speichere die Mitarbeiter-Zeilen als Tuple in der Liste employees.
# Vorsicht: Passe auf die Spaltennamen in den Dateien auf - es handelt sich hier um einen Export aus einem alten SAP Programm!
# Solltest du Probleme haben hier eine Lösung zu finden, schaue dir diese Seite an: https://www.kite.com/python/answers/how-to-reorder-columns-in-a-pandas-dataframe-in-python

from supermarket import Supermarket, Employee, Product
import pandas as pd

products = pd.read_csv("products.csv", sep=";")
prod_columns = ["Name", "Prod_id", "Category", "PRICE"]
products = products.reindex(columns=prod_columns)
products = list(products.to_records(index=False))

employees = pd.read_csv("employees.csv", sep=";")
emp_columns = ["Name", "Age", "Pers_id", "JOB_ID"]
employees = employees.reindex(columns=emp_columns)
employees = list(employees.to_records(index=False))

# Aufgabe 5: Supermarkt mit Mitarbeitern und Produkten erstellen
# Erstelle einen Supermarkt my_supermarket mit den Werten "Supermarkt Deluxe", "Marienplatz 1", "München".
# Nimm deine employees und products und erstelle aus jedem Tupel ein Objekt.
# Für Elemente der employees Liste erstellst du Employee-Objekte und speicherst diese dann gesammelt in deinem Supermarkt.
# Für Elemente der products Liste erstellst du Products-Objekte und speichers diese dann gesammelt in deinem Supermarkt.
# Dein Supermarkt soll am Schluss alle Attribute gesetzt haben - keine leeren Listen mehr!

my_supermarket = Supermarket("Supermarkt Deluxe", "Marienplatz 1", "München")
my_supermarket.employees = [Employee(*item) for item in employees]
my_supermarket.products = [Product(*item) for item in products]

# Aufgabe 6: Supermarkt Management
# Verschaffe dir einen Überblick über deinen Supermarkt und beantworte die folgenden Fragen.
# P.S.: Wir lieben aussagekräftige Antwortsätze - f-String!! ;)
# Überlege dir für welche der Anfragen es ggf. Sinn macht in Zukunft eine neue Methode in einer der Klassen zu implementieren.
# Wie viele Mitarbeiter hast du aktuell?
# Was ist das teuerste Produkt in deinem Supermarkt?
# Wie viel kostet ein Produkt im Durchschnitt in deinem Supermarkt?
# Wie viele Produkte hast du für jede Kategorie?
# Wie heißt der älteste Mitarbeiter?

my_supermarket.count_employees()
my_supermarket.get_most_expensive_product()
my_supermarket.calculate_average_price()
my_supermarket.count_products_per_category()
my_supermarket.get_oldest_employee()
