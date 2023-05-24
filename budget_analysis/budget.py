# Aufgabe 1: Budget Daten verstehen und einlesen.

#     Lade die Datei budget.csv herunter und öffne sie in Cloud9.
#     Analysiere den Datensatz und finde folgende Punkte heraus:
#     Um welche Daten handelt es sich?
#     Wie viele Zeilen und Spalten sind im Datensatz enthalten?
#     Gibt es auf den ersten Blick bereits auffällige Datenpunkte?
"""private Einnahmen/Ausgaben von Mario und Laura, bestehend aus 36 Zeilen/5 Spalten"""

#     Lade nun den Datensatz mithilfe von pandas und der read_csv() Methode in ein DataFrame.
#     Benutze die Methode info(), um einen Überblick über das DataFrame zu bekommen.
#     Welche Datentypen haben wir in den einzelnen Spalten?

import pandas as pd
budget_df = pd.read_csv("budget.csv", sep = ";")
print(budget_df)
print(budget_df.info())
print(budget_df.dtypes)
"""die Datentypen sind object(Date, Description, Category) und float64(Out, In)"""

# Aufgabe 2: Gesamtsumme für Einnahmen und Ausgaben berechnen

#     Mario und Laura sind daran interessiert, wie hoch ihre Einnahmen und Ausgaben in den letzten Monaten waren.
#     Berechne daher zuerst die Summe der Einnahmen und die Summe der Ausgaben für den ganzen Datensatz.
#     Wie viel konnten Mario und Laura in den letzten Monaten sparen und zur Seite legen?
#     Tipp: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

sum_income = budget_df["In"].sum()
sum_expense = budget_df["Out"].sum()
savings = sum_income - sum_expense
print(savings.round(2))
"""die beiden haben 22.219,98 gespart"""

# Aufgabe 3: Ausgaben pro Kategorie

#     Lass uns einen Blick auf die einzelnen Ausgaben werfen und verstehen, wo Mario und Laura am meisten ausgegeben haben.
#     Gruppiere die Ausgaben anhand der Kategorie und lasse dir die Summe der Ausgaben pro Kategorie anzeigen.
#     Wofür geben Mario und Laura am meisten Geld aus?
#     Tipp: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

exp_per_category = budget_df[["Category", "Out"]].groupby("Category").sum()
print(exp_per_category)
"""die höchsten Ausgaben waren 3.862,29 für monthly redemption payment"""

# Aufgabe 4: Visualisiere die Ausgaben pro Kategorie

#     Benutze nun seaborn, um einen Barplot für die Ausgaben pro Kategorie zu erstellen.
#     Die Kategorie soll auf der y-Achse sein, die Höhe der Ausgaben auf der x-Achse.
#     Mache folgende Anpassungen an den Chart:
#         Titel: Ausgaben pro Kategorie
#         x-Achsen Benennung: Höhe der Ausgaben
#         y-Achsen Benennung: Kategorie
#         Seaborn Theme: default

#     Speichere den Plot in der Datei expenses_per_category.png
#     Tipp: Benutze Code-Teile aus den vorherigen Hausaufgaben
#     Tipp: Benutze bbox_inches='tight' in deinem savefig() Befehl, um ein schönes Plottingergebnis zu erhalten.

import seaborn as sns
sns.set_theme()
exp_per_category_sns = sns.barplot(data = exp_per_category, x = "Out", y = exp_per_category.index)
exp_per_category_sns.set(title = "Ausgaben pro Kategorie", xlabel = "Höhe der Ausgaben", ylabel = "Kategorie")
exp_per_category_sns.get_figure().savefig("expenses_per_category.png", bbox_inches = "tight")
exp_per_category_sns.figure.clf()

# Bonusaufgabe: Ausgaben pro Monat

#     Mario und Laura wollen verstehen, ob sich ihre Ausgaben über die Monate hinweg verändert haben.
#     Gruppiere die Ausgaben nun pro Monat und speichere das Ergebnis in einem neuen DataFrame ab.
#     Tipp: Convertiere zuerst deine Date-Spalte in das pandas datetime Format: https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime
#     Tipp: Benutze den pandas Grouper, um die Gruppierung pro Monat zu erzielen: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html?highlight=grouper

budget_df["Date"] = pd.to_datetime(budget_df["Date"], format = "%Y-%m-%d")
exp_per_month = budget_df[["Date", "Out"]].groupby(pd.Grouper(key = "Date", freq = "M")).sum()
print(exp_per_month)

#     Erstelle einen weiteren Plot, der die Ausgaben pro Monat aus deinem neuen DataFrame abbildet.
#     Benutze hierfür nochmal den Barplot von seaborn.
#     Wir möchten in diesem Plot die Monatsnamen auf der x-Achse und die Höhe der Ausgaben auf der y-Achse.
#     Speichere den Plot in der Datei expenses_per_month.png.
#     Passe die Achsenbenennung und den Titel des Plots entsprechend an.
#     Tipp: Benutze die Methode month_name(), um die Monatsnamen aus deinem DataFrameIndex zu bekommen: https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html

exp_per_month_sns = sns.barplot(data = exp_per_month, y = "Out", x = exp_per_month.index.month_name())
exp_per_month_sns.set(title = "Ausgaben pro Monat", xlabel = "Monat", ylabel = "Höhe der Ausgaben")
exp_per_month_sns.get_figure().savefig("expenses_per_month.png", bbox_inches = "tight")
exp_per_month_sns.figure.clf()