import sqlite3

# kurze Einführung relational vs. non-relational databases
# https://aloa.co/blog/relational-vs-non-relational-database-pros-cons

# eine Verbindung herstellen (erzeugt ein Datei (siehe links))
conn = sqlite3.connect("my_db.db")

# einen Cursor ("Zeiger") erstellen, der für uns die SQL queries ausführt
c = conn.cursor()

# wir nutzen dann die .execute() Methode, um eine neue Tabelle zu erstellen
# wir müssen dazu die Datentypen der Spalten definieren
"""
Übersicht Datentypen SQLite
    Null: fehlender Wert
    Integer: Ganzzahlen (z.B., 1, 2, 3, 4)
    Real: Fließkommazahlen (z.B., 6.2, 7.6, 11.2)
    Text: beliebige Zeichen
    Blob: binäre Daten, um bspw. Dateien abzuspeichern
"""
c.execute(
    """CREATE TABLE personen (
        name TEXT,
        age INTEGER,
        height REAL
    )
    """
)

# ähnlich wie bei git commit
conn.commit()

# Verbindung schließen
conn.close()
