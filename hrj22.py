#Marcus Krutto 15.01.25
#Harjutus 22

from datetime import datetime, timedelta

import dateparser

# Kuva praegune päev, kuu, aasta, tund, minut
# Vorminda praegune kuupäev järgmiselt: d.m Y,  H:M:S
# Lisa oma sünniaeg, arvuta ja kuva, mitu päeva vana oled
# Kuva vanus aastates
# Kuva, kas tegemist on juubeliaastaga

sp = datetime(2008, 1, 14)
now = datetime.now
print(now)
