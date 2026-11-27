# Der Spuk von Herings Gaststätte

Ein Weihnachtskrimi-Adventskalender in 24 Türchen.

- Seite: https://silak12.github.io/herings-kalender/
- Türchen direkt: `https://silak12.github.io/herings-kalender/#tuer-1` … `#tuer-24`
- QR-Codes zum Ausdrucken: `qr/QR-Codes.pdf`

## Aufbau

- `kapitel/*.md` – die Texte (Quelle)
- `template.html` – Design und Logik der Seite
- `build.py` – erzeugt `index.html` aus Texten und Vorlage: `python3 build.py`
- `index.html` – die veröffentlichte Seite

Jedes Türchen öffnet sich ab seinem Datum im Dezember 2026; davor gibt es den Knopf „Ich schummle trotzdem“.
