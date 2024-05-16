"""
Letztes Kapitel dieser Einführung. Dinge wie Zeilen aktualisieren (update),
löschen (delete), sortieren (sorting), verwerfen (dropping) sind möglich.
Dafür muss man nur die entsprechenden SQL-Befehle verwenden.
Hinweis: Google :)
"""
import sqlite3
import pandas as pd


conn = sqlite3.connect("students_db.db")
c = conn.cursor()

c.execute(
    """CREATE TABLE students (
        name TEXT,
        vorname TEXT,
        matrikelnummer INTEGER,
        studienfach TEXT,
        abschluss TEXT,
        lieblingsfarbe TEXT
    )
    """
)


# Dataframe durch einlesen der csv Datei erstellen
df = pd.read_csv("studenten_datensatz.csv", sep=";")
# die ersten 5 Einträge inspizieren
print(df.head())

# Dataframe zur Datenbank hinzufügen
df.to_sql("students", con=conn, if_exists="append", index=False)

# Daten aus der Datenbank anzeigen
print(c.execute("SELECT * FROM students").fetchall())


conn.commit()
conn.close()

