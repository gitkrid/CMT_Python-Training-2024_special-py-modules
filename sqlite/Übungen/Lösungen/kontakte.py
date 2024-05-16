import tkinter as tk
from tkinter import messagebox
import sqlite3

# Datenbankverbindung und Tabelleninitialisierung
def init_db():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Funktion zum Hinzufügen eines Kontakts
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
        conn.commit()
        conn.close()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        messagebox.showinfo("Erfolg", "Kontakt wurde hinzugefügt")
    else:
        messagebox.showerror("Fehler", "Name und Telefonnummer dürfen nicht leer sein")

# Funktion zum Abrufen und Anzeigen aller Kontakte
def show_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT name, phone FROM contacts')
    contacts = c.fetchall()
    conn.close()
    display_area.delete('1.0', tk.END)
    for contact in contacts:
        display_area.insert(tk.END, f"Name: {contact[0]}, Telefon: {contact[1]}\n")

# GUI Setup
root = tk.Tk()
root.title("Kontaktmanager")

# Eingabefelder für Name und Telefonnummer
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Telefonnummer:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

# Buttons für Aktionen
add_button = tk.Button(root, text="Kontakt hinzufügen", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2)

show_button = tk.Button(root, text="Kontakte anzeigen", command=show_contacts)
show_button.grid(row=3, column=0, columnspan=2)

# Bereich zum Anzeigen der Kontakte
display_area = tk.Text(root, height=10, width=50)
display_area.grid(row=4, column=0, columnspan=2)

init_db()  # Initialisiere die Datenbank und die Tabelle
root.mainloop()
