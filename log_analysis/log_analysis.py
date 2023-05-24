# Aufgabe 0: Log Analyse und Apache verstehen

"""
Ein Apache HTTP Server ist eine weit verbreitete Webserver-Software, die für ihre Stabilität, Skalierbarkeit und Flexibilität bekannt ist.
Sie ist in der Lage, statische und dynamische Webinhalte bereitzustellen und unterstützt viele Funktionen wie Virtual Hosting, SSL/TLS-Verschlüsselung,
Authentifizierung und Autorisierung. Der Apache HTTP Server ist Open-Source-Software und kann kostenlos heruntergeladen, angepasst und eingesetzt werden.

Common Log Format (CLF), Combined Log Format (CLFv2)

IP-Adresse des Clients, der die Anfrage gesendet hat
Datum und die Uhrzeit des Zugriffs
HTTP-Methode, die vom Client verwendet wurde (z. B. GET, POST)
angeforderte Ressource (URL, Dateipfad usw.)
HTTP-Statuscode, der vom Server an den Client zurückgegeben wurde
Größe der übertragenen Daten
Referer, der die URL der vorherigen Seite enthält, die den Client zur aktuellen Seite geführt hat (falls verfügbar)
User-Agent, der Informationen über den verwendeten Browser und Betriebssystem des Clients enthält (falls verfügbar)
"""

# Aufgabe 1: Apache Logs analysieren

"""
IP-Adresse des Clients: 83.149.9.216
Benutzeridentität und Authentifizierungsstatus: "-" "-" (diese Informationen sind normalerweise leer und werden durch einen Bindestrich "-" dargestellt)
Datum und Uhrzeit des Zugriffs: [17/May/2015:10:05:03 +0000]
HTTP-Methode, die vom Client verwendet wurde: "GET"
Angeforderte Ressource (URL, Dateipfad usw.): "/presentations/logstash-monitorama-2013/images/kibana-search.png"
Verwendete HTTP-Version: "HTTP/1.1"
HTTP-Statuscode, der vom Server an den Client zurückgegeben wurde: 200 (erfolgreiche Anfrage)
Größe der übertragenen Daten (in Bytes): 203023
Referer: "http://semicomplete.com/presentations/logstash-monitorama-2013/" (die URL der vorherigen Seite, die den Client zur aktuellen Seite geführt hat)
User-Agent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36" (Informationen über den verwendeten Browser und Betriebssystem des Clients)
"""

# Import aller erfoderlichen Klassen und Module
from collections import Counter
from log_pdf import PDF
import seaborn as sns
import matplotlib.pyplot as plt

# Datei öffnen und alle Zeilen in eine Liste einlesen
with open("apache_logs", "r") as fh:
    apache_logs = fh.readlines()
print(apache_logs[0])

# Aufgabe 2: HTTP Status Code des ersten Log Eintrags

# Speichern der ersten Zeile in einer zusätzlichen Variablen
first_line = apache_logs[0]

# Splitten der Zeile in ihre Einzelteile
line_parts = first_line.split()

# Extrahieren des HTTP Status Code
http_status_code = line_parts[8]
print(f"HTTP Status Code: {http_status_code}")

"""
HTTP Status Code: 200 (erfolgreiche Anfrage)
"""

# Aufgabe 3: HTTP Status Code Analyse

# Extrahieren aller HTTP Status Codes aus den Log-Zeilen
status_codes = [line.split()[8] for line in apache_logs]

# Zählen des Status Code 200
status_code_200 = status_codes.count("200")
print(f"Anzahl des Status Code 200: {status_code_200}")

# Zählen des Status Code 404
status_code_404 = status_codes.count("404")
print(f"Anzahl des Status Code 404: {status_code_404}")

# Verwendung der Counter-Klasse, um die Anzahl jedes Status Code zu bestimmen
status_count = Counter(status_codes)

# Ermittlung der 3 häufigsten HTTP-Status Codes
top_status_codes = status_count.most_common(3)
print(f"Die 3 häufigsten HTTP Status Codes: {top_status_codes}")
    
# Aufgabe 4: Fehlerbehebung auf dem HTTP Server
    
# Filtern der Log-Zeilen nach Statuscode 404
lines_with_404 = list(filter(lambda line: line.split()[8] == "404", apache_logs))

# Extrahieren der angefragten URL-Paths (Resource Requested)
resource_list = [line.split()[6] for line in lines_with_404]

# Ermitteln der Anzahl verschiedener Fehlerquellen
error_sources_count = len(set(resource_list))
print(f"Anzahl verschiedener Fehlerquellen: {error_sources_count}")

# Ermitteln der 3 häufigsten Fehlerquellen
top_errors = Counter(resource_list).most_common(3)
print(f"Die 3 häufigsten Fehlerquellen: {top_errors}")

# Bonus Aufgabe: Log Report

# Erstellen der Histogramme und Speicherung als Plot
sns.histplot(status_codes)
plt.savefig("status_codes.png")
sns.histplot(resource_list)
plt.savefig("resource_list.png")

# Erstellen der Liste für die Plots
plots = ["status_codes.png", "resource_list.png"]

# Erstellen einer Instanz der PDF-Klasse
log_report = PDF()

# Erstellen einer for-loop für die plots
for plot in plots:
    log_report.print_page(plot)

# Erstellen des PDF Reports
log_report.output("LogReport.pdf", "F")
