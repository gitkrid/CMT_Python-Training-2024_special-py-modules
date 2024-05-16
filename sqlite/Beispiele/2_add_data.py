import sqlite3


conn = sqlite3.connect("my_db.db")
c = conn.cursor()

# wir fügen einen Wert ein:
# Heinrich, 23 Jahre alt, 1.89 m groß
c.execute("INSERT INTO personen VALUES ('Heinrich', 23, 1.89)")

# wir können auch mehrere Einträge hinzufügen, dazu benutzen wir ? als
# Platzhalter, wenn wir bspw. Daten aus einer Liste einlesen
family = [
    ('Gerda', 27, 1.65),
    ('Johannes', 31, 1.81),
    ('Sabine', 97, 1.59)
]
# statt 'execute' nutzen wir 'executemany'
c.executemany("INSERT INTO personen VALUES (?, ?, ?)", family)


conn.commit()
conn.close()
