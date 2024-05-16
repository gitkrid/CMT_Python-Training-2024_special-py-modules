import sqlite3


# wir können auch dieses Tool nutzen, um unsere .db Datei anzeigen zu lassen
# einfach per drag and drop in das Fenster ziehen:
# https://inloop.github.io/sqlite-viewer/

conn = sqlite3.connect("my_db.db")
c = conn.cursor()

# wir wählen die Daten aus unserer Datenbank mit SELECT
# und laden sie mit .fetchall
c.execute("SELECT * FROM personen")
print(c.fetchall())

conn.commit()
conn.close()
