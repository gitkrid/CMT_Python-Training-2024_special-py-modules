"""
Aufgabe: Schreibe eine einfache Funktion mit dem Modul datetime, welches dir
die Arbeitszeit erfasst.

Unterschiedliche Tage und Zeitzonen können ignoriert werden. Außerdem sollte die
Startzeit vor der Endzeit liegen, da das Ergebnis sonst negativ ist.
"""
import datetime

def erfasse_arbeitszeit():
    start_input = input("Gib die Startzeit der Arbeit ein (YYYY-MM-DD HH:MM): ")
    ende_input = input("Gib die Endzeit der Arbeit ein (YYYY-MM-DD HH:MM): ")

    # Umwandeln der Eingaben in datetime-Objekte
    start_zeit = datetime.datetime.strptime(start_input, "%Y-%m-%d %H:%M")
    ende_zeit = datetime.datetime.strptime(ende_input, "%Y-%m-%d %H:%M")

    # Differenz zwischen Start- und Endzeit
    arbeitsdauer = ende_zeit - start_zeit

    print(f"Die Arbeitsdauer beträgt: {arbeitsdauer}")

erfasse_arbeitszeit()
