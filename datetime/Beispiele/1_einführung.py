from datetime import datetime, timedelta


# aktuelles Datum und Uhrzeit
now = datetime.now()
print("Aktuelles Datum und Uhrzeit:", now)

# spezifisches Datum erstellen
date = datetime(2023, 5, 10)
print("Spezifisches Datum:", date)

# Zeitdifferenz
one_week = timedelta(weeks=1)
future_date = now + one_week
print("Datum in einer Woche:", future_date)
