"""
Aufgabe: Führe folgende Schritte aus:
1. erstelle einen neuen Ordner
2. lass dir den absoluten Pfad dieses Ordners ausgeben
3. erstelle eine Datei in dem Ordner
4. wechsle das Arbeitsverzeichnis so, dass du nicht mehr den Namen des Ordners
aus 1. angeben brauchst
5. überprüfe, ob die Datei "readme.txt" in dem Verzeichnis existiert, wenn
nicht: erstelle sie
"""
import os


# 1.
folder_name = 'new_folder'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Ordner '{folder_name}' wurde erstellt.")
else:
    print(f"Ordner '{folder_name}' existiert bereits.")

# 2.
absolute_path = os.path.abspath(folder_name)
print(f"Absoluter Pfad: {absolute_path}")

# 3.
file_path = os.path.join(absolute_path, 'dummy_file.txt')
with open(file_path, 'w') as file:
    file.write("Das ist eine Testdatei.")

# 4.
os.chdir(folder_name)
print(f"Aktuelles Verzeichnis: {os.getcwd()}")

# 5.
readme_path = 'readme.txt'
if not os.path.exists(readme_path):
    with open(readme_path, 'w') as file:
        file.write("Willkommen in der README-Datei.")
    print(f"'{readme_path}' wurde erstellt.")
else:
    print(f"Datei '{readme_path}' existiert bereits.")

