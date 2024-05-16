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
    
    # TODO: dein Code hier
    
    print("Danke fürs Spielen!")


reaktionsspiel()
