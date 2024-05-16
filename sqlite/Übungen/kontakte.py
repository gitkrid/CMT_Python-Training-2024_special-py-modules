"""
Aufgabe: Nutze dein bisher gewonnenes Wissen über sqlite3 und tkinter,
um eine GUI zu Speicherung und zum Anzeigen von Kontaktdaten (Name, Telefonnummer)
zu erstellen.

Hinweis: Statt .pack() kann man grid(row=..., column=...) verwenden, um Widgets
auch nebeneinander zu platzieren. Aber das ist für diese Aufgabe rein kosmetischer
Natur.
"""
import tkinter as tk
from tkinter import messagebox
import sqlite3


# Datenbankverbindung und Tabelleninitialisierung
def init_db():
    # TODO: dein Code hier
    ...


# Funktion zum Hinzufügen eines Kontakts
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        # TODO: dein Code hier
        ...
        messagebox.showinfo("Erfolg", "Kontakt wurde hinzugefügt")
    else:
        messagebox.showerror("Fehler", "Name und Telefonnummer dürfen nicht leer sein")


# Funktion zum Abrufen und Anzeigen aller Kontakte
def show_contacts():
    # TODO: dein Code hier
    ...


# GUI Setup
root = tk.Tk()
root.title("Kontaktmanager")

# Eingabefelder für Name und Telefonnummer
# TODO: dein Code hier
...

# Buttons für Aktionen
# TODO: dein Code hier
...


# Bereich zum Anzeigen der Kontakte
display_area = tk.Text(root, height=10, width=50)
display_area.grid(row=4, column=0, columnspan=2)

init_db()  # Initialisiere die Datenbank und die Tabelle
root.mainloop()
