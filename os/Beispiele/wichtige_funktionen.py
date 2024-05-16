import os


# aktuelles Arbeitsverzeichnis holen
current_cwd = os.getcwd()
print("aktuelles CWD:", current_cwd)

# neuen Ordner erstellen
# os.mkdir("new_folder")
# oder
os.makedirs("new_folder", exist_ok=True)

# Pfad zum neuen Ordner holen und alle Verzeichnisse auflisten
path = os.path.join(current_cwd, "new_folder")
print(os.listdir(path))

# Arbeitsverzeichnis in neuen Ordner wechseln
os.chdir(path)
print("aktuelles CWD:", os.getcwd())

# neuen Ordner im neuen Arbeitsverzeichnis erstellen
os.makedirs("new_subfolder", exist_ok=True)

print(os.listdir(path))
