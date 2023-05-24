# Aufgabe 0: File Struktur für das Projekt
# Wir werden in diesem Projekt zwei Pythonfiles benötigen: 
# supermarket.py: Enthält die Klassen, die wir für unseren Supermarkt benötigen.
# market_management.py: Benutzt supermarket.py und wird für die Bearbeitung von Aufgabe 4-6 benutzt.

# Aufgabe 1: Die Supermarkt Klasse
# Erstelle zunächst eine Klasse Supermarket, mit den Attributen name (str), street (str), city (str).
# Jeder Supermarkt soll auch die Attribute employees und products haben, die zunächst als leere Liste implementiert werden sollen.

from datetime import datetime
import statistics
from collections import Counter

class Supermarket:
    def __init__(self, name, street, city):
        self.name = name
        self.street = street
        self.city = city
        self.employees = []
        self.products = []

    def count_employees(self):
        all_employees = len(self.employees)
        print(f"Der Supermarkt hat aktuell {all_employees} Mitarbeiter.")

    def get_most_expensive_product(self):
        most_expensive = max(self.products, key=lambda product: product.price)
        print(f"Das teuerste Produkt ist {most_expensive.name.title()}.")

    def calculate_average_price(self):
        prices = [product.price for product in self.products]
        average_price = statistics.mean(prices)
        print(f"Der Durchschnittspreis beträgt {average_price:.2f}€.")

    def count_products_per_category(self):
        categories = ["food", "drinks", "others"]
        count_per_category = Counter(product.category for product in self.products)
        for category in categories:
            count = count_per_category.get(category, 0)
            print(f"Es gibt {count} Produkte in der Kategorie '{category.title()}'.")

    def get_oldest_employee(self):
        oldest_employee = max(self.employees, key=lambda employee: employee.age)
        print(f"Der älteste Mitarbeiter heißt {oldest_employee.name.title()}.")
        
# Aufgabe 2: Die Mitarbeiter Klasse
# Erstelle eine Klasse Employee mit den Attributen name (str), age (int), pers_id (int), job (str).
# Jeder Mitarbeiter soll sich höflich den Kunden deines Supermarket vorstellen und einmal im Jahr seinen Geburtstag feiern können.
# Implementiere daher 2 Methoden, greet_customer und celebrate_birthday, die folgende Funktionen haben:
# greet_customer: Gibt folgenden Text aus: "Guten Tag. Mein Name ist __ und ich bin ___ in diesem Supermarkt. Es ist momentan __ Uhr - wie kann ich Ihnen helfen?"
# celebrate_birthday: Inkrementiert das Alter des Mitarbeiters und gibt den Text "Juhu! Heute werde ich _ Jahre!" aus.

class Employee:
    def __init__(self, name, age, pers_id, job):
        self.name = name
        self.age = age
        self.pers_id = pers_id
        self.job = job
    
    def greet_customer(self):
        time = datetime.now().strftime("%H%M")
        print(f"Guten Tag. Mein Name ist {self.name} und ich bin {self.job} in diesem Supermarkt. Es ist momentan {time} Uhr - wie kann ich Ihnen helfen?")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Juhu! Heute werde ich {self.age} Jahre!")

# Aufgabe 3: Die Produkt Klasse
# Erstelle eine Klasse Product mit den Attributen name (str), prod_id (int), category (str), price (float).
# Jedes Produkt gehört in eine der folgenden Kategorien: food, drinks, others
# Überprüfe schon beim Erstellen eines neuen Objekts, ob die Kategorie richtig gesetzt ist. 
# Falls eine falsche Eingabe bei der Objekterstellung gemacht wurde, wähle stets die Kategorie others.
# Implementiere eine Methode apply_discount, die den Parameter discount (float) hat und eine Prozentzahl entgegennimmt.
# Teste in der Methode, ob discount zwischen 0 und 100 ist und wende den discount auf den Preis des Produkts an.
# Sollte ein fehlerhafter discount eingegeben worden sein, printe eine Warnung und berechne einen 5%-Rabatt.

class Product:
    def __init__(self, name, prod_id, category, price):
        self.name = name
        self.prod_id = prod_id
        if category in ["food", "drinks", "others"]:
            self.category = category
        else:
            self.category = "others"
        self.price = price

    def apply_discount(self, discount):
        if 0 <= discount <= 100:
            self.price = self.price * (1-discount/100)
        else:
            print("Rabattwert ungültig! Es wird ein 5%-Rabatt berechnet.")
            self.price = self.price * 0.95
