import time

# Aktuelle Zeit in Sekunden seit der Epoch
current_time = time.time()
print("Aktuelle Zeit (in Sekunden seit der Epoch):", current_time)

# Verzögerung von 2s
time.sleep(2)

# Lokale Zeit
local_time = time.localtime(current_time)
print("Lokale Zeit:", time.strftime("%Y-%m-%d %H:%M:%S", local_time))