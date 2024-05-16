"""
Aufgabe: Schreibe ein Spiel, welches deine Reaktion testet. Dazu soll nach einer
zufälligen Zeit zwischen 2 und 10 Sekunden eine Zahl (zwischen 1 und 8)
auf dem Bildschirm erscheinen.
Miss die Zeit, die du benötigst, um den Nachfolger dieser Zahl einzugeben
und mit "Enter" zu bestätigen. Prüfe auch, ob das Ergebnis richtig ist, d.h. du
dich in der Eile nicht vertippt hast.
Bsp.: Die Zahl 4 erscheint, dann musst du schnell die Zahl 5 eingeben und bestätigen.

Hinweis: Mit der Funktion .isdigit() kann bei einem String überprüft werden, ob
es sich um eine Zahl handelt. Type casting ist hier nicht notwendig.
"""
import time
import random


def reaktionsspiel():
    print("Willkommen zum Reaktionsspiel!")
    # kurze Pause vor dem Spielbeginn
    time.sleep(2)
    
    # zufällige Wartezeit generieren und warten
    wartezeit = random.randint(2, 10)
    time.sleep(wartezeit)
    
    zahl = random.randint(1, 8)
    print(f"Gegebene Zahl: {zahl}")
    print("Gib den Nachfolger dieser Zahl so schnell wie möglich ein und drücke Enter!")
    
    start_zeit = time.time()

    eingabe = input()
    
    end_zeit = time.time()
    
    # Reaktionszeit berechnen
    reaktionszeit = end_zeit - start_zeit
    reaktionszeit_formatiert = "{:.2f}".format(reaktionszeit)
    
    # überprüfen, ob die Eingabe korrekt ist
    korrekte_antwort = zahl + 1
    if eingabe.isdigit() and int(eingabe) == korrekte_antwort:
        print(f"Richtig! Deine Reaktionszeit war {reaktionszeit_formatiert} Sekunden.")
    else:
        print(f"Falsch! Die richtige Antwort wäre {korrekte_antwort} gewesen. Deine Reaktionszeit war {reaktionszeit_formatiert} Sekunden.")
    
    print("Danke fürs Spielen!")


reaktionsspiel()
