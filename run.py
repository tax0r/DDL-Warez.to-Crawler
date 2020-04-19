#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import datetime
import time

# Liest das Datum und formatiert es in "Monat / Tag / Jahr".

wPreDatum = datetime.datetime.now()
wPostDatum  = wPreDatum.strftime('%x')

# Ziel des Programmes = Eine bestimmte Query suchen und alle ergebnisse anzeigen und downloaden.

# Verschieden Prefixe für Ausgaben um mir das Leben leichter zu machen.

pDebug = '[DEBUG]: '
pInfo = '[INFO]: '
pWarning = "[WARNING]: "
pError  = '[ERROR]: '
pInput ="[INPUT]: "

# Funktion zum erstellen eines Logs mit Datum, HTML-Status Code und der Searchquery

def log(Datum, Query, Status):
    f = open('log - ' + Datum.replace('/', '.'), 'a')
    f.write(Datum + " | " + Status + " | " + Query)
    f.close()

# Information über die Searchquery.

print(pWarning + 'Beachte, dass weder "ä", "ö" noch "ü" funktioniert. Bitte verwende stattdessen Umlaute wie "ae" oder "ue"')

# Aufforderung die gewünschte Searchquery einzugeben für das gewollte Ergebnis.

print(pInput + 'Bitte gebe eine Searchquery ein: ')

# Setzt die Variable "searchQuery" mit dem Input gleich.

searchQuery = input ()

# Die "Such-URL" zusammen mit der Searchquery, die für das URL Format optimiert wurde, für das Suchen.

url = 'https://ddl-warez.to/?search=' + searchQuery.replace(' ', '_')

# Ausgabe der Searchquery und des fertigen URL's

#print(pInfo + 'Ihre Query: ' + searchQuery)
#print(pInfo + 'Der fertige URL: ' + url)

aZeit = time.time()

r = requests.get(url)

if str(r.status_code).startswith('2'):
    print(pInfo + 'Die Verbindung wurde erfolgreich aufgebaut.')
    
    log(wPostDatum, searchQuery, str(r.status_code))
    
    # Stoppt die Zeit

    eZeit = time.time()
    zZeit = eZeit- aZeit
    
    sep = '.'
    tZeit = str(zZeit).split(sep, 1)[0]

    # Giebt die gestoppte Zeit in Sekunden wieder

    print(pInfo + 'Das besuchen der Seite hat ' + tZeit + " ganze Sekunden gedauert.")

else:
    print(pError + 'Die Verbingung konnte nicht erfolgreich aufgebaut werden!')

    log(wPostDatum, searchQuery, str(r.status_code))
    
    # Stoppt die Zeit

    eZeit = time.time()
    zZeit = eZeit- aZeit
    
    sep = '.'
    tZeit = str(zZeit).split(sep, 1)[0]

    # Giebt die gestoppte Zeit in Sekunden wieder

    print(pInfo + 'Das besuchen der Seite hat ' + tZeit + " ganze Sekunden gedauert.")
