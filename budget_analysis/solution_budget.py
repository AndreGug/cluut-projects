# Aufgabe 1: Budget Daten verstehen und einlesen.
# Lade die Datei budget.csv herunter und öffne sie in Cloud9.
# Analysiere den Datensatz und finde folgende Punkte heraus:
# Um welche Daten handelt es sich?
# Wieviele Zeilen und Spalten sind im Datensatz enthalten?
# Gibt es auf den ersten Blick bereits auffällige Datenpunkte?

# Lade nun den Datensatz mit Hilfe von pandas und der read_csv() Methode in ein DataFrame.
# Benutze die Methode info(), um einen Überblick über das DataFrame zu bekommen.
# Welche Datentypen haben wir in den einzelnen Spalten?
import pandas as pd
budget = pd.read_csv("budget.csv", sep=";")
print(budget.info())

# Aufgabe 2: Gesamtsumme für Einnahmen und Ausgaben berechnen
# Mario und Julia sind daran interessiert, wie hoch ihre Einnahmen und Ausgaben in den letzten Monaten waren.
# Berechne daher zuerst die Summe der Einnahmen und die Summe der Ausgaben für den ganzen Datensatz.
# Wieviel konnten Mario und Julia in den letzten Monaten sparen und zur Seite legen?
# Tip: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
sum_income = budget["In"].sum()
sum_expense = budget["Out"].sum()
print(sum_income)
print(f'Differenz Einnahmen - Ausgaben: {sum_income - sum_expense}')

# Aufgabe 3: Ausgaben pro Kategorie
# Lass uns nun einen Blick auf die einzenlen Ausgaben werfen und verstehen, wo Mario und Julia am meisten ausgegeben haben.
# Gruppiere die Ausgaben anhand der Kategorie und lasse dir die Summe der Ausgaben pro Kategorie anzeigen.
# Wofür geben Mario und Julia am meisten Geld aus?
# Tip: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
sum_per_category = budget[["Category", "Out"]].groupby("Category").sum()
print(sum_per_category)


# Aufgabe 4: Visualisiere die Ausgaben pro Kategorie
# Benutze nun seaborn, um einen Barplot für die Ausgaben pro Kategorie zu erstellen.
# Die Kategorie soll auf der y-Achse sein, die Höhe der Ausgaben auf der x-Achse.
# Mache folgende Anpassungen an den Chart:
# - Titel: Ausgaben pro Kategorie
# - x-Achsen Benennung: Höhe der Ausgaben
# - y-Achsen Benennung: Kategorie
# - Seaborn Theme: default
# Speichere den Plot in der Datei expenses_per_category.png
# Tip: Benutze Code-Teile aus der Hausaufgabe zum Thema API - github_plotting.py
# Tip: Benutze bbox_inches='tight' in deinem savefig() Befehl, um ein schönes Plottingergebnis zu haben.
import seaborn as sns
sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})
sns_plot = sns.barplot(data = sum_per_category, x = "Out", y = sum_per_category.index)
sns_plot.set_title("Ausgaben pro Kategorie")
sns_plot.set_xlabel("Höhe der Ausgaben")
sns_plot.set_ylabel("Kategorie")
sns_plot.get_figure().savefig("expenses_per_category.png", bbox_inches='tight')
sns_plot.figure.clf()

# Bonusaufgabe: Ausgaben pro Monat
# Mario und Julia wollen nun verstehen, ob sich ihre Ausgaben über die Monate hinweg geändert haben.
# Gruppiere die Ausgaben nun pro Monat und speichere das Ergebnis in einem neuen DataFrame ab.
# Tip: Convertiere zuerst deine Date-Spalte in das pandas datetime Format: 
# https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
# Tip: Benutze den pandas Grouper, um die Gruppierung pro Monat zu erzielen: 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html?highlight=grouper
budget["Date"] = pd.to_datetime(budget["Date"], format = '%Y-%m-%d')
sum_per_month = budget[["Date", "Out"]].groupby(pd.Grouper(key="Date", freq="M")).sum()
print(sum_per_month)


# Erstelle nun einen weiteren Plot, der Ausgaben pro Monat aus deinem neuen DataFrame abbildet.
# Benutze hierfür nochmal den Barplot von seaborn. 
# Wir möchten in diesem Plot die Monatsnamen auf der x-Achse und die Höhe der Ausgaben auf der y-Achse.
# Speichere den Plot in der Datei expenses_per_month.png.
# Passe die Achsenbenennung und den Titel des Plots entsprechend an.
# Tip: Benutze die Methode month_name(), um die Monatsnamen aus deinem DataFrameIndex zu bekommen:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html

sns_plot = sns.barplot(data = sum_per_month, y = "Out", x = sum_per_month.index.month_name())
sns_plot.set_title("Ausgaben pro Monat")
sns_plot.set_xlabel("Zeitraum in Monaten")
sns_plot.set_ylabel("Ausgaben")
sns_plot.get_figure().savefig("expenses_per_month.png", bbox_inches='tight')
sns_plot.figure.clf()