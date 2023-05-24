# Aufgabe 0: Log Analyse und Apache verstehen
# Unter dem Begriff Logging verstehen wir die Aufzeichnung von Fehlern und Ereignissen von Software.
# Jede Software, die du benutzt, hat eine Logging-Systematik implementiert, die dir bei der Fehlersuche hilft, wenn etwas mal nicht funktioniert.
# Fehlermeldungen und Ereignisse werden meistens in eine oder mehrere Dateien geschrieben, sogenannte Log Files.
# In der folgenden Aufgabe werden wir uns genau so ein Log File anschauen und es analysieren.
# Bevor wir loslegen, starte eine kurze Recherche und beantworte folgende Fragen:
# Was ist ein Apache HTTP Server? 
# Welches Format haben Apache Access Logs?
# Welche Informationen sind in einer Access Log Zeile enthalten? 
# Tip 1: https://en.wikipedia.org/wiki/Apache_HTTP_Server#Feature_overview
# Tip 2: https://httpd.apache.org/docs/2.2/logs.html#common%20
# Tip 3: https://www.sumologic.com/blog/apache-access-log/

# Aufgabe 1: Apache Logs analysieren
# Lade die Datei apache_logs herunter und speichere sie bei dir in einem Cloud9 Folder für dieses Projekt.
# Öffne die Datei in einem Python Skript namens log_analysis.py und lese alle Zeilen in eine Liste ein.
# Schau dir die erste Zeile der Datei an und schreibe in einem Kommentar auf, welche Informationen wir in jeder Log Zeile haben.
with open("apache_logs", "r") as file:
    log_lines = file.readlines()
print(log_lines[0])
# IP - - Datetime GMTOffset RequestType ResourceRequested Protocol HTTPStatusCode FileSize ReferrerSite Browser

# Aufgabe 2: HTTP Status Code des ersten Log Eintrags
# Speichere die erste Zeile des Log Files in eine separate Variable first_line.
# Splitte die Zeile in ihre Einzelteile mit dem split()-Befehl.
# Extrahiere nun den HTTP Status Code.
# Welcher Status Code wurde für diese Anfrage an den HTTP Server zurückgegeben?
# Was bedeutet der HTTP Status Code?
first_line = log_lines[0]
parts = first_line.split()
print(parts[8])
# Status Code 200 - Success

# Aufgabe 3: HTTP Status Code Analyse
# Analysiere nun alle Log Zeilen und speichere alle HTTP Status Codes in einer Liste mit dem Namen status_codes.
# Zähle, wie oft der Status Code 200 vorkommt und speichere den Wert in status_200.
# Zähle, wie oft der Status Code 404 vorkommt und speichere den Wert in status_404.
# Importiere nun die Klasse Counter aus dem Modul collections.
# https://docs.python.org/3/library/collections.html#collections.Counter
# Benutze die Counter Klasse, um für jeden Status Code in status_codes die Anzahl an Vorkommen zu bestimmen.
# Welche sind die 3 häufigsten HTTP Status Codes?
from collections import Counter
status_codes = [line.split()[8] for line in log_lines]
status_200 = status_codes.count("200")
status_404 = status_codes.count("404")

counter = Counter(status_codes)
# Starte eine Google Suche für den Suchbegriff: HTTP Status Codes
print(counter.most_common(3))

# Aufgabe 4: Fehlerbehebung auf dem HTTP Server
# Um deine Webapplikation für Benutzer zu verbessern, musst du herausfinden, welche Anfragen nicht funktioniert haben.
# Filtere deshalb die Log Zeilen nach dem Status Code 404 und speichere alle Zeilen, die diesen Status Code beinhalten, in der Liste lines_with_404.
# Benutze für das filtern die filter()-Funktion und lambda.
# Speichere in einer neuen Liste namens resource_list die angefragten URL Paths (resource requested).
# Benutze hier wieder die split()-Methode.
# Tip: https://www.sumologic.com/blog/apache-access-log/
# Wieviele verschiedene Fehlerquellen haben hast du gefunden?
# Welche sind die 3 häufigsten Fehlerquellen bei den Anfragen auf unseren Apache Server?
# Tip: https://docs.python.org/3/library/collections.html#collections.Counter
lines_with_404 = list(filter(lambda x : x.split()[8] == "404", log_lines))
resource_list = [line.split()[6] for line in lines_with_404]
print(len(set(resource_list)))
print(Counter(resource_list).most_common(3))


# Bonus Aufgabe: Log Report
# Ziel der Aufgabe ist es einen Log Report zu erstellen, der zwei Abbildungen beinhaltet.
# Installiere hierfür das Python Modul fpdf mit pip: https://pypi.org/project/fpdf/
# Lade das Skript log_pdf.py aus dem LMS herunter und speichere es in deinem Projektordner.
# Importiere die Klasse PDF aus dem Modul log_pdf in dein Skript.
# Erstelle ein Histogram mit seaborn für deine Liste status_codes und speichere den Plot in der Datei status_codes.png.
# Erstelle ein Histogram mit seaborn für deine Liste resource_list und speichere den Plot in der Datei resource_list.png.
# Erstelle eine Liste plots, die zwei Strings enthält: status_codes.png, resource_list.png
# Erstelle eine Instanz der Klasse PDF mit dem Namen log_report.
# Erstelle nun eine for-Schleife über die Elemente plot in deiner Liste plots und rufe in der for-Schleife den Befehl log_report.print_page(x) auf. 
# Um den PDF Report nun zu erstellen, füge die Zeile log_report.output("LogReport.pdf", "F") ein.
# Schaue dir den PDF Report an. Was könnte noch verbessert werden?
from log_pdf import PDF
import seaborn as sns
sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})
# Histo für status codes
sns_plot_status = sns.histplot(status_codes)
sns_plot_status.set_title("Überblick über die HTTP Status Codes")
sns_plot_status.set_xlabel("HTTP Status Codes")
sns_plot_status.set_ylabel("Anzahl")
sns_plot_status.get_figure().savefig("status_codes.png", bbox_inches="tight")
sns_plot_status.figure.clf()

# Histo für resource_list
sns_plot_resource = sns.histplot(y = resource_list)
sns_plot_resource.set_title("Überblick über die angefragten Resourcen mit 404 Status Code")
sns_plot_resource.set_xlabel("Anzahl")
sns_plot_resource.set_ylabel("Resource Namen")
# Adjust figure size for plot
sns_plot_resource.get_figure().set_figwidth(8)
sns_plot_resource.get_figure().set_figheight(11)
# Save plot to file
sns_plot_resource.get_figure().savefig("resource_list.png", bbox_inches="tight")
sns_plot_resource.figure.clf()

# Create report PDF file
plots = ["status_codes.png", "resource_list.png"]
log_report = PDF()
for plot in plots:
    log_report.print_page(plot)
log_report.output("LogReport.pdf", "F")