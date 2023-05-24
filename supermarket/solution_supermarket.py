# In diesem Projekt werden wir in die Schuhe eines Supermarkteigentümers schlüpfen.
# Um die Verwaltung von deinen Produkten und Angestellten zu erleichtern, nutzt du deine OOP Kenntnisse
# und wirst im folgenden passende Klassen und Methoden implementieren.
# Wie zuvor ist dieses Projekt ein reeller Use Case, der so oder so ähnlich in der Industrie oder in deinem
# zukünftigen Arbeitsalltag auftreten kann.
# Daher lass uns ans Werk gehen und ein cleveres Verwaltungssystem für Supermärkte implementieren!

# Aufgabe 0: File Struktur für das Projekt
# Wir werden in diesem Projekt zwei Pythonfiles benötigen: 
# supermarket.py: Enthält die Klassen, die wir für unseren Supermarkt benötigen.
# market_management.py: Benutzt supermarket.py und wir für die Bearbeitung von Aufgabe X-Y benutzt.

# Aufgabe 1: Die Supermarkt Klasse
# Erstelle zunächst eine Klasse Supermarket, mit den Attributen name (str), street (str), city (str).
# Jeder Supermarkt soll auch die Attribute employees und products haben, die zunächst als leere Liste implementiert 
# werden sollen.
from datetime import datetime

class Supermarket():
    def __init__(self, name, street, city):
        """
        Creates a supermarket with location information.
        Supermarkets have employees and products.
        """
        self.name = name
        self.street = street
        self.city = city
        self.employees = []
        self.products = []


# Aufgabe 2: Die Mitarbeiter Klasse
# Erstelle eine Klasse Employee mit den Attributen name (str), age (int), pers_id (int), job (str).
# Jeder Mitarbeiter soll sich höflich den Kunden deines Supermarket vorstellen und einmal im Jahr
# seinen Geburtstag feiern können.
# Implementiere daher 2 Methoden, greet_customer und celebrate_birthday, die folgende Funktionen haben:
# - greet_customer(): Gibt folgenden Text aus: "Guten Tag. Mein Name ist __ und ich bin ___ in diesem Supermarkt.
# Es ist momentan __ Uhr - wie kann ich Ihnen helfen?"
# - celebrate_birthday(): Inkrementiert das Alter des Mitarbeiters und gibt den Text "Juhu! Heute werde ich _ Jahre!" aus.

class Employee():
    def __init__(self, name, age, pers_id, job):
        """Creates an employee of a supermarket."""
        self.name = name.title()
        self.age = age
        self.pers_id = pers_id
        self.job = job.title()
    
    def greet_customer(self):
        """Greets the customer of a supermarket."""
        current_time = datetime.now().strftime("%H:%M")
        print(f'Guten Tag. Mein Name ist {self.name} und ich bin {self.job} in diesem Supermarkt.\n'\
        f'Es ist momentan {current_time} Uhr - wie kann ich Ihnen helfen?')

    def celebrate_birthday(self):
        """Increment age of employee and prints celebration message."""
        self.age += 1
        print(f'Juhu! Heute werde ich {self.age} Jahre!')

# Aufgabe 3: Die Produkt Klasse
# Erstelle eine Klasse Product mit den Attributen name (str), prod_id (int), category (int), price (float).
# Jedes Produkt gehört in eine der folgenden Kategorien: food, drinks, others
# Überprüfe schon beim Erstellen eines neuen Objekts, ob die Kategorie richtig gesetzt ist. 
# Falls eine falsche Eingabe bei der Objekterstellung gemacht wurde, wähle stets die Kategorie others.

class Product():
    def __init__(self, name, prod_id, category, price):
        """
        Creates a supermarket product.
        Prossible category values are "food", "drinks", "others".
        """
        self.name = name.title()
        self.prod_id = prod_id
        self.price = price
        
        if category in ["food", "drinks", "others"]:
            self.category = category
        else:
            self.category = "others"
    
    def apply_discount(self, discount):
        """Applies discount to product price."""
        if 0 <= discount <= 100:
            self.price = self.price - self.price * (discount / 100)
        else:
            print("Falscher Discount eingegeben. Es wir der Standarddiscount von 5% berechnet.")
            self.price = self.price - self.price * 0.05


# Implementiere eine Methode apply_discount, die den Parameter discount (float) hat und eine Prozentzahl entgegennimmt.
# Teste in der Methode, ob discount zwischen 0 und 100 ist und wende den discount auf den Preis des Produkts an.
# Sollte ein fehlerhafter discount eingegeben worden sein, printe eine Warnung und berechne einen 5%-Rabatt.

if __name__ == "__main__":
    # Teste deine Klassen hier
    my_market = Supermarket("Denn's", "Schanzenstraße 119", "Hamburg")
    print(my_market.name)
    mario = Employee("Mario", 35, 2889, "store manager")
    mario.greet_customer()

